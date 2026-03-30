# Week 3 실습 추적 문서

이 문서는 `week-03.md new`의 실습 5 및 제출물 기준을 포함해 week3 산출물을 추적하기 위한 문서다.
부록 아래의 도구별 확장 설명은 제출물 대상에서 제외하고, 실습 1~5와 직접 연결된 산출물만 기록한다.

## 제출물 현황

- [x] MCP 연결 설정 파일
  `practice/week3/.mcp.json`
- [x] skill 또는 instruction 파일 1개
  `practice/week3/copilot-cli-plugin/week3-helper/skills/doc-summary/SKILL.md`
- [x] 최소 MCP 서버 코드
  `practice/week3/code/practice3_minimal_mcp_server.py`
- [x] Copilot CLI plugin 디렉토리 1개
  `practice/week3/copilot-cli-plugin/week3-helper`
- [x] hook 또는 자동 검증 설계 메모 1개
  `practice/week3/docs/hook-design.md`
- [x] project memory 초안 1개
  `practice/week3/PROJECT_MEMORY.md`
- [x] 테스트 로그
  `practice/week3/logs/practice3_minimal_mcp.log`, `practice/week3/logs/practice5_hook.log`
- [x] 비교 결과 문서
  `practice/week3/output/practice2_comparison.md`, `practice/week3/output/practice5_comparison.md`
- [x] 업데이트된 체크리스트
  `practice/week3/docs/practice5-checklist.md`

## 실습 상태

### 실습 1: 기존 MCP 서버 연결해서 써 보기
- 상태: 완료
- 핵심 산출물: `practice1_existing_mcp_result.json`, `practice1-checklist.md`

### 실습 2: 규칙 파일 만들고 전후 비교하기
- 상태: 완료
- 핵심 산출물: `summary.md`, `summary_without_rules.md`, `practice2_comparison.md`

### 실습 3: 최소 MCP 서버 직접 만들기
- 상태: 완료
- 핵심 산출물: `practice3_minimal_mcp_server.py`, `practice3_mcp_result.json`, `server-design.md`

### 실습 4: Plugin은 선택 실습으로 보기
- 상태: 완료
- 핵심 산출물: `practice4_plugin_structure.json`, `practice4-checklist.md`

### 실습 5: hooks와 memory를 붙여 보기
- 상태: 완료
- 핵심 산출물: `.mcp.json`, `PROJECT_MEMORY.md`, `hook-design.md`, `practice5_hook_report.json`, `copilot-cli-plugin/week3-helper`, `practice5-checklist.md`

## 작업 후 핵심 확인

- 실제 MCP 호출 기록은 실습 1과 실습 3에 남아 있다.
- 결과 파일, 로그, 비교 문서, 실패 사례 기록은 각 체크리스트에 정리되어 있다.
- 문서 규칙, hook, memory 역할 차이는 실습 5 비교 문서에 따로 정리했다.
