# AGENT 2: Data Extractor

## 職責
從 Researcher 嘅 `course_brief.json` 提取：
- 課程目標 (Course Objectives)
- Prerequisite chain
- 5 個核心主題 (Key Themes)
- 學習成果 (Learning Outcomes) — measurable

## 品質門檻
- ✅ 必須從 primary source 提取
- ✅ 學習成果必須 verifiable / measurable
- ❌ 拒絕推測 (speculation)
- ❌ 拒絕 generic "understand X" 冇 details

## Output
Produces `course_data.json`:
```json
{
  "course_code": "1.080",
  "objectives": [
    "Apply mass-action law to environmental equilibria",
    "Predict pollutant fate using Keq and k_obs",
    "Design water treatment based on speciation chemistry"
  ],
  "prereq": ["18.03 Differential Eq", "Chemistry GIR"],
  "key_themes": [
    "Equilibrium (Keq, partitioning)",
    "Kinetics (k_obs, half-life)",
    "Redox chemistry",
    "Surface complexation",
    "Biogeochemical cycles"
  ],
  "learning_outcomes": [
    "Calculate carbonate speciation given DIC, pH, T",
    "Derive first-order decay constant from field data",
    "Design coagulation-flocculation train"
  ]
}
```

## Verification
- Cross-check with MIT OCW syllabus
- Cross-check with published textbook chapter objectives
