from pysmt.shortcuts import (
    And,
    Or,
    Symbol,
    BOOL,
    ExactlyOne,
    Solver,
    TRUE,
    write_smtlib,
)
from pysmt.solvers.msat import MathSAT5Solver


guests = list("ABCDE")
rooms = list("12345")

xx = {f"{g}{r}": Symbol(f"{g}{r}", BOOL) for g in guests for r in rooms}


def print_model(model, last_guest_arrived):
    assignment = {}
    for g in guests:
        room = [r for r in rooms if model[xx[f"{g}{r}"]] == TRUE()]
        assert len(room) == 1
        room = room[0]
        assignment[g] = room
        if g == last_guest_arrived:
            break
    print(", ".join(f"{g} -> {r}" for g, r in assignment.items()))


def print_core(core):
    print("\n".join(map(lambda v: f"- {v}", core)))
    # print(core)


assertions = []


# Every guest goes in exactly one room
for g in guests:
    assertions.append(
        (
            ExactlyOne(xx[f"{g}{r}"] for r in rooms),
            f"guest {g} goes in exactly one room",
        )
    )

# Every room hosts exactly one guest
for r in rooms:
    assertions.append(
        (
            ExactlyOne(xx[f"{g}{r}"] for g in guests),
            f"room {r} hosts exactly one guest",
        )
    )

guests_preferences = [
    (Or(xx["A1"], xx["A2"]), "Guest A"),
    (Or(xx["B2"], xx["B4"]),"Guest B."),
    (xx["C1"], "Guest C"),
    (Or(xx["D2"], xx["D4"]), "Guest D"),
    (Or(xx["E1"], xx["E5"]), "Guest E"),
]



with Solver("msat", unsat_cores_mode="named") as msat:
    for assertion, name in assertions:
        msat.add_assertion(assertion, named=name)

    for g, (ass, name) in zip(guests, guests_preferences):
        msat.push()
        msat.add_assertion(ass, named=name)
        if msat.solve():
            print("SAT")
        else:
            print(
                f"Guest {g} cannot be satisfied, because of: ",
            )
            print_core(msat.get_named_unsat_core())
            break