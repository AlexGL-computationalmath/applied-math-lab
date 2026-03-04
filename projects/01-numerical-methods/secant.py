def secant(f, x0, x1, tol=1e-8, max_iter=100, verbose=True):

    for i in range(1, max_iter + 1):

        f0 = f(x0)
        f1 = f(x1)

        if abs(f1 - f0) < 1e-14:
            raise ValueError("Denominator too small.")

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

        if verbose:
            step = abs(x2 - x1)
            print(f"iter {i:02d} | x={x2:.12f} | step={step:.3e}")

        if abs(x2 - x1) < tol:
            return x2

        x0 = x1
        x1 = x2

    print("Stopped: did not converge.")
    return x2


def f(x):
    return x**2 - 2


def main():
    root = secant(f, 1, 2)
    print("\nApproximate root:", root)


if __name__ == "__main__":
    main()