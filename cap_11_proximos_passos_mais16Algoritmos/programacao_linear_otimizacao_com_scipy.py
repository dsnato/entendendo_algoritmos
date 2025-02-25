from scipy.optimize import linprog

# Maximizar: 3x + 4y
# Sujeito a:
# 2x + y ≤ 8
# x + 2y ≤ 6
# x ≥ 0, y ≥ 0

obj = [-3, -4]  # Coeficientes a maximizar (negativos para linprog)
lhs = [[2, 1], [1, 2]]
rhs = [8, 6]

res = linprog(obj, A_ub=lhs, b_ub=rhs, bounds=[(0, None), (0, None)], method="highs")

print(f"Valor ótimo: {-res.fun}")
print(f"Valores de x, y: {res.x}")
