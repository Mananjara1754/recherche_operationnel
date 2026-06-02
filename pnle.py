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

# 1. Résoudre la relaxation continue du problème.
print("\n--- 1. Relaxation continue initiale ---")
print(f"Solution continue : x = {x_2.value()}, y = {y_2.value()}, Z = {model_v2.objective.value()}")

# 2. Identifier la variable non entière.
print("\n--- 2. Identifier la variable non entière ---")
print("La variable y a une valeur fractionnaire (1.5). On va donc brancher sur y.")

# 3. Créer deux branches.
print("\n--- 3. Créer deux branches ---")
print("Branche 1 : y <= 1")
print("Branche 2 : y >= 2")

# 4. Résoudre chaque sous-problème relaxé.
# Sous-problème 1 (Branche 1 : y <= 1)
sp1 = LpProblem(name="SP1", sense=LpMaximize)
x_sp1 = LpVariable(name="x_sp1", lowBound=0, cat=LpContinuous)
y_sp1 = LpVariable(name="y_sp1", lowBound=0, cat=LpContinuous)
sp1 += 5 * x_sp1 + 4 * y_sp1, "Objectif"
sp1 += 3 * x_sp1 + 2 * y_sp1 <= 12, "C1"
sp1 += x_sp1 + 2 * y_sp1 <= 6, "C2"
sp1 += y_sp1 <= 1, "Branche_y_leq_1"
sp1.solve()

# Sous-problème 2 (Branche 2 : y >= 2)
sp2 = LpProblem(name="SP2", sense=LpMaximize)
x_sp2 = LpVariable(name="x_sp2", lowBound=0, cat=LpContinuous)
y_sp2 = LpVariable(name="y_sp2", lowBound=0, cat=LpContinuous)
sp2 += 5 * x_sp2 + 4 * y_sp2, "Objectif"
sp2 += 3 * x_sp2 + 2 * y_sp2 <= 12, "C1"
sp2 += x_sp2 + 2 * y_sp2 <= 6, "C2"
sp2 += y_sp2 >= 2, "Branche_y_geq_2"
sp2.solve()

print("\n--- 4 et 5. Résoudre chaque sous-problème relaxé et Calculer les bornes supérieures ---")
print("Sous-problème 1 (y <= 1):")
if LpStatus[sp1.status] == 'Optimal':
    print(f"Statut : {LpStatus[sp1.status]}")
    print(f"x = {x_sp1.value():.4f}, y = {y_sp1.value():.4f}")
    Z_sp1 = sp1.objective.value()
    print(f"Borne supérieure (Z) = {Z_sp1:.4f}")
else:
    print("Pas de solution optimale.")

print("\nSous-problème 2 (y >= 2):")
if LpStatus[sp2.status] == 'Optimal':
    print(f"Statut : {LpStatus[sp2.status]}")
    print(f"x = {x_sp2.value():.4f}, y = {y_sp2.value():.4f}")
    Z_sp2 = sp2.objective.value()
    print(f"Borne supérieure (Z) = {Z_sp2:.4f}")
else:
    print("Pas de solution optimale.")

# 6. Élaguer les branches inutiles.
print("\n--- 6. Élaguer les branches inutiles ---")
print("Dans le Sous-problème 2, la solution (x=2, y=2) est entièrement entière. Z = 18.")
print("Cela nous donne une borne inférieure pour la solution optimale : Z* >= 18.")
print("La branche 2 est explorée et donne une solution entière, pas besoin de la subdiviser (Élagage par optimalité).")

print("\nDans le Sous-problème 1, la solution est (x=3.33, y=1) avec Z = 20.66.")
print("Puisque la borne supérieure (20.66) est plus grande que la borne inférieure actuelle (18),")
print("on ne peut pas l'élaguer. Il faut la subdiviser (brancher sur x <= 3 et x >= 4).")

# Sous-problème 3 (SP1 + x <= 3)
sp3 = LpProblem(name="SP3", sense=LpMaximize)
x_sp3 = LpVariable(name="x_sp3", lowBound=0, cat=LpContinuous)
y_sp3 = LpVariable(name="y_sp3", lowBound=0, cat=LpContinuous)
sp3 += 5 * x_sp3 + 4 * y_sp3, "Objectif"
sp3 += 3 * x_sp3 + 2 * y_sp3 <= 12, "C1"
sp3 += x_sp3 + 2 * y_sp3 <= 6, "C2"
sp3 += y_sp3 <= 1, "Branche_y_leq_1"
sp3 += x_sp3 <= 3, "Branche_x_leq_3"
sp3.solve()

# Sous-problème 4 (SP1 + x >= 4)
sp4 = LpProblem(name="SP4", sense=LpMaximize)
x_sp4 = LpVariable(name="x_sp4", lowBound=0, cat=LpContinuous)
y_sp4 = LpVariable(name="y_sp4", lowBound=0, cat=LpContinuous)
sp4 += 5 * x_sp4 + 4 * y_sp4, "Objectif"
sp4 += 3 * x_sp4 + 2 * y_sp4 <= 12, "C1"
sp4 += x_sp4 + 2 * y_sp4 <= 6, "C2"
sp4 += y_sp4 <= 1, "Branche_y_leq_1"
sp4 += x_sp4 >= 4, "Branche_x_geq_4"
sp4.solve()

print("\nRésolution des sous-problèmes enfants de SP1 :")
print("Sous-problème 3 (x <= 3):")
if LpStatus[sp3.status] == 'Optimal':
    print(f"Statut : {LpStatus[sp3.status]}")
    print(f"x = {x_sp3.value():.4f}, y = {y_sp3.value():.4f}")
    print(f"Z = {sp3.objective.value():.4f}")
else:
    print(f"Statut : {LpStatus[sp3.status]}")

print("\nSous-problème 4 (x >= 4):")
if LpStatus[sp4.status] == 'Optimal':
    print(f"Statut : {LpStatus[sp4.status]}")
    print(f"x = {x_sp4.value():.4f}, y = {y_sp4.value():.4f}")
    print(f"Z = {sp4.objective.value():.4f}")
else:
    print(f"Statut : {LpStatus[sp4.status]}")

# 7. Déterminer la meilleure solution entière.
print("\n--- 7. Déterminer la meilleure solution entière ---")
print("En comparant toutes les solutions entières trouvées :")
print("SP2 : (x=2.0, y=2.0) avec Z=18")
print("SP3 : (x=3.0, y=1.0) avec Z=19")
print("SP4 : (x=4.0, y=0.0) avec Z=20")
print("La meilleure solution entière optimale est x = 4, y = 0 avec Z = 20.")

# 8. Représenter l’arbre de Branch and Bound.
print("\n--- 8. Arbre de Branch and Bound ---")
print("""
                 P0 (Relaxation Continue)
                 x = 3.0, y = 1.5, Z = 21
                      /      \\
              y <= 1 /        \\ y >= 2
                    /          \\
            SP1                    SP2
      x = 3.33, y = 1         x = 2, y = 2
      Z = 20.66               Z = 18
   (Non entière -> Brancher)  (Entière -> Élaguer, Z*=18 locale)
           /    \\
    x <= 3/      \\ x >= 4
         /        \\
       SP3         SP4
    x=3, y=1    x=4, y=0
     Z=19        Z=20
  (Entière)    (Entière)
  Z*=19        Z*=20 (Optimal !)
""")
