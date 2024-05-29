import random

# -- -- -- -- -- --

#TASKS:

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
    print('1. Lockar itens')
    print('2. Lockar contratante')
    print('3. Lockar Local')
    print('4. Lockar Local específico')
    print('5. Sair...')

def selecionar_opcoes():
    try:
        opcao_escolhida=int(input('Escolha uma opção: '))
        if opcao_escolhida==1:
            lock_itens()
        elif opcao_escolhida==2:
            print('mostrar opcoes de lock')
        elif opcao_escolhida==3:
            print('mostrar opcoes de lock')
        elif opcao_escolhida==4:
            print('mostrar opcoes de lock')
        elif opcao_escolhida==5:
            print('voltando ao menu...')
        else:
            print('opcao invalida')
    except:
        print('opcao invalida')


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
            print('mostrar opcoes de lock')
        elif opcao_escolhida==3:
            print('mostrar opcoes de lock')
        elif opcao_escolhida==4:
            print('finalizando programa...')
        else:
            print('opcao invalida')
    except:
        print('opcao invalida')
    

#-- -- --
#famigerada main
def main():
    exibir_opcoes()
    selecionar_opcoes()

# -- -- --
#iniciando
main()
