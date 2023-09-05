print()
def celsius():
    print()
    gf = float(input('Converta fahrenheit para celsius. Digite a temperatura em fahrenheit: '))
    gc = float(gf - 32) * 5/9
    print()
    print(f'A temperatura em celsius é de {gc} graus.')
    print()
def fahrenheit():
    print()
    c = float(input('Converta celsius para fahrenheit. Digite a temperatura em celsius: '))
    f = float(c * 9/5) + 32
    print()
    print(f'A temperatura em fahrenheit é de {f} graus.')
    print()

escolha = 0
while True:
    escolha = int(input('Escolha qual conversão de temperatura voce deseja realizar. Digite 1 para celsius. Ou 2 para fahrenheit: '))
    print()
    match escolha: 
        case 1:
           celsius()
        case 2:
            fahrenheit()
        case _:
            print('Invalido')
    resp = input(('Você deseja continuar [S/N]? '))
    if resp.lower() == 'n':
        break
    
