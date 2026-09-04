# PROJECT_RULES.md

## 목표

이 저장소는 98일 동안 “기술을 많이 넣는 것”이 아니라 **제한된 시간 안에 요구사항을 해석하고, 검증 가능한 결과물을 제출하며, 자기 코드를 설명하고 변경할 수 있는 능력**을 훈련한다.

## 고정 규칙

1. IDE는 Cursor를 사용한다.
2. `VERSION_LOCK.md`를 기준으로 하고 임의 업그레이드하지 않는다.
3. 과제를 받으면 바로 코딩하지 않는다. 정책 → 요구사항 → 모호함/가정 → 우선순위 → 계획 순서로 간다.
4. AI 출력은 증거가 아니다. 사람이 diff를 읽고 테스트·공식 문서로 검증한다.
5. 작은 과제에서 불필요한 Kafka, Redis, Kubernetes, Microservice, 과도한 DDD/Hexagonal 구조를 기본 선택으로 넣지 않는다.
6. 기존 repository 과제는 기존 convention과 tests를 먼저 읽고 최소 변경한다.
7. 실제 기업 공개 과제는 원문 전체를 복제하거나 공개 답안 repository로 재배포하지 않는다.
8. 실행했다고 주장하려면 실제 command와 observed result가 있어야 한다.
9. Secret/API key는 `.env.example`에 실제 값으로 넣지 않는다.
10. 제출 직전 `git diff`, 테스트, README 실행 절차, clean clone 관점을 확인한다.

## Evidence 우선순위

```text
Requirement traceability
> Reproducible execution
> Core behavior
> Risk-based tests
> Data integrity
> README / decisions
> Error handling
> CI
> Security / performance
> Bonus features
```

## 문서 작성 규칙

- 문서는 평가자가 5분 안에 핵심을 찾을 수 있게 짧고 구조적으로 쓴다.
- 사실, 가정, 추론을 구분한다.
- 시간 부족으로 포기한 항목은 숨기지 않고 Known Limitations / If I Had More Time에 기록한다.
- AI가 대신 작성한 설명을 이해하지 못한 채 제출하지 않는다.

## Commit 예시

좋음:

```text
feat: add reservation creation
test: cover duplicate slot reservation
fix: enforce unique reservation constraint
docs: explain concurrency trade-off
```

피함:

```text
update
fix
final
real-final
```
