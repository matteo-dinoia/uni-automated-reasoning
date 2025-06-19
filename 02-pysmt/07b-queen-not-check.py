from pysmt.shortcuts import And, BOOL, Solver, Symbol, ExactlyOne, TRUE, AtMostOne

m = {
    f"m{x}{y}": Symbol(f"m{x}{y}", BOOL)
    for x in range(8)
    for y in range(8)
}

assetions = []

# Take care of both having 8 queen and only one for row
assetions.append(And(
    ExactlyOne(
        m[f"m{x}{y}"]
        for x in range(8)
    )
    for y in range(8)
))

# Same with colomn
assetions.append(And(
    ExactlyOne(
        m[f"m{x}{y}"]
        for y in range(8)
    )
    for x in range(8)
))

# Same with colomn
assetions.append(
    And(
        And(
            AtMostOne(
                m[f"m{x}{summ - x}"]
                for x in range(summ + 1)
                if x < 8 and summ - x < 8
            ),
            AtMostOne(
                m[f"m{7 - x}{summ - x}"]
                for x in range(summ + 1)
                if x < 8 and summ - x < 8
            )
        )
        for summ in range(15)
    )
)

with Solver("msat") as solver:
    solver.add_assertions(assetions)
    if solver.solve():
        print("Sat")
        model = solver.get_model()
        for y in range(8):
            for x in range(8):
                if model[m[f"m{x}{y}"]] == TRUE():
                    print("X", end='')
                else:
                    print("-", end='')
            print()
    else:
        print("Unsat")
