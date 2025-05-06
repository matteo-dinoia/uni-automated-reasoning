from pysmt.shortcuts import Symbol, Solver, And, Or, ExactlyOne, TRUE, Iff, Not
from pysmt.typing import BOOL

def encode_row_single(row, number):
    cases = []
    for start in range(0, 5-number + 1):
        case = []
        for pos in range(0, start):
            case.append(Not(m[f"{row}{pos}"]))
        for pos in range(start, start + number):
            case.append(m[f"{row}{pos}"])
        for pos in range(start + number, 5):
            case.append(Not(m[f"{row}{pos}"]))
        cases.append(And(case))
    return Or(cases)

def encode_col_single(col, number):
    cases = []
    for start in range(0, 5-number + 1):
        case = []
        for pos in range(0, start):
            case.append(Not(m[f"{pos}{col}"]))
        for pos in range(start, start + number):
            case.append(m[f"{pos}{col}"])
        for pos in range(start + number, 5):
            case.append(Not(m[f"{pos}{col}"]))
        cases.append(And(case))
    return Or(cases)

m = {
    f"{i}{j}" : Symbol(f"{i}{j}", BOOL)
    for i in range(5)
    for j in range(5)
}

assertions = []

# 3 1 in forth row
assertions.append(
    And(
        m["30"], m["31"], m["32"], ~m["33"], m["34"]
    )
)

assertions.append(encode_row_single(0, 2))
assertions.append(encode_row_single(1, 3))
assertions.append(encode_row_single(2, 3))
assertions.append(encode_row_single(4, 1))

assertions.append(encode_col_single(0, 2))
assertions.append(encode_col_single(1, 3))
assertions.append(encode_col_single(2, 4))
assertions.append(encode_col_single(3, 2))
assertions.append(encode_col_single(4, 2))

with Solver(name="msat") as solver:
    solver.add_assertions(assertions)

    if solver.solve():
        model = solver.get_model()
        for i in range(5):
            for j in range(5):
                if model[m[f"{i}{j}"]] == TRUE():
                    print("X", end="")
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
