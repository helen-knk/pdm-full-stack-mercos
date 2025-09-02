def obter_idades():
    lista_de_idades = []
    while True:
        idade = input('Informe a idade (digite 0 para finalizar): ')

        if idade == '0':
            break

        try:
            idade_float = float(idade)

            if idade_float.is_integer() and idade_float > 0:
                lista_de_idades.append(int(idade_float))
            else:
                print("Uma idade precisa ser um número inteiro positivo.")
        except ValueError:
            print("Digite um número válido.")

    return lista_de_idades


def ordenar_lista_idades(lista_de_idades):
    return sorted(lista_de_idades)


def contar_maiores_de_idade(lista_de_idades):
    return sum(1 for idade in lista_de_idades if idade >= 18)


def formatar_mensagem(idades_ordenadas, quant_maiores):
    if quant_maiores == 0:
        print('Ninguém é maior de idade.')

    titulo = 'Idade informada' if quant_maiores == 1 else 'Idades informadas'
    pessoa = 'pessoa maior' if quant_maiores == 1 else 'pessoas maiores'
    verbo = 'Existe' if quant_maiores == 1 else 'Existem'

    idades_formatadas = ", ".join(map(str, idades_ordenadas))
    return f'\n{titulo}: {idades_formatadas}.\n{verbo} {quant_maiores} {pessoa}.'


def main():
    idades = obter_idades()
    idades_ordenadas = ordenar_lista_idades(idades)
    quant_maiores = contar_maiores_de_idade(idades_ordenadas)

    mensagem = formatar_mensagem(idades_ordenadas, quant_maiores)
    print(mensagem)


if __name__ == '__main__':
    main()
