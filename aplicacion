import math

# -----------------------------------
# ENUNCIADO DEL PROBLEMA
# -----------------------------------

print("PROBLEMA:")
print("Una persona camina 3 metros hacia el Este y luego 4 metros hacia el Norte.")
print("Determine:")
print("1. El vector desplazamiento resultante")
print("2. La magnitud del desplazamiento")
print("3. El ángulo respecto al eje horizontal")

# -----------------------------------
# DATOS
# -----------------------------------

v1 = [3, 0]   # Este
v2 = [0, 4]   # Norte

print("\nDATOS:")
print(f"v1 = {v1}")
print(f"v2 = {v2}")

# -----------------------------------
# SOLUCIÓN
# -----------------------------------

# 1. Vector resultante
R = [v1[0] + v2[0], v1[1] + v2[1]]

print("\nSOLUCIÓN:")

print("\n1. Vector resultante:")
print(f"R = v1 + v2 = ({v1[0]} + {v2[0]}, {v1[1]} + {v2[1]})")
print(f"R = {R}")

# 2. Magnitud
modulo = math.sqrt(R[0]**2 + R[1]**2)

print("\n2. Magnitud del desplazamiento:")
print(f"|R| = √({R[0]}² + {R[1]}²)")
print(f"|R| = {modulo} metros")

# 3. Ángulo
angulo = math.degrees(math.atan(R[1] / R[0]))

print("\n3. Ángulo:")
print(f"θ = arctan({R[1]}/{R[0]})")
print(f"θ = {angulo} grados")