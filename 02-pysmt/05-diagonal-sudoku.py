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

# Diagonal
assertions.append(
    And(
        ExactlyOne(
            m[f"{d}{d}{v}"]
            for d in range(9)
        )
        for v in range(9)
    )
)

# Secondary diagonal
assertions.append(
    And(
        ExactlyOne(
            m[f"{d}{8 - d}{v}"]
            for d in range(9)
        )
        for v in range(9)
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
        m["024"],
        m["060"],
        m["133"],
        m["148"],
        m["151"],
        m["208"],
        m["282"],
        m["312"],
        m["375"],
        m["418"],
        m["470"],
        m["511"],
        m["576"],
        m["600"],
        m["687"],
        m["735"],
        m["747"],
        m["756"],
        m["822"],
        m["863"],
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
