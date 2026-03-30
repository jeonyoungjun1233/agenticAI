from __future__ import annotations

import asyncio
import json
from pathlib import Path
from typing import Any

from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client


CODE_DIR = Path(__file__).resolve().parent
WEEK3_DIR = CODE_DIR.parent
ROOT_DIR = WEEK3_DIR.parent.parent
OUTPUT_DIR = WEEK3_DIR / "data" / "output"
LOG_DIR = WEEK3_DIR / "logs"
DOCS_DIR = WEEK3_DIR / "docs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)
DOCS_DIR.mkdir(parents=True, exist_ok=True)

CLIENT_RESULT_PATH = OUTPUT_DIR / "practice1_existing_mcp_result.json"
SUMMARY_PATH = DOCS_DIR / "practice1-summary.md"
STDERR_LOG_PATH = LOG_DIR / "practice1_server_stderr.log"


def normalize_content_items(items: list[Any]) -> list[dict[str, Any]]:
    normalized: list[dict[str, Any]] = []
    for item in items:
        if hasattr(item, "model_dump"):
            normalized.append(item.model_dump(mode="json"))
        else:
            normalized.append({"repr": repr(item)})
    return normalized


def first_text(result: Any) -> str:
    content = getattr(result, "content", [])
    if not content:
        return ""

    first = content[0]
    text = getattr(first, "text", None)
    if text is not None:
        return text

    if hasattr(first, "model_dump"):
        return json.dumps(first.model_dump(mode="json"), ensure_ascii=False)
    return repr(first)


def load_json_text(text: str) -> dict[str, Any]:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"raw_text": text}


async def run_practice() -> dict[str, Any]:
    server_params = StdioServerParameters(
        command=str(ROOT_DIR / ".venv" / "Scripts" / "python.exe"),
        args=[str(CODE_DIR / "run_chapter4_server_stdio.py")],
        cwd=str(ROOT_DIR),
    )

    with STDERR_LOG_PATH.open("w", encoding="utf-8") as errlog:
        async with stdio_client(server_params, errlog=errlog) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                initialize_result = await session.initialize()
                tools_result = await session.list_tools()

                invalid_latitude_result = await session.call_tool(
                    "get_current_weather",
                    {"latitude": 91, "longitude": 126.9780, "units": "metric"},
                )

                missing_key_result = await session.call_tool(
                    "get_current_weather",
                    {"latitude": 37.5665, "longitude": 126.9780, "units": "metric"},
                )

    invalid_text = first_text(invalid_latitude_result)
    missing_key_text = first_text(missing_key_result)

    result = {
        "practice": "실습 1: 기존 MCP 서버 연결해서 써 보기",
        "server": {
            "name": "chapter4 weather server",
            "transport": "stdio",
            "command": str(ROOT_DIR / ".venv" / "Scripts" / "python.exe"),
            "args": [str(CODE_DIR / "run_chapter4_server_stdio.py")],
        },
        "initialize": initialize_result.model_dump(mode="json"),
        "tools": [tool.model_dump(mode="json") for tool in tools_result.tools],
        "calls": [
            {
                "case": "invalid_latitude",
                "input": {"latitude": 91, "longitude": 126.9780, "units": "metric"},
                "is_error": invalid_latitude_result.isError,
                "content": normalize_content_items(invalid_latitude_result.content),
                "parsed_text": load_json_text(invalid_text),
            },
            {
                "case": "missing_api_key",
                "input": {"latitude": 37.5665, "longitude": 126.9780, "units": "metric"},
                "is_error": missing_key_result.isError,
                "content": normalize_content_items(missing_key_result.content),
                "parsed_text": load_json_text(missing_key_text),
            },
        ],
        "verification": [
            "tools/list 결과에 get_current_weather 도구가 노출되는지 확인",
            "잘못된 위도 입력에서 서버 검증 메시지가 반환되는지 확인",
            "유효 좌표지만 API 키가 없는 경우 환경 변수 오류가 반환되는지 확인",
        ],
        "artifacts": {
            "result_json": str(CLIENT_RESULT_PATH),
            "summary_md": str(SUMMARY_PATH),
            "stderr_log": str(STDERR_LOG_PATH),
            "server_log": str(ROOT_DIR / "practice" / "chapter4" / "logs" / "mcp_server.log"),
        },
    }
    return result


def render_summary(result: dict[str, Any]) -> str:
    tools = ", ".join(tool["name"] for tool in result["tools"]) or "(없음)"
    invalid_message = result["calls"][0]["parsed_text"]
    missing_key_message = result["calls"][1]["parsed_text"]

    lines = [
        "# 실습 1 요약",
        "",
        "- 연결 서버: `practice/chapter4/code/4-6-weather-mcp-server.py`",
        "- 연결 방식: stdio",
        f"- 확인된 도구: {tools}",
        "- 호출 1: 위도 91 입력으로 검증 오류 응답 확인",
        f"- 호출 1 결과: `{json.dumps(invalid_message, ensure_ascii=False)}`",
        "- 호출 2: 서울 좌표 입력으로 환경 변수 오류 응답 확인",
        f"- 호출 2 결과: `{json.dumps(missing_key_message, ensure_ascii=False)}`",
        "- 검증:",
        "  1. tools/list에 `get_current_weather`가 포함됨",
        "  2. 잘못된 입력이 서버에서 즉시 차단됨",
        "  3. API 키가 없을 때도 오류 원인이 구체적으로 반환됨",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    result = asyncio.run(run_practice())
    CLIENT_RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    SUMMARY_PATH.write_text(render_summary(result), encoding="utf-8")

    print(f"결과 저장: {CLIENT_RESULT_PATH}")
    print(f"요약 저장: {SUMMARY_PATH}")
    print(f"stderr 로그: {STDERR_LOG_PATH}")


if __name__ == "__main__":
    main()
