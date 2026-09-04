# Take-home 2026 Version Lock

- 기준일: **2026-09-03 (Asia/Seoul)**
- 원칙: **Stable / GA / LTS만 기본 실습에 사용**한다.
- 유지 규칙: 사용자가 명시적으로 버전 갱신을 요청하기 전까지 Day 98까지 이 Lock을 유지한다.
- Spring 계열: Spring Boot BOM / Dependency Management를 우선하며 Spring Security, Spring Data, Jackson, Micrometer 등 하위 모듈을 임의로 개별 최신화하지 않는다.
- 설치 시점: Day 1에 전부 설치하지 않는다. 해당 기술이 처음 필요한 Day에 이 파일의 버전을 사용한다.

## 1. Course baseline

| Category | Technology | Locked Version | Status | First major use | Official source | Lock reason |
|---|---|---:|---|---:|---|---|
| IDE | Cursor | 3.9 | Stable desktop line | Day 1 | https://cursor.com/downloads | 과정 전체 IDE 고정 |
| Language | Java | 25.0.4.1 | LTS / GA | Day 8 | https://www.oracle.com/java/technologies/javase/25all-relnotes.html | Java 25 LTS 최신 CPU/patch 기준 |
| Backend | Spring Boot | 4.1.1 | Stable | Day 8 | https://spring.io/projects/spring-boot | Boot BOM을 호환성 기준으로 사용 |
| Build | Gradle | 9.7.1 | Stable | Day 8 | https://gradle.org/releases/ | Wrapper로 재현성 고정 |
| Database | PostgreSQL | 18.6 | Stable | Day 18/22 | https://www.postgresql.org/docs/release/18.6/ | PG 19 beta가 아닌 안정화 라인 |
| DB migration | Flyway Engine | 13.4.0 | Stable | Day 23 | https://documentation.red-gate.com/flyway/reference/release-notes | 스키마 변경 재현성 |
| Integration test | Testcontainers Java | 2.0.5 | Stable | Day 18 | https://github.com/testcontainers/testcontainers-java/releases/tag/2.0.5 | 실제 PostgreSQL 통합 테스트 |
| API docs | springdoc-openapi | 3.0.3 | Stable | Day 12 | https://github.com/springdoc/springdoc-openapi/releases/tag/v3.0.3 | Spring Boot 4.x 계열 API 문서 |
| Runtime | Node.js | 24.20.0 | LTS (Krypton) | Day 36 | https://nodejs.org/en/blog/release/v24.20.0 | 프론트 도구 실행 기반 |
| Frontend | React | 19.2.7 | Stable 19.2 line | Day 36 | https://react.dev/versions | 과정 프론트 기준 |
| Language | TypeScript | 7.0.2 | Stable | Day 36 | https://github.com/microsoft/typescript-go/releases/tag/v7.0.2 | 타입 경계 훈련 |
| Build | Vite | 8.1.0 | Stable | Day 36 | https://github.com/vitejs/vite/releases/tag/v8.1.0 | 빠른 프론트 빌드/개발 서버 |
| Server state | TanStack Query | 5.102.2 | Stable | Day 38 | https://github.com/TanStack/query/releases/tag/v5.102.2 | 서버 상태 처리 |
| Frontend test | Vitest | 4.1.11 | Stable | Day 40 | https://github.com/vitest-dev/vitest/releases/tag/v4.1.11 | 컴포넌트/유닛 테스트 |
| Frontend test | React Testing Library | 16.3.2 | Stable | Day 40 | https://github.com/testing-library/react-testing-library/releases/tag/v16.3.2 | 사용자 행동 중심 테스트 |
| E2E | Playwright | 1.62.1 | Stable | Day 41 | https://github.com/microsoft/playwright/releases/tag/v1.62.1 | 핵심 사용자 여정 검증 |
| Container desktop | Docker Desktop | 4.89.0 | Stable | Day 44 | https://docs.docker.com/desktop/release-notes/ | 로컬 재현 환경 |
| Compose | Docker Compose | 5.5.0 | Stable | Day 45 | https://docs.docker.com/desktop/release-notes/ | DB 포함 원-command 실행 |
| Observability | OpenTelemetry Java API/SDK | 1.65.0 | Stable | Day 55 | https://github.com/open-telemetry/opentelemetry-java/releases/tag/v1.65.0 | trace 개념/실습 기준 |
| CI action | actions/checkout | 7.0.1 (`@v7`) | Stable | Day 50 | https://github.com/actions/checkout/releases | checkout action major 고정 |
| CI action | actions/setup-java | 6.0.0 (`@v6`) | Stable | Day 50 | https://github.com/actions/setup-java/releases | JDK setup action major 고정 |
| CI action | actions/setup-node | 7.0.0 (`@v7`) | Stable | Day 50 | https://github.com/actions/setup-node/releases | Node setup action major 고정 |
| CI action | actions/cache | 5.0.5 (`@v5`) | Stable | Day 50 | https://github.com/actions/cache/releases | 캐시 action major 고정 |

> `Exact version`과 GitHub Actions의 `@major` 사용은 목적이 다르다. 앱/라이브러리는 재현성을 위해 정확한 버전을 적고, 공식 Action은 해당 major의 보안/patch 업데이트를 받도록 major tag 사용을 기본으로 한다. 평가 규칙이 SHA pinning을 요구하면 그 규칙이 우선한다.

## 2. Day 1에서 실제 설치해야 하는 것

Day 1의 본래 목적은 환경 구축이 아니라 **평가 방식 전체 지도를 이해하는 것**이다. 따라서 오늘 필수는 다음 정도다.

```text
Cursor
Git
Markdown을 읽고 편집할 수 있는 환경
```

Java/Spring/PostgreSQL/Node/Docker는 각 기술이 처음 필요한 Day에 설치·검증한다. 버전은 위 표를 그대로 사용한다.

## 3. 검증 규칙

새 기술을 실제로 설치하는 Day에는 다음을 기록한다.

```text
1. 실제 설치 버전 확인 명령
2. VERSION_LOCK.md와 일치 여부
3. 호환성 문제 여부
4. Preview/Beta가 섞이지 않았는지
```

예시:

```bash
java -version
./gradlew --version
psql --version
node --version
docker version
docker compose version
```

## 4. 버전 변경 금지 규칙

다음 이유만으로 버전을 올리지 않는다.

- 새 버전이 방금 출시됨
- AI가 더 최신이라고 추천함
- 블로그 예제가 다른 버전을 사용함
- dependency update bot이 제안함

버전 갱신은 별도 작업으로 다루고, 공식 릴리스·호환성·테스트를 확인한 뒤 결정한다.
