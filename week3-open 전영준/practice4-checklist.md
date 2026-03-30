# 실습 4 체크리스트

## 실습 개요

- 실습명: Plugin은 선택 실습으로 보기
- plugin 예시 폴더: `practice/week3/plugin/week3-plugin`
- 메타데이터 파일: `plugin.json`
- MCP 설정 파일: `.mcp.json`
- skill 파일: `skills/doc-summary/SKILL.md`
- 구조 기록: `practice/week3/output/practice4_plugin_structure.json`
- 로그 파일: `practice/week3/logs/practice4_plugin_structure.log`

## 학생이 직접 확인할 것

- [x] 묶음 구조가 한눈에 보이는가
  plugin 메타데이터, MCP 설정, skill 파일이 한 폴더에 모여 있다.
- [x] 어떤 역할을 묶는지 설명 가능한가
  plugin은 MCP 설정과 skill을 함께 묶는 단위라는 점을 README에 적었다.
- [x] 실제 제품 포맷과 수업용 예시를 구분했는가
  `plugin.json`과 README에 수업용 예시임을 명시했다.
- [x] 나중에 확장 가능한 구조인가
  `skills/` 디렉터리를 분리해 추가 skill을 넣기 쉽게 만들었다.

## 작업 전

- [x] 어떤 구조를 만들지 정했는가
  `plugin.json + .mcp.json + skills/doc-summary/SKILL.md` 구조로 정했다.
- [x] 어떤 내용을 넣을지 정했는가
  실습 3의 최소 MCP 서버와 문서 요약 skill을 묶기로 정했다.
- [x] 출력 위치를 정했는가
  `practice/week3/plugin/week3-plugin` 아래와 `practice/week3/output` 아래에 두기로 정했다.
- [x] 검증 방법을 정했는가
  폴더 구조, 파일 역할, README 설명, 구조 기록 JSON 존재 여부를 확인하기로 정했다.
- [x] 위험한 동작이 없는가
  설정 파일과 문서만 생성했고 삭제나 이동은 없었다.

## 작업 후

- [x] 실제 묶음 구조가 남았는가
  plugin 폴더와 내부 파일들이 생성되었다.
- [x] 결과 파일이 남았는가
  `plugin.json`, `.mcp.json`, `SKILL.md`, `README.md`, `practice4_plugin_structure.json`이 남았다.
- [x] 로그가 남았는가
  `practice4_plugin_structure.log`를 생성했다.
- [x] plugin 역할을 설명할 수 있는가
  README와 체크리스트에 묶음 배포 방식으로 정리했다.
- [x] 실패 사례가 있었다면 원인을 적었는가
  별도 실패 사례는 없었다.
- [x] 체크리스트 또는 짧은 회고 문서가 있는가
  현재 문서와 `practice4-summary.md`로 남겼다.

## 제출물 반영 상태

- [x] MCP 사용 기록 1회 이상
  실습 1과 실습 3에서 충족
- [x] 규칙 적용 전후 비교 기록 1회
  실습 2에서 충족
- [x] 최소 MCP 서버 코드
  실습 3에서 충족
- [x] 실행 로그 1개 이상
  실습 1~4에서 충족
- [x] 출력 파일 1개 이상
  실습 1~4에서 충족
- [x] 체크리스트 또는 짧은 회고 문서
  `practice/week3/docs/practice4-checklist.md`

## 짧은 회고

- plugin은 실제 제품 종속 포맷보다 먼저, 무엇을 한 묶음으로 배포하는지 이해하는 것이 중요하다는 점을 구조로 보여줄 수 있었다.
