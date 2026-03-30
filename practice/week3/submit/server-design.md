# 최소 MCP 서버 설계 메모

## 서버 개요

- 서버 이름: `week3-minimal-server`
- 목적: `week3` 실습 폴더 안의 허용된 하위 폴더에서 Markdown 파일 목록만 읽기 전용으로 반환한다.
- 제공 도구: `list_markdown_files`

## 도구 설계

### 도구 이름

- `list_markdown_files`

### 도구 설명

- `docs`, `output`, `submit` 중 하나의 상대 디렉터리를 입력받아 Markdown 파일 목록을 반환한다.
- 반환 수는 `limit`로 제한한다.
- 삭제, 이동, 수정 기능은 제공하지 않는다.

### 입력 검증

- `directory`는 비어 있을 수 없다.
- `directory`는 `docs`, `output`, `submit` 중 하나만 허용한다.
- `limit`는 1 이상 20 이하만 허용한다.

### 오류 메시지 원칙

- 사용자가 바로 수정할 수 있도록 허용값을 포함한다.
- 내부 예외 이름보다 입력 조건을 먼저 설명한다.

## 테스트 절차

1. `python practice/week3/code/03_minimal_mcp_test.py`를 실행한다.
2. `tools/list` 결과에 `list_markdown_files`가 노출되는지 확인한다.
3. 정상 입력 `directory=docs`, `limit=5` 호출 결과를 확인한다.
4. 잘못된 입력 `directory=../class` 호출이 차단되는지 확인한다.
5. 잘못된 입력 `limit=0` 호출이 차단되는지 확인한다.
6. `practice/week3/output/practice3_mcp_result.json`과 `practice/week3/logs/practice3_minimal_mcp.log`를 확인한다.

## 기대 결과

- 정상 호출에서는 파일 목록이 JSON 문자열로 반환된다.
- 잘못된 입력에서는 읽기 쉬운 오류 메시지가 JSON 문자열로 반환된다.
- 서버 로그에는 도구 호출과 검증 실패 기록이 남는다.
