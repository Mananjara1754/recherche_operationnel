import numpy as np
from scipy.optimize import minimize, linprog

print("--- 1. Optimisation sans contraintes ---")
print("\nExercice 1")
# Minimiser f(x, y) = (x - 1)^2 + (y - 2)^2 + xy
def f1(vars):
    x, y = vars
    return (x - 1)**2 + (y - 2)**2 + x*y

x0_1 = np.array([0, 0])
res1 = minimize(f1, x0_1, method='BFGS')
print("Solution optimale (x, y):", res1.x)
print("Valeur minimum:", res1.fun)


print("\nExercice 2")
# Minimiser C(x, y) = x^2 + y^2 - 3x - 4y + xy
def f2(vars):
    x, y = vars
    return x**2 + y**2 - 3*x - 4*y + x*y

x0_2 = np.array([0, 0])
res2 = minimize(f2, x0_2, method='BFGS')
print("Solution optimale (x, y):", res2.x)
print("Valeur minimum:", res2.fun)


print("\n--- 2. Optimisation avec contraintes ---")
print("\nExercice 3")
# Minimiser f(x, y) = (x - 2)^2 + (y + 1)^2
# Contrainte: x + 2y = 3 => x + 2y - 3 = 0
def f3(vars):
    x, y = vars
    return (x - 2)**2 + (y + 1)**2

constraint3 = {'type': 'eq', 'fun': lambda vars: vars[0] + 2*vars[1] - 3}
x0_3 = np.array([0, 0])
res3 = minimize(f3, x0_3, method='SLSQP', constraints=[constraint3])
print("Solution optimale (x, y):", res3.x)
print("Valeur minimum:", res3.fun)


print("\nExercice 4")
# Minimiser L(x, y) = 3x^2 + 2y^2 + xy
# Contrainte: x + y = 100 => x + y - 100 = 0
def f4(vars):
    x, y = vars
    return 3*x**2 + 2*y**2 + x*y

constraint4 = {'type': 'eq', 'fun': lambda vars: vars[0] + vars[1] - 100}
x0_4 = np.array([50, 50])
res4 = minimize(f4, x0_4, method='SLSQP', constraints=[constraint4])
print("Solution optimale (x, y):", res4.x)
print("Valeur minimum:", res4.fun)


print("\n--- 3. Programmation linéaire ---")
print("\nExercice 5")
# Maximiser Z = 3x + 2y => Minimiser -3x - 2y
# Contraintes:
# x + y <= 4
# x <= 2
# y <= 3
# x >= 0, y >= 0

c5 = [-3, -2]
A_ub5 = [
    [1, 1],
    [1, 0],
    [0, 1]
]
b_ub5 = [4, 2, 3]
bounds5 = ((0, None), (0, None))

res5 = linprog(c5, A_ub=A_ub5, b_ub=b_ub5, bounds=bounds5, method='highs')
print("Solution optimale (x, y):", res5.x)
print("Valeur maximum Z:", -res5.fun)


print("\nExercice 6")
# Maximiser Gain = 5x + 4y => Minimiser -5x - 4y
# Contraintes:
# 3x + 2y <= 18 (CPU)
# 1x + 2y <= 12 (I/O)
# x >= 0, y >= 0

c6 = [-5, -4]
A_ub6 = [
    [3, 2],
    [1, 2]
]
b_ub6 = [18, 12]
bounds6 = ((0, None), (0, None))

res6 = linprog(c6, A_ub=A_ub6, b_ub=b_ub6, bounds=bounds6, method='highs')
print("Solution optimale (Tâche CPU, Tâche I/O):", res6.x)
print("Gain maximum:", -res6.fun)
