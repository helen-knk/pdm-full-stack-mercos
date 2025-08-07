import datetime

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

def calcular_ano_100(idade):
    ano_atual = datetime.datetime.now().year
    return ano_atual + (100 - idade)

ano_100 = calcular_ano_100(idade)

print(f'{nome}, você fará 100 anos em {ano_100}.')
