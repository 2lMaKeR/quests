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
local_esp=['residência Mill','Igreja','ponte Strefield']

#randomizer
item_random=random.choice(item)
contratante_random=random.choice(contratante)
local_random=random.choice(local)
local_esp_random=random.choice(local_esp)

#lock
its=0
item_selec=[its]

cts=0
contratante_selec=[cts]

lcs=0
local_selec=[lcs]

lces=0
local_esp_selec=[lces]

# -- -- --
#concluido

#randomização
def mostrar_random():
    print('\n########################\n')
    print('Sua quest será...\n')
    print('Entregue {} para {} na {} na {}.'.format(item_random,contratante_random,local_esp_random,local_random))
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
#contratante

#listar itens cadastrados
def mostrar_contratante():
    cont_it=1
    print('Selecione 0 para retornar as opções.\n')
    for contratantes in contratante:
        nome_contratante=contratantes
        print(f'{cont_it}. {nome_contratante}')
        cont_it+=1
  

#escolha de itens
def escolher_contratante():
    verd=len(contratante)
    its=int(input('Escolha o contratante que irá fazer a quest: '))
    if cts<=verd and cts>0:
        contratante_selec[0]=(cts-1)
        pr=(contratante[contratante_selec[0]]).upper()
        print('Contratante {} selecionado!!'.format(pr))
        voltando_ao_lock()
    elif its==0:
        voltando_ao_lock()
    else:
        print('\nOpção inválida!\n')
        escolher_contratante()

#cadastrar novo item
def cadastrar_contratante():
    novo_contratante=str(input('Qual novo contratante gostaria de cadastrar: '))
    contratante.append(novo_contratante)

#mostrando opcoes de lock de itens
def lock_contratantes():
    mostrar_contratante()
    escolher_contratante()


# -- -- --
#local

#listar itens cadastrados
def mostrar_local():
    cont_it=1
    print('Selecione 0 para retornar as opções.\n')
    for locais in local:
        nome_local=locais
        print(f'{cont_it}. {nome_local}')
        cont_it+=1
  

#escolha de itens
def escolher_local():
    verd=len(local)
    lcs=int(input('Escolha o local que irá fazer a quest: '))
    if lcs<=verd and lcs>0:
        local_selec[0]=(lcs-1)
        pr=(local[local_selec[0]]).upper()
        print('Local {} selecionado!!'.format(pr))
        voltando_ao_lock()
    elif its==0:
        voltando_ao_lock()
    else:
        print('\nOpção inválida!\n')
        escolher_local()

#cadastrar novo item
def cadastrar_local():
    novo_local=str(input('Qual novo local gostaria de cadastrar: '))
    local.append(novo_local)

#mostrando opcoes de lock de itens
def lock_local():
    mostrar_local()
    escolher_local()


# -- -- --
#local E

#listar itens cadastrados
def mostrar_local_esp():
    cont_it=1
    print('Selecione 0 para retornar as opções.\n')
    for locais_esp in local_esp:
        nome_local_esp=locais_esp
        print(f'{cont_it}. {nome_local_esp}')
        cont_it+=1
  

#escolha de itens
def escolher_local_esp():
    verd=len(local_esp)
    lces=int(input('Escolha o local específico que irá fazer a quest: '))
    if lces<=verd and lces>0:
        local_esp_selec[0]=(lces-1)
        pr=(local_esp[local_esp_selec[0]]).upper()
        print('Local específico {} selecionado!!'.format(pr))
        voltando_ao_lock()
    elif its==0:
        voltando_ao_lock()
    else:
        print('\nOpção inválida!\n')
        escolher_local_esp()

#cadastrar novo item
def cadastrar_local_esp():
    novo_local_esp=str(input('Qual novo local específico gostaria de cadastrar: '))
    local_esp.append(novo_local_esp)

#mostrando opcoes de lock de itens
def lock_local_esp():
    mostrar_local_esp()
    escolher_local_esp()


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
            lock_contratantes()
        elif opcao_escolhida==4:
            lock_local()
        elif opcao_escolhida==5:
            lock_local_esp()
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