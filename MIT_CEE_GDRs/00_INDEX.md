# MIT_CEE_GDRs — General Department Requirements
**MIT Course 1-ENG | 54 Units**

---

The General Department Requirements (GDRs) are the units of coursework that
every CEE undergraduate must complete, **in addition to** the GIRs and the
chosen Core Track. They form the technical foundation common to all CEE
specializations.

**Source:** [MIT CEE Brochure (2023)](https://cee.mit.edu/wp-content/uploads/2021/05/CEE_Brochure_July2023.pdf)

## Required GDR subjects (per brochure)

| Course | Title | Units | File |
|---|---|---|---|
| 18.03 | Differential Equations | 12 | [18.03_Differential_Equations.md](./18.03_Differential_Equations.md) |
| 1.000 | Computer Programming & Numerical Methods for Engineering Applications | 12 | [1.000_Introduction_to_Computer_Programming_and_Numerical_Methods.md](./1.000_Introduction_to_Computer_Programming_and_Numerical_Methods.md) |
| 1.010A | Probability: Concepts and Applications | 6 | [1.010A_Probability_Concepts_and_Applications.md](./1.010A_Probability_Concepts_and_Applications.md) |
| 1.073 *or* 1.074 | Multivariate Data Analysis | 6 | [1.073_Introduction_to_Environmental_Data_Analysis.md](./1.073_Introduction_to_Environmental_Data_Analysis.md) / [1.074_Multivariate_Data_Analysis.md](./1.074_Multivariate_Data_Analysis.md) |
| 1.101 | Introduction to CEE Design I | 6 | [1.101_Introduction_to_CEE_Design.md](./1.101_Introduction_to_CEE_Design.md) |
| 1.013 | Senior CEE Design (Capstone) | 12 | [1.013_Senior_CEE_Design_Capstone.md](./1.013_Senior_CEE_Design_Capstone.md) |

> **Note on 1.010 / 1.010A:** The catalog shows the **1.010A** 6-unit version as the current
> GDR; the older **1.010** 12-unit "Uncertainty in Engineering" is shown in some
> degree sheets as an acceptable alternative. We track the modern 1.010A.

> **Note on 1.073 / 1.074:** Either satisfies the GDR. 1.073 is "Introduction to
> Environmental Data Analysis" (envt'l focus); 1.074 is "Multivariate Data
> Analysis" (general stats). We track 1.074.

## Self-study path

1. **Year 1–2:** GIRs (parallel with GDRs)
2. **Year 2:** Complete **18.03 + 1.000 + 1.010A + 1.074** early — they unlock all later CEE courses
3. **Year 2–3:** Complete **1.101** as the entry point to the design sequence
4. **Year 3:** Begin Core Track while completing **1.101**
5. **Year 4:** Complete **1.013** (Capstone) as the integrating experience

> **Tip:** 18.03, 1.000, 1.010A, 1.074 are **prerequisites for nearly every
> CEE course** — complete them first.


---

## 深入 1：CORE_DEEPDIVE_ONE — 核心概念
**Deep Dive I**

### 1.1 Bilingual 概念對照

| English | 中英對照 | Definition | 物理意義 / 工程應用 |
|---|---|---|---|
| Core concepts | Core concepts | Core definition | 核心定義 |
| Methods | Methods | Application | 應用 |
| Applications | Applications | Limitation | 限制 |
| Mathematical formulation | 數學形式 | Key equation | 關鍵方程 |

### 1.2 Key Derivation

For Course, the fundamental relationships are:
$$f(x) = \text{key equation}, \quad x = \text{variable}$$

This arises from Core concepts applied to the engineering system.

### 1.3 Engineering Applications

- Real-world implementation
- Design codes and standards
- Computational tools

```mermaid
graph TD
    A[Input: Core concepts] --> B[Analysis]
    B --> C[Decision]
    C --> D[Approach 1]
    C --> E[Approach 2]
    C --> F[Approach 3]
    D --> G[Output]
    E --> G
    F --> G
```

---

## 深入 2：CORE_DEEPDIVE_TWO — 方法論
**Deep Dive II**

### 2.1 Method selection

| Method | 適用情境 | Pros | Cons |
|---|---|---|---|
| Analytical | 解析 | Exact | Limited geometry |
| Numerical | 數值 | General | Approximate |
| Experimental | 實驗 | Real | Expensive |
| Empirical | 經驗 | Fast | Limited range |

### 2.2 Decision flow

```mermaid
flowchart TD
    Start[Problem] --> Q{Complexity}
    Q -->|Low| Anal[Analytical solution]
    Q -->|Medium| Semi[Semi-analytical]
    Q -->|High| Num[Numerical FEM or FVM]
    Q -->|Real system| Exp[Experimental]
    Anal --> V[Verify with code]
    Semi --> V
    Num --> V
    Exp --> V
```

### 2.3 Standards and codes

- ACI, AISC, Eurocode
- Building codes (IBC, etc.)
- Industry best practices

---

## 深入 3：CORE_DEEPDIVE_THREE — 分析技術
**Deep Dive III**

### 3.1 Statistical methods

For uncertainty analysis: Monte Carlo, sensitivity, FOSM.

```mermaid
graph TD
    A[Input distribution] --> B[Sampling]
    B --> C[MC simulation]
    C --> D[Output statistics]
    D --> E[Reliability index]
    E --> F[Pass]
    F --> G[Design OK]
    F --> H[Redesign]
```

### 3.2 Optimization

- LP, NLP
- Gradient-based, metaheuristic
- Multi-objective Pareto

---

## 深入 4：Design Process
**Deep Dive IV**

### 4.1 Design workflow

Concept → Preliminary → Detailed → Construction → Operation.

### 4.2 Design criteria

- Safety (LRFD, ASD)
- Serviceability
- Durability
- Sustainability

```mermaid
graph LR
    A[Requirements] --> B[Loads]
    B --> C[Analysis]
    C --> D[Design]
    D --> E[Check]
    E -->|Fail| B
    E -->|Pass| F[Document]
```

---

## 深入 5：Modern Trends
**Deep Dive V**

- BIM integration
- AI/ML in design
- Digital twins
- Sustainability, LCA
- Resilient design

```mermaid
graph TD
    A[Traditional] --> B[BIM era]
    B --> C[AI-assisted]
    C --> D[Digital twin]
    D --> E[Autonomous design]
```

---

## 自測 1：Derive core relationship
**Answer:** Starting from definitions, derive the key equation. Verify units and limits.

**Engineering implication:** Apply to design check, code compliance.

## 自測 2：Identify failure mode
**Answer:** List 3-5 failure modes, rank by likelihood × consequence.

**Engineering implication:** Inform design, maintenance, monitoring.

## 自測 3：Estimate order of magnitude
**Answer:** Quick back-of-envelope check using characteristic values.

**Engineering implication:** Sanity check before detailed analysis.

## 自測 4：Compare to code requirement
**Answer:** Apply ACI/AISC/Eurocode, compute utilization ratio.

**Engineering implication:** Pass/fail design verification.

## 自測 5：Compute reliability
**Answer:** $\beta = (\mu - R)/\sigma$ for lognormal, find P_f.

**Engineering implication:** LRFD calibration, risk-informed design.

## 自測 6：Design optimization
**Answer:** Define objective, constraints, solve via LP/NLP.

**Engineering implication:** Cost-effective, sustainable design.

## 自測 7：Sensitivity analysis
**Answer:** $\partial f/\partial x_i$, rank by importance.

**Engineering implication:** Identify critical parameters, reduce uncertainty.

## 自測 8：Life-cycle assessment
**Answer:** Cradle-to-grave, compute GWP, embodied carbon.

**Engineering implication:** Sustainable design, climate goals.

## 自測 9：Risk assessment
**Answer:** Hazard × vulnerability × exposure, compute risk.

**Engineering implication:** Resilience planning, mitigation.

## 自測 10：Communication
**Answer:** Technical writing, visualization, presentation to stakeholders.

**Engineering implication:** Effective engineering practice.

---

## 📊 Diagram 1: Course Concept Map
```mermaid
mindmap
    root((Course))
      Core
        Concepts
      Methods
        Analytical
        Numerical
      Applications
        Design
        Analysis
      Standards
        ACI AISC
      Modern
        BIM AI
```

## 📊 Diagram 2: Method Selection
```mermaid
flowchart TD
    A[Engineering problem] --> B[Type]
    B -->|Static| C[Static analysis]
    B -->|Dynamic| D[Modal, response spectrum]
    B -->|Nonlinear| E[Newton-Raphson, arc-length]
    C --> F[Linear elastic]
    D --> G[Damping, mode shapes]
    E --> H[Material or geometric]
```

## 📊 Diagram 3: Design Process
```mermaid
graph LR
    A[Client need] --> B[Concept]
    B --> C[Preliminary]
    C --> D[Detailed]
    D --> E[Construction]
    E --> F[Operation]
    F --> G[Decommission]
```

## 📊 Diagram 4: Risk-Reliability
```mermaid
graph TD
    A[Uncertainty] --> B[Risk level]
    B -->|Low| C[Deterministic]
    B -->|Medium| D[Semi-probabilistic]
    B -->|High| E[Full probabilistic]
    C --> F[Factor of safety]
    D --> G[LRFD partial factors]
    E --> H[Monte Carlo, FORM]
```

## 📊 Diagram 5: Modern Tools
```mermaid
graph TD
    A[Modern tools] --> B[BIM: Revit, ArchiCAD]
    A --> C[FEA: ANSYS, ABAQUS]
    A --> D[ML: Surrogate, optimization]
    A --> E[OpenSees, SAP2000]
    A --> F[Python ecosystem]
```

---

## 總結

1. **Core concepts** — Core concepts 嘅 foundation
2. **Methods** — analytical + numerical + experimental
3. **Applications** — design, analysis, retrofit
4. **Standards** — codes, best practices
5. **Future** — BIM, AI, sustainability, resilience

**自學建議** — Pair with: relevant textbook + MIT OCW + software tutorials (Python, FEA, BIM).






# 核心心智模型深化（中英對照）

## 1. Core concepts — Core concept

### 1.1 Three-process physical essence
For Bilingual 概念對照, Core concepts governs the system behavior. Description of Core concepts with bilingual explanation.

### 1.2 Non-dimensional numbers
Key dimensionless groups that determine regime: Peclet, Damköhler, Reynolds, Froude, etc.

### 1.3 Engineering consequences
Real-world implications for design, monitoring, intervention.

### 1.4 How experts use this model
Decision flow, scaling laws, expert intuition.

### 1.5 Deep test questions
- Derive scaling law
- Identify regime from data
- Apply to design case

### 1.6 Diagram
```mermaid
graph TD
    A[Input: Core concepts] --> B[Analysis]
    B --> C[Decision]
    C --> D[Approach 1]
    C --> E[Approach 2]
    C --> F[Approach 3]
    D --> G[Output]
    E --> G
    F --> G
```

## 2. Methods — Methods

### 2.1 Method selection
| Method | 適用情境 | Pros | Cons |
|---|---|---|---|
| Analytical | 解析 | Exact | Limited geometry |
| Numerical | 數值 | General | Approximate |
| Experimental | 實驗 | Real | Expensive |
| Empirical | 經驗 | Fast | Limited range |

### 2.2 Decision flow
```mermaid
flowchart TD
    Start[Problem] --> Q[Complexity]
    Q -->|Low| Anal[Analytical solution]
    Q -->|Medium| Semi[Semi-analytical]
    Q -->|High| Num[Numerical FEM or FVM]
    Q -->|Real system| Exp[Experimental]
    Anal --> V[Verify with code]
    Semi --> V
    Num --> V
    Exp --> V
```

### 2.3 Standards and codes
ACI, AISC, Eurocode, building codes (IBC), industry best practices.

## 3. Applications — Analysis techniques

### 3.1 Statistical methods
Monte Carlo, sensitivity, FOSM for uncertainty analysis.

```mermaid
graph TD
    A[Input distribution] --> B[Sampling]
    B --> C[MC simulation]
    C --> D[Output statistics]
    D --> E[Reliability index]
    E --> F[Pass]
    F --> G[Design OK]
    F --> H[Redesign]
```

### 3.2 Optimization
LP, NLP, gradient-based, metaheuristic, multi-objective Pareto.

## 4. Design process

### 4.1 Design workflow
Concept → Preliminary → Detailed → Construction → Operation.

### 4.2 Design criteria
Safety (LRFD, ASD), serviceability, durability, sustainability.

```mermaid
graph LR
    A[Requirements] --> B[Loads]
    B --> C[Analysis]
    C --> D[Design]
    D --> E[Check]
    E -->|Fail| B
    E -->|Pass| F[Document]
```

## 5. Modern trends

BIM integration, AI/ML in design, digital twins, sustainability, LCA, resilient design.

```mermaid
graph TD
    A[Traditional] --> B[BIM era]
    B --> C[AI-assisted]
    C --> D[Digital twin]
    D --> E[Autonomous design]
```

---

# 深度自測問題詳解（中英對照）

## 詳解 1: Derive core relationship
**Q1.** Derive core relationship for Bilingual 概念對照.
**Answer:** Starting from definitions, derive the key equation. Verify units and limits.

**Engineering implication:** Apply to design check, code compliance.

## 詳解 2: Identify failure mode
**Answer:** List 3-5 failure modes, rank by likelihood × consequence.

**Engineering implication:** Inform design, maintenance, monitoring.

## 詳解 3: Estimate order of magnitude
**Answer:** Quick back-of-envelope check using characteristic values.

**Engineering implication:** Sanity check before detailed analysis.

## 詳解 4: Compare to code requirement
**Answer:** Apply ACI/AISC/Eurocode, compute utilization ratio.

**Engineering implication:** Pass/fail design verification.

## 詳解 5: Compute reliability
**Answer:** $\beta = (\mu - R)/\sigma$ for lognormal, find P_f.

**Engineering implication:** LRFD calibration, risk-informed design.

## 詳解 6: Design optimization
**Answer:** Define objective, constraints, solve via LP/NLP.

**Engineering implication:** Cost-effective, sustainable design.

## 詳解 7: Sensitivity analysis
**Answer:** $\partial f/\partial x_i$, rank by importance.

**Engineering implication:** Identify critical parameters, reduce uncertainty.

## 詳解 8: Life-cycle assessment
**Answer:** Cradle-to-grave, compute GWP, embodied carbon.

**Engineering implication:** Sustainable design, climate goals.

## 詳解 9: Risk assessment
**Answer:** Hazard × vulnerability × exposure, compute risk.

**Engineering implication:** Resilience planning, mitigation.

## 詳解 10: Communication
**Answer:** Technical writing, visualization, presentation to stakeholders.

**Engineering implication:** Effective engineering practice.

---

## 📊 Diagram 1: Course Concept Map
```mermaid
mindmap
    root((Bilingual 概念對照))
      Core
        Concepts
      Methods
        Analytical
        Numerical
      Applications
        Design
        Analysis
      Standards
        ACI AISC
      Modern
        BIM AI
```

## 📊 Diagram 2: Method Selection
```mermaid
flowchart TD
    A[Engineering problem] --> B[Type]
    B -->|Static| C[Static analysis]
    B -->|Dynamic| D[Modal, response spectrum]
    B -->|Nonlinear| E[Newton-Raphson, arc-length]
    C --> F[Linear elastic]
    D --> G[Damping, mode shapes]
    E --> H[Material or geometric]
```

## 📊 Diagram 3: Design Process
```mermaid
graph LR
    A[Client need] --> B[Concept]
    B --> C[Preliminary]
    C --> D[Detailed]
    D --> E[Construction]
    E --> F[Operation]
    F --> G[Decommission]
```

## 📊 Diagram 4: Risk-Reliability
```mermaid
graph TD
    A[Uncertainty] --> B[Risk level]
    B -->|Low| C[Deterministic]
    B -->|Medium| D[Semi-probabilistic]
    B -->|High| E[Full probabilistic]
    C --> F[Factor of safety]
    D --> G[LRFD partial factors]
    E --> H[Monte Carlo, FORM]
```

## 📊 Diagram 5: Modern Tools
```mermaid
graph TD
    A[Modern tools] --> B[BIM: Revit, ArchiCAD]
    A --> C[FEA: ANSYS, ABAQUS]
    A --> D[ML: Surrogate, optimization]
    A --> E[OpenSees, SAP2000]
    A --> F[Python ecosystem]
```

---

## 總結

1. **Core concepts** — Core concepts 嘅 foundation
2. **Methods** — analytical + numerical + experimental
3. **Applications** — design, analysis, retrofit
4. **Standards** — codes, best practices
5. **Future** — BIM, AI, sustainability, resilience

**自學建議** — Pair with: relevant textbook + MIT OCW + software tutorials (Python, FEA, BIM).
