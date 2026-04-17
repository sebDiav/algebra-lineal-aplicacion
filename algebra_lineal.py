import numpy as np

# =========================
# OPERACIONES BÁSICAS
# =========================

print("=== OPERACIONES BÁSICAS ===")

A = np.array([2, 3])
B = np.array([4, 5])

print("Vector A:", A)
print("Vector B:", B)

# Suma
print("Suma A + B:", A + B)

# Resta
print("Resta A - B:", A - B)

# Producto por escalar
print("3 * A:", 3 * A)


# =========================
# 5 EJEMPLOS DE CADA UNO
# =========================

print("\n=== MÁS EJEMPLOS ===")

vectores = [
    (np.array([1,2]), np.array([3,4])),
    (np.array([0,5]), np.array([2,1])),
    (np.array([-1,3]), np.array([4,-2])),
    (np.array([6,1]), np.array([2,2])),
    (np.array([3,3]), np.array([1,0]))
]

# SUMAS
print("\n--- SUMAS ---")
for v1, v2 in vectores:
    print(v1, "+", v2, "=", v1 + v2)

# RESTAS
print("\n--- RESTAS ---")
for v1, v2 in vectores:
    print(v1, "-", v2, "=", v1 - v2)

# PRODUCTO POR ESCALAR
print("\n--- PRODUCTO POR ESCALAR ---")

escalares = [2, -1, 3, -2, 0.5]
vectores_escalar = [
    np.array([3,4]),
    np.array([5,-2]),
    np.array([0,7]),
    np.array([-3,1]),
    np.array([8,6])
]

for k, v in zip(escalares, vectores_escalar):
    print(k, "*", v, "=", k * v)


# =========================
# APLICACIÓN EN SALUD
# =========================

print("\n=== APLICACIÓN: DOSIS DE MEDICAMENTOS ===")

# Sistema:
# 2x + y = 5
# x + 3y = 7

A = np.array([[2,1],
              [1,3]])

b = np.array([5,7])

sol = np.linalg.solve(A, b)

print("Solución (x, y):", sol)

print("\nInterpretación:")
print(f"Tomar {sol[0]:.2f} dosis del medicamento A")
print(f"Tomar {sol[1]:.2f} dosis del medicamento B")