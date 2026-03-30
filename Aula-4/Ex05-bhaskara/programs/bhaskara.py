import math
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))
delta = b**2 - 4*a*c
if delta < 0:
    print("Não há raízes reais.")
elif delta == 0:
    print(f"Raiz única: x = {-b / (2*a):.4f}")
else:
    print(f"x1 = {(-b + math.sqrt(delta)) / (2*a):.4f}")
    print(f"x2 = {(-b - math.sqrt(delta)) / (2*a):.4f}")
