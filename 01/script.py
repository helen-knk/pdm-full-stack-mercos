import datetime

def obter_nome_usuario():
    while True:
        nome = input('Digite seu nome: ').strip().title()
        if not nome:
            print('Digite corretamente o seu nome.')
            continue

        return nome

def obter_idade_usuario():
    while True:
        entrada = input('Digite sua idade: ').strip()
        if not entrada.isdigit():
            print('OPA! Digite apenas números.')
            continue

        idade = int(entrada)
        if 0 < idade < 120:
            return idade
        else:
            print('Idade inválida. Fora do intervalo de 0 ao 120.')

def calcular_ano_centenario(idade):
    ano_atual = datetime.datetime.now().year
    return ano_atual + (100 - idade)

def exibir_resultado(nome, ano_centenario):
    print(f'{nome}, você fará 100 anos em {ano_centenario}.')

def main():
    nome = obter_nome_usuario()
    idade = obter_idade_usuario()
    ano_100 = calcular_ano_centenario(idade)
    exibir_resultado(nome, ano_100)

if __name__ == '__main__':
    main()
