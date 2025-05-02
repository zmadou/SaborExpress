import os

restaurantes = [{'nome':'Sabor Express','categoria': 'serviços','ativo': True}, {'nome':'Sabor do Brasil','categoria':'bahiana','ativo': False}, {'nome':'Sabor do Mundo','categoria':'pratos do exterior', 'ativo': False}]

def exibir_nome():  
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o programa')
def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu:\n')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(f'{texto}\n')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu()
    

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()
    

def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | Ativo: {ativo}')
    voltar_ao_menu()
    

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:opcao_invalida()

def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()