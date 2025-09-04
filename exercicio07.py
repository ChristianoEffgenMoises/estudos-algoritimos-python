# Solicita três notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Verifica se o aluno está aprovado
if media >= 7:
    print(f"Média: {media:.2f} - Aluno aprovado!")
else:
    print(f"Média: {media:.2f} - Aluno reprovado.")