from pysmt.shortcuts import Symbol, Solver, And, Or, ExactlyOne, TRUE, Iff, Not, AtMostOne
from pysmt.typing import BOOL

n=8

m = {
    f"{i}Q{j}" : Symbol(f"{i}Q{j}", BOOL)
    for i in range(n)
    for j in range(n)
}

assertions = []

# Row & Col
assertions.append(
    And(
        ExactlyOne(
            m[f"{i}Q{j}"]
            for j in range(n)
        )
        for i in range(n)
    )
)

assertions.append(
    And(
        ExactlyOne(
            m[f"{i}Q{j}"]
            for i in range(n)
        )
        for j in range(n)
    )
)

# Secondary diagonal
assertions.append(
    And(
        AtMostOne(
            m[f"{i}Q{j}"]
            for i in range(n)
            for j in range(n)
            if i + j == summ
        )
        for summ in range(2 * n - 1)
    )
)

# Primary diagonal
assertions.append(
    And(
        AtMostOne(
            m[f"{i}Q{j}"]
            for i in range(n)
            for j in range(n)
            if i - j == dif
        )
        for dif in range(1 - n, n - 1)
    )
)

with Solver(name="msat") as solver:
    solver.add_assertions(assertions)

    if solver.solve():
        model = solver.get_model()
        for i in range(n):
            for j in range(n):
                if model[m[f"{i}Q{j}"]] == TRUE():
                    print("x", end="")
                else:
                    print("_", end="")
            print()


        model_formula = And(
            Iff(variable, value)
            for variable, value in model
        )

        solver.add_assertion(Not(model_formula))
        if solver.solve():
            print("The solution is not unique")
        else:
            print("The solution is unique")

    else:
        print("UNSAT")
