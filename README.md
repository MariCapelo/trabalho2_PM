# Teste 2 - Método Simplex - Pyomo Programação Matemática

**Instrução 1:** Resolver os problemas utilizando Python e a biblioteca Pyomo. Para mais informações sobre a biblioteca, consulte a [documentação oficial do Pyomo](https://pyomo.readthedocs.io/en/stable/).

**Instrução 2:** Baixe o solver GLPK para conseguir executar as funções a função "solve". No Windows baixe a versão 4.65 com a extenção .gz no site [GLPK GNU](https://www-gnu-org.translate.goog/software/glpk/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc). Configure o Path nas variaveis de ambiente com o caminho para a pasta win64.

**Instrução 3:** Crie um ambiente Virtual e execute o arquivo requirements.txt para baixar as bibliotecas necessárias.

---

## Questão 1

Considere o seguinte problema de Programação Linear (PL):

**Maximizar**  
\( z = x1 + x2 + 3x3 + 2x4 \)

**Sujeito a:**  
\( x1 + 2x2 - x3 + 5x4 <= 4 \)  
\( 5x1 - 2x2 + 6x4 <=\)  
\( 2x_1 + 3x_2 - 2x_3 + 3x_4 <= 3 \)  
\( -x_1 + x_3 + 2x_4 <= 0 \)  
\( x_1, x_2, x_3, x_4 >= 0 \)

**Tarefa:**  
Resolva o problema mostrando a solução ótima e os valores das variáveis.

---

## Questão 2

A Burroughs Garment Company fabrica camisas masculinas e blusas femininas para a Walmark Discount Stores. A Walmark aceitará toda a produção fornecida pela Burroughs. O processo de produção inclui cortar, costurar e embalar. A Burroughs emprega 25 trabalhadores no departamento de corte, 35 no departamento de costura e 5 no departamento de embalagem. A empresa trabalha com um turno de 8 horas por dia, 5 dias por semana. A Tabela D fornece os requisitos de tempo e os preços por unidade para as duas peças de vestuário.

**Tabela D:**  
| Produto   | Corte (min) | Costura (min) | Embalagem (min) | Preço unitário ($) |  
|-----------|-------------|---------------|-----------------|--------------------|  
| Camisas   | 20          | 70            | 12              | 8                  |  
| Blusas    | 60          | 60            | 4               | 12                 |  

**Tarefa:**  
Determine a programação de produção semanal ótima para a Burroughs.

---

## Questão 3

A Gutchi Company fabrica carteiras, estojos de barbear e mochilas. A produção dessas peças utiliza couro e materiais sintéticos, sendo o couro a matéria-prima que limita a produção. O processo de produção usa dois tipos de mão-de-obra especializada: costura e acabamento. A Tabela F fornece a disponibilidade dos recursos, sua utilização pelos três produtos e os preços por unidade.

**Tabela F:**  
| Recurso            | Carteira | Estojo de barbear | Mochila | Disponibilidade diária |  
|--------------------|----------|-------------------|---------|------------------------|  
| Couro (pés²)       | 2        | 1                 | 3       | 42                     |  
| Costura (h)        | 2        | 1                 | 2       | 40                     |  
| Acabamento (h)     | 1        | 0.5               | 1       | 45                     |  
| Preço ($)          | 24       | 22                | 45      |                        |  

**Tarefa:**  
1. Formule a questão como um problema de programação linear e ache a solução ótima.  
2. Indique se as seguintes variações nos recursos manterão a solução atual viável. Para os casos em que a viabilidade for mantida, determine a nova solução ótima (valores das variáveis e da função objetivo):  
   - (a) Disponibilidade de couro é aumentada para 45 pés².  
   - (b) Disponibilidade de couro é reduzida em 1 pé².  
   - (c) Horas de costura disponíveis são alteradas para 38 horas.  
   - (d) Horas de costura disponíveis são alteradas para 46 horas.  
   - (e) Horas de acabamento disponíveis são reduzidas para 15 horas.  
   - (f) Horas de acabamento disponíveis são aumentadas para 50 horas.  
   - (g) Você recomendaria a contratação de um trabalhador a mais para o setor de costura a $15 por hora?

---
