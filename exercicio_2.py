"""
#### Exercício 2

Uma fórmula recomenda 2mg de medicamento por kg de peso do paciente.

Peça o peso de uma pessoa e calcule a dose recomendada.

Exemplo:

Digite o peso do paciente (em kg):
70

Resposta:
Média: 140 mg
"""
## Entrada de dados

peso = float(input("Digite o peso do paciente (em kg): "))

# Cálculo da dose
dose = peso*2

# Saída de dados
print("Média: ", dose, "mg")
