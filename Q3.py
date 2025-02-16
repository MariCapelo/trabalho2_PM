from pyomo.environ import *

model = ConcreteModel("questão_3")

model.x1 = Var(within=NonNegativeReals)
model.x2 = Var(within=NonNegativeReals)
model.x3 = Var(within=NonNegativeReals)

model.Z = Objective(expr= 24*model.x1 + 22*model.x2 + 45*model.x3, sense=maximize)

#Disponibilidade de Couro
model.r1 = Constraint(expr= 2*model.x1 + model.x2 + 3*model.x3 <= 42)
#Tempo para costura
model.r2 = Constraint(expr= 2*model.x1 + model.x2 + 2*model.x3 <= 40)
#Tempo para acabamento
model.r3 = Constraint(expr=  model.x1 + 0.5*model.x2 + model.x3 <= 45)

solver = SolverFactory('glpk')
solver.solve(model)

# primeiro vamos achar a solução otima e os valores de x1, x2 e x3 que correspondem ao lucro máximo
print("-"*40)
print("-"*40)
print(f"O lucro máximo é: {model.Z()}")
print(f"Carteiras = {model.x1()}\nEstojos = {model.x2()}\nMochilas = {model.x3()}")
print("-"*40)
print("-"*40)

#Item A
print("A)")
model.del_component(model.r1)
model.r1 = Constraint(expr= 2*model.x1 + model.x2 + 3*model.x3 <= 45)
solver.solve(model)
print(f"O lucro máximo é: {model.Z()}")
print(f"Carteiras = {model.x1()}\nEstojos = {model.x2()}\nMochilas = {model.x3()}")
print("-"*40)

#Item B
print("B)")
model.del_component(model.r1)
model.r1 = Constraint(expr= 2*model.x1 + model.x2 + 3*model.x3 <= 41)
solver.solve(model)
print(f"O lucro máximo é: {model.Z()}")
print(f"Carteiras = {model.x1()}\nEstojos = {model.x2()}\nMochilas = {model.x3()}")
print("-"*40)

#Item C
print("C)")
model.del_component(model.r2)
model.r2 = Constraint(expr= 2*model.x1 + model.x2 + 2*model.x3 <= 38)
solver.solve(model)
print(f"O lucro máximo é: {model.Z()}")
print(f"Carteiras = {model.x1()}\nEstojos = {model.x2()}\nMochilas = {model.x3()}")
print("-"*40)

#Item D
print("D)")
model.del_component(model.r2)
model.r2 = Constraint(expr= 2*model.x1 + model.x2 + 2*model.x3 <= 46)
solver.solve(model)
print(f"O lucro máximo é: {model.Z()}")
print(f"Carteiras = {model.x1()}\nEstojos = {model.x2()}\nMochilas = {model.x3()}")
print("-"*40)

#Item E
print("E)")
model.del_component(model.r3)
model.r3 = Constraint(expr=  model.x1 + 0.5*model.x2 + model.x3 <= 15)
solver.solve(model)
print(f"O lucro máximo é: {model.Z()}")
print(f"Carteiras = {model.x1()}\nEstojos = {model.x2()}\nMochilas = {model.x3()}")
print("-"*40)

#Item F
print("F)")
model.del_component(model.r3)
model.r3 = Constraint(expr=  model.x1 + 0.5*model.x2 + model.x3 <= 50)
solver.solve(model)
print(f"O lucro máximo é: {model.Z()}")
print(f"Carteiras = {model.x1()}\nEstojos = {model.x2()}\nMochilas = {model.x3()}")
print("-"*40)

#Item G
print("G)")
print("?")
print("-"*40)
