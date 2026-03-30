# 실습 5 체크리스트

## 실습 개요

- 실습명: hooks와 memory를 붙여 보기
- MCP 설정 파일: `practice/week3/.mcp.json`
- hook 스크립트: `practice/week3/hooks/check_outputs.ps1`
- hook 설계 메모: `practice/week3/docs/hook-design.md`
- project memory 초안: `practice/week3/PROJECT_MEMORY.md`
- Copilot CLI plugin 디렉토리: `practice/week3/copilot-cli-plugin/week3-helper`
- hook 결과 파일: `practice/week3/output/practice5_hook_report.json`
- hook 로그: `practice/week3/logs/practice5_hook.log`
- 비교 문서: `practice/week3/output/practice5_comparison.md`

## 학생이 직접 확인할 것

- [x] 문서 규칙만 둘 때와 hook을 붙였을 때 무엇이 달라지는가
  문서 규칙은 사람이 직접 확인해야 하지만, hook은 작업 완료 뒤 핵심 출력 파일 존재를 자동 검사한다.
- [x] 같은 규칙을 memory에 둘 때 세션 간 일관성이 높아지는가
  출력 위치, 기본 검증 절차, 금지 명령을 `PROJECT_MEMORY.md`에 적어 세션이 바뀌어도 같은 기준을 유지하게 했다.
- [x] skill, instruction, hook, memory가 서로 어떤 역할을 나누는가
  skill/instruction은 작업 방식, hook은 자동 검사, memory는 지속 문맥, MCP는 도구 연결 역할로 분리해 정리했다.
- [x] 테스트와 검증 기록이 남았는가
  hook 결과 JSON, hook 로그, 비교 문서를 모두 남겼다.

## 작업 전

- [x] 어떤 hook 아이디어를 적용할지 정했는가
  `output/` 생성 여부와 핵심 결과 파일 존재 여부를 검사하는 hook으로 정했다.
- [x] 어떤 memory 문맥을 남길지 정했는가
  출력 위치, 기본 검증 절차, 금지 명령을 project memory로 정했다.
- [x] MCP 설정 파일 위치를 정했는가
  프로젝트 루트 `practice/week3/.mcp.json`으로 정했다.
- [x] plugin 디렉토리 구조를 정했는가
  `plugin.json + .mcp.json + skills/doc-summary/SKILL.md` 구조로 정했다.
- [x] 위험한 동작이 없는가
  읽기 전용 MCP 서버와 출력 검증 중심으로 구성했고 파괴적 명령은 memory에 금지로 적었다.

## 작업 후

- [x] 실제로 MCP 호출이 일어났는가
  주차 기준에서는 실습 1과 실습 3에서 실제 MCP 호출이 이미 일어났고, 실습 5 hook은 그 산출물 존재를 자동 검증하도록 적용했다.
- [x] 결과 파일이 남았는가
  `practice5_hook_report.json`, `.mcp.json`, `PROJECT_MEMORY.md`, plugin 디렉토리 파일들이 모두 남았다.
- [x] 로그가 남았는가
  `practice5_hook.log`가 생성되었다.
- [x] 규칙 적용 전후 차이를 설명할 수 있는가
  `practice5_comparison.md`에서 문서 규칙만 있을 때와 hook/memory를 붙였을 때 차이를 설명했다.
- [x] 실패 사례가 있었다면 원인을 적었는가
  실습 5 자체의 hook 실행은 성공했고, 실패 사례 항목은 이전 실습의 MCP 오류와 입력 검증 실패 사례를 체크리스트에 유지했다.
- [x] 체크리스트 또는 짧은 회고 문서가 있는가
  현재 문서와 `practice5-summary.md`로 남겼다.

## 제출물 반영 상태

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

## 짧은 회고

- 문서 규칙만 둘 때보다 hook과 memory를 붙였을 때 자동성, 일관성, 검토성이 더 분명해졌다.
- 부록성 제품 비교 내용은 제외하고, 실습 5 본문에 필요한 산출물만 정리했다.
