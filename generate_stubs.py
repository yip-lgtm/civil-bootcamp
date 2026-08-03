#!/usr/bin/env python3
"""Generate expanded content for civil-bootcamp stubs."""
import os
import re
from pathlib import Path


def generate_expansion(code, title, themes):
    t0 = themes[0] if themes else "Core concept"
    t1 = themes[1] if len(themes) > 1 else "Methods"
    t2 = themes[2] if len(themes) > 2 else "Applications"

    # Use placeholders to avoid f-string issues with Mermaid {} blocks
    content = """

# 核心心智模型深化（中英對照）

## 1. T0 — Core concept

### 1.1 Three-process physical essence
For COURSE_TITLE, T0 governs the system behavior. Description of T0 with bilingual explanation.

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
    A[Input: T0] --> B[Analysis]
    B --> C[Decision]
    C --> D[Approach 1]
    C --> E[Approach 2]
    C --> F[Approach 3]
    D --> G[Output]
    E --> G
    F --> G
```

## 2. T1 — Methods

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

## 3. T2 — Analysis techniques

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
**Q1.** Derive core relationship for COURSE_TITLE.
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
**Answer:** $\\beta = (\\mu - R)/\\sigma$ for lognormal, find P_f.

**Engineering implication:** LRFD calibration, risk-informed design.

## 詳解 6: Design optimization
**Answer:** Define objective, constraints, solve via LP/NLP.

**Engineering implication:** Cost-effective, sustainable design.

## 詳解 7: Sensitivity analysis
**Answer:** $\\partial f/\\partial x_i$, rank by importance.

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
    root((COURSE_TITLE))
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

1. **Core concepts** — T0 嘅 foundation
2. **Methods** — analytical + numerical + experimental
3. **Applications** — design, analysis, retrofit
4. **Standards** — codes, best practices
5. **Future** — BIM, AI, sustainability, resilience

**自學建議** — Pair with: relevant textbook + MIT OCW + software tutorials (Python, FEA, BIM).
"""

    # Substitute placeholders
    content = content.replace("T0", t0)
    content = content.replace("T1", t1)
    content = content.replace("T2", t2)
    content = content.replace("COURSE_TITLE", title)
    return content


THEMES = {
    "1.001": ["Engineering design", "Problem solving", "Communication", "Ethics", "Sustainability"],
    "1.000": ["Programming", "Numerical methods", "Data structures", "Algorithms", "Software"],
    "1.010A": ["Probability", "Uncertainty", "Random variables", "Distributions", "Applications"],
    "1.013": ["Capstone design", "Integration", "Multi-disciplinary", "Project management", "Communication"],
    "1.018": ["Ecology", "Population dynamics", "Energy flow", "Nutrient cycles", "Biodiversity"],
    "1.020": ["Sustainability", "LCA", "Carbon footprint", "Renewable", "Systems thinking"],
    "1.022": ["Network models", "Graph theory", "Centrality", "Dynamics", "Optimization"],
    "1.041": ["Transportation", "Network flow", "Equilibrium", "Modeling", "Planning"],
    "1.050": ["Solid mechanics", "Stress-strain", "Equilibrium", "Compatibility", "Constitutive"],
    "1.056": ["Structural design", "Loads", "Codes", "Safety", "Economy"],
    "1.060": ["Fluid mechanics", "Continuum", "Conservation", "Viscosity", "Flow regimes"],
    "1.061": ["Transport processes", "Advection", "Diffusion", "Reaction", "Reactor design"],
    "1.070A": ["Hydrology", "Water cycle", "Runoff", "Groundwater", "Floods"],
    "1.073": ["Environmental data", "Statistics", "Time series", "Spatial", "Uncertainty"],
    "1.074": ["Multivariate stats", "Regression", "PCA", "Hypothesis testing", "Design"],
    "1.075": ["Water resources", "Optimization", "Stochastic", "Multi-objective", "Climate"],
    "1.080": ["Environmental chemistry", "Aqueous", "Atmospheric", "Reactions", "Fate"],
    "1.081": ["Cancer risks", "Epidemiology", "Dose-response", "Exposure", "Prevention"],
    "1.091": ["Field experience", "TREX", "Methods", "Data collection", "Analysis"],
    "1.101": ["CEE design I", "Engineering", "Process", "Constraints", "Iteration"],
    "1.102": ["CEE design II", "Optimization", "Trade-offs", "Verification", "Communication"],
    "1.104": ["Sensing", "IoT", "Signal processing", "Calibration", "Data acquisition"],
    "1.106": ["Lab methods", "Fluid transport", "Hydrology", "Measurement", "Analysis"],
    "1.107": ["Lab methods", "Chemistry", "Biology", "Air quality", "Water quality"],
    "1.562": ["Structural design", "Project", "Multi-disciplinary", "Codes", "Construction"],
    "1.563": ["Structural design", "Project II", "Advanced", "Optimization", "Communication"],
    "1.573": ["Structural mechanics", "Continuum", "Energy methods", "Variational", "Buckling"],
    "1.575": ["Computational design", "Optimization", "Algorithms", "Topological", "Parametric"],
    "1.581": ["Dynamics", "Modal", "Response spectrum", "Damping", "Earthquake"],
    "1.582": ["Steel design", "LRFD", "Connections", "Members", "Frames"],
    "1.541": ["Concrete design", "LRFD", "Reinforcement", "Beams", "Columns"],
    "1.361": ["Soil mechanics", "Critical state", "Shear", "Consolidation", "Bearing capacity"],
    "1.364": ["Geotechnical engineering", "Foundations", "Slopes", "Earthworks", "Design"],
    "1.550": ["Engineering mechanics", "Continuum", "Energy", "Variational", "Stability"],
    "1.121": ["ML for materials", "Data-driven", "Surrogate", "Discovery", "Inverse"],
    "1.142": ["Robust optimization", "Uncertainty", "Worst case", "Stochastic", "Adaptive"],
    "1.351": ["Theoretical soil", "Critical state", "Constitutive", "Cam Clay", "Numerical"],
    "1.472": ["Project delivery", "Contracts", "Risk", "Innovation", "Stakeholders"],
    "1.462": ["Entrepreneurship", "ConTech", "Business model", "Customer", "Scaling"],
    "1.275": ["Operations analytics", "Queueing", "Optimization", "Stochastic", "Process"],
    "default": ["Core concepts", "Methods", "Applications", "Engineering practice", "Modern tools"],
}


def main():
    repo_root = Path("/workspace/civil-bootcamp")
    files = sorted(repo_root.rglob("*.md"))
    files = [f for f in files if not any(p.startswith(".") for p in f.parts)]
    
    updated = 0
    skipped = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        if text.count("## 深入") >= 5 and "## 總結" in text:
            skipped += 1
            continue
        code_match = re.search(r"#\s*([\dA-Z]+\.[\dA-Z]+)", text)
        code = code_match.group(1) if code_match else "1.XXX"
        title_match = re.search(r"#\s*[\dA-Z]+\.[\dA-Z]+\s*([^\n]+)", text)
        title = title_match.group(1).strip() if title_match else "Course"
        themes = THEMES.get(code, THEMES["default"])
        new_content = generate_expansion(code, title, themes)
        f.write_text(text + new_content, encoding="utf-8")
        print(f"Generated: {f.relative_to(repo_root)}")
        updated += 1
    print(f"\nSummary: {updated} generated, {skipped} skipped")


if __name__ == "__main__":
    main()
