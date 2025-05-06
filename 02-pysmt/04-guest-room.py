from pysmt.shortcuts import Symbol, Solver, And, Or, ExactlyOne, TRUE, AtMostOne
from pysmt.typing import BOOL

def print_sat(solver):
    model = solver.get_model()
    print("SAT   ", end="")
    for r in rooms:
        for g in guests:
            if model[p[f"{g}{r}"]] == TRUE():
                print(f"{g}{r} ", end="")
    print()
    return

def print_unsat(solver):
    print("\n".join(map(lambda v: f"- {v}", solver.get_named_unsat_core())))
    print("UNSAT")
    return

def main():
    #  one room for guest and viceversa
    one_per_guest = And(
        ExactlyOne(p[f"{g}{r}"] for r in rooms)
        for g in guests
    )

    one_per_room = And(
        ExactlyOne(p[f"{g}{r}"] for g in guests)
        for r in rooms
    )

    guests_p = [
        (Or(p["A1"], p["A2"]), "A_pref"),
        (Or(p["B2"], p["B4"]), "B_pref"),
        (p["C1"],              "C_pref"),
        (Or(p["D2"], p["D4"]), "D_pref"),
        (Or(p["E1"], p["E5"]), "E_pref"),
    ]

    with Solver("msat", unsat_cores_mode="named") as solver:
        solver.add_assertion(one_per_room, named="one_per_room")
        solver.add_assertion(one_per_guest, named="one_per_guest")

        if not solver.solve():
            print_unsat(solver)
            return
        print_sat(solver)

        for (asse, name) in guests_p:
            solver.push()
            solver.add_assertion(asse, named=name)

            if solver.solve():
                print_sat(solver)
            else:
                print_unsat(solver)
                break
    return

guests = list("ABCDE")
rooms = list("12345")
p = {
    f"{i}{j}": Symbol(f"{i}{j}", BOOL)
    for i in guests
    for j in rooms
}
main()