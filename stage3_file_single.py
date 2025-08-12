import math

# Read coefficients from a file (single set of inputs)
filename = "input_single.txt"

with open(filename, "r") as file:
    a, b, c = map(float, file.readline().split())

print(f"Read from file: a={a}, b={b}, c={c}")
print(f"Solving equation: {a}x² + {b}x + {c} = 0")

if a == 0:
    if b != 0:
        print(f"Linear equation solution: x = {-c / b}")
    else:
        print("Invalid equation: a and b cannot both be zero.")
else:
    D = b**2 - 4*a*c
    print(f"Discriminant (D) = {D}")

    if D > 0:
        r1 = (-b + math.sqrt(D)) / (2*a)
        r2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Two real roots: {r1} and {r2}")
    elif D == 0:
        r = -b / (2*a)
        print(f"One real double root: {r}")
    else:
        real = -b / (2*a)
        imag = math.sqrt(-D) / (2*a)
        print(f"Two complex roots: {real}+{imag}j and {real}-{imag}j")
