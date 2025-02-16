from pyomo.environ import *

# Criando o modelo
model = ConcreteModel("questão_1")

# Definição das variáveis de decisão
model.x1 = Var(within=NonNegativeReals)
model.x2 = Var(within=NonNegativeReals)
model.x3 = Var(within=NonNegativeReals)
model.x4 = Var(within=NonNegativeReals)

# Função objetivo
model.obj = Objective(expr=model.x1 + model.x2 + 3*model.x3 + 2*model.x4, sense=maximize)

# Restrições
model.con1 = Constraint(expr=model.x1 + 2*model.x2 - model.x3 + 5*model.x4 <= 4)
model.con2 = Constraint(expr=5*model.x1 - 2*model.x2 + 6*model.x4 <= 8)
model.con3 = Constraint(expr=2*model.x1 + 3*model.x2 - 2*model.x3 + 3*model.x4 <= 3)
model.con4 = Constraint(expr=-model.x1 + model.x3 + 2*model.x4 <= 0)

# Resolvendo o problema
solver = SolverFactory('glpk')
solver.solve(model)

# Exibindo a solução
print(f"Valor ótimo de z: {model.obj()}")
print(f"x1 = {model.x1()}\nx2 = {model.x2()}\nx3 = {model.x3()}\nx4 = {model.x4()}")