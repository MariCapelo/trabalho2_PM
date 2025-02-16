from pyomo.environ import * 
""""A questão especifica que cada peça de camiseta(x1) vale 8 reais e de blusa(x2) vale 12 reais. 
    Defini para a questão que o total de horas trabalhadas pelos funcionarios foi de 12 horas, o que da 720 minutos,
    3600 minutos por semana. Cada setor tem de produção (corte, costura e empacotamento) tem respectivamente 25, 35 e 5 
    funcionários. Porém, nesse contexto, eu irei descosiderar esses numeros, pois considerá-los significa que devemos considerar
    produções em paralelo, o que seria um calculo mais dificil, por causa do número descrepante de funcionários em cada um dos 
    setores. Nesse caso, irei considerar irei considerar apenas o número do setor de empacotamento, que é 5."""

model = ConcreteModel("questão_2")

model.x1 = Var(within=NonNegativeReals)
model.x2 = Var(within=NonNegativeReals)

#Vou multiplicar cada um dos lucros por 5, uma vez que 5 funcionários produzem 5 blusas paralealmente em uma mesma quantidade de tempo
model.obj = Objective(expr= 40*model.x1 + 60*model.x2, sense=maximize)

#Tempo total para produzir os produtos
model.r1 = Constraint(expr= 510*model.x1 + 620*model.x2 <= 3600)

# Resolvendo o problema
solver = SolverFactory('glpk')
solver.solve(model)

# Exibindo a solução
print(f"Lucro semanal: {round(model.obj()*5, 2)}")
print(f"Camisetas produzidas = {round(model.x1()*5)}\nBlusas Produzidas = {round(model.x2()*5)}")