from pysmt.shortcuts import And, Not, BOOL, Iff, Symbol, Equals, Or, ExactlyOne, Ite, Int, Bool, Plus, Solver
from pysmt.typing import INT

b = Bool(True)
a = Bool(False)

mary = [ b, b, a, b, a, b, b, a, b, b ]
dan  = [ b, a, a, a, b, a, b, a, a, a ]
lisa = [ b, a, a, a, b, b, b, a, b, a ]
john = [ b, b, a, a, a, b, b, a, a, a ]

sol = [
    Symbol(f"sol{i}", BOOL)
    for i in range(10)
]

ms = Int(70)
ds = Int(50)
ls = Int(30)

prob = []

prob.append(
    Equals(ms,
        Plus(
            Ite (Iff (mary[i], sol[i]), Int(10), Int(0))
            for i in range(10)
        )))

prob.append(
    Equals(ds,
           Plus(
               Ite (Iff (dan[i], sol[i]), Int(10), Int(0))
               for i in range(10)
           )))

prob.append(
    Equals(ls,
           Plus(
               Ite (Iff (lisa[i], sol[i]), Int(10), Int(0))
               for i in range(10)
           )))

with Solver("msat") as solver:
    solver.add_assertions(prob)

    if solver.solve():
        model = solver.get_model()
        print(model)
        sum = 0
        for i in range(10):
            if model[sol[i]] == john[i]:
                sum += 10
        print(sum)

        model_formula = Equals(Int(60),
            Plus(
               Ite (Iff (john[i], sol[i]), Int(10), Int(0))
               for i in range(10)
            ))

        solver.add_assertion(Not(model_formula))
        if solver.solve():
            print("The solution is not unique")
            model = solver.get_model()
            print(model)
            sum = 0
            for i in range(10):
                if model[sol[i]] == john[i]:
                    sum += 10
            print(sum)
        else:
            print("The solution is unique")
    else:
        print("UNSAT")