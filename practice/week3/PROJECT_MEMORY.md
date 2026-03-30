# Project Memory Draft

## 출력 위치

- 기본 출력 폴더는 `practice/week3/output/`이다.
- 비교 문서와 자동 검증 결과도 가능하면 이 폴더 안에 둔다.

## 기본 검증 절차

1. MCP 관련 작업 후 실제 호출 기록이 남았는지 확인한다.
2. 결과 파일이 `output/` 또는 제출 폴더에 존재하는지 확인한다.
3. 로그 파일이 남았는지 확인한다.
4. 규칙 적용 전후 차이가 있다면 비교 문서에 적는다.
5. 실패 사례가 있으면 원인과 수정 사항을 체크리스트에 적는다.

## 금지 또는 주의 명령

- `git reset --hard`
- `git checkout -- <file>`
- 무차별 `Remove-Item -Recurse`
- 출력 파일을 검증 없이 삭제하는 작업

## 세션 간 일관성을 위한 기억

- 요약 결과는 항상 `output/summary.md`를 우선 확인한다.
- 최소 MCP 서버 테스트는 `03_minimal_mcp_test.py`를 기준으로 재현한다.
- 제출 전에는 `week3-submission-guide.md`, `week3-final-summary.md`, `week3-tracker.md`를 함께 확인한다.
