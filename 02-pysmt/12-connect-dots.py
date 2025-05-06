from pysmt.shortcuts import Symbol, Equals, Or, ExactlyOne, Ite, Int, Plus, Solver
from pysmt.typing import INT

E = Int(0)
Y = Int(1)
R = Int(2)
B = Int(3)
G = Int(4)

m = {
    f"{x}{y}": Symbol(f"m{x}{y}", INT)
    for x in range(5)
    for y in range(5)
}

prob = []

grid = [
    [R, Y, E, E, E],
    [E, E, E, B, E],
    [E, B, Y, E, E],
    [E, G, E, E, E],
    [E, E, E, R, G],
]

# Every cell has a color (and fixed are so)
for i in range(5):
    for j in range(5):
        if(grid[i][j] != E):
            prob.append(Equals(m[f"{i}{j}"], grid[i][j]))
        else:
            prob.append(Or(
                Equals(m[f"{i}{j}"], col)
                for col in [Y, R, B, G]
            ))

# Possible path
incr = [(-1, 0), (0, -1), (1, 0), (0,1)]

for i in range(5):
    for j in range(5):
        curr_col = grid[i][j]
        neighbours = [
            m[f"{ni}{nj}"]
            for (i_i, i_j) in incr
            if 0 <= (ni := i + i_i) < 5
            if 0 <= (nj := j + i_j) < 5
        ]

        if(curr_col != E):
            prob.append(ExactlyOne(
                Equals(neigh, curr_col)
                for neigh in neighbours
            ))
        else:
            prob.append(Equals(Int(2), Plus(
               Ite(Equals(neigh, curr_col), Int(1), Int(0))
               for neigh in neighbours
           )))

with Solver("msat") as solver:
    solver.add_assertions(prob)

    if solver.solve():
        model = solver.get_model()
        print(model)
    else:
        print("UNSAT")
