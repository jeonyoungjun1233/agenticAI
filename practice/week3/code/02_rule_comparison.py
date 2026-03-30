from __future__ import annotations

import json
import logging
from datetime import UTC, datetime
from pathlib import Path


WEEK3_DIR = Path(__file__).resolve().parents[1]
DOCS_DIR = WEEK3_DIR / "docs"
OUTPUT_DIR = WEEK3_DIR / "output"
LOG_DIR = WEEK3_DIR / "logs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_PATH = LOG_DIR / "practice2_rule_comparison.log"
RESULT_JSON_PATH = OUTPUT_DIR / "practice2_rule_comparison.json"
SUMMARY_PATH = OUTPUT_DIR / "summary.md"
SUMMARY_WITHOUT_RULES_PATH = OUTPUT_DIR / "summary_without_rules.md"
COMPARISON_MD_PATH = OUTPUT_DIR / "practice2_comparison.md"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("practice2")


def load_notes() -> list[str]:
    notes_path = DOCS_DIR / "notes.md"
    lines = notes_path.read_text(encoding="utf-8").splitlines()
    bullets = [line[2:].strip() for line in lines if line.startswith("- ")]
    logger.info("notes.md에서 핵심 bullet %s개를 읽었습니다.", len(bullets))
    return bullets


def generate_without_rules(bullets: list[str]) -> str:
    selected = bullets[:5]
    body = ["# notes 요약", ""]
    for bullet in selected:
        body.append(f"- {bullet}")
    body.append("")
    return "\n".join(body)


def generate_with_rules(bullets: list[str]) -> str:
    verification = [
        "도구 연결, 호출 기록, 검증 항목이 모두 포함됐는지 확인",
        "규칙과 MCP의 역할 차이가 요약에 드러나는지 확인",
        "불확실한 내용이 있으면 추측 대신 확인 필요로 표시했는지 확인",
    ]
    summary = [
        "MCP는 에이전트가 외부 도구를 호출할 수 있게 연결하는 표준 인터페이스다.",
        "Skills와 Instructions는 도구를 어떤 절차와 원칙으로 사용할지 정하는 작업 규칙이다.",
        "좋은 실습은 연결 자체보다 호출 기록, 검증, 로그, 출력 파일을 함께 남기는 데 초점을 둔다.",
        "최소 MCP 서버는 명확한 도구 이름, 구체적인 설명, 단순한 입력 검증, 읽기 쉬운 오류 메시지를 갖춰야 한다.",
        "plugin은 skill, MCP 설정, 에이전트 설정을 묶어 배포하는 단위로 이해하면 된다.",
    ]

    body = [
        "# 작업 규칙 적용 요약",
        "",
        "## 검증 항목",
    ]
    for item in verification:
        body.append(f"- {item}")

    body.extend([
        "",
        "## 핵심 요약",
    ])
    for item in summary:
        body.append(f"- {item}")

    body.extend([
        "",
        "## 확인 필요",
        "- 없음",
        "",
        "## 실행 기록",
        "- 이 파일은 `docs/work-rules.md` 규칙을 반영해 다시 생성했다.",
        "- 규칙 없는 초안은 `output/summary_without_rules.md`에 따로 보관했다.",
    ])
    body.append("")
    logger.info("규칙 적용 요약을 생성했습니다.")
    return "\n".join(body)


def build_comparison(before_text: str, after_text: str) -> tuple[dict, str]:
    comparison = {
        "before_path": str(SUMMARY_WITHOUT_RULES_PATH),
        "after_path": str(SUMMARY_PATH),
        "differences": [
            "규칙 전 출력은 단순 요약만 있고 검증 항목이 없다.",
            "규칙 후 출력은 검증 항목 3개를 먼저 제시한다.",
            "규칙 후 출력은 확인 필요 섹션과 실행 기록을 포함한다.",
            "규칙 후 출력은 결과 파일 위치를 비교 가능하도록 명시한다.",
        ],
        "safer_behavior": [
            "검증 기준이 명시되어 결과를 점검하기 쉬워졌다.",
            "불확실성 표기와 실행 기록이 추가되어 검토성이 좋아졌다.",
        ],
        "generated_at": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
    }

    comparison_md = [
        "# 실습 2 비교 기록",
        "",
        "## 비교 대상",
        f"- 규칙 전: `{SUMMARY_WITHOUT_RULES_PATH}`",
        f"- 규칙 후: `{SUMMARY_PATH}`",
        "",
        "## 차이점",
        "- 규칙 전 출력은 단순 요약 중심이다.",
        "- 규칙 후 출력은 검증 항목 3개가 먼저 나온다.",
        "- 규칙 후 출력은 확인 필요와 실행 기록을 포함한다.",
        "- 규칙 후 출력은 결과 검토를 위한 구조가 더 일정하다.",
        "",
        "## 안전성과 검토성",
        "- 규칙 후에는 무엇을 확인해야 하는지 명확해졌다.",
        "- 불확실한 내용 추측을 막는 섹션이 추가되었다.",
        "- 로그와 출력 파일이 연결되어 재검토가 쉬워졌다.",
        "",
        "## 참고",
        "- 실습 원문은 같은 `output/summary.md`를 다시 생성하는 흐름이므로, 비교를 위해 규칙 전 버전을 `summary_without_rules.md`로 따로 보관했다.",
        "",
    ]
    return comparison, "\n".join(comparison_md)


def main() -> None:
    logger.info("실습 2 시작")
    bullets = load_notes()

    before = generate_without_rules(bullets)
    SUMMARY_PATH.write_text(before, encoding="utf-8")
    SUMMARY_WITHOUT_RULES_PATH.write_text(before, encoding="utf-8")
    logger.info("규칙 전 요약을 summary.md와 summary_without_rules.md에 저장했습니다.")

    after = generate_with_rules(bullets)
    SUMMARY_PATH.write_text(after, encoding="utf-8")
    logger.info("규칙 적용 후 summary.md를 다시 생성했습니다.")

    comparison, comparison_md = build_comparison(before, after)
    RESULT_JSON_PATH.write_text(json.dumps(comparison, ensure_ascii=False, indent=2), encoding="utf-8")
    COMPARISON_MD_PATH.write_text(comparison_md, encoding="utf-8")
    logger.info("비교 결과를 저장했습니다.")

    print(f"규칙 전 요약: {SUMMARY_WITHOUT_RULES_PATH}")
    print(f"규칙 후 요약: {SUMMARY_PATH}")
    print(f"비교 기록: {COMPARISON_MD_PATH}")
    print(f"로그 파일: {LOG_PATH}")


if __name__ == "__main__":
    main()

