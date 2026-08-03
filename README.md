# civil-bootcamp

[![CI](https://github.com/yip-lgtm/civil-bootcamp/actions/workflows/ci.yml/badge.svg)](https://github.com/yip-lgtm/civil-bootcamp/actions/workflows/ci.yml)

**MIT CEE Self-Study Bootcamp**  
Bachelor equivalent → MEng Structural Mechanics & Design → ICE Professional (IEng/CEng MICE)

Source: [MIT CEE](https://cee.mit.edu/) + [SMD Track](https://cee.mit.edu/structural-mechanics-and-design-smd-track/)

---

## Course 1-ENG Degree Structure

This repository mirrors the **MIT CEE Course 1-ENG (Bachelor of Science in
Civil Engineering)** degree structure exactly.

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

## File Format (every course)

1. **5 core mental models** every expert shares
2. **3 fundamental disagreements** + strongest arguments of each side
3. **10 deep questions** that distinguish real understanding from memorization
4. **5 deep dives** (one per mental model) with bilingual tables, derivations, decision flows
5. **10 detailed self-test solutions** (bilingual, with engineering implications)
6. **5 diagram sections** with Mermaid flowcharts (renders natively on GitHub)
7. **Closing 5-point "deep insights" summary**

All content is bilingual (中英對照).

## How to use

Self-study path:

1. **Year 1–2:** Complete GIRs (alongside) and GDRs (18.03, 1.000 first)
2. **End of Year 2:** Choose a Core Track
3. **Year 3–4:** Complete CORE + REs in the chosen Track
4. **Year 4:** Capstone design / thesis
5. **Post-grad:** MEng SMD (natural continuation for the Mechanics & Materials track)
6. **ICE:** Write Professional Review evidence from the Capstone and Project files

## CI/CD

GitHub Actions pipeline runs on every push and pull request to `main` (3 jobs):

- **Structure:** top-level folders, 00_INDEX.md files, critical course files
- **Markdown lint:** markdownlint-cli with project style (advisory)
- **Content quality:** per-file checks for 5 mental models, 3 disagreements, 10 deep questions, 5 deep dives, 10 solutions, diagram sections, Mermaid blocks

Workflow file: [`.github/workflows/ci.yml`](./.github/workflows/ci.yml)
Content check: [`.github/scripts/check_content.py`](./.github/scripts/check_content.py)
