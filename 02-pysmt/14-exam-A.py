from pysmt.shortcuts import And, Not, BOOL, Iff, Symbol, Equals, Or, ExactlyOne, Ite, Int, Bool, Plus, Solver
from pysmt.typing import INT


def print_sol(model):
    for y in range(5):
        for x in range(5):
            if model[grid[f"{x}{y}"]] == B:
                print("X", end="")
            elif model[grid[f"{x}{y}"]] == W:
                print("O", end="")
            elif model[grid[f"{x}{y}"]] == F:
                print("=", end="")
            else:
                print(" ", end="")
        print()


E = Int(0)
F = Int(1)
W = Int(2)
B = Int(3)

grid = {
    f"{x}{y}": Symbol(f"grid{x}{y}", INT)
    for x in range(5)
    for y in range(5)
}
groups = [
    ["00", "01", "02", "03", "04", "14"],
    ["11", "12", "13"],
    ["20", "21", "22"],
    ["30", "40", "41", "42"],
    ["31", "32", "33"],
    ["24", "34", "44"],
]

assertions = []

assertions.append(Equals(grid["10"], F))
assertions.append(Equals(grid["23"], F))
assertions.append(Equals(grid["43"], F))

assertions.append(
    And(
        And(
            ExactlyOne(
                Equals(W, grid[el])
                for el in group
            ),
            ExactlyOne(
                Equals(B, grid[el])
                for el in group
            ),
            And(
                Or(
                    Equals(B, grid[el]),
                    Equals(W, grid[el]),
                    Equals(E, grid[el])
                )
                for el in group
            )
        )
        for group in groups
    )
)

assertions.append(
    And(
        Or(
            Not(Equals(grid[f"{x}{y}"], W)),
            Or(
                Equals(grid[f"{x}{y - 1}"], W),
                Equals(grid[f"{x}{y - 1}"], F)
            )
        )
        for x in range(5)
        for y in range(1, 5)
    )
)

assertions.append(
    And(
        Or(
            Not(Equals(grid[f"{x}{y}"], B)),
            Or(
                Equals(grid[f"{x}{y + 1}"], B),
                Equals(grid[f"{x}{y + 1}"], F)
            )
        )
        for x in range(5)
        for y in range(4)
    )
)

with Solver(name="msat") as solver:
    solver.add_assertions(assertions)

    if solver.solve():
        print("SAT")
        model = solver.get_model()
        print_sol(model)

        solver.add_assertion(Or(
            Not(Equals(grid[f"{x}{y}"], model[grid[f"{x}{y}"]]))
            for x in range(5)
            for y in range(5)
        ))

        # there are two solution in this case
        if solver.solve():
            print("Solution not unique")
            model = solver.get_model()
            print_sol(model)
    else:
        print("UNSAT")
