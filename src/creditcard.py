import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import StandardScaler
from statsmodels.genmod.families import family

# ====================================================================================
#               Importation du jeu de donnee
# ====================================================================================

creditcard = pd.read_csv(r"C:\Users\yvano\Downloads\creditcard.csv", sep=',')


# ====================================================================================
#               Standardisation des covariables Time et Amount
# ====================================================================================

creditcard_analyse = creditcard.copy()
scaler =  StandardScaler(with_mean=True, with_std=True)
colonnes_a_standardiser = ['Time', 'Amount']
creditcard_analyse[colonnes_a_standardiser] = scaler.fit_transform(creditcard_analyse[colonnes_a_standardiser])


# ====================================================================================
#               Creation du modele Complet
# ====================================================================================
Variables = ['Time'] + [f"V{i}" for i in range(1, 29)] + ['Amount']
modele_complet = smf.glm(formula='Class ~' + '+'.join(Variables), data=creditcard_analyse, family=sm.families.Binomial(link=sm.families.links.logit())).fit()
print(modele_complet.summary())
print("Modele 1")
print(f"AIC : {modele_complet.aic:.1f}")


# ====================================================================================
#               Creation du modele sans V18 (Plus grande p-value)
# ====================================================================================
Variables.remove('V18')
modele2 = smf.glm(formula='Class ~' + '+'.join(Variables), data=creditcard_analyse, family=sm.families.Binomial(link=sm.families.links.logit())).fit()
print(modele2.summary())
print("Modele 2")
print(f"AIC: {modele2.aic:.2f}")


# ====================================================================================
#               Creation du modele sans V26 (Plus grande p-value)
# ====================================================================================
Variables.remove('V26')
modele3 = smf.glm(formula='Class ~' + '+'.join(Variables), data=creditcard_analyse, family=sm.families.Binomial(link=sm.families.links.logit())).fit()
print(modele3.summary())
print("Modele 3")
print(f"AIC: {modele3.aic:.2f}")

# ====================================================================================
#               Creation du modele sans V2 (Plus grande p-value)
# ====================================================================================
Variables.remove('V2')
modele4 = smf.glm(formula='Class ~' + '+'.join(Variables), data=creditcard_analyse, family=sm.families.Binomial(link=sm.families.links.logit())).fit()
print(modele4.summary())
print("Modele 4")
print(f"AIC: {modele4.aic:.2f}")


# ====================================================================================
#               Creation du modele sans V3 (Plus grande p-value)
# ====================================================================================
Variables.remove('V3')
modele5 = smf.glm(formula='Class ~' + '+'.join(Variables), data=creditcard_analyse, family=sm.families.Binomial(link=sm.families.links.logit())).fit()
print(modele5.summary())
print("Modele 5")
print(f"AIC: {modele5.aic:.2f}")

# ====================================================================================
#               Creation du modele sans V17 (Plus grande p-value)
# ====================================================================================
Variables.remove('V17')
modele6 = smf.glm(formula='Class ~' + '+'.join(Variables), data=creditcard_analyse, family=sm.families.Binomial(link=sm.families.links.logit())).fit()
print(modele6.summary())
print("Modele 6")
print(f"AIC: {modele6.aic:.2f}")

# ====================================================================================
#               Creation du modele sans V25 (Plus grande p-value)
# ====================================================================================
Variables.remove('V25')
modele7 = smf.glm(formula='Class ~' + '+'.join(Variables), data=creditcard_analyse, family=sm.families.Binomial(link=sm.families.links.logit())).fit()
print(modele7.summary())
print("Modele 7")
print(f"AIC: {modele7.aic:.2f}")


# ====================================================================================
#               Creation du modele sans V11 (Plus grande p-value)
# ====================================================================================
Variables.remove('V11')
modele8 = smf.glm(formula='Class ~' + '+'.join(Variables), data=creditcard_analyse, family=sm.families.Binomial(link=sm.families.links.logit())).fit()
print(modele8.summary())
print("Modele 8")
print(f"AIC: {modele8.aic:.2f}")


# ====================================================================================
#               Creation du modele sans V24 (Plus grande p-value)
# ====================================================================================
Variables.remove('V24')
modele9 = smf.glm(formula='Class ~' + '+'.join(Variables), data=creditcard_analyse, family=sm.families.Binomial(link=sm.families.links.logit())).fit()
print(modele9.summary())
print("Modele 9")
print(f"AIC: {modele9.aic:.2f}")


# ====================================================================================
#               Creation du modele sans V12 (Plus grande p-value)
# ====================================================================================
Variables.remove('V12')
modele10 = smf.glm(formula='Class ~' + '+'.join(Variables), data=creditcard_analyse, family=sm.families.Binomial(link=sm.families.links.logit())).fit()
print(modele10.summary())
print("Modele 10")
print(f"AIC: {modele10.aic:.2f}")


# ====================================================================================
#               Creation du modele sans V19 (Plus grande p-value)
# ====================================================================================
Variables.remove('V19')
modele11 = smf.glm(formula='Class ~' + '+'.join(Variables), data=creditcard_analyse, family=sm.families.Binomial(link=sm.families.links.logit())).fit()
print(modele11.summary())
print("Modele 11")
print(f"AIC: {modele11.aic:.2f}")


# ====================================================================================
#               Creation du modele sans V15 (Plus grande p-value)
# ====================================================================================
Variables.remove('V15')
modele12 = smf.glm(formula='Class ~' + '+'.join(Variables), data=creditcard_analyse, family=sm.families.Binomial(link=sm.families.links.logit())).fit()
print(modele12.summary())
print("Modele 12")
print(f"AIC: {modele12.aic:.2f}")


# ====================================================================================
#               Creation du modele sans Time (Plus grande p-value)
# ====================================================================================
Variables.remove('Time')
modele13 = smf.glm(formula='Class ~' + '+'.join(Variables), data=creditcard_analyse, family=sm.families.Binomial(link=sm.families.links.logit())).fit()
print(modele13.summary())
print("Modele 13")
print(f"AIC: {modele13.aic:.2f}")


# ====================================================================================
#               Creation du modele sans V6 (Plus grande p-value)
# ====================================================================================
Variables.remove('V6')
modele14 = smf.glm(formula='Class ~' + '+'.join(Variables), data=creditcard_analyse, family=sm.families.Binomial(link=sm.families.links.logit())).fit()
print(modele14.summary())
print("Modele 14")
print(f"AIC: {modele14.aic:.2f}")

# ====================================================================================
#               Validation du modele sur echantillon Train/Test
# ====================================================================================
from sklearn.model_selection import train_test_split
Y = creditcard_analyse['Class']
X = creditcard_analyse[Variables]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)
modele_validation = smf.glm(formula='Y_train ~' + '+'.join(Variables), data=X_train, family=sm.families.Binomial(link=sm.families.links.Logit())).fit()
proba_predi = modele_validation.predict(X_test)
print(modele_validation.summary())

# Test de differents seuils de decision
y_predi1 = np.where((proba_predi > 0.5), 1, 0)
y_predi2 = np.where((proba_predi > 0.4), 1, 0)
y_predi3 = np.where((proba_predi > 0.3), 1, 0)
y_predi4 = np.where((proba_predi > 0.2), 1, 0)
y_predi5 = np.where((proba_predi > 0.1), 1, 0)
y_predi6 = np.where((proba_predi > 0.08), 1, 0)
y_predi7 = np.where((proba_predi > 0.06), 1, 0)
y_predi8 = np.where((proba_predi > 0.04), 1, 0)
y_predi9 = np.where((proba_predi > 0.02), 1, 0)

# Calcul des matrices de confusion
from sklearn.metrics import roc_curve, confusion_matrix, precision_score, recall_score, accuracy_score, f1_score, roc_auc_score, precision_recall_curve, average_precision_score
matrix_confusion1 = confusion_matrix(Y_test, y_predi1)
matrix_confusion2 = confusion_matrix(Y_test, y_predi2)
matrix_confusion3 = confusion_matrix(Y_test, y_predi3)
matrix_confusion4 = confusion_matrix(Y_test, y_predi4)
matrix_confusion5 = confusion_matrix(Y_test, y_predi5)
matrix_confusion6 = confusion_matrix(Y_test, y_predi6)
matrix_confusion7 = confusion_matrix(Y_test, y_predi7)
matrix_confusion8 = confusion_matrix(Y_test, y_predi8)
matrix_confusion9 = confusion_matrix(Y_test, y_predi9)

print(f'seuil 1 matrix confusion : {matrix_confusion1}')
print(f'seuil 2 matrix confusion : {matrix_confusion2}')
print(f'seuil 3 matrix confusion : {matrix_confusion3}')
print(f'seuil 4 matrix confusion : {matrix_confusion4}')
print(f'seuil 5 matrix confusion : {matrix_confusion5}')
print(f'seuil 6 matrix confusion : {matrix_confusion6}')
print(f'seuil 7 matrix confusion : {matrix_confusion7}')
print(f'seuil 8 matrix confusion : {matrix_confusion8}')
print(f'seuil 9 matrix confusion : {matrix_confusion9}')

index = ['Y_Reel : 0', 'Y_Reel : 1']
column = ['Y_Predi : 0', 'Y_Predi : 1']
Matrice_Confusion1 = pd.DataFrame(matrix_confusion1, index=index, columns=column)
Matrice_Confusion2 = pd.DataFrame(matrix_confusion2, index=index, columns=column)
Matrice_Confusion3 = pd.DataFrame(matrix_confusion3, index=index, columns=column)
Matrice_Confusion4 = pd.DataFrame(matrix_confusion4, index=index, columns=column)
Matrice_Confusion5 = pd.DataFrame(matrix_confusion5, index=index, columns=column)
Matrice_Confusion6 = pd.DataFrame(matrix_confusion6, index=index, columns=column)
Matrice_Confusion7 = pd.DataFrame(matrix_confusion7, index=index, columns=column)
Matrice_Confusion8 = pd.DataFrame(matrix_confusion8, index=index, columns=column)
Matrice_Confusion9 = pd.DataFrame(matrix_confusion9, index=index, columns=column)

print("Matrice de Confusion 1 :\n")
print(Matrice_Confusion1)
print("\n")
print("Matrice de Confusion 2 :\n")
print(Matrice_Confusion2)
print("\n")
print("Matrice de Confusion 3 :\n")
print(Matrice_Confusion3)
print("\n")
print("Matrice de Confusion 4 :\n")
print(Matrice_Confusion4)
print("\n")
print("Matrice de Confusion 5 :\n")
print(Matrice_Confusion5)
print("\n")
print("Matrice de Confusion 6 :\n")
print(Matrice_Confusion6)
print("\n")
print("Matrice de Confusion 7 :\n")
print(Matrice_Confusion7)
print("\n")
print("Matrice de Confusion 8 :\n")
print(Matrice_Confusion8)
print("\n")
print("Matrice de Confusion 9 :\n")
print(Matrice_Confusion9)

# Calcul des metriques de performance
print(f"Precision 1 : {precision_score(Y_test, y_predi1)*100:.1f}% \t Recall 1 : {recall_score(Y_test, y_predi1)*100:.1f}% \t F1_score : {f1_score(Y_test, y_predi1)*100:.1f}%")
print(f"Precision 2 : {precision_score(Y_test, y_predi2)*100:.1f}% \t Recall 2 : {recall_score(Y_test, y_predi2)*100:.1f}% \t F1_score : {f1_score(Y_test, y_predi2)*100:.1f}%")
print(f"Precision 3 : {precision_score(Y_test, y_predi3)*100:.1f}% \t Recall 3 : {recall_score(Y_test, y_predi3)*100:.1f}% \t F1_score : {f1_score(Y_test, y_predi3)*100:.1f}%")
print(f"Precision 4 : {precision_score(Y_test, y_predi4)*100:.1f}% \t Recall 4 : {recall_score(Y_test, y_predi4)*100:.1f}% \t F1_score : {f1_score(Y_test, y_predi4)*100:.1f}%")
print(f"Precision 5 : {precision_score(Y_test, y_predi5)*100:.1f}% \t Recall 5 : {recall_score(Y_test, y_predi5)*100:.1f}% \t F1_score : {f1_score(Y_test, y_predi5)*100:.1f}%")
print(f"Precision 6 : {precision_score(Y_test, y_predi6)*100:.1f}% \t Recall 6 : {recall_score(Y_test, y_predi6)*100:.1f}% \t F1_score : {f1_score(Y_test, y_predi6)*100:.1f}%")
print(f"Precision 7 : {precision_score(Y_test, y_predi7)*100:.1f}% \t Recall 7 : {recall_score(Y_test, y_predi7)*100:.1f}% \t F1_score : {f1_score(Y_test, y_predi7)*100:.1f}%")
print(f"Precision 8 : {precision_score(Y_test, y_predi8)*100:.1f}% \t Recall 8 : {recall_score(Y_test, y_predi8)*100:.1f}% \t F1_score : {f1_score(Y_test, y_predi8)*100:.1f}%")
print(f"Precision 9 : {precision_score(Y_test, y_predi9)*100:.1f}% \t Recall 9 : {recall_score(Y_test, y_predi9)*100:.1f}% \t F1_score : {f1_score(Y_test, y_predi9)*100:.1f}%")

# Courbe ROC
fpr, tpr, seuil = roc_curve(Y_test, proba_predi)
AUC = roc_auc_score(Y_test, proba_predi)
AUC
plt.style.use("default")
fig, ax = plt.subplots()
ax.plot(fpr, tpr, color='blue', label=f'ROC curve : {AUC :.3f}')
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')
ax.legend(loc="lower right")
ax.set_title('ROC curve')
ax.legend()
plt.tight_layout()
plt.show()

# Courbe Precision-Rappel (AUPRC)
precision, recall, seuil = precision_recall_curve(Y_test, proba_predi)
AUPRC = average_precision_score(Y_test, proba_predi)
AUPRC
plt.style.use("default")
fig, ax = plt.subplots()
ax.plot(precision, recall, color='blue', label=f'AUPRC : {AUPRC :.3f}')
ax.set_xlabel('Recall')
ax.set_ylabel('Precision')
ax.set_title('Courbe Precision-Rappel - Detection de fraude bancaire')
ax.legend(loc="lower left")
plt.tight_layout()
plt.show()