# mcrc-cetuximab-analysis

Анализ молекулярных механизмов резистентности связанных с выживаемостью и ответом на терапию цетуксимабом среди пациентов страдающих от метастатического колоректального рака

Цель работы
Понять, какие молекулярные механизмы могут быть связаны с выживаемостью и ответом на терапию цетуксимабом у пациентов с метастатическим колоректальным раком (мКРР). Особое внимание будет уделено роли гена MET, активности сигнальных путей MAPK и PI3K, а также эпителиально-мезенхимальному переходу (EMT).


# SETUP INSTRUCTIONS

        curl https://pyenv.run | bash

Add to .bashrc: 

        export PATH="$HOME/.pyenv/bin:$PATH"
        eval "$(pyenv init --path)"
        eval "$(pyenv init -)"

Then:

        pyenv install 3.12.0
        pyenv global 3.12.0 

<<<<<<< HEAD
        cd YOUR_REPO_DIR
        python -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
=======
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
   - Follow step-by-step sections: 0->1->2->3->4->5->Elza

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
>>>>>>> 09354341872f4d40c8f5adbb966c565424391fc1
