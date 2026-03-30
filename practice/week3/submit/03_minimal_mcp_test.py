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
OUTPUT_DIR = WEEK3_DIR / "output"
DOCS_DIR = WEEK3_DIR / "docs"
LOG_DIR = WEEK3_DIR / "logs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
DOCS_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

RESULT_PATH = OUTPUT_DIR / "practice3_mcp_result.json"
SUMMARY_PATH = DOCS_DIR / "practice3-summary.md"
STDERR_LOG_PATH = LOG_DIR / "practice3_server_stderr.log"


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


async def run_test() -> dict[str, Any]:
    server_params = StdioServerParameters(
        command=str(ROOT_DIR / ".venv" / "Scripts" / "python.exe"),
        args=[str(CODE_DIR / "practice3_minimal_mcp_server.py")],
        cwd=str(ROOT_DIR),
    )

    with STDERR_LOG_PATH.open("w", encoding="utf-8") as errlog:
        async with stdio_client(server_params, errlog=errlog) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                initialize_result = await session.initialize()
                tools_result = await session.list_tools()
                valid_result = await session.call_tool(
                    "list_markdown_files",
                    {"directory": "docs", "limit": 5},
                )
                invalid_directory_result = await session.call_tool(
                    "list_markdown_files",
                    {"directory": "../class", "limit": 5},
                )
                invalid_limit_result = await session.call_tool(
                    "list_markdown_files",
                    {"directory": "docs", "limit": 0},
                )

    valid_text = first_text(valid_result)
    invalid_directory_text = first_text(invalid_directory_result)
    invalid_limit_text = first_text(invalid_limit_result)

    result = {
        "practice": "실습 3: 최소 MCP 서버 직접 만들기",
        "server": {
            "name": "week3-minimal-server",
            "transport": "stdio",
            "command": str(ROOT_DIR / ".venv" / "Scripts" / "python.exe"),
            "args": [str(CODE_DIR / "practice3_minimal_mcp_server.py")],
        },
        "initialize": initialize_result.model_dump(mode="json"),
        "tools": [tool.model_dump(mode="json") for tool in tools_result.tools],
        "calls": [
            {
                "case": "valid_docs_query",
                "input": {"directory": "docs", "limit": 5},
                "is_error": valid_result.isError,
                "content": normalize_content_items(valid_result.content),
                "parsed_text": load_json_text(valid_text),
            },
            {
                "case": "invalid_directory",
                "input": {"directory": "../class", "limit": 5},
                "is_error": invalid_directory_result.isError,
                "content": normalize_content_items(invalid_directory_result.content),
                "parsed_text": load_json_text(invalid_directory_text),
            },
            {
                "case": "invalid_limit",
                "input": {"directory": "docs", "limit": 0},
                "is_error": invalid_limit_result.isError,
                "content": normalize_content_items(invalid_limit_result.content),
                "parsed_text": load_json_text(invalid_limit_text),
            },
        ],
        "verification": [
            "tools/list 결과에 list_markdown_files 도구가 노출되는지 확인",
            "허용되지 않은 directory 입력이 차단되는지 확인",
            "limit 범위 검증과 읽기 전용 설명이 결과에 드러나는지 확인",
        ],
        "artifacts": {
            "result_json": str(RESULT_PATH),
            "summary_md": str(SUMMARY_PATH),
            "stderr_log": str(STDERR_LOG_PATH),
            "server_log": str(LOG_DIR / "practice3_minimal_mcp.log"),
        },
    }
    return result


def render_summary(result: dict[str, Any]) -> str:
    tool_name = result["tools"][0]["name"] if result["tools"] else "(없음)"
    valid_preview = json.dumps(result["calls"][0]["parsed_text"], ensure_ascii=False)
    invalid_directory_preview = json.dumps(result["calls"][1]["parsed_text"], ensure_ascii=False)
    invalid_limit_preview = json.dumps(result["calls"][2]["parsed_text"], ensure_ascii=False)

    lines = [
        "# 실습 3 요약",
        "",
        f"- 구현 서버: `practice/week3/code/practice3_minimal_mcp_server.py`",
        f"- 구현 도구: `{tool_name}`",
        "- 연결 방식: stdio",
        "- 정상 호출: `directory=docs`, `limit=5`로 Markdown 파일 목록 조회 확인",
        f"- 정상 호출 결과: `{valid_preview}`",
        "- 실패 호출 1: 허용되지 않은 `directory=../class` 입력 차단 확인",
        f"- 실패 호출 1 결과: `{invalid_directory_preview}`",
        "- 실패 호출 2: `limit=0` 입력 차단 확인",
        f"- 실패 호출 2 결과: `{invalid_limit_preview}`",
        "- 핵심 확인:",
        "  1. 도구 설명에 허용 디렉터리와 limit 범위가 명시되어 있다.",
        "  2. 입력 검증이 잘못된 폴더와 잘못된 limit를 모두 차단한다.",
        "  3. 오류 메시지가 즉시 이해 가능한 문장으로 반환된다.",
        "- 설계 문서: `practice/week3/docs/server-design.md`",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    result = asyncio.run(run_test())
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    SUMMARY_PATH.write_text(render_summary(result), encoding="utf-8")
    print(f"결과 저장: {RESULT_PATH}")
    print(f"요약 저장: {SUMMARY_PATH}")
    print(f"stderr 로그: {STDERR_LOG_PATH}")


if __name__ == "__main__":
    main()
