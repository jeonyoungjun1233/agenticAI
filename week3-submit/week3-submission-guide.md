# Week 3 제출 안내 및 최종 점검

## 1. week-03.md 기준 제출 형식

`class/week-03.md`의 3.10 제출물 기준을 보면, 이번 주차는 특정 한 개 파일 형식보다 아래 산출물이 모두 포함되도록 제출하는 방식이 맞다.

### 제출물 기준

- MCP 사용 기록 1회 이상
- 규칙 적용 전후 비교 기록 1회
- 최소 MCP 서버 코드
- 실행 로그 1개 이상
- 출력 파일 1개 이상
- 체크리스트 또는 짧은 회고 문서

## 2. 실제 제출 권장 방식

가장 깔끔한 제출 방식은 `practice/week3/submit` 폴더 전체 또는 `week3-submit.zip` 파일 1개를 제출하는 것이다.

### 제출용 루트

- 폴더: `C:\agenticAI\practice\week3\submit`
- 압축본: `C:\agenticAI\practice\week3\week3-submit.zip`

## 3. 제출물 매핑

| 요구 제출물 | 제출 파일 |
|---|---|
| MCP 사용 기록 | `practice1_existing_mcp_result.json`, `practice3_mcp_result.json` |
| 규칙 적용 전후 비교 기록 | `practice2_comparison.md`, `summary_without_rules.md`, `summary.md` |
| 최소 MCP 서버 코드 | `practice3_minimal_mcp_server.py` |
| 실행 로그 | `practice1_mcp_server.log`, `practice2_rule_comparison.log`, `practice3_minimal_mcp.log`, `practice4_plugin_structure.log` |
| 출력 파일 | `practice1_existing_mcp_result.json`, `summary.md`, `practice3_mcp_result.json`, `practice4_plugin_structure.json` |
| 체크리스트/회고 | `practice1-checklist.md`, `practice2-checklist.md`, `practice3-checklist.md`, `practice4-checklist.md` |

## 4. 작업 후 체크리스트 재확인

아래 항목은 사용자가 다시 요청한 기준으로 한 번 더 확인한 결과다.

| 확인 항목 | 상태 | 근거 파일 |
|---|---|---|
| 실제로 MCP 호출이 일어났는가 | 확인 완료 | `practice1-checklist.md`, `practice3-checklist.md`, `practice1_mcp_server.log`, `practice3_minimal_mcp.log` |
| 결과 파일이 남았는가 | 확인 완료 | `practice1_existing_mcp_result.json`, `summary.md`, `practice3_mcp_result.json`, `practice4_plugin_structure.json` |
| 로그가 남았는가 | 확인 완료 | `practice1_mcp_server.log`, `practice2_rule_comparison.log`, `practice3_minimal_mcp.log`, `practice4_plugin_structure.log` |
| 규칙 적용 전후 차이를 설명할 수 있는가 | 확인 완료 | `practice2_comparison.md`, `practice2-checklist.md` |
| 실패 사례가 있었다면 원인을 적었는가 | 확인 완료 | `practice1-checklist.md`, `practice2-checklist.md`, `practice3-checklist.md` |

## 5. 눈으로 바로 보면 되는 파일

### 가장 먼저 볼 파일

- `week3-final-summary.md`
- `week3-tracker.md`
- 이 문서 `week3-submission-guide.md`

### 실습별 대표 파일

- 실습 1: `practice1_existing_mcp_result.json`, `practice1-checklist.md`
- 실습 2: `practice2_comparison.md`, `practice2-checklist.md`
- 실습 3: `practice3_minimal_mcp_server.py`, `practice3_mcp_result.json`, `practice3-checklist.md`
- 실습 4: `week3-plugin/`, `practice4_plugin_structure.json`, `practice4-checklist.md`

## 6. 최종 판단

- `week-03.md`의 제출물 기준은 현재 제출본에 모두 반영되어 있다.
- 사용자가 다시 강조한 작업 후 5개 항목도 근거 파일까지 포함해 모두 확인됐다.
- 따라서 현재 상태는 `submit` 폴더 또는 `week3-submit.zip` 그대로 제출 가능한 상태다.
