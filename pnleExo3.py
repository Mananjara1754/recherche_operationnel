

print("les variables de decisions : A et B (entières, non négatives)")\

print("la fonction objectif : Z=50000*A+30000*B")

print("les contraintes : 5*A+2*B<82 et 3*A+2*B<61")

print("la nature desvariables est entiere")


print("Resolution avec PULP : \n")
from pulp import *

model = LpProblem("PNLE exo 3", LpMaximize)

A = LpVariable("A", 0, None, LpInteger)
B = LpVariable("B", 0, None, LpInteger)

model += 50000*A + 30000*B, "Objectif"
model += 5*A + 2*B <= 82, "Contrainte_1"
model += 3*A + 2*B <= 61, "Contrainte_2"

model.solve()

if model.status == LpStatusOptimal:
    print("Solution optimale trouvée")
    print("A = ", A.value(), ", B = ", B.value())
    print("Z = ", model.objective.value())
else:
    print("Aucune solution optimale trouvée")   


print("Conclusion : 9 unités de A et 17 unités de B permettent d'obtenir un profit maximum de 570000 euros.")