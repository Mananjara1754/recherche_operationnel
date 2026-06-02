# exercice 0
# la fonction objectif maximise :
# Z=3x+2y
# sous les contraintes :
# x+y≤4
# 2x+y≤5
from pulp import LpMaximize, LpProblem, LpVariable, LpInteger, LpStatus

# 1. Définir le modèle d’optimisation avec un objectif de maximisation
model = LpProblem(name="exemple-plne", sense=LpMaximize)

# 2. Définir les variables de décision : x et y (entières, non négatives)
x = LpVariable(name="x", lowBound=0, cat=LpInteger)
y = LpVariable(name="y", lowBound=0, cat=LpInteger)

# 3. Définir la fonction objectif
model += 3 * x + 2 * y, "Fonction_objectif"

# 4. Ajouter les contraintes
model += x + y <= 4, "Contrainte_1"
model += 2 * x + y <= 5, "Contrainte_2"

# 5. Résoudre le problème avec le solveur par défaut (CBC)
model.solve()

# 6. Afficher les résultats
print(f"Statut : {LpStatus[model.status]}")
print(f"x = {x.value()}, y = {y.value()}")
print(f"Valeur optimale de Z = {model.objective.value()}")