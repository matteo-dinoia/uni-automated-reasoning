from pysmt.shortcuts import Symbol, Solver, Equals, And, Plus, Int, GE, Not
from pysmt.typing import INT

def add_row(row: int, tot: int, start, end):
    prob.append(
        Equals(Int(tot),
           Plus(
               m[f"{x}{row}"]
               for x in range(start, end)
           )
        )
    )
    prob.append(
        And(
            And(
                GE(m[f"{x}{row}"], Int(1)),
                GE(Int(9), m[f"{x}{row}"])

            )
            for x in range(start, end)
        )
    )
    prob.append(
        And(
            Not(Equals(m[f"{x1}{row}"], m[f"{x2}{row}"]))
            for x1 in range(start, end)
            for x2 in range(start, end)
            if x1 != x2
        )
    )

def add_col(col, tot, start, end):
    prob.append(
        Equals(Int(tot),
           Plus(
                m[f"{col}{y}"]
                for y in range(start, end)
            )
       )
    )
    prob.append(
        And(
            Not(Equals(m[f"{col}{y1}"], m[f"{col}{y2}"]))
            for y1 in range(start, end)
            for y2 in range(start, end)
            if y1 != y2
        )
    )


m = {
    f"{x}{y}": Symbol(f"m{x}{y}", INT)
    for x in range(4)
    for y in range(5)
}

prob = []

add_row(0, 9, 0, 3)
add_row(1, 13, 0, 3)
add_row(2, 13, 0, 2)
add_row(3, 7, 1, 4)
add_row(4, 19, 1, 4)

add_col(0, 9, 0, 3)
add_col(1, 34, 0, 5)
add_col(2, 4, 0, 2)
add_col(2, 11, 3, 5)
add_col(3, 3, 3, 5)

prob.append(Equals(Int(0), m["30"]))
prob.append(Equals(Int(0), m["31"]))
prob.append(Equals(Int(0), m["32"]))
prob.append(Equals(Int(0), m["22"]))
prob.append(Equals(Int(0), m["03"]))
prob.append(Equals(Int(0), m["04"]))

prob.append(
    And(
        GE(m[f"{x}{y}"],Int(0))
        for x in range(4)
        for y in range(5)
    )
)

with Solver("msat") as solver:
    solver.add_assertions(prob)

    if solver.solve():
        model = solver.get_model()
        for y in range(5):
            for x in range(4):
                print(model[m[f"{x}{y}"]], end="\t")
            print("")
    else:
        print("UNSAT")
