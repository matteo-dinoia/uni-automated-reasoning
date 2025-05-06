from pysmt.shortcuts import Symbol, GT, Solver, Not, Equals, And, Or
from pysmt.typing import INT

A = Symbol("A", INT)
B = Symbol("B", INT)
C = Symbol("C", INT)
D = Symbol("D", INT)
E = Symbol("E", INT)

prob = []

prob.append(GT(A, D))

prob.append(And(
    GT(B, C),
    GT(B, E)
))

prob.append(Or(
    GT(E, B),
    GT(E, D)
))

prob.append(GT(C, A))

with Solver("msat") as solver:
    solver.add_assertions(prob)

    if solver.solve():
        model = solver.get_model()
        print(model)

        solver.push()
        model_formula = And(
            Equals(variable, value)
            for variable, value in model
        )

        solver.add_assertion(Not(model_formula))
        if solver.solve():
            print("The solution is not unique")
        else:
            print("The solution is unique")
    else:
        print("UNSAT")
