import pulp

model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

L = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
F = pulp.LpVariable('Fruits juice', lowBound=0, cat='Integer')

model += L + F, "Profit"

model += 2 * L + F <= 100  # Обмеження для water
model += L <= 50  # Обмеження для Sugar
model += L <= 30  # Обмеження для Lemon juice
model += 2 * F <= 40  # Обмеження для Melted fruits

model.solve()

print("Виробляти Lemonade:", L.varValue)
print("Виробляти Fruits juice:", F.varValue)
