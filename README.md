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
| 7 | **HKIE Practice** | [`HKIE_Structural_Practice/`](./HKIE_Structural_Practice/) | Section 1 judgement |

### The three Core Tracks (choose ONE)

| Track | Folder | Sub-areas |
|---|---|---|
| **Environment** | [`MIT_CEE_Core/Track_1_Environment/`](./MIT_CEE_Core/Track_1_Environment/) | Environmental life sciences · Fluids and transport engineering |
| **Mechanics & Materials** | [`MIT_CEE_Core/Track_2_Mechanics_Materials/`](./MIT_CEE_Core/Track_2_Mechanics_Materials/) | Structural Design · Materials |
| **Energy, Transportation & Societal Systems** | [`MIT_CEE_Core/Track_3_Energy_Transportation_Societal_Systems/`](./MIT_CEE_Core/Track_3_Energy_Transportation_Societal_Systems/) | Transportation and Urban Systems · Energy Systems |

---

## HKIE Structural Practice

After the MIT design track, continue in [`HKIE_Structural_Practice/`](./HKIE_Structural_Practice/): 12-week tutorial plus Volume 1 structural behaviour and Volume 2 construction / statutory / contract judgement.

Start here: [`HKIE_Structural_Practice/00_INDEX.md`](./HKIE_Structural_Practice/00_INDEX.md)

---

## 📂 Course Format — Deep Study Format (5MM/3DG/10Q/5DD/10SL/5MR)

每一個 course file 都係用 **Deep Study Format (5MM/3DG/10Q/5DD/10SL/5MR)** 寫成。每個 course 有：

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

所有 course files 經過 **5-Agent Pipeline** 嚴格審核。Agent 目錄見 [`_agents/`](./_agents/)。Pipeline：`python3 _pipeline/run_pipeline.py --course 1.080`

### Quality Gates (10 gates, 100 points)

**Decision:** APPROVED ≥ 85 · REVISE 70-84 · REJECT < 70

---

## How to use

1. **Year 1–2:** GIRs and GDRs
2. **End of Year 2:** Choose a Core Track
3. **Year 3–4:** CORE + REs
4. **Year 4:** Capstone
5. **Post-grad:** MEng SMD
6. **HKIE Section 1:** [`HKIE_Structural_Practice/`](./HKIE_Structural_Practice/)
7. **ICE:** Professional Review evidence from Capstone and Project files

---

## CI/CD

GitHub Actions on push/PR to `main`: structure, markdownlint (advisory), content quality.

Workflow: [`.github/workflows/ci.yml`](./.github/workflows/ci.yml)
