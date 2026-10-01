### `regression-logistique-de-detection-de-fraude`

```markdown
# 💳 Détection de Fraude par Carte Bancaire : Régression Logistique & GLM

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Statsmodels](https://img.shields.io/badge/Statsmodels-GLM-green)

## 📌 Présentation du Projet
Projet de modélisation statistique du risque ciblant la détection de transactions bancaires frauduleuses. L'enjeu principal réside dans la gestion du fort déséquilibre de classe propre aux données de fraude et dans le réglage optimal des seuils de décision pour minimiser le coût financier des fausses négatives.

## 📊 Données & Méthodologie
- **Corpus :** Jeu de données de **284 807 transactions bancaires**.
- **Modélisation :** Régression logistique appliquée dans le cadre des Modèles Linéaires Généralisés (GLM).
- **Sélection de variables :** Élimination des colinéarités et test de significativité statistique des coefficients.
- **Optimisation du Seuil :** Ajustement du seuil de décision à **0,02** afin de maximiser le rappel sur la classe minoritaire (fraude).

## 📈 Performances Obtenues
- **Recall (Rappel) :** `87,8 %` (détection effective de la grande majorité des fraudes)
- **ROC-AUC :** `0,961`
- **AUPRC :** `0,742` (métrique de référence pour classification déséquilibrée)

## 🛠️ Technologies Utilisées
- **Langage :** Python[cite: 4]
- **Analyse & Stats :** Statsmodels, Scikit-learn, Pandas, NumPy[cite: 4]
- **Visualisation :** Matplotlib, Seaborn[cite: 4]
- **Environnement & Rapport :** Jupyter, PyCharm, LaTeX[cite: 4]

### 💻 Exécution du Projet

1. **Cloner le projet :**
   ```bash
   git clone [https://github.com/yvesgnonhoue/regression-logistique-de-detection-de-fraude.git](https://github.com/yvesgnonhoue/regression-logistique-de-detection-de-fraude.git)
   cd regression-logistique-de-detection-de-fraude
