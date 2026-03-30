# 실습 3 체크리스트

## 실습 개요

- 실습명: 최소 MCP 서버 직접 만들기
- 서버 코드: `practice/week3/code/practice3_minimal_mcp_server.py`
- 테스트 스크립트: `practice/week3/code/03_minimal_mcp_test.py`
- 설계 문서: `practice/week3/docs/server-design.md`
- 결과 파일: `practice/week3/output/practice3_mcp_result.json`
- 로그 파일: `practice/week3/logs/practice3_minimal_mcp.log`, `practice/week3/logs/practice3_server_stderr.log`

## 학생이 직접 확인할 것

- [x] 도구 설명이 충분히 구체적인가
  허용된 디렉터리, limit 범위, 읽기 전용 반환 형식이 도구 설명에 포함됐다.
- [x] 잘못된 입력을 막는가
  `../class`와 `limit=0` 입력이 모두 차단됐다.
- [x] 오류 메시지가 이해하기 쉬운가
  허용값과 범위를 직접 알려주는 문장으로 반환됐다.
- [x] 테스트 절차가 실제로 가능한가
  `03_minimal_mcp_test.py`와 `server-design.md`에 재현 절차를 남겼다.

## 작업 전

- [x] 어떤 MCP를 연결할지 정했는가
  새로 만든 `week3-minimal-server`를 stdio로 테스트하기로 정했다.
- [x] 어떤 작업으로 테스트할지 정했는가
  정상 조회 1건과 입력 검증 실패 2건으로 테스트하기로 정했다.
- [x] 출력 파일 위치를 정했는가
  결과는 `practice/week3/output/practice3_mcp_result.json`으로 정했다.
- [x] 검증 방법을 정했는가
  도구 목록, 정상 호출, 잘못된 directory, 잘못된 limit, 로그 파일을 확인하기로 정했다.
- [x] 위험한 동작이 없는가
  읽기 전용 목록 조회만 지원하도록 설계했다.

## 작업 후

- [x] 실제로 MCP 호출이 일어났는가
  `ListToolsRequest` 1회와 `CallToolRequest` 3회가 로그에 남았다.
- [x] 결과 파일이 남았는가
  `practice3_mcp_result.json`이 생성되었다.
- [x] 로그가 남았는가
  `practice3_minimal_mcp.log`와 `practice3_server_stderr.log`가 남았다.
- [x] 규칙 적용 전후 차이를 설명할 수 있는가
  이 실습은 규칙 비교가 아니라 서버 구현 실습이므로 해당 차이 설명은 실습 2에서 이미 충족했다.
- [x] 실패 사례가 있었다면 원인을 적었는가
  잘못된 directory와 limit 입력이 검증 오류로 반환된 것을 결과와 로그에 남겼다.
- [x] 체크리스트 또는 짧은 회고 문서가 있는가
  현재 문서와 `practice3-summary.md`로 남겼다.

## 제출물 반영 상태

- [x] MCP 사용 기록 1회 이상
  실습 1과 실습 3에서 충족
- [x] 규칙 적용 전후 비교 기록 1회
  실습 2에서 충족
- [x] 최소 MCP 서버 코드
  `practice/week3/code/practice3_minimal_mcp_server.py`
- [x] 실행 로그 1개 이상
  `practice/week3/logs/practice3_minimal_mcp.log`
- [x] 출력 파일 1개 이상
  `practice/week3/output/practice3_mcp_result.json`
- [x] 체크리스트 또는 짧은 회고 문서
  `practice/week3/docs/practice3-checklist.md`

## 실패 사례와 원인

- 잘못된 directory 입력은 허용된 폴더 목록 오류로 반환됐다.
- 잘못된 limit 입력은 범위 오류로 반환됐다.
- 둘 다 의도한 검증 실패 사례로 기록했다.

## 짧은 회고

- 아주 작은 읽기 전용 MCP 서버여도 구조를 직접 만들고 호출해보니 실습 목표에 맞게 핵심이 분명해졌다.
- 도구 설명, 입력 검증, 오류 메시지, 테스트 절차가 모두 눈에 보이는 형태로 남았다.
