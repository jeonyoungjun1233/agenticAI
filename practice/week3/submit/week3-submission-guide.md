# Week 3 제출 안내 및 최종 점검

## 반영 기준

이번 제출본은 `week-03.md new`에서 추가된 **실습 5**, **3.9 테스트와 검증**, **3.10 제출물** 기준만 반영했다.
실습 5 아래에 붙어 있던 Claude Code, ChatGPT/Codex, Gemini CLI, Antigravity 부록 설명은 제출물 대상에서 제외했다.

## 새 제출물 기준

- MCP 연결 설정 파일
- skill 또는 instruction 파일 1개
- 최소 MCP 서버 코드
- Copilot CLI plugin 디렉토리 1개
- hook 또는 자동 검증 설계 메모 1개
- project memory 초안 1개
- 테스트 로그
- 비교 결과 문서
- 업데이트된 체크리스트

## 제출물 매핑

| 요구 제출물 | 제출 파일 |
|---|---|
| MCP 연결 설정 파일 | `.mcp.json` |
| skill 또는 instruction 파일 1개 | `copilot-cli-plugin/week3-helper/skills/doc-summary/SKILL.md` |
| 최소 MCP 서버 코드 | `practice3_minimal_mcp_server.py` |
| Copilot CLI plugin 디렉토리 1개 | `copilot-cli-plugin/week3-helper/` |
| hook 또는 자동 검증 설계 메모 1개 | `hook-design.md` |
| project memory 초안 1개 | `PROJECT_MEMORY.md` |
| 테스트 로그 | `practice3_minimal_mcp.log`, `practice5_hook.log` |
| 비교 결과 문서 | `practice2_comparison.md`, `practice5_comparison.md` |
| 업데이트된 체크리스트 | `practice5-checklist.md` |

## 작업 후 체크리스트 재확인

| 확인 항목 | 상태 | 근거 파일 |
|---|---|---|
| 실제로 MCP 호출이 일어났는가 | 확인 완료 | `practice1_existing_mcp_result.json`, `practice3_mcp_result.json`, `practice3-checklist.md` |
| 결과 파일이 남았는가 | 확인 완료 | `summary.md`, `practice3_mcp_result.json`, `practice5_hook_report.json` |
| 로그가 남았는가 | 확인 완료 | `practice1_mcp_server.log`, `practice3_minimal_mcp.log`, `practice5_hook.log` |
| 규칙 적용 전후 차이를 설명할 수 있는가 | 확인 완료 | `practice2_comparison.md`, `practice5_comparison.md` |
| 실패 사례가 있었다면 원인을 적었는가 | 확인 완료 | `practice1-checklist.md`, `practice2-checklist.md`, `practice3-checklist.md` |

## 바로 확인할 파일

- `week3-final-summary.md`
- `week3-tracker.md`
- `practice5-checklist.md`
- `hook-design.md`
- `PROJECT_MEMORY.md`
