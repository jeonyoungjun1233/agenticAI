from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def load_server_module():
    root_dir = Path(__file__).resolve().parents[2]
    server_path = root_dir / "chapter4" / "code" / "4-6-weather-mcp-server.py"
    spec = importlib.util.spec_from_file_location("chapter4_weather_mcp_server", server_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"서버 모듈을 불러올 수 없습니다: {server_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    server_module = load_server_module()
    server_module.mcp.run(transport="stdio")
