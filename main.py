import random

# -- -- -- -- -- --

#TASKS:

# UI cadastrar
# terminal cleaner

# -- -- -- -- -- --
#variaveis

item=['flor','cordão','balde']
contratante=['Moça','Padre','Construtor']
local=['Capital','Campos Verdejantes','Gabara']
localE=['residência Mill','Igreja','ponte Strefield']

#randomizer
item_random=random.choice(item)
contratante_random=random.choice(contratante)
local_random=random.choice(local)
localE_random=random.choice(localE)

#lock
its=0
item_selec=[its]

cts=0
contratante_selec=[cts]

lcs=0
local_selec=[lcs]

lces=0
localE_selec=[lces]

# -- -- --
#concluido

#randomização
def mostrar_random():
    print('\n########################\n')
    print('Sua quest será...\n')
    print('Entregue {} para {} na {} na {}.'.format(item_random,contratante_random,localE_random,local_random))
    print('\n########################')


# -- -- --
#itens

#listar itens cadastrados
def mostrar_item():
    cont_it=1
    print('Selecione 0 para retornar as opções.\n')
    for itens in item:
        nome_item=itens
        print(f'{cont_it}. {nome_item}')
        cont_it+=1
  

#escolha de itens
def escolher_item():
    verd=len(item)
    its=int(input('Escolha o item que irá fazer a quest: '))
    if its<=verd and its>0:
        item_selec[0]=(its-1)
        pr=(item[item_selec[0]]).upper()
        print('Item {} selecionado!!'.format(pr))
    elif its==0:
        voltando_ao_lock()
    else:
        print('\nOpção inválida!\n')
        escolher_item()

#cadastrar novo item
def cadastrar_item():
    novo_item=str(input('Qual novo item gostaria de cadastrar: '))
    item.append(novo_item)

#mostrando opcoes de lock de itens
def lock_itens():
    mostrar_item()
    escolher_item()


# -- -- --
#locks

def exibir_locks():
    print('1. Lockar tipo de quest')
    print('2. Lockar itens')
    print('3. Lockar contratante')
    print('4. Lockar Local')
    print('5. Lockar Local específico')
    print('6. Voltar...')

def selecionar_locks():
    try:
        opcao_escolhida=int(input('Escolha uma opção: '))
        if opcao_escolhida==1:
            print('mostrar opcoes de lock')
        elif opcao_escolhida==2:
            lock_itens()
        elif opcao_escolhida==3:
            print('mostrar opcoes de lock')
        elif opcao_escolhida==4:
            print('mostrar opcoes de lock')
        elif opcao_escolhida==5:
            print('mostrar opcoes de lock')
        elif opcao_escolhida==6:
            voltando_ao_menu()
        else:
            opcao_invalida(lock)
    except:
        opcao_invalida(lock)


#conjunto locks
def locks():
    exibir_locks()
    selecionar_locks()


# -- -- --
#UI

def exibir_opcoes():
    print('1. RAnDomIzaR')
    print('2. Lockar opções')
    print('3. Cadastrar variações')
    print('4. Sair...')

def selecionar_opcoes():
    try:
        opcao_escolhida=int(input('Escolha uma opção: '))
        if opcao_escolhida==1:
            mostrar_random()
        elif opcao_escolhida==2:
            locks()
        elif opcao_escolhida==3:
            print('mostrar opcoes de lock')
        elif opcao_escolhida==4:
            finalizar_app()
        else:
            opcao_invalida(menu)
    except:
        opcao_invalida(menu)
    

# -- -- --
#voltar e finalizando

#voltar ao menu
def voltando_ao_menu():
    input('\nDigite qualquer tecla para voltar ao menu principal...')
    main()

#voltar ao lockar opçoes
def voltando_ao_lock():
    input('\nDigite qualquer tecla para voltar ao lockar itens...')
    locks()

#reiniciando sessões por invalidez
def opcao_invalida(cat):
    print('\nOpção inválida!\n')
    input('reiciando opções...\n')
    #adicionar clear
    if cat=='menu':
        main()
    elif cat=='lock':
        locks()
    else:
        print('\nERRO {OPÇÃO INVÁLIDA}!!')

#finalizar app
def finalizar_app():
    print('\n########################\n')
    print('Encerrando o programa...\n')


#-- -- --
#famigerada main
def main():
    exibir_opcoes()
    selecionar_opcoes()


# -- -- --
#iniciando
main()