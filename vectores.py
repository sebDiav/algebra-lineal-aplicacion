import math

# -----------------------------------
# FUNCIONES
# -----------------------------------

def producto_punto(u, v):
    return u[0]*v[0] + u[1]*v[1]

def modulo(v):
    return math.sqrt(v[0]**2 + v[1]**2)


# -----------------------------------
# 1. PARALELOS (3 EJERCICIOS)
# -----------------------------------

print("==== PARALELOS ====")

vectores = [
    ([2,4], [1,2]),
    ([3,6], [-1,-2]),
    ([1,2], [2,5])
]

for u, v in vectores:
    print(f"\nVectores: {u} y {v}")

    dot = producto_punto(u, v)
    mod_u = modulo(u)
    mod_v = modulo(v)

    print(f"Producto punto: {dot}")
    print(f"|u| = {mod_u}")
    print(f"|v| = {mod_v}")
    print(f"|u||v| = {mod_u * mod_v}")

    if dot == mod_u * mod_v or dot == -mod_u * mod_v:
        print("→ Son paralelos")
    else:
        print("→ No son paralelos")


# -----------------------------------
# 2. PERPENDICULARES (3 EJERCICIOS)
# -----------------------------------

print("\n==== PERPENDICULARES ====")

vectores = [
    ([1,0], [0,5]),
    ([2,2], [2,-2]),
    ([3,1], [2,4])
]

for u, v in vectores:
    print(f"\nVectores: {u} y {v}")

    dot = producto_punto(u, v)

    print(f"Producto punto: {u[0]}*{v[0]} + {u[1]}*{v[1]} = {dot}")

    if dot == 0:
        print("→ Son perpendiculares")
    else:
        print("→ No son perpendiculares")


# -----------------------------------
# 3. MODULO (3 EJERCICIOS)
# -----------------------------------

print("\n==== MODULO ====")

vectores = [
    [3,4],
    [5,12],
    [8,15]
]

for v in vectores:
    print(f"\nVector: {v}")
    print(f"|v| = √({v[0]}² + {v[1]}²)")

    resultado = modulo(v)

    print(f"|v| = {resultado}")


# -----------------------------------
# 4. ANGULO (3 EJERCICIOS)
# -----------------------------------

print("\n==== ANGULO ENTRE VECTORES ====")

vectores = [
    ([1,0], [0,1]),
    ([1,1], [1,-1]),
    ([2,3], [4,1])
]

for u, v in vectores:
    print(f"\nVectores: {u} y {v}")

    dot = producto_punto(u, v)
    mod_u = modulo(u)
    mod_v = modulo(v)

    print(f"Producto punto: {dot}")
    print(f"|u| = {mod_u}")
    print(f"|v| = {mod_v}")

    cos_theta = dot / (mod_u * mod_v)
    angulo = math.degrees(math.acos(cos_theta))

    print(f"cos(θ) = {cos_theta}")
    print(f"θ = {angulo} grados")