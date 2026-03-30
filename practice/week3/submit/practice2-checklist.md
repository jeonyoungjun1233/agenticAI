# 실습 2 체크리스트

## 실습 개요

- 실습명: 규칙 파일 만들고 전후 비교하기
- 입력 문서: `practice/week3/docs/notes.md`
- 규칙 파일: `practice/week3/docs/work-rules.md`
- 규칙 전 출력: `practice/week3/output/summary_without_rules.md`
- 규칙 후 출력: `practice/week3/output/summary.md`
- 비교 기록: `practice/week3/output/practice2_comparison.md`, `practice/week3/output/practice2_rule_comparison.json`
- 로그 파일: `practice/week3/logs/practice2_rule_comparison.log`

## 학생이 직접 확인할 것

- [x] 도구 설명이 충분히 구체적인가
  이번 실습은 MCP 도구 호출보다는 규칙 적용 비교가 중심이므로, 규칙 파일 내용과 요약 구조가 충분히 구체적인지 확인했다.
- [x] 잘못된 입력을 막는가
  규칙 파일이 출력 위치와 검증 항목을 강제해 결과 형식이 흔들리지 않도록 막았다.
- [x] 오류 메시지가 이해하기 쉬운가
  실습 자체에 오류는 없었고, 로그에는 각 생성 단계가 순서대로 남아 재확인이 쉬웠다.
- [x] 테스트 절차가 실제로 가능한가
  같은 notes 문서에 대해 규칙 전과 규칙 후 출력을 연속 생성하고 비교 기록까지 남겼다.

## 작업 전

- [x] 어떤 MCP를 연결할지 정했는가
  실습 2는 MCP 추가 연결보다 규칙 비교가 핵심이므로, 기존 주차 실습 환경 안에서 재현하기로 정했다.
- [x] 어떤 작업으로 테스트할지 정했는가
  `docs/notes.md` 요약 생성 전후 비교로 테스트했다.
- [x] 출력 파일 위치를 정했는가
  `practice/week3/output/summary.md`와 `summary_without_rules.md`로 정했다.
- [x] 검증 방법을 정했는가
  검증 항목 3개 포함 여부, 확인 필요 섹션 존재 여부, 로그 생성 여부를 확인하기로 정했다.
- [x] 위험한 동작이 없는가
  문서 생성과 로그 기록만 수행했고 파괴적 작업은 없었다.

## 작업 후

- [x] 실제로 MCP 호출이 일어났는가
  이 실습은 MCP 호출 자체보다 규칙 적용 비교가 목적이라 MCP 호출은 수행하지 않았다.
- [x] 결과 파일이 남았는가
  규칙 전후 요약 파일과 비교 기록이 모두 남았다.
- [x] 로그가 남았는가
  `practice2_rule_comparison.log`가 생성되었다.
- [x] 규칙 적용 전후 차이를 설명할 수 있는가
  규칙 후 요약에는 검증 항목, 확인 필요, 실행 기록이 추가되어 검토성이 높아졌다.
- [x] 실패 사례가 있었다면 원인을 적었는가
  실행 중 `utcnow()` 경고가 있었고, 스크립트를 수정해 `datetime.now(UTC)`로 정리했다.
- [x] 체크리스트 또는 짧은 회고 문서가 있는가
  현재 문서와 `practice2-summary.md`로 남겼다.

## 제출물 반영 상태

- [x] MCP 사용 기록 1회 이상
  실습 1에서 충족
- [x] 규칙 적용 전후 비교 기록 1회
  `practice/week3/output/practice2_comparison.md`
- [ ] 최소 MCP 서버 코드
  실습 3에서 작성 예정
- [x] 실행 로그 1개 이상
  `practice/week3/logs/practice2_rule_comparison.log`
- [x] 출력 파일 1개 이상
  `practice/week3/output/summary.md`
- [x] 체크리스트 또는 짧은 회고 문서
  `practice/week3/docs/practice2-checklist.md`

## 실패 사례와 원인

- 첫 실행에서 Python 3.14 기준 `datetime.utcnow()` 사용에 대한 경고가 나타났다.
- 기능 실패는 아니었지만 재현성을 위해 스크립트를 수정해 경고 없이 다시 실행했다.

## 짧은 회고

- 규칙이 없을 때는 단순 요약만 남아 검토 기준이 부족했다.
- 규칙을 적용하자 출력 형식과 검증 기준이 일정해져 결과를 검토하기 쉬워졌다.
