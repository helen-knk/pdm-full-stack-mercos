import datetime

def calcular_ano_100(idade):
    ano_atual = datetime.datetime.now().year
    return ano_atual + (100 - idade)

nome = input('Digite seu nome: ')

while True:
    try:
        idade = int(input('Digite sua idade: '))
        if 0 >= idade or idade >= 120:
            print('Idade inválida. (intervalo de 0 ao 120).')
        else:
            break
    except ValueError:
        print('OPA! Escreva uma idade válida.')

ano_100 = calcular_ano_100(idade)

print(f'{nome}, você fará 100 anos em {ano_100}.')
