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
