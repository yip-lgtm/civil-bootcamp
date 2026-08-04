# AGENT 1: Researcher

## 職責
- 查 MIT Catalog、OCW、教科書真實內容
- 找出 primary source (paper, textbook chapter, technical report)
- 確認 instructor + course number + 學期
- 列出真實事件 / 真實數字 / 真實學者

## 品質門檻 (Quality Gate)
- ✅ 必須有 primary source citation (URL or textbook)
- ✅ 必須有真實日期 / 數字 / 學者名
- ❌ 拒絕 generic Wikipedia-only research
- ❌ 拒絕未經 verify 嘅二手 source

## Output
Produces `course_brief.json`:
```json
{
  "course_code": "1.080",
  "title": "Environmental Chemistry",
  "instructors": ["Hemond (former)", "Kroll Group"],
  "prereq": ["Chemistry GIR"],
  "primary_sources": [
    "Hemond & Fechner (2000) Chemical Fate and Transport",
    "MIT OCW 1.725",
    "MIT Catalog 2024-25"
  ],
  "key_authors": ["Stumm & Morgan 1996", "Schwarzenbach 2003"],
  "key_numbers": ["OH ≈ 10^6 molecules cm^-3", "CH4 lifetime ≈ 9 yr"],
  "key_dates": ["1952 London smog", "1986 Chernobyl", "1972 DDT ban"]
}
```

## Tools
- `web_search` (MIT Catalog, OCW, JSTOR)
- `web_fetch` (primary sources)
- `scholar_lookup.py`

## Output script
```bash
python3 _agents/researcher/lookup.py --course 1.080
```
