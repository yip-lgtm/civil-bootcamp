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
