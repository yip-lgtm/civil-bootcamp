# civil-bootcamp

[![CI](https://github.com/yip-lgtm/civil-bootcamp/actions/workflows/ci.yml/badge.svg)](https://github.com/yip-lgtm/civil-bootcamp/actions/workflows/ci.yml)

**MIT CEE Self-Study Bootcamp**  
Bachelor equivalent → MEng Structural Mechanics & Design → ICE Professional (IEng/CEng MICE)

Source: [MIT CEE](https://cee.mit.edu/) + [SMD Track](https://cee.mit.edu/structural-mechanics-and-design-smd-track/)

## Tracks

| Folder | Description |
|--------|-------------|
| `MIT_CEE_Structural_Design_Track/` | Core Structural Design (1.050, 1.035, 1.036, 1.060, Design, Capstone, GDR) |
| `MIT_CEE_Materials_Track/` | Materials & Geotech focus |
| `MIT_CEE_Environmental_Track/` | Environment, Transport, Chemistry, TREX |
| `MIT_CEE_Transportation_Track/` | Networks, Sustainability, Water Resources |
| `MIT_CEE_Microbiology_Track/` | Fluids & Disease, Cancer Risks |
| `MIT_CEE_MEng_SMD/` | MEng core (1.562/563) + electives (1.573, 1.581, 1.541, Geotech, Engineering Mechanics) |

## File Format (every course)

1. **5 core mental models** every expert shares
2. **3 fundamental disagreements** + strongest arguments of each side
3. **10 deep questions** that distinguish real understanding from memorization

All content is bilingual (中英對照).

## How to use

Study in order: Structural Design → choose specialization track → MEng SMD electives → write ICE Professional Review evidence from the Capstone and Project files.

## CI/CD

GitHub Actions pipeline runs on every push and pull request to `main`:

- Validates all 6 track folders exist
- Checks critical course files and INDEX files
- Counts markdown files (expects ≥ 30)
- Basic structure check for the standard 3-question format

Workflow file: `.github/workflows/ci.yml`
