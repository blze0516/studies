# VERSION_LOCK — backend-interview-lab

- 잠금 기준일: 2026-09-10 (Asia/Seoul)
- 정책: 이 파일의 버전은 10주 과정 종료까지 임의 변경하지 않는다.
- 예외: 치명적 보안 취약점 또는 공식 호환성 문제로 즉시 교체가 필요한 경우에만 변경하고 변경 사유를 기록한다.

## 1. 핵심 개발 환경

| 항목 | 잠금 버전 | 선택 이유 |
|---|---:|---|
| Cursor | 3.19 Stable | 공식 다운로드 페이지의 최신 Desktop 안정 버전 |
| Java / JDK | 25.0.4.1 (LTS) | Java 25는 LTS이며 25.0.4.1은 2026-08-18 GA 업데이트. Spring Boot 4.1.x 및 Gradle 9.7.1 지원 범위 안에 있음 |
| Spring Boot | 4.1.1 | 공식 Spring 문서에서 최신 Stable |
| Spring Framework | 7.0.9 | Spring Boot 4.1.1이 관리하는 버전 |
| Gradle | 9.7.1 | 공식 Releases의 최신 안정 패치. Java 25 실행 지원 |
| Gradle DSL | Kotlin DSL | 과정 고정 정책 |

## 2. 데이터/미들웨어/운영 도구

| 항목 | 잠금 버전 | 비고 |
|---|---:|---|
| PostgreSQL | 18.6 | 18 메이저의 현재 minor |
| Redis Open Source | 8.10.1 | 8.10 GA 계열의 2026-08 보안 패치 포함 버전 |
| Apache Kafka | 4.3.1 | 공식 Supported release |
| Docker Desktop | 4.90.0 | 2026-09-07 공식 안정 릴리스 |
| Docker Engine | 29.8.0 | Linux에서 직접 Engine을 쓸 경우의 최신 안정 버전 |
| Docker Compose | 5.5.0 | Docker 공식 설치 문서의 최신 Compose plugin |

## 3. 테스트/마이그레이션 라이브러리

아래는 Spring Boot 4.1.1의 dependency management(BOM)를 우선 사용한다. `build.gradle.kts`에서 특별한 이유가 없으면 개별 버전을 직접 쓰지 않는다.

| 항목 | Boot 4.1.1 관리 버전 |
|---|---:|
| JUnit Jupiter | 6.0.3 |
| AssertJ | 3.27.7 |
| Testcontainers | 2.0.5 |
| Flyway | 12.4.0 |

## 4. 과정 고정 데이터

| 항목 | 값 |
|---|---|
| dataset | `backend_interview_fixed_sample_dataset.json` |
| dataset_version | `1.0.0` |
| canonical path | `src/main/resources/data/backend_interview_fixed_sample_dataset.json` |
| timezone | `Asia/Seoul` |
| expansion seed | `20260910` |

Day 1 검증 결과: users 12, products 15, inventory 15, orders 30, order_items 50, payments 30, stock_movements 38, events 25, api_logs 40. 주문 상세 합계와 `orders.total_amount` 불일치 0건, 주요 참조 무결성 오류 0건.

## 5. 공식 확인 출처

- Cursor Downloads: https://cursor.com/download
- Oracle JDK 25 consolidated release notes: https://www.oracle.com/java/technologies/javase/25all-relnotes.html
- Oracle Java SE Support Roadmap: https://www.oracle.com/java/technologies/java-se-support-roadmap.html
- Spring Boot 4.1.1 release: https://spring.io/blog/2026/08/20/spring-boot-4-1-1-available-now/
- Spring Boot managed dependencies: https://docs.spring.io/spring-boot/appendix/dependency-versions/coordinates.html
- Spring Boot Gradle plugin: https://docs.spring.io/spring-boot/gradle-plugin/
- Gradle Releases: https://gradle.org/releases/
- Gradle Java compatibility: https://docs.gradle.org/current/userguide/compatibility.html
- PostgreSQL versioning policy: https://www.postgresql.org/support/versioning/
- Redis 8.10 release notes: https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.10-release-notes/
- Kafka downloads: https://kafka.apache.org/community/downloads/
- Docker Desktop release notes: https://docs.docker.com/desktop/release-notes/
- Docker Engine 29 release notes: https://docs.docker.com/engine/release-notes/29/
- Docker Compose installation: https://docs.docker.com/compose/install/linux/
