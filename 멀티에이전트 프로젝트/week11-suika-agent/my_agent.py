from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path


AGENT_DIR = Path(__file__).resolve().parent
PREPARED_FILES = ("AGENTS.md", "GEMINI.md", "context.md", "todo.md")


def configure_stdout() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def verify_prepared_files() -> dict[str, bool]:
    return {file_name: (AGENT_DIR / file_name).exists() for file_name in PREPARED_FILES}


def load_agent_context() -> dict[str, str]:
    return {
        "context.md": read_text(AGENT_DIR / "context.md"),
        "todo.md": read_text(AGENT_DIR / "todo.md"),
    }


def find_project_root(start: Path) -> Path | None:
    for candidate in (start, *start.parents):
        if (candidate / "src" / "main.js").exists() and (candidate / "package.json").exists():
            return candidate
    return None


def extract_level_keys(main_js: str) -> list[str]:
    keys = re.findall(r'key:\s*"([^"]+)"', main_js)
    return list(dict.fromkeys(keys))


def extract_function_names(main_js: str) -> list[str]:
    names = re.findall(r"\bfunction\s+([A-Za-z0-9_]+)\s*\(", main_js)
    return list(dict.fromkeys(names))


def extract_python_function_names(python_source: str) -> list[str]:
    names = re.findall(r"^def\s+([A-Za-z0-9_]+)\s*\(", python_source, flags=re.MULTILINE)
    return list(dict.fromkeys(names))


def inspect_game_project(project_root: Path | None) -> dict[str, object]:
    if project_root is None:
        return {
            "project_root": "찾지 못함",
            "key_files": [],
            "levels": [],
            "function_count": 0,
            "sample_functions": [],
            "faces_count": 0,
            "media_count": 0,
            "dependencies": [],
            "note": "이 폴더만 따로 옮긴 상태로 보고, context.md/todo.md 기반 보고서만 생성합니다.",
        }

    main_path = project_root / "src" / "main.js"
    package_path = project_root / "package.json"
    main_js = read_text(main_path)
    package_data = json.loads(read_text(package_path))
    dependencies = sorted(
        {
            *package_data.get("dependencies", {}).keys(),
            *package_data.get("devDependencies", {}).keys(),
        }
    )

    key_files = [
        "index.html",
        "src/main.js",
        "src/style.css",
        "public/faces",
        "public/media",
        "package.json",
    ]

    return {
        "project_root": str(project_root),
        "key_files": [file_name for file_name in key_files if (project_root / file_name).exists()],
        "levels": extract_level_keys(main_js),
        "function_count": len(extract_function_names(main_js)),
        "sample_functions": extract_function_names(main_js)[:8],
        "faces_count": len(list((project_root / "public" / "faces").glob("*"))) if (project_root / "public" / "faces").exists() else 0,
        "media_count": len(list((project_root / "public" / "media").glob("*"))) if (project_root / "public" / "media").exists() else 0,
        "dependencies": dependencies,
        "note": "원래 게임 코드는 읽기만 했고 수정하지 않았습니다.",
    }


def transform_schedule_agent() -> list[tuple[str, str, str]]:
    return [
        ("입력", "수업 일정, 날짜, 장소", "게임 코드 구조, 과제 체크리스트, context.md, todo.md"),
        ("분석", "공지 대상과 긴급도 분류", "게임 파일 구조와 수정 금지 범위 확인"),
        ("출력", "일정 공지문", "수박게임 작업공지, 실행 보고서, 다음 개선 항목"),
        ("검토", "공지 누락 확인", "Week 11 체크리스트와 Week 12 확장 결정 확인"),
    ]


def build_rule_based_plan() -> list[str]:
    return [
        "1. 준비 파일 4개를 확인한다.",
        "2. context.md와 todo.md를 읽어 과제 맥락을 확보한다.",
        "3. 원래 수박게임 프로젝트의 핵심 파일을 읽기 전용으로 점검한다.",
        "4. 일정공지 에이전트 구조를 수박게임 작업공지 에이전트 구조로 바꾼다.",
        "5. 규칙 기반 v0 결과와 12주차 Groq API 확장 방향을 보고서로 남긴다.",
    ]


def decide_week12_extension() -> dict[str, str]:
    return {
        "decision": "Groq API 먼저 연결",
        "reason": "현재 v0는 규칙 기반이라 안정적으로 실행된다. 12주차에는 Groq API로 보고서 문장 생성과 개선 제안을 확장하는 편이 학습 목표에 가장 잘 맞는다.",
        "later": "브라우저 QA, GitHub 이슈 작성, 파일 변경 요약 같은 외부 도구는 Groq API 연결 뒤 단계적으로 붙인다.",
    }


def format_report(
    prepared_files: dict[str, bool],
    docs: dict[str, str],
    inventory: dict[str, object],
    week12: dict[str, str],
) -> str:
    prepared_lines = "\n".join(
        f"- [{'x' if exists else ' '}] {file_name}" for file_name, exists in prepared_files.items()
    )
    transform_lines = "\n".join(
        f"| {old} | {schedule} | {suika} |" for old, schedule, suika in transform_schedule_agent()
    )
    plan_lines = "\n".join(f"- {item}" for item in build_rule_based_plan())
    key_file_lines = "\n".join(f"- {file_name}" for file_name in inventory["key_files"]) or "- 프로젝트 밖에서 실행되어 핵심 파일 점검을 생략함"
    level_lines = ", ".join(inventory["levels"]) if inventory["levels"] else "감지된 단계 없음"
    dependency_lines = ", ".join(inventory["dependencies"]) if inventory["dependencies"] else "외부 의존성 감지 안 됨"

    return f"""# Week 11 에이전트 실행 결과

생성 시각: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## 준비 파일 확인

{prepared_lines}

## 읽은 문서

- context.md 글자 수: {len(docs["context.md"])}
- todo.md 글자 수: {len(docs["todo.md"])}

## 일정공지 예시 변환

| 구분 | 일정공지 에이전트 | 수박게임 작업공지 에이전트 |
| --- | --- | --- |
{transform_lines}

## 게임 코드 기반 점검

- 프로젝트 루트: {inventory["project_root"]}
- 얼굴 이미지 수: {inventory["faces_count"]}
- 미디어 파일 수: {inventory["media_count"]}
- 감지된 단계 키: {level_lines}
- `src/main.js` 함수 수: {inventory["function_count"]}
- 샘플 함수: {", ".join(inventory["sample_functions"]) if inventory["sample_functions"] else "없음"}
- 감지된 의존성: {dependency_lines}
- 메모: {inventory["note"]}

핵심 파일:

{key_file_lines}

## 게임 코드 수정 여부

- 결과: 기존 게임 실행 코드는 수정하지 않았습니다.
- 확인 대상: `src/main.js`, `src/style.css`, `index.html`, `public`, `package.json`, `package-lock.json`
- 에이전트 동작: 게임 파일은 읽기 전용으로 점검하고, 결과 파일은 이 에이전트 폴더의 `agent_output.md`에만 저장합니다.

## 규칙 기반 v0 계획

{plan_lines}

## v0와 이후 확장의 차이

- 규칙 기반 v0: 로컬 파일과 정해진 규칙만 사용한다. API 키가 없어도 실행되고 결과가 예측 가능하다.
- Groq API 확장: 규칙 기반으로 만든 요약과 계획을 LLM에 넘겨 더 자연스러운 설명, 개선 제안, 발표 문장을 만든다.
- 외부 도구 확장: 브라우저 실행 확인, GitHub 이슈 작성, 파일 변경 요약처럼 실제 도구 호출이 필요한 작업을 맡긴다.

## 12주차 결정

- 결정: {week12["decision"]}
- 이유: {week12["reason"]}
- 이후: {week12["later"]}
"""


def print_intermediate_results(
    prepared_files: dict[str, bool],
    docs: dict[str, str],
    inventory: dict[str, object],
    week12: dict[str, str],
) -> None:
    checked_count = sum(prepared_files.values())
    print(f"[1] 준비 파일 확인: {checked_count}/{len(prepared_files)}개 발견")
    print(f"[2] context.md 읽기: {len(docs['context.md'])}글자")
    print(f"[3] todo.md 읽기: {len(docs['todo.md'])}글자")
    print(f"[4] 게임 코드 점검: 얼굴 이미지 {inventory['faces_count']}개, 미디어 {inventory['media_count']}개")
    own_functions = extract_python_function_names(read_text(Path(__file__)))
    print(f"[5] 함수 분리 확인: my_agent.py 내부 함수 {len(own_functions)}개")
    print(f"[6] Week 12 결정: {week12['decision']}")


def main() -> None:
    configure_stdout()
    prepared_files = verify_prepared_files()
    docs = load_agent_context()
    project_root = find_project_root(AGENT_DIR)
    inventory = inspect_game_project(project_root)
    week12 = decide_week12_extension()

    print_intermediate_results(prepared_files, docs, inventory, week12)

    report = format_report(prepared_files, docs, inventory, week12)
    output_path = AGENT_DIR / "agent_output.md"
    output_path.write_text(report, encoding="utf-8")
    print(f"[완료] 실행 결과 저장: {output_path.name}")


if __name__ == "__main__":
    main()
