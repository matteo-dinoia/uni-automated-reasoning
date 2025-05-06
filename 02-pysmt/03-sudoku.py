from pysmt.shortcuts import Symbol, Solver, And, Or, ExactlyOne, TRUE, Iff, Not
from pysmt.typing import BOOL

m = {
    f"{i}{j}{v}" : Symbol(f"{i}{j}{v}", BOOL)
    for i in range(9)
    for j in range(9)
    for v in range(9)
}

assertions = []

# Single color
assertions.append(
    And(
        ExactlyOne(
            m[f"{i}{j}{v}"]
            for v in range(9)
        )
        for i in range(9)
        for j in range(9)
    )
)

# Each row and each col contains a number only once
assertions.append(
    And(
        ExactlyOne(
            m[f"{i}{j}{v}"]
            for j in range(9)
        )
        for i in range(9)
        for v in range(9)
    )
)
assertions.append(
    And(
        ExactlyOne(
            m[f"{i}{j}{v}"]
            for i in range(9)
        )
        for v in range(9)
        for j in range(9)
    )
)

# Each in each chunk
assertions.append(
    And(
        ExactlyOne(
            m[f"{chunk_i*3 + di}{chunk_j*3 + dj}{v}"]
            for di in range(3)
            for dj in range(3)
        )
        for chunk_i in range(3)
        for chunk_j in range(3)
        for v in range(9)
    )
)

# Already set
assertions.append(
    And(
        m["038"],
        m["060"],
        m["172"],
        m["184"],
        m["227"],
        m["246"],
        m["344"],
        m["368"],
        m["400"],
        m["423"],
        m["432"],
        m["461"],
        m["516"],
        m["558"],
        m["582"],
        m["624"],
        m["641"],
        m["656"],
        m["713"],
        m["728"],
        m["767"],
        m["806"],
        m["830"],
        m["871"],
    )
)


with Solver(name="msat") as solver:
    solver.add_assertions(assertions)

    if solver.solve():
        model = solver.get_model()
        for i in range(9):
            if i % 3 == 0:
                print()
            for j in range(9):
                if j % 3 == 0:
                    print(" ", end="")
                for v in range(9):
                    if model[m[f"{i}{j}{v}"]] == TRUE():
                        print(f"{v+1}", end="")
                print(" ", end="")
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
