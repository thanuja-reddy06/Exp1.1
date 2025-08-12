import math

# Hard-coded coefficients
a = 1.0
b = -3.0
c = 2.0

print(f"Solving {a}x^2 + {b}x + {c} = 0")

if a == 0:
    if b != 0:
        x = -c / b
        print(f"Linear solution: x = {x}")
    else:
        print("Degenerate equation: a = 0 and b = 0 (no solution or infinite solutions)")
else:
    D = b * b - 4 * a * c
    print(f"Discriminant: {D}")
    if D > 0:
        r1 = (-b + math.sqrt(D)) / (2 * a)
        r2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"Two real roots: {r1} and {r2}")
    elif D == 0:
        r = -b / (2 * a)
        print(f"One real (double) root: {r}")
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-D) / (2 * a)
        print(f"Two complex roots: {real}+{imag}j and {real}-{imag}j")
