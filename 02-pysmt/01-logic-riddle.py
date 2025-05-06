from pysmt.shortcuts import Symbol, Solver, And, Or, ExactlyOne, TRUE, Iff, Not
from pysmt.typing import BOOL

days = ["20", "21", "22", "23"]
positions = ["copywriter", "graphics", "sales", "media"]
companies = ["alpha", "laneplex", "sancode", "streeter"]

p = {
    f"{day}{position}" : Symbol(f"p{day}{position}", BOOL)
    for day in days
    for position in positions
}

c = {
    f"{day}{company}" : Symbol(f"c{day}{company}", BOOL)
    for day in days
    for company in companies
}

assertions = []
# ASS 1
assertions.append(
    Or(
        And(c["20alpha"], p["22copywriter"]),
        And(c["21alpha"], p["23copywriter"]),
    )
)
# ASS 2
assertions.append(
    Or(
        And(
            p[f"{graphic_day}graphics"],
            c[f"{sancode_day}sancode"],
        )
        for graphic_day in days
        for sancode_day in days
        if sancode_day < graphic_day
    )
)

# ASS 3
assertions.append(
    Or(
        And(c["20laneplex"], p["23sales"]),
        And(c["23laneplex"], p["20sales"]),
    )
)

# ASS 4
assertions.append(
    Or(
        And(c["20alpha"], c["22streeter"]),
        And(c["21alpha"], c["23streeter"]),
    )
)

# ASS 5
assertions.append(
    ~(p["23media"])
)

# each day has exactly one company and position

for day in days:
    assertions.append(
        ExactlyOne(
            c[f"{day}{company}"] for company in companies
        )
    )

    assertions.append(
        ExactlyOne(
            p[f"{day}{position}"] for position in positions
        )
    )

#  each position is only on one day
for position in positions:
    assertions.append(
        ExactlyOne(
            p[f"{day}{position}"]
            for day in days
        )
    )

#  each companies is only on one day
for company in companies:
    assertions.append(
        ExactlyOne(
            c[f"{day}{company}"]
            for day in days
        )
    )


with Solver(name="msat") as solver:
    solver.add_assertions(assertions)

    if solver.solve():
        model = solver.get_model()
        for day in days:
            company = [
                company
                for company in companies
                if model[c[f"{day}{company}"]] == TRUE()
            ]
            position = [
                position
                for position in positions
                if model[p[f"{day}{position}"]] == TRUE()
            ]
            print(f"Day {day}: {company} {position}")

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
