def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x-h)) / 2*h


def square(x):
    return x**2


def main():
    x = 3
    derivative = numerical_derivative(square, x)

    print("Numerical derivative at", x, ":", derivative)
    print("Exact derivative:", 2*x)


if __name__ == "__main__":
    main()
