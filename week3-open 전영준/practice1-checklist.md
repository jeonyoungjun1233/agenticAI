# 실습 1 체크리스트

## 실습 개요

- 실습명: 기존 MCP 서버 연결해서 써 보기
- 사용한 MCP: `practice/chapter4/code/4-6-weather-mcp-server.py`
- 연결 방식: stdio
- 테스트 도구: `get_current_weather`
- 결과 파일: `practice/week3/data/output/practice1_existing_mcp_result.json`
- 요약 문서: `practice/week3/docs/practice1-summary.md`
- 로그 파일: `practice/chapter4/logs/mcp_server.log`, `practice/week3/logs/practice1_server_stderr.log`

## 학생이 직접 확인할 것

- [x] 도구 설명이 충분히 구체적인가
  설명에 위도, 경도, 단위와 반환 형식이 모두 포함되어 있었다.
- [x] 잘못된 입력을 막는가
  `latitude=91` 호출에서 서버가 즉시 검증 오류를 반환했다.
- [x] 오류 메시지가 이해하기 쉬운가
  `위도는 -90에서 90 사이여야 합니다`, `OPENWEATHERMAP_API_KEY 환경 변수가 설정되지 않았습니다`처럼 원인이 직접 드러났다.
- [x] 테스트 절차가 실제로 가능한가
  로컬 stdio 연결 스크립트로 도구 목록 조회와 실제 호출 2건을 재현했다.

## 작업 전

- [x] 어떤 MCP를 연결할지 정했는가
  기존 예제 중 `practice/chapter4/code/4-6-weather-mcp-server.py`를 선택했다.
- [x] 어떤 작업으로 테스트할지 정했는가
  도구 목록 조회, 잘못된 입력 검증, 환경 변수 누락 오류 확인으로 정했다.
- [x] 출력 파일 위치를 정했는가
  `practice/week3/data/output/practice1_existing_mcp_result.json`으로 고정했다.
- [x] 검증 방법을 정했는가
  `tools/list` 결과, 호출 응답, 서버 로그를 함께 확인하기로 정했다.
- [x] 위험한 동작이 없는가
  읽기 중심 호출만 수행했고 삭제나 이동 같은 파괴적 동작은 없었다.

## 작업 후

- [x] 실제로 MCP 호출이 일어났는가
  `ListToolsRequest` 1회와 `CallToolRequest` 2회가 로그에 남았다.
- [x] 결과 파일이 남았는가
  `practice1_existing_mcp_result.json`이 생성되었다.
- [x] 로그가 남았는가
  `practice/chapter4/logs/mcp_server.log`와 `practice/week3/logs/practice1_server_stderr.log`가 남았다.
- [ ] 규칙 적용 전후 차이를 설명할 수 있는가
  이 항목은 실습 2에서 채울 예정이다.
- [x] 실패 사례가 있었다면 원인을 적었는가
  API 키 미설정으로 실제 날씨 조회가 실패했고, 원인을 결과와 로그에 남겼다.
- [x] 체크리스트 또는 짧은 회고 문서가 있는가
  현재 문서와 `practice1-summary.md`로 남겼다.

## 제출물 반영 상태

- [x] MCP 사용 기록 1회 이상
  `practice/week3/data/output/practice1_existing_mcp_result.json`
- [ ] 규칙 적용 전후 비교 기록 1회
  실습 2에서 작성 예정
- [ ] 최소 MCP 서버 코드
  실습 3에서 작성 예정
- [x] 실행 로그 1개 이상
  `practice/chapter4/logs/mcp_server.log`
- [x] 출력 파일 1개 이상
  `practice/week3/data/output/practice1_existing_mcp_result.json`
- [x] 체크리스트 또는 짧은 회고 문서
  `practice/week3/docs/practice1-checklist.md`

## 실패 사례와 원인

- API 키가 없는 상태라 실제 외부 날씨 데이터 조회는 성공하지 못했다.
- 하지만 이 실패 덕분에 환경 변수 오류 메시지와 실패 원인을 로그로 검증할 수 있었다.

## 짧은 회고

- 기존 MCP 서버를 바로 연결해 보는 실습 목적은 달성했다.
- 입력 검증과 오류 메시지 품질은 확인됐고, 실제 외부 API 성공 경로는 API 키가 준비되면 같은 방식으로 이어서 검증할 수 있다.
