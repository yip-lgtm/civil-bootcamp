# civil-bootcamp

[![CI](https://github.com/yip-lgtm/civil-bootcamp/actions/workflows/ci.yml/badge.svg)](https://github.com/yip-lgtm/civil-bootcamp/actions/workflows/ci.yml)

**MIT CEE Self-Study Bootcamp**  
Bachelor equivalent → MEng Structural Mechanics & Design → ICE Professional (IEng/CEng MICE)

Source: [MIT CEE](https://cee.mit.edu/) + [SMD Track](https://cee.mit.edu/structural-mechanics-and-design-smd-track/)

---

## Course 1-ENG Degree Structure

This repository mirrors the **MIT CEE Course 1-ENG (Bachelor of Science in Civil Engineering)** degree structure exactly.

| # | Bucket | Folder | Units / Subjects |
|---|---|---|---|
| 1 | **GIRs** (General Institute Requirements) | [`MIT_CEE_GIRs/`](./MIT_CEE_GIRs/) | 17 subjects |
| 2 | **GDRs** (General Department Requirements) | [`MIT_CEE_GDRs/`](./MIT_CEE_GDRs/) | 54 units |
| 3 | **CORE** (Core Coursework) | [`MIT_CEE_Core/`](./MIT_CEE_Core/) | 54–66 units |
| 4 | **REs** (Restricted Electives) | inside each Track folder | 48–60 units |
| 5 | **UREs** (Unrestricted Electives) | [`MIT_CEE_UREs/`](./MIT_CEE_UREs/) | 48–60 units |
| 6 | **MEng SMD** (graduate, post-bachelor) | [`MIT_CEE_MEng_SMD/`](./MIT_CEE_MEng_SMD/) | 90 units |

### The three Core Tracks (choose ONE)

| Track | Folder | Sub-areas |
|---|---|---|
| **Environment** | [`MIT_CEE_Core/Track_1_Environment/`](./MIT_CEE_Core/Track_1_Environment/) | Environmental life sciences · Fluids and transport engineering |
| **Mechanics & Materials** | [`MIT_CEE_Core/Track_2_Mechanics_Materials/`](./MIT_CEE_Core/Track_2_Mechanics_Materials/) | Structural Design · Materials |
| **Energy, Transportation & Societal Systems** | [`MIT_CEE_Core/Track_3_Energy_Transportation_Societal_Systems/`](./MIT_CEE_Core/Track_3_Energy_Transportation_Societal_Systems/) | Transportation and Urban Systems · Energy Systems |

---

## 📂 Course Format — 袁騰飛格式 (5MM / 3DG / 10Q / 5DD / 10SL / 5MR)

每一個 course file 都係用 **袁騰飛格式** 寫成。每個 course 有：

| 元素 | 數量 | 內容 | 品質門檻 |
|---|---|---|---|
| **5MM** | 5 | 核心心智模型 + 方程式 + 真實數字 + 學者 | Specific, 拒 generic |
| **3DG** | 3 | 根本分歧 + A/B 兩方 + 引用 | Position A + 學者, Position B + 學者 |
| **10Q** | 10 | 深度問題 + 詳解 + 中英對照 | Probing, 區分 deep vs memorize |
| **5DD** | 5 | Deep Dive + Bilingual 概念對照 + Key Derivation | 拒絕 "Core concept" placeholder |
| **10SL** | 10 | Solutions + worked example | 必須有 specific numbers |
| **5MR** | 5 | Mermaid 圖 | stateDiagram/flowchart/class/sequence/er |

---

## 🛠️ Multi-Agent Course Generation Pipeline

所有 course files 經過 **5-Agent Pipeline** 嚴格審核：

```
┌─────────────────────────────────────────┐
│  1. Researcher                          │
│     查 MIT Catalog / OCW / 教科書        │
│     品質門檻: 必須有 primary source     │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  2. Data Extractor                      │
│     提取 course 目標/prereq/主題/學習成果│
│     品質門檻: 無推測, verifiable        │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  3. Engineer (袁騰飛 Producer)          │
│     5MM + 3DG + 10Q + 5DD + 10SL       │
│     品質門檻: Specific, 禁通用廢話      │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  4. Diagram                             │
│     5 個 Mermaid 圖                     │
│     品質門檻: 對應本課程, 禁模板圖      │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  5. Professor Supervisor (Quality Gate) │
│     APPROVED / REVISE / REJECT          │
│     品質門檻: 不通過不推送              │
└─────────────────────────────────────────┘
```

### Agent 目錄

- [`_agents/researcher/`](./_agents/researcher/) — 查 primary sources
- [`_agents/data_extractor/`](./_agents/data_extractor/) — 提取 objectives/themes
- [`_agents/engineer/`](./_agents/engineer/) — 袁騰飛格式 producer
- [`_agents/diagram/`](./_agents/diagram/) — 5 Mermaid diagrams
- [`_agents/professor_supervisor/`](./_agents/professor_supervisor/) — Quality gate reviewer

### Pipeline Orchestrator

```bash
# Single course
python3 _pipeline/run_pipeline.py --course 1.080

# Review all courses
python3 _agents/professor_supervisor/review.py --all
```

### Quality Gates (10 gates, 100 points)

| Gate | Check | 拒絕 if |
|---|---|---|
| **G1 Length** | `wc -l` | < 400 lines |
| **G2 Format** | 袁騰飛 sections | Missing 5MM, 3DG, 10Q, 5DD, 10SL |
| **G3 Citations** | Real scholars + year | < 3 named scholars |
| **G4 Specificity** | Numbers + equations | < 3 equations |
| **G5 Bilingual** | 中英對照 | EN-only section |
| **G6 No Placeholder** | `[TBD]`, `待補充`, `CORE_DEEPDIVE` | Any placeholder |
| **G7 Mermaid** | 5 diagrams | < 5 |
| **G8 Solutions** | 10 detailed | < 10 numbered |
| **G9 Deep Dives** | 5 specific | Generic "Concept 1, 2, 3..." |
| **G10 No Template** | No T0/T1/T2 | `T0 — Core` style |

**Decision:**
- ✅ **APPROVED** ≥ 85
- ⚠️ **REVISE** 70-84
- ❌ **REJECT** < 70 (auto-quarantine, no push)

---

## ❌ 拒絕 Garbage

**呢啲內容全部禁止:**

- `[TBD]`, `待補充`, `placeholder`, `Lorem ipsum`
- `T0 — Core concept`, `T1 — Methods`, `T2 — Applications`
- `CORE_DEEPDIVE_ONE/TWO/THREE/FOUR/FIVE` template headers
- 通用 "Core concepts 嘅 foundation" 冇 details
- 冇 equation, 冇 number, 冇 scholar 嘅 paragraph
- 純 definition 嘅 question ("What is X?")
- 冇 detailed answer 嘅 10Q list
- 一式一樣嘅 5 個 Mermaid graph TD 模板

---

## How to use

Self-study path:

1. **Year 1–2:** Complete GIRs (alongside) and GDRs (18.03, 1.000 first)
2. **End of Year 2:** Choose a Core Track
3. **Year 3–4:** Complete CORE + REs in the chosen Track
4. **Year 4:** Capstone design / thesis
5. **Post-grad:** MEng SMD (natural continuation for the Mechanics & Materials track)
6. **ICE:** Write Professional Review evidence from the Capstone and Project files

---

## CI/CD

GitHub Actions pipeline runs on every push and pull request to `main`:

- **Structure:** top-level folders, 00_INDEX.md files, critical course files
- **Markdown lint:** markdownlint-cli with project style (advisory)
- **Content quality:** runs Professor Supervisor `review.py` on each course file

Workflow: [`.github/workflows/ci.yml`](./.github/workflows/ci.yml)
Reviewer: [`_agents/professor_supervisor/review.py`](./_agents/professor_supervisor/review.py)
