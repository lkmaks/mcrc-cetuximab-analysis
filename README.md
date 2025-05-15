# Cetuximab Resistance in Metastatic Colorectal Cancer (mCRC)

This repository contains the code, data, and results of a study analyzing molecular mechanisms of resistance to anti-EGFR therapy (cetuximab) in metastatic colorectal cancer (mCRC). The focus is on identifying biomarkers and transcriptomic signatures associated with therapy response and survival.

---

## 📌 Objectives

- Investigate the role of **MET gene** expression in response and survival
- Explore **EMT (epithelial–mesenchymal transition)** signature relevance
- Classify samples using **CMS (Consensus Molecular Subtypes)**
- Perform **clustering** based on transcriptomic profiles to reveal resistant phenotypes
- Correlate clusters with survival, CMS distribution, and immune profiles

---

## 🧾 Data Sources

- **GSE196576**: RNA-seq and clinical data from mCRC patients treated with cetuximab, with OS and PFS + flags
- **GSE183984**: Another cohort treated with cetuximab, in comparison with first one we pre- and post-treatement data


---

## ⚙️ Technologies & Libraries

- **Python 3.12**, **R 4.5.0**
- `pandas`, `numpy`, `matplotlib`, `seaborn`, `lifelines`, `scipy`, `scikit-learn`
- CMS classification: `CMScaller` (R)
- Gene signature enrichment: `decoupler`, `ssGSEA`
- Survival analysis: Kaplan-Meier, Cox regression, Log-rank test
- Statistics: Chi-square, Mann–Whitney U, Wilcoxon, Pearson

---

## 📈 Analysis Workflow

1. **Data Preprocessing & Annotation**
   - Merge CMS and clinical data
   - Filter and clean missing/unclassified entries

2. **Gene Expression & Biomarker Evaluation**
   - MET expression before/after treatment
   - EMT signature analysis (score and correlation with MET)

3. **Survival Analysis**
   - Kaplan-Meier survival curves by:
     - MET expression
     - EMT signature
     - CMS subtype
     - Transcriptomic clusters

4. **CMS Analysis**
   - CMS classification using CMScaller
   - Stacked bar plots by response, cohort, and clusters
   - Chi-square tests for CMS distribution differences

5. **Clustering & Immune Profiling**
   - ssGSEA enrichment for BG immune/stromal signatures
   - Visualization of clusters and heatmaps
   - Association with survival and CMS types

---

## 📊 Key Results

- **MET expression** was **not significantly associated** with survival or treatment response.
- **EMT signature** showed stronger association patterns than single-gene markers, but still requires further validation.
- **CMS subtypes** revealed clear survival differences, with **CMS1 showing the poorest prognosis**.
- **Four tumor clusters** were identified, each with distinct CMS distributions, immune profiles, and survival trends.


---

## ▶️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/lkmaks/mcrc-cetuximab-analysis
   cd mcrc-cetuximab-resistance
   ```

2. Set up environment (optional but recommended):
   ```bash
         pyenv install 3.12.0
         pyenv global 3.12.0 

         cd YOUR_REPO_DIR
         python -m venv .venv
         source .venv/bin/activate
         pip install -r requirements.txt
   ```

3. Run analysis:
   - Open notebooks in `notebooks/`
   - Follow step-by-step sections: preprocessing → CMS → survival → clustering

---

## 📌 Limitations

- Sample size is limited in some subgroups (e.g., responders vs non-responders)
- Requires external validation in larger, independent cohorts
- EMT/MET not sufficient alone as predictive biomarkers

---

## 🧠 Conclusion

> **Single genes (e.g., MET) are insufficient predictors of resistance. Composite transcriptomic signatures and CMS/clustering provide more robust insight into cetuximab resistance mechanisms.**

---

## 🔗 Citation

If you use this repository, please cite:
```
A. X., M. Y., E. Z., D. Belousov. "Analysis of Molecular Mechanisms of Resistance Associated with Cetuximab Survival Response in mCRC Patients" (2025)
```

---

## 📬 Contact

For questions or collaboration:
- [hommurat9001@gmail.com](mailto:hommurat9001@gmail.com)
