# Hook 설계 메모

## 목표

- 문서 규칙을 사람이 직접 확인하는 수준에서 끝내지 않고, 작업 완료 뒤 자동 검증으로 확장한다.

## 선택한 hook 아이디어

- 작업 완료 후 `output/` 생성 여부 검사
- 핵심 결과 파일이 없으면 실패로 간주

## 적용 방식

- 스크립트: `practice/week3/hooks/check_outputs.ps1`
- 검사 대상:
  - `practice/week3/output/`
  - `practice/week3/output/summary.md`
  - `practice/week3/output/practice3_mcp_result.json`
- 보조 경고:
  - 정상/오류 입력 테스트 스크립트가 없으면 경고
  - 테스트 로그가 없으면 경고

## 기대 효과

- 문서 규칙만 둘 때보다 결과 누락을 더 빨리 발견할 수 있다.
- 출력 파일이 없으면 바로 실패로 표시되어 제출 직전 확인이 쉬워진다.
- 사람이 매번 같은 체크를 반복하지 않아도 된다.

## 실행 예시

```powershell
powershell -ExecutionPolicy Bypass -File practice/week3/hooks/check_outputs.ps1
```

## 산출물

- 결과 JSON: `practice/week3/output/practice5_hook_report.json`
- 실행 로그: `practice/week3/logs/practice5_hook.log`
