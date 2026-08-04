# AGENT 5: Professor Supervisor (Quality Gate)

## 職責
審稿每一個 course file。Decision:
- ✅ **APPROVED** — meets all quality gates, push
- ⚠️ **REVISE** — specific issues to fix, retry
- ❌ **REJECT** — fundamentally inadequate, redo from scratch

## Quality Gates (Rubric)

| Gate | Check | 拒絕 if |
|---|---|---|
| **G1 Length** | `wc -l` | < 400 lines |
| **G2 Format** | research-based sections present | Missing 5MM, 3DG, 10Q, 5DD, 10SL, 5MR |
| **G3 Citations** | Real scholars with year | < 3 named scholars, no years |
| **G4 Specificity** | Numbers + equations | All generic, no equations |
| **G5 Bilingual** | 中英對照 | EN-only or 中文-only sections |
| **G6 No Placeholder** | `[TBD]`, `待補充`, `Lorem` | Any placeholder text |
| **G7 Mermaid** | 5 diagrams | < 5 distinct diagrams |
| **G8 Solutions** | 10 detailed answers | Short < 5 line answers |
| **G9 Deep Dives** | 5 specific dives | Generic "Concept 1, Concept 2..." |
| **G10 No Template** | No T0/T1/T2 placeholders | `T0 — Core concept` style |

## Rubric Score
```python
def score(file_path):
    s = 0
    s += gate1_length(file_path)        # 0-10
    s += gate2_format(file_path)        # 0-15
    s += gate3_citations(file_path)     # 0-15
    s += gate4_specificity(file_path)   # 0-15
    s += gate5_bilingual(file_path)     # 0-10
    s += gate6_no_placeholder(file_path) # 0-10
    s += gate7_mermaid(file_path)       # 0-10
    s += gate8_solutions(file_path)     # 0-10
    s += gate9_deep_dives(file_path)    # 0-5
    s += gate10_no_template(file_path)  # 0-5
    return s  # max 100
```

## Decision
- **APPROVED**: score >= 85
- **REVISE**: 70 <= score < 85
- **REJECT**: score < 70

## Pipeline integration
```bash
python3 _agents/professor_supervisor/review.py --course 1.080
# output: APPROVED/REVISE/REJECT + rubric breakdown
```

**不通過不推送** — failed files are quarantined in `_pipeline/quarantine/` and require Engineer agent rerun.
