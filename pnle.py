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

# ==========================================
# Exercice 1
# ==========================================
print("\n--- Exercice 1 ---")
from pulp import LpContinuous

# 1. Résoudre d’abord la relaxation continue
model_cont = LpProblem(name="exo1-relaxation-continue", sense=LpMaximize)
xc = LpVariable(name="xc", lowBound=0, cat=LpContinuous)
yc = LpVariable(name="yc", lowBound=0, cat=LpContinuous)

model_cont += 3 * xc + 2 * yc, "Objectif"
model_cont += 2 * xc + yc <= 7, "C1"
model_cont += xc + 2 * yc <= 7, "C2"

model_cont.solve()

# 2. Montrer que la solution continue optimale est x = 7/3, y = 7/3
print("2. Solution continue optimale :")
print(f"xc = {xc.value()} (7/3 = {7/3:.4f})")
print(f"yc = {yc.value()} (7/3 = {7/3:.4f})")

# 3. Calculer la valeur de la fonction objectif pour cette solution continue
Z_continue = model_cont.objective.value()
print(f"3. Valeur de Z (continue) = {Z_continue:.4f}")

# 4. Arrondir cette solution à l’entier le plus proche
x_arrondi = round(xc.value())
y_arrondi = round(yc.value())
print(f"4. Solution arrondie : x = {x_arrondi}, y = {y_arrondi}")

# 5. Vérifier si la solution arrondie est réalisable
c1_respectee = (2 * x_arrondi + y_arrondi) <= 7
c2_respectee = (x_arrondi + 2 * y_arrondi) <= 7
est_realisable = c1_respectee and c2_respectee
print(f"5. La solution arrondie est-elle réalisable ? {est_realisable} (C1: {c1_respectee}, C2: {c2_respectee})")

# 6. Tester ensuite les solutions entières réalisables autour de cette zone : (2, 2), (3, 1), (1, 3)
solutions_a_tester = [(2, 2), (3, 1), (1, 3)]
print("6 & 7. Test des solutions entières réalisables et comparaison des valeurs de Z :")
meilleure_Z = -1
meilleure_sol = None
for (xt, yt) in solutions_a_tester:
    realisable = (2 * xt + yt) <= 7 and (xt + 2 * yt) <= 7
    Z_val = 3 * xt + 2 * yt
    if realisable:
        print(f"  - Solution ({xt}, {yt}) est réalisable. Z = 3*{xt} + 2*{yt} = {Z_val}")
        if Z_val > meilleure_Z:
            meilleure_Z = Z_val
            meilleure_sol = (xt, yt)
    else:
        print(f"  - Solution ({xt}, {yt}) n'est PAS réalisable. Z = {Z_val}")

print(f"La meilleure solution entière parmi celles testées est x={meilleure_sol[0]}, y={meilleure_sol[1]} avec Z={meilleure_Z}")

# 8. Conclure
print("8. Conclusion :")
print("L'arrondi de la solution continue (2, 2) donne Z=10 et est réalisable.")
print("Cependant, la solution entière (3, 1) est également réalisable et donne un meilleur Z=11.")
print("L'arrondi de la solution continue ne donne donc pas toujours la solution entière optimale,")
print("et peut même parfois donner une solution non réalisable (si les contraintes sont plus strictes).")
print("C'est pourquoi l'arrondi n'est pas une méthode fiable pour résoudre une PLNE.")



# ======================================
# Exercice 2

#resolution relaxation continue du problème

print("\n--- Exercice 2 ---")
model_v2 = LpProblem(name="exemple-plne", sense=LpMaximize)


x_2 = LpVariable(name="x_2", lowBound=0, cat=LpContinuous)
y_2 = LpVariable(name="y_2", lowBound=0, cat=LpContinuous)

model_v2 += 5 * x_2 + 4 * y_2, "Fonction_objectif"
model_v2 += 3 * x_2 + 2 * y_2 <= 12, "Contrainte_1"
model_v2 += x_2 + 2 * y_2 <= 6, "Contrainte_2"

model_v2.solve()

print(f"Statut : {LpStatus[model_v2.status]}")
print(f"x_2 = {x_2.value()}, y_2 = {y_2.value()}")
print(f"Valeur optimale de Z = {model_v2.objective.value()}")
