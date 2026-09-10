# Take-home 2026 — 98 Day Practice Workspace

대기업 Take-home / AI-Assisted Coding / Repository-based Assessment 대비용 14주·98일 누적 워크스페이스.

## Day 1

주제: **2026 Take-home / Agentic Assessment 전체 지도**

핵심 산출물:

- `VERSION_LOCK.md`
- `PROJECT_RULES.md`
- `AI_POLICY.md`
- `lessons/day001/lecture.md`
- `lessons/day001/practice.md`
- `lessons/day001/exercises.md`
- `lessons/day001/review.md`
- `lessons/day001/assessment_landscape.md`

## Day 2

주제: **요구사항 추출과 Ambiguity Log**

핵심 산출물:

- `lessons/day002/lecture.md`
- `lessons/day002/practice.md`
- `lessons/day002/exercises.md`
- `lessons/day002/review.md`
- `docs/requirements/REQUIREMENTS.md`

Day 2에서는 모호한 예약 과제를 Functional/NFR/Constraint/Ambiguity/Assumption/Acceptance Criteria/Out of Scope로 분해한다. 버전 Lock은 변경하지 않는다.

### Day 2 확인

```bash
test -f docs/requirements/REQUIREMENTS.md && echo OK
grep -n 'FR-\|AMB-\|Q-\|ASM-\|AC-' docs/requirements/REQUIREMENTS.md
```


## Day 4

주제: **Acceptance Criteria + Definition of Done**

핵심 산출물:

- `lessons/day004/lecture.md`
- `lessons/day004/practice.md`
- `lessons/day004/exercises.md`
- `lessons/day004/exercise-solutions.md`
- `lessons/day004/review.md`
- `docs/requirements/ACCEPTANCE_CRITERIA.md`

Day 4에서는 Day 2~3의 예약 요구사항/Timebox를 Given/When/Then 15개와 Definition of Done으로 연결한다. 새 기술이 없으므로 `VERSION_LOCK.md`는 변경하지 않는다.

## Source of Truth

- Curriculum: `curriculum/take_home_assignment_curriculum.md`
- Lecture-generation rules: `prompts/take_home_assignment_lecture_prompt.md`
- Versions: `VERSION_LOCK.md`

## Day 1 확인

```bash
find lessons/day001 -maxdepth 1 -type f -print
sed -n '1,80p' VERSION_LOCK.md
sed -n '1,120p' lessons/day001/assessment_landscape.md
```

아직 애플리케이션 build는 없다. Day 1의 Evidence는 **평가 유형을 분류하고, 공개 과제에서 평가 신호를 근거와 함께 추출한 문서**다.


## Learning Progress

- Day 1: Complete
- Day 2: Complete
- Day 3: Complete — Must/Should/Could + Timeboxing
- Day 4: Complete — Acceptance Criteria + Definition of Done
