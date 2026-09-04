# Coding Test Version Lock

- 기준일: 2026-09-03 (Asia/Seoul)
- 정책: 이 파일의 버전은 사용자가 명시적으로 갱신을 요청하기 전까지 과정 중 자동 변경하지 않는다.
- 채널 원칙: Stable / GA만 사용한다. Alpha / Beta / RC / Nightly / Preview는 기본 과정에서 사용하지 않는다.

| Category | Tool | Locked Version | Channel | Official Source | Notes |
|---|---|---:|---|---|---|
| IDE | Cursor Desktop | 3.18 | Latest Stable | https://cursor.com/download | 공식 다운로드 페이지에서 `3.18 Latest` 확인. 전체 224일 과정 기본 IDE |
| Runtime | Python | 3.14.7 | Stable | https://www.python.org/downloads/release/python-3147/ | 2026-08-05 공개된 3.14 계열 유지보수 릴리스. 전체 과정 기본 언어 |

## Stable 선택 메모

- Python 3.15.0rc2는 2026-09-01 공개된 **Release Candidate**이므로 본 과정에서는 사용하지 않는다.
- Python 3.14.7을 Stable로 고정한다.
- Cursor는 공식 다운로드 페이지의 최신 데스크톱 버전 `3.18 Latest`를 고정한다.

## 전체 과정에서 기본적으로 사용하는 Python 표준 라이브러리

설치가 필요 없는 표준 라이브러리만 우선 사용한다.

- `sys`
- `collections`
- `heapq`
- `bisect`
- `itertools`
- `functools`
- `math`

새 외부 도구가 실제 커리큘럼에서 필요해지는 최초 Day에만 이 표를 확장한다.
