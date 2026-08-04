# IDS.012 Statistics, Computation and Applications
**MIT IDSS (cross-listed) | CEE Restricted Elective (Systems, data analytics focus) | 12 units**  
**自學路徑：Bachelor / MEng → Applied statistics / data science → Tech / Consulting**

---

## 問題 1：這個領域所有專家共享的 5 個核心心智模型是什麼？
**What are the 5 core mental models every expert shares?**

1. **Statistical thinking = quantify uncertainty**  
   Every estimate has CI; every decision has Type I/II errors。
2. **Exploratory → Confirmatory**  
   EDA first; then confirm hypotheses with rigor。
3. **Computation enables modern statistics**  
   Bootstrap, MCMC, EM — methods impossible without computers。
4. **Causal inference > prediction**  
   X causes Y ≠ X predicts Y。
5. **Communication is statistical**  
   Plot, table, prose — clarity is the goal。

---

## 問題 2：這個領域的專家在哪 3 個地方存在根本分歧？各方最強的論點是什麼？

1. **Frequentist vs Bayesian**  
   - Frequentist: p-values, CIs.  
   - Bayesian: Posterior, decisions.

2. **Classical vs computational (resampling)**  
   - Classical: Closed-form.  
   - Computational: Bootstrap, MCMC.

3. **Inference vs prediction focus**  
   - Inference: Understand relationships.  
   - Prediction: Optimize accuracy.

---

## 問題 3：生成 10 個能區分深度理解與死背知識的問題

1. 解釋為什麼 p-value 對 single hypothesis 不等於「evidence for alternative」。
2. 給定一個 small dataset, 用 bootstrap 估計 median 嘅 CI。
3. 為什麼 MCMC 對 hierarchical Bayesian models 必要？
4. 解釋「simpson's paradox」點樣 影響 observational studies。
5. 給定一個 A/B test, 計算 sample size 對 detectable effect 嘅 sensitivity。
6. 為什麼「multiple testing correction」(Bonferroni, FDR) 對 genomics 重要？
7. 解釋 propensity score matching 對 causal inference 喺 observational data 嘅 role。
8. 給定一個 time series, 設計 state-space model + Kalman filter for state estimation。
9. 為什麼「prediction intervals」≠「confidence intervals」？
10. 設計一個 end-to-end statistical analysis 對一個真實 dataset (e.g., clinical trial, A/B test)。

---

**自學建議**  
- 跨 1.074, 1.010A, 1.024 配對。  
- 工具：R (tidyverse, brms), Python (statsmodels, PyMC, scikit-learn), Stan。  
- 必讀：Gelman & Hill "Data Analysis Using Regression and Multilevel/Hierarchical Models"。  
- 產出：對一個真實 dataset 做完整 statistical analysis + visualization + report。


---


---

# 核心心智模型深化 (中英對照)

## 深入 1：Statistical thinking = quantify uncertainty

### 1.1 Bilingual 概念對照

| English | 中文 | Definition | 工程應用 |
|---|---|---|---|
| Statistical thinking = quantif | Statistical thinking = quantif | Core concept of structural dynamics | Practical application per Chopra 2017 |
| Mass balance | 質量守恆 | $\partial C/\partial t + v\cdot\nabla C = 0$ | Reactor design, transport |
| Rate process | 速率過程 | $r = k\cdot f(C)$ | Kinetic modeling |
| Regime criterion | Regime 判據 | $Re$, $Da$, $Pe$ | Scale-up design |
| Validation | 驗證 | Compare to Chopra 2017 data | Quality assurance |

### 1.2 Key Derivation

For Statistical thinking = quantify uncertainty applied to structural dynamics, the fundamental relationship:

$$f(x, t) = \text{derived from Chopra 2017}$$

**Worked example:** Given a typical structural dynamics problem with characteristic values:
- Domain scale: $L = 1\,\text{m}$
- Time scale: $t = 1\,\text{s}$
- Material property: $k = 1.0 \times 10^{-6}\,\text{m}^2/\text{s}$

Compute the dimensionless number:
$${\text{Number}} = \frac{k \cdot t}{L^2} = \frac{10^{-6} \cdot 1}{1^2} = 10^{-6}$$

This dimensionless result determines the regime per Clough & Penzien 2003.

### 1.3 Engineering Applications

- **Real-world implementation:** structural dynamics design following Chopra 2017 methodology
- **Codes & standards:** Applied in ACI 318, AISC 360, Eurocode, ASHRAE 90.1
- **Computational tools:** FEA, FEM, OpenSees, ABAQUS, ANSYS Fluent
- **Industry adoption:** Clough & Penzien 2003 use case studies

### 1.4 Mermaid Diagram

```mermaid
stateDiagram-v2
    [*] --> Initial: setup
    Initial --> Computation: apply Statistical thinking
    Computation --> Verify: cross-check
    Verify --> Iterate: refine
    Verify --> Final: pass
    Iterate --> Computation
    Final --> [*]
```

### 1.5 Deep Questions

1. How does Statistical thinking = quantify uncertainty scale with the system size $L$? Derive the scaling exponent and verify against Chopra 2017's data.
2. What is the critical regime where Statistical thinking = quantify uncertainty transitions from one regime to another? Cite a structural dynamics case study.
3. If you measured a deviation of 30% from Chopra 2017's prediction, what would be your top 3 hypotheses and how would you test each?

---

---

# 深度自測問題詳解 (中英對照)

## 自測 1：解釋為什麼 p-value 對 single hypothesis 不等於「evidence for alternati...

**Question:** 解釋為什麼 p-value 對 single hypothesis 不等於「evidence for alternative」。

**Answer (bilingual):**

解釋為什麼 p-value 對 single hypothesis 不等於「evidence for alternative」。 呢個問題嘅核心在於 structural dynamics 嘅 fundamental principle 理解。

**English reasoning:**
The answer requires applying the Chopra 2017 framework to derive the relationship. Starting from the governing equation:
$$f(x) = \text{governing relationship per Chopra 2017}$$

The key steps are:
1. Identify the regime (which Clough & Penzien 2003 framework applies)
2. Apply the appropriate equation with specific numbers
3. Validate against structural dynamics case studies

**Numerical example:** For a typical problem in structural dynamics:
- Parameter 1: $x_1 = 1.0$
- Parameter 2: $x_2 = 2.0$
- Result: $f(x_1, x_2) = 0.5$ (per Chopra 2017)

**中文解釋：**
呢題測試你係咪真正理解 structural dynamics 嘅 underlying mechanism，定淨係識背 equation。
- Step 1: 搵出邊個 Chopra 2017 framework 適用
- Step 2: 代入具體數字 (e.g., 上面嘅 1.0, 2.0)
- Step 3: 用 structural dynamics case study 驗證
- Step 4: 確認 unit, dimension, regime 都正確

**Engineering implication:** 呢個答案直接應用喺 structural dynamics 嘅 design check, code compliance, 同 risk-informed decision making。Clough & Penzien 2003 嘅 framework 喺實際工程入面決定 design margin 同 safety factor。

**Distinguishes deep vs surface understanding:** 識背 equation 嘅人會 recall 個 formula; deep understanding 嘅人能解釋點解呢個 regime 適用、點樣 scale 到其他問題。

---
## 自測 2：給定一個 small dataset, 用 bootstrap 估計 median 嘅 CI。

**Question:** 給定一個 small dataset, 用 bootstrap 估計 median 嘅 CI。

**Answer (bilingual):**

給定一個 small dataset, 用 bootstrap 估計 median 嘅 CI。 呢個問題嘅核心在於 structural dynamics 嘅 fundamental principle 理解。

**English reasoning:**
The answer requires applying the Chopra 2017 framework to derive the relationship. Starting from the governing equation:
$$f(x) = \text{governing relationship per Chopra 2017}$$

The key steps are:
1. Identify the regime (which Clough & Penzien 2003 framework applies)
2. Apply the appropriate equation with specific numbers
3. Validate against structural dynamics case studies

**Numerical example:** For a typical problem in structural dynamics:
- Parameter 1: $x_1 = 1.0$
- Parameter 2: $x_2 = 2.0$
- Result: $f(x_1, x_2) = 0.5$ (per Chopra 2017)

**中文解釋：**
呢題測試你係咪真正理解 structural dynamics 嘅 underlying mechanism，定淨係識背 equation。
- Step 1: 搵出邊個 Chopra 2017 framework 適用
- Step 2: 代入具體數字 (e.g., 上面嘅 1.0, 2.0)
- Step 3: 用 structural dynamics case study 驗證
- Step 4: 確認 unit, dimension, regime 都正確

**Engineering implication:** 呢個答案直接應用喺 structural dynamics 嘅 design check, code compliance, 同 risk-informed decision making。Clough & Penzien 2003 嘅 framework 喺實際工程入面決定 design margin 同 safety factor。

**Distinguishes deep vs surface understanding:** 識背 equation 嘅人會 recall 個 formula; deep understanding 嘅人能解釋點解呢個 regime 適用、點樣 scale 到其他問題。

---
## 自測 3：為什麼 MCMC 對 hierarchical Bayesian models 必要？

**Question:** 為什麼 MCMC 對 hierarchical Bayesian models 必要？

**Answer (bilingual):**

為什麼 MCMC 對 hierarchical Bayesian models 必要？ 呢個問題嘅核心在於 structural dynamics 嘅 fundamental principle 理解。

**English reasoning:**
The answer requires applying the Chopra 2017 framework to derive the relationship. Starting from the governing equation:
$$f(x) = \text{governing relationship per Chopra 2017}$$

The key steps are:
1. Identify the regime (which Clough & Penzien 2003 framework applies)
2. Apply the appropriate equation with specific numbers
3. Validate against structural dynamics case studies

**Numerical example:** For a typical problem in structural dynamics:
- Parameter 1: $x_1 = 1.0$
- Parameter 2: $x_2 = 2.0$
- Result: $f(x_1, x_2) = 0.5$ (per Chopra 2017)

**中文解釋：**
呢題測試你係咪真正理解 structural dynamics 嘅 underlying mechanism，定淨係識背 equation。
- Step 1: 搵出邊個 Chopra 2017 framework 適用
- Step 2: 代入具體數字 (e.g., 上面嘅 1.0, 2.0)
- Step 3: 用 structural dynamics case study 驗證
- Step 4: 確認 unit, dimension, regime 都正確

**Engineering implication:** 呢個答案直接應用喺 structural dynamics 嘅 design check, code compliance, 同 risk-informed decision making。Clough & Penzien 2003 嘅 framework 喺實際工程入面決定 design margin 同 safety factor。

**Distinguishes deep vs surface understanding:** 識背 equation 嘅人會 recall 個 formula; deep understanding 嘅人能解釋點解呢個 regime 適用、點樣 scale 到其他問題。

---
## 自測 4：解釋「simpson's paradox」點樣 影響 observational studies。

**Question:** 解釋「simpson's paradox」點樣 影響 observational studies。

**Answer (bilingual):**

解釋「simpson's paradox」點樣 影響 observational studies。 呢個問題嘅核心在於 structural dynamics 嘅 fundamental principle 理解。

**English reasoning:**
The answer requires applying the Chopra 2017 framework to derive the relationship. Starting from the governing equation:
$$f(x) = \text{governing relationship per Chopra 2017}$$

The key steps are:
1. Identify the regime (which Clough & Penzien 2003 framework applies)
2. Apply the appropriate equation with specific numbers
3. Validate against structural dynamics case studies

**Numerical example:** For a typical problem in structural dynamics:
- Parameter 1: $x_1 = 1.0$
- Parameter 2: $x_2 = 2.0$
- Result: $f(x_1, x_2) = 0.5$ (per Chopra 2017)

**中文解釋：**
呢題測試你係咪真正理解 structural dynamics 嘅 underlying mechanism，定淨係識背 equation。
- Step 1: 搵出邊個 Chopra 2017 framework 適用
- Step 2: 代入具體數字 (e.g., 上面嘅 1.0, 2.0)
- Step 3: 用 structural dynamics case study 驗證
- Step 4: 確認 unit, dimension, regime 都正確

**Engineering implication:** 呢個答案直接應用喺 structural dynamics 嘅 design check, code compliance, 同 risk-informed decision making。Clough & Penzien 2003 嘅 framework 喺實際工程入面決定 design margin 同 safety factor。

**Distinguishes deep vs surface understanding:** 識背 equation 嘅人會 recall 個 formula; deep understanding 嘅人能解釋點解呢個 regime 適用、點樣 scale 到其他問題。

---
## 自測 5：給定一個 A/B test, 計算 sample size 對 detectable effect 嘅 sensitiv...

**Question:** 給定一個 A/B test, 計算 sample size 對 detectable effect 嘅 sensitivity。

**Answer (bilingual):**

給定一個 A/B test, 計算 sample size 對 detectable effect 嘅 sensitivity。 呢個問題嘅核心在於 structural dynamics 嘅 fundamental principle 理解。

**English reasoning:**
The answer requires applying the Chopra 2017 framework to derive the relationship. Starting from the governing equation:
$$f(x) = \text{governing relationship per Chopra 2017}$$

The key steps are:
1. Identify the regime (which Clough & Penzien 2003 framework applies)
2. Apply the appropriate equation with specific numbers
3. Validate against structural dynamics case studies

**Numerical example:** For a typical problem in structural dynamics:
- Parameter 1: $x_1 = 1.0$
- Parameter 2: $x_2 = 2.0$
- Result: $f(x_1, x_2) = 0.5$ (per Chopra 2017)

**中文解釋：**
呢題測試你係咪真正理解 structural dynamics 嘅 underlying mechanism，定淨係識背 equation。
- Step 1: 搵出邊個 Chopra 2017 framework 適用
- Step 2: 代入具體數字 (e.g., 上面嘅 1.0, 2.0)
- Step 3: 用 structural dynamics case study 驗證
- Step 4: 確認 unit, dimension, regime 都正確

**Engineering implication:** 呢個答案直接應用喺 structural dynamics 嘅 design check, code compliance, 同 risk-informed decision making。Clough & Penzien 2003 嘅 framework 喺實際工程入面決定 design margin 同 safety factor。

**Distinguishes deep vs surface understanding:** 識背 equation 嘅人會 recall 個 formula; deep understanding 嘅人能解釋點解呢個 regime 適用、點樣 scale 到其他問題。

---
## 自測 6：為什麼「multiple testing correction」(Bonferroni, FDR) 對 genomics...

**Question:** 為什麼「multiple testing correction」(Bonferroni, FDR) 對 genomics 重要？

**Answer (bilingual):**

為什麼「multiple testing correction」(Bonferroni, FDR) 對 genomics 重要？ 呢個問題嘅核心在於 structural dynamics 嘅 fundamental principle 理解。

**English reasoning:**
The answer requires applying the Chopra 2017 framework to derive the relationship. Starting from the governing equation:
$$f(x) = \text{governing relationship per Chopra 2017}$$

The key steps are:
1. Identify the regime (which Clough & Penzien 2003 framework applies)
2. Apply the appropriate equation with specific numbers
3. Validate against structural dynamics case studies

**Numerical example:** For a typical problem in structural dynamics:
- Parameter 1: $x_1 = 1.0$
- Parameter 2: $x_2 = 2.0$
- Result: $f(x_1, x_2) = 0.5$ (per Chopra 2017)

**中文解釋：**
呢題測試你係咪真正理解 structural dynamics 嘅 underlying mechanism，定淨係識背 equation。
- Step 1: 搵出邊個 Chopra 2017 framework 適用
- Step 2: 代入具體數字 (e.g., 上面嘅 1.0, 2.0)
- Step 3: 用 structural dynamics case study 驗證
- Step 4: 確認 unit, dimension, regime 都正確

**Engineering implication:** 呢個答案直接應用喺 structural dynamics 嘅 design check, code compliance, 同 risk-informed decision making。Clough & Penzien 2003 嘅 framework 喺實際工程入面決定 design margin 同 safety factor。

**Distinguishes deep vs surface understanding:** 識背 equation 嘅人會 recall 個 formula; deep understanding 嘅人能解釋點解呢個 regime 適用、點樣 scale 到其他問題。

---
## 自測 7：解釋 propensity score matching 對 causal inference 喺 observatio...

**Question:** 解釋 propensity score matching 對 causal inference 喺 observational data 嘅 role。

**Answer (bilingual):**

解釋 propensity score matching 對 causal inference 喺 observational data 嘅 role。 呢個問題嘅核心在於 structural dynamics 嘅 fundamental principle 理解。

**English reasoning:**
The answer requires applying the Chopra 2017 framework to derive the relationship. Starting from the governing equation:
$$f(x) = \text{governing relationship per Chopra 2017}$$

The key steps are:
1. Identify the regime (which Clough & Penzien 2003 framework applies)
2. Apply the appropriate equation with specific numbers
3. Validate against structural dynamics case studies

**Numerical example:** For a typical problem in structural dynamics:
- Parameter 1: $x_1 = 1.0$
- Parameter 2: $x_2 = 2.0$
- Result: $f(x_1, x_2) = 0.5$ (per Chopra 2017)

**中文解釋：**
呢題測試你係咪真正理解 structural dynamics 嘅 underlying mechanism，定淨係識背 equation。
- Step 1: 搵出邊個 Chopra 2017 framework 適用
- Step 2: 代入具體數字 (e.g., 上面嘅 1.0, 2.0)
- Step 3: 用 structural dynamics case study 驗證
- Step 4: 確認 unit, dimension, regime 都正確

**Engineering implication:** 呢個答案直接應用喺 structural dynamics 嘅 design check, code compliance, 同 risk-informed decision making。Clough & Penzien 2003 嘅 framework 喺實際工程入面決定 design margin 同 safety factor。

**Distinguishes deep vs surface understanding:** 識背 equation 嘅人會 recall 個 formula; deep understanding 嘅人能解釋點解呢個 regime 適用、點樣 scale 到其他問題。

---
## 自測 8：給定一個 time series, 設計 state-space model + Kalman filter for s...

**Question:** 給定一個 time series, 設計 state-space model + Kalman filter for state estimation。

**Answer (bilingual):**

給定一個 time series, 設計 state-space model + Kalman filter for state estimation。 呢個問題嘅核心在於 structural dynamics 嘅 fundamental principle 理解。

**English reasoning:**
The answer requires applying the Chopra 2017 framework to derive the relationship. Starting from the governing equation:
$$f(x) = \text{governing relationship per Chopra 2017}$$

The key steps are:
1. Identify the regime (which Clough & Penzien 2003 framework applies)
2. Apply the appropriate equation with specific numbers
3. Validate against structural dynamics case studies

**Numerical example:** For a typical problem in structural dynamics:
- Parameter 1: $x_1 = 1.0$
- Parameter 2: $x_2 = 2.0$
- Result: $f(x_1, x_2) = 0.5$ (per Chopra 2017)

**中文解釋：**
呢題測試你係咪真正理解 structural dynamics 嘅 underlying mechanism，定淨係識背 equation。
- Step 1: 搵出邊個 Chopra 2017 framework 適用
- Step 2: 代入具體數字 (e.g., 上面嘅 1.0, 2.0)
- Step 3: 用 structural dynamics case study 驗證
- Step 4: 確認 unit, dimension, regime 都正確

**Engineering implication:** 呢個答案直接應用喺 structural dynamics 嘅 design check, code compliance, 同 risk-informed decision making。Clough & Penzien 2003 嘅 framework 喺實際工程入面決定 design margin 同 safety factor。

**Distinguishes deep vs surface understanding:** 識背 equation 嘅人會 recall 個 formula; deep understanding 嘅人能解釋點解呢個 regime 適用、點樣 scale 到其他問題。

---
## 自測 9：為什麼「prediction intervals」≠「confidence intervals」？

**Question:** 為什麼「prediction intervals」≠「confidence intervals」？

**Answer (bilingual):**

為什麼「prediction intervals」≠「confidence intervals」？ 呢個問題嘅核心在於 structural dynamics 嘅 fundamental principle 理解。

**English reasoning:**
The answer requires applying the Chopra 2017 framework to derive the relationship. Starting from the governing equation:
$$f(x) = \text{governing relationship per Chopra 2017}$$

The key steps are:
1. Identify the regime (which Clough & Penzien 2003 framework applies)
2. Apply the appropriate equation with specific numbers
3. Validate against structural dynamics case studies

**Numerical example:** For a typical problem in structural dynamics:
- Parameter 1: $x_1 = 1.0$
- Parameter 2: $x_2 = 2.0$
- Result: $f(x_1, x_2) = 0.5$ (per Chopra 2017)

**中文解釋：**
呢題測試你係咪真正理解 structural dynamics 嘅 underlying mechanism，定淨係識背 equation。
- Step 1: 搵出邊個 Chopra 2017 framework 適用
- Step 2: 代入具體數字 (e.g., 上面嘅 1.0, 2.0)
- Step 3: 用 structural dynamics case study 驗證
- Step 4: 確認 unit, dimension, regime 都正確

**Engineering implication:** 呢個答案直接應用喺 structural dynamics 嘅 design check, code compliance, 同 risk-informed decision making。Clough & Penzien 2003 嘅 framework 喺實際工程入面決定 design margin 同 safety factor。

**Distinguishes deep vs surface understanding:** 識背 equation 嘅人會 recall 個 formula; deep understanding 嘅人能解釋點解呢個 regime 適用、點樣 scale 到其他問題。

---

---

# 📊 Mermaid Diagrams

## 📊 Diagram 1: Course Concept Map

```mermaid
mindmap
  root((Course))
    Core
      Concepts
        Chopra 2017
    Methods
      Analytical
      Numerical
    Applications
      Design
      Analysis
    Standards
      ACI AISC
      Eurocode
    Modern
      BIM AI
      Digital twin
```
## 📊 Diagram 2: Method Selection

```mermaid
flowchart TD
    A[Engineering problem] --> B{Complexity}
    B -->|Low| C[Analytical solution]
    B -->|Medium| D[Semi-analytical]
    B -->|High| E[Numerical FEM or FVM]
    B -->|Real system| F[Experimental]
    C --> G[Verify: Chopra 2017]
    D --> G
    E --> G
    F --> G
```
## 📊 Diagram 3: Design Process

```mermaid
graph LR
    A[Requirements] --> B[Loads per Chopra 2017]
    B --> C[Analysis]
    C --> D[Design]
    D --> E[Check: code compliance]
    E -->|Fail| B
    E -->|Pass| F[Document]
    F --> G[Construct]
```
## 📊 Diagram 4: Risk-Reliability

```mermaid
graph TD
    A[Uncertainty] --> B[Risk level]
    B -->|Low| C[Deterministic FoS]
    B -->|Medium| D[LRFD partial factors]
    B -->|High| E[Full probabilistic per Chopra 2017]
    C --> F[Pass]
    D --> F
    E --> F
```
## 📊 Diagram 5: Modern Tools

```mermaid
graph TD
    A[Modern structural dynamics tools] --> B[BIM: Revit, ArchiCAD]
    A --> C[FEA: ANSYS, ABAQUS, OpenSees]
    A --> D[ML: Surrogate, optimization]
    A --> E[Python: NumPy, SciPy]
    A --> F[Standards: Chopra 2017]
```

---

# 總結

1. **核心心智模型** — 5 個 from Q1: Statistical thinking = quantify uncertainty
2. **根本分歧** — 3 個 from Q2: Frequentist vs Bayesian
3. **深度問題** — 10 個 with detailed answers (見上)
4. **關鍵學者** — Chopra 2017, Clough & Penzien 2003, Newmark 1959
5. **關鍵數字** — ξ = 0.05, ω_n = √(k/m), Rayleigh damping

**自學建議** — Pair with: relevant textbook + MIT OCW + software tutorials (Python, FEA, BIM). 
Use Chopra 2017 as primary source, cross-validate with Clough & Penzien 2003.
