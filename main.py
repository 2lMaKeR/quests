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
def mostrar_locks(lock_cat):
    if lock_cat=='item':
        cont_it=1
        print(retorno_ops)
        for itens in item:
            nome_item=itens
            print(f'{cont_it}. {nome_item}')
            cont_it+=1

    elif lock_cat=='contratante':
        cont_it=1
        print(retorno_ops)
        for contratantes in contratante:
            nome_contratante=contratantes
            print(f'{cont_it}. {nome_contratante}')
            cont_it+=1

    elif lock_cat=='local':
        cont_it=1
        print(retorno_ops)
        for locais in local:
            nome_local=locais
            print(f'{cont_it}. {nome_local}')
            cont_it+=1

    elif lock_cat=='local especifico':
        cont_it=1
        print(retorno_ops)
        for locais_esp in local_esp:
            nome_local_esp=locais_esp
            print(f'{cont_it}. {nome_local_esp}')
            cont_it+=1

    else:
        print('#######################')
        print('ERRO def mostrar_locks')
        print('#######################')


def escolher_locks(lock_cat):
    if lock_cat=='item':
        verd=len(item)
        its=int(input('Escolha o item que irá fazer a quest: '))
        if its<=verd and its>0:
            item_selec[0]=(its-1)
            pr=(item[item_selec[0]]).upper()
            print('Item {} selecionado!!'.format(pr))
            voltando('lockar opções')
        elif its==0:
            voltando('lockar opções')
        else:
            print(op_inval)
            escolher_locks('item')

    elif lock_cat=='contratante':
        verd=len(contratante)
        its=int(input('Escolha o contratante que irá fazer a quest: '))
        if cts<=verd and cts>0:
            contratante_selec[0]=(cts-1)
            pr=(contratante[contratante_selec[0]]).upper()
            print('Contratante {} selecionado!!'.format(pr))
            voltando('lockar opções')
        elif its==0:
            voltando('lockar opções')
        else:
            print(op_inval)
            escolher_locks('contratante')

    elif lock_cat=='local':
        verd=len(local)
        lcs=int(input('Escolha o local que irá fazer a quest: '))
        if lcs<=verd and lcs>0:
            local_selec[0]=(lcs-1)
            pr=(local[local_selec[0]]).upper()
            print('Local {} selecionado!!'.format(pr))
            voltando('lockar opções')
        elif its==0:
            voltando('lockar opções')
        else:
            print(op_inval)
            escolher_locks('local')

    elif lock_cat=='local especifico':
        verd=len(local_esp)
        lces=int(input('Escolha o local específico que irá fazer a quest: '))
        if lces<=verd and lces>0:
            local_esp_selec[0]=(lces-1)
            pr=(local_esp[local_esp_selec[0]]).upper()
            print('Local específico {} selecionado!!'.format(pr))
            voltando('lockar opções')
        elif its==0:
            voltando('lockar opções')
        else:
            print(op_inval)
            escolher_locks('local especifico')
    else:
        print('#######################')
        print('ERRO def escolher_locks')
        print('#######################')

#mostrando opcoes de lock de itens
def fixar_locks(look_cat):
    mostrar_locks(look_cat)
    escolher_locks(look_cat)

# -- -- --
#locks

def exibir_locks():
    print('Selecione a variável de que desejar fixar:')
    print('1. Tipo de quest')
    print('2. Item')
    print('3. Contratante')
    print('4. Local')
    print('5. Local específico')
    print('6. Voltar...')

def selecionar_locks():
    try:
        opcao_escolhida=int(input('Escolha uma opção: '))
        if opcao_escolhida==1:
            print('mostrar opcoes de lock')
        elif opcao_escolhida==2:
            fixar_locks('item')
        elif opcao_escolhida==3:
            fixar_locks('contratante')
        elif opcao_escolhida==4:
            fixar_locks('local')
        elif opcao_escolhida==5:
            fixar_locks('local especifico')
        elif opcao_escolhida==6 or opcao_escolhida==0:
            voltando('menu principal')
        else:
            opcao_invalida('lock')
    except:
        opcao_invalida('lock')


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
        elif opcao_escolhida==4 or opcao_escolhida==0:
            finalizar_app()
        else:
            opcao_invalida('menu')
    except:
        opcao_invalida('menu')
    

# -- -- --
#voltar e finalizando  

#voltando
def voltando(volta):
    if volta=='menu principal':
        input('\nDigite qualquer tecla para voltar ao {}...'.format(volta))
        main()
    elif volta=='lockar opções':
        input('\nDigite qualquer tecla para voltar ao {}...'.format(volta))
        locks()
    else:
        print('#######################')
        print('ERRO def voltando')
        print('#######################')


#reiniciando sessões por invalidez
def opcao_invalida(cat):
    print('\nOpção inválida!\n')
    #adicionar clear
    if cat=='menu':
        voltando('menu principal')
    elif cat=='lock':
        voltando('lockar opções')
    else:
        print('#######################')
        print('ERRO def opcao_invalida')
        print('#######################')

#finalizar app
def finalizar_app():
    print('\n########################\n')
    print('Encerrando o programa...\n')

retorno_ops='Selecione 0 para retornar as opções.\n'
op_inval='\nOpção inválida!\n'


#-- -- --
#famigerada main
def main():
    exibir_opcoes()
    selecionar_opcoes()


# -- -- --
#iniciando
main()