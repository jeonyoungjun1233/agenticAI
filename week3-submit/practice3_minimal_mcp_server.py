from __future__ import annotations

import json
import logging
from pathlib import Path

from mcp.server.fastmcp import FastMCP


WEEK3_DIR = Path(__file__).resolve().parents[1]
LOG_DIR = WEEK3_DIR / "logs"
OUTPUT_DIR = WEEK3_DIR / "output"
LOG_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

LOG_PATH = LOG_DIR / "practice3_minimal_mcp.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("practice3-minimal-mcp")

mcp = FastMCP("week3-minimal-server")

ALLOWED_DIRS = {
    "docs": WEEK3_DIR / "docs",
    "output": WEEK3_DIR / "output",
    "submit": WEEK3_DIR / "submit",
}


def _error(message: str) -> str:
    logger.error(message)
    return json.dumps({"success": False, "error": message}, ensure_ascii=False)


@mcp.tool()
async def list_markdown_files(directory: str = "docs", limit: int = 10) -> str:
    """
    week3 실습 폴더 안의 허용된 하위 디렉터리에서 Markdown 파일 목록을 읽기 전용으로 반환합니다.

    Args:
        directory: 조회할 상대 디렉터리 이름. `docs`, `output`, `submit` 중 하나만 허용됩니다.
        limit: 반환할 최대 파일 수. 1 이상 20 이하만 허용됩니다.

    Returns:
        조회 디렉터리, 파일 목록, 파일 개수를 담은 JSON 문자열
    """
    logger.info("list_markdown_files 호출: directory=%s, limit=%s", directory, limit)

    normalized_directory = directory.strip()
    if not normalized_directory:
        return _error("directory는 비어 있을 수 없습니다. docs, output, submit 중 하나를 입력하세요.")

    if normalized_directory not in ALLOWED_DIRS:
        allowed = ", ".join(ALLOWED_DIRS.keys())
        return _error(f"directory는 허용된 폴더만 사용할 수 있습니다: {allowed}")

    if not 1 <= limit <= 20:
        return _error(f"limit는 1 이상 20 이하이어야 합니다: {limit}")

    target_dir = ALLOWED_DIRS[normalized_directory]
    markdown_files = sorted(path.name for path in target_dir.glob("*.md"))
    selected_files = markdown_files[:limit]

    result = {
        "success": True,
        "directory": normalized_directory,
        "file_count": len(selected_files),
        "files": selected_files,
        "note": "읽기 전용 목록 조회만 지원합니다.",
    }
    logger.info("list_markdown_files 완료: %s개 반환", len(selected_files))
    return json.dumps(result, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    mcp.run(transport="stdio")
