# Week 3 실습 추적 문서

이 문서는 `class/week-03.md`의 체크리스트와 제출물 기준을 실습 1~4에 공통 적용하기 위한 작업 기준서다.
각 실습이 끝날 때마다 상태를 갱신한다.

## 공통 확인 항목

### 학생이 직접 확인할 것

- [ ] 도구 설명이 충분히 구체적인가
- [ ] 잘못된 입력을 막는가
- [ ] 오류 메시지가 이해하기 쉬운가
- [ ] 테스트 절차가 실제로 가능한가

### 작업 전

- [ ] 어떤 MCP를 연결할지 정했는가
- [ ] 어떤 작업으로 테스트할지 정했는가
- [ ] 출력 파일 위치를 정했는가
- [ ] 검증 방법을 정했는가
- [ ] 위험한 동작이 없는가

### 작업 후

- [ ] 실제로 MCP 호출이 일어났는가
- [ ] 결과 파일이 남았는가
- [ ] 로그가 남았는가
- [ ] 규칙 적용 전후 차이를 설명할 수 있는가
- [ ] 실패 사례가 있었다면 원인을 적었는가
- [ ] 체크리스트 또는 짧은 회고 문서가 있는가

## 제출물 현황

- [x] MCP 사용 기록 1회 이상
  경로: `practice/week3/data/output/practice1_existing_mcp_result.json`
- [x] 규칙 적용 전후 비교 기록 1회
  경로: `practice/week3/output/practice2_comparison.md`
- [ ] 최소 MCP 서버 코드
  예정: 실습 3
- [x] 실행 로그 1개 이상
  경로: `practice/week3/logs/practice2_rule_comparison.log`
- [x] 출력 파일 1개 이상
  경로: `practice/week3/output/summary.md`
- [x] 체크리스트 또는 짧은 회고 문서
  경로: `practice/week3/docs/practice2-checklist.md`

## 실습 상태

### 실습 1: 기존 MCP 서버 연결해서 써 보기

- 상태: 완료
- 사용한 MCP: `practice/chapter4/code/4-6-weather-mcp-server.py`
- 테스트 작업: `get_current_weather` 도구 목록 확인, 잘못된 위도 입력, API 키 누락 상황 확인
- 출력 위치: `practice/week3/data/output/practice1_existing_mcp_result.json`
- 검증 문서: `practice/week3/docs/practice1-checklist.md`

### 실습 2: 규칙 파일 만들고 전후 비교하기

- 상태: 완료
- 입력 문서: `practice/week3/docs/notes.md`
- 규칙 파일: `practice/week3/docs/work-rules.md`
- 출력 위치: `practice/week3/output/summary.md`, `practice/week3/output/summary_without_rules.md`
- 비교 문서: `practice/week3/output/practice2_comparison.md`
- 검증 문서: `practice/week3/docs/practice2-checklist.md`

### 실습 3: 최소 MCP 서버 직접 만들기

- 상태: 대기
- 비고: 도구 설명, 입력 검증, 오류 메시지, 테스트 절차를 필수 항목으로 기록 예정

### 실습 4: Plugin은 선택 실습으로 보기

- 상태: 대기
- 비고: 최소 구조 예시와 묶음 배포 관점 요약을 남길 예정
