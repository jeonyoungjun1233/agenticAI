# 실습 1 요약

- 연결 서버: `practice/chapter4/code/4-6-weather-mcp-server.py`
- 연결 방식: stdio
- 확인된 도구: `get_current_weather`
- 호출 1: 위도 `91` 입력으로 검증 오류 응답 확인
- 호출 1 결과: `{"error": "위도는 -90에서 90 사이여야 합니다: 91.0"}`
- 호출 2: 서울 좌표 입력으로 환경 변수 오류 응답 확인
- 호출 2 결과: `{"error": "OPENWEATHERMAP_API_KEY 환경 변수가 설정되지 않았습니다."}`
- 핵심 확인:
  1. 도구 설명이 위도, 경도, 단위, 반환 형식을 포함해 구체적이었다.
  2. 잘못된 입력이 서버에서 즉시 차단되었다.
  3. 실패 원인이 오류 메시지에 직접 드러났다.
- 체크리스트 문서: `practice/week3/docs/practice1-checklist.md`
- 주차 추적 문서: `practice/week3/docs/week3-tracker.md`
