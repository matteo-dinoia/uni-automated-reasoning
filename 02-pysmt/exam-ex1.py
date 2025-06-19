from pysmt.shortcuts import (
    And,
    Not,
    BOOL,
    Iff,
    Symbol,
    Equals,
    Or,
    Ite,
    Int,
    Bool,
    Plus,
    Solver,
)
from pysmt.typing import INT

SHEEP = Bool(False)
COW = Bool(True)
cow_for_row = Symbol("cow", INT)

grid = {f"{x}{y}": Symbol(f"m{x}{y}", BOOL) for x in range(6) for y in range(6)}

assertions = []

# Already filled cell
assertions.append(
    And(
        Iff(grid["20"], SHEEP),
        Iff(grid["31"], COW),
        Iff(grid["22"], COW),
        Iff(grid["33"], SHEEP),
        Iff(grid["24"], SHEEP),
        Iff(grid["35"], COW),
    )
)

# Equal and Differents simbols
assertions.append(
    And(
        Not(Iff(grid["00"], grid["01"])),
        Not(Iff(grid["11"], grid["12"])),
        Not(Iff(grid["02"], grid["03"])),
        Not(Iff(grid["13"], grid["14"])),
        Not(Iff(grid["04"], grid["05"])),
        Iff(grid["40"], grid["41"]),
        Not(Iff(grid["51"], grid["52"])),
        Not(Iff(grid["42"], grid["43"])),
        Iff(grid["53"], grid["54"]),
        Iff(grid["44"], grid["45"]),
    )
)

# Fixed number for col
assertions.append(
    And(
        Equals(
            Plus(Ite(Iff(grid[f"{x}{y}"], COW), Int(1), Int(0)) for y in range(6)),
            cow_for_row,
        )
        for x in range(6)
    )
)

# Fixed number for row
assertions.append(
    And(
        Equals(
            Plus(Ite(Iff(grid[f"{x}{y}"], COW), Int(1), Int(0)) for x in range(6)),
            cow_for_row,
        )
        for y in range(6)
    )
)

# At most 2 consecutive horizontally
assertions.append(
    And(
        Not(
            And(
                Iff(grid[f"{x}{y}"], grid[f"{x + 1}{y}"]),
                Iff(grid[f"{x}{y}"], grid[f"{x + 2}{y}"]),
            )
        )
        for x in range(6 - 3 + 1)
        for y in range(6)
    )
)

# At most 2 consecutive vertically
assertions.append(
    And(
        Not(
            And(
                Iff(grid[f"{x}{y}"], grid[f"{x}{y + 1}"]),
                Iff(grid[f"{x}{y}"], grid[f"{x}{y + 2}"]),
            )
        )
        for y in range(6 - 3 + 1)
        for x in range(6)
    )
)

with Solver(name="msat") as solver:
    solver.add_assertions(assertions)

    if solver.solve():
        print("SAT")
        model = solver.get_model()

        for y in range(6):
            for x in range(6):
                if model[grid[f"{x}{y}"]] == COW:
                    print("C", end=" ")
                else:
                    print("S", end=" ")
            print()

        solver.add_assertion(
            Or(
                Not(Iff(grid[f"{x}{y}"], model[grid[f"{x}{y}"]]))
                for x in range(6)
                for y in range(6)
            )
        )

        if solver.solve():
            print("Solution not unique")
        else:
            print("Solution is unique")
    else:
        print("UNSAT")

# SAT
# S C S S C C
# C S S C C S
# S C C S S C
# C S C S C S 
# C C S C S S
# S S C C S C
# Solution is unique

# There is a single solution in this case
# Because asking for solution which has also at least a different cell
# from the solution found, provide UNSAT, meaning that is the only solution.


# ADDITIONAL QUESTION
# The code given, creates a bit vector (4 bits),
# and then it assert that it is smaller (with unsigned comparison)
# then 1. This is possible as the BitVec can contains 0. And as it is
# unsigned that is the only possible solution (solution is unique).
