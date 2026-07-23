# Données

Le jeu de données utilisé dans ce projet est le jeu de données `creditcard`.

Il contient des transactions par carte bancaire effectuées en septembre 2013 par des titulaires européens. Le jeu de données regroupe 284 807 transactions réalisées sur deux jours, dont 492 transactions frauduleuses.

Le jeu de données est fortement déséquilibré : les transactions frauduleuses représentent seulement 0,172 % de l'ensemble des transactions.

Pour des raisons de confidentialité, les variables d'origine ne sont pas disponibles. Les variables `V1` à `V28` correspondent à des composantes principales obtenues par Analyse en Composantes Principales (ACP). Les variables `Time` et `Amount` n'ont pas été transformées par ACP.

La variable `Class` constitue la variable cible :
- `0` : transaction normale
- `1` : transaction frauduleuse

Le fichier de données n'est pas inclus directement dans ce dépôt GitHub. Il doit être téléchargé séparément et placé dans ce dossier avant l'exécution du code.