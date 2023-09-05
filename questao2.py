
while True:
    nota1 = int(input('Insira sua nota 1: '))
    nota2 = int(input('Insira sua nota 2: '))
    nota3 = int(input('Insira sua nota 3: '))

    media = float(nota1 + nota2 + nota3)/3
    print(media)
    if media >= 7:
        print('Aprovado')
    elif media < 7 and media >= 4:
        print('Reposição')
    else:
        print('Reprovado')
    resp = input('Deseja continuar[S/N]? ')
    if resp.lower() == 'n':
        break

