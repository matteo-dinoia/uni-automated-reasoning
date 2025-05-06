from pysmt.shortcuts import Symbol, Solver, And, Or, ExactlyOne, TRUE, Iff, Not
from pysmt.typing import BOOL

hik = ["A", "C", "D", "J", "S"]
dist = ["8", "9", "10", "11", "12"]
start = ["Bull", "Cassia", "Green", "Lake", "Teso"]

hds = {
    f"{h}{d}{s}" : Symbol(f"{h}{d}{s}", BOOL)
    for h in hik
    for d in dist
    for s in start
}

assertions = []


# ASS 1
assertions.append(
    Or(
        And(
            hds[f"{h1}{dist[i]}Teso"],
            hds[f"{h2}{dist[j]}Lake"]
        )
        for h1 in hik
        for h2 in hik
        for i in range(5)
        for j in range(5)
        if i < j
    )
)

# ASS 2
assertions.append(
    Or(
        hds[f"{h}8Cassia"]
        for h in hik
    )
)

# ASS 3
assertions.append(
    Or(
        And(
            hds[f"C{dist[i]}{s1}"],
            hds[f"D{dist[j]}{s2}"]
        )
        for s1 in start
        for s2 in start
        for i in range(5)
        for j in range(5)
        if i + 2 == j
    )
)

# ASS 4
assertions.append(
    Or(
        And(
            hds[f"{h}{dist[i]}Cassia"],
            hds[f"A{dist[j]}{s}"]
        )
        for s in start
        for h in hik
        for i in range(5)
        for j in range(5)
        if i + 3 == j
    )
)

# ASS 5
assertions.append(
    Or(
        Or(
            hds[f"D{d}Teso"]
            for d in dist
        ),
        Or(
            hds[f"A9{s}"]
            for s in start
        ),
    )
)

# ASS 6
assertions.append(
    Not(
        Or(
            hds[f"S{d}Green"]
            for d in dist
        )
    )
)

# ASS 7
assertions.append(
    Or(
        Or(
            hds[f"J{d}Lake"],
            hds[f"C{d}Lake"]
        )
        for d in dist
    )
)

# Exactly one
assertions.append(
    And(
        ExactlyOne(
            hds[f"{h}{d}{s}"]
            for h in hik
            for d in dist
        )
        for s in start
    )
)
assertions.append(
    And(
        ExactlyOne(
            hds[f"{h}{d}{s}"]
            for h in hik
            for s in start
        )
        for d in dist
    )
)
assertions.append(
    And(
        ExactlyOne(
            hds[f"{h}{d}{s}"]
            for s in start
            for d in dist
        )
        for h in hik
    )
)


with Solver(name="msat") as solver:
    solver.add_assertions(assertions)

    if solver.solve():
        model = solver.get_model()
        for h in hik:
            for d in dist:
                for s in start:
                    if model[hds[f"{h}{d}{s}"]] == TRUE():
                        print(f"Hiker {h}: {d} {s}")


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
