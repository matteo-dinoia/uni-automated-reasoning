from pysmt.shortcuts import Symbol, Solver, Not, Int, Equals, Or, And, Implies, ForAll, Exists
from pysmt.typing import INT, FunctionType, BOOL

A = Int(0)
B = Int(1)
C = Int(2)
people = [A, B, C]
killer = Symbol("Killer", INT)
x = Symbol("x", INT)
y = Symbol("y", INT)
hates = Symbol("hates", FunctionType(BOOL, [INT, INT]))
richer = Symbol("richer", FunctionType(BOOL, [INT, INT]))

prob = []

# Killer in the house
prob.append(Or(
    Equals(killer, x)
    for x in people
))

# Killer hate is victims
prob.append(hates(killer, A))
# Killer not richer than victim
prob.append(Not(richer(killer, A)))

#  Charles hates no one that Aunt Agatha hates.
prob.append(And(
    Implies(hates(A, x), (Not (hates(C, x))))
    for x in people
))

# Agatha hates everyone except the butler.
prob.append(And(
    hates(A, x)
    for x in people
    if x != B
))

# Butler hates everyone not richer than A
prob.append(And(
    Implies(Not(richer(x, A)), hates(B, x))
    for x in people
))

# The butler hates everyone Aunt Agatha hates.
prob.append(And(
    Implies(hates(A, x), (hates(B, x)))
    for x in people
))

# No one hates everyone.
prob.append(
    ForAll([x], Exists([y], hates(x, y)))
)

# Richer not symmetry
prob.append(
    ForAll([x,y], Implies(richer(x,y), Not(richer(y, x))))
)

# Richer not reflexivity
prob.append(And(
    Not(richer(x,x))
    for x in people
))

with Solver("z3") as solver:
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
