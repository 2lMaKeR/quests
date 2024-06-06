import random
import os

# -- -- -- -- -- --

#TASKS:

## fazer o modulop de orientação a objetos para refatorar esse projeto em varios files
## ou fazer novo projeto já com esse intuito

## ficha de cadastro que gera excel no save

# -- -- -- -- -- --
#variaveis

#lock
its=0
selec_item=False
item_selec=[its]

cts=0
selec_contratante=False
contratante_selec=[cts]

lcs=0
selec_local=False
local_selec=[lcs]

lces=0
selec_local_esp=False
local_esp_selec=[lces]

qts=0
selec_quest=False
quest_selec=[qts]
qrmin=0
qrmax=2

# -- -- --
#variaveis de texto

ast='\n########################\n'

#volta e finaliza
retorno_ops='Selecione 0 para retornar as opções.\n'
op_inval='\nOpção inválida!\n'
volte_ao='\nDigite qualquer tecla para voltar ao {}...'

#cadastro
novo_cad='\nQual novo {} gostaria de cadastrar: '
adin_lock=' {} foi adicionado a seleção!! Agora disponível para fixar.'
ret_cad='Retornando as escolhas de cadastro...'

#título
titulo='\n     QUESTIONS WITH QUESTS     '
divisorias='---------------------------------'


# -- -- --
#quests
apresentando_quest='Sua quest será...\n'

#arrays
item=['Flor','Cordão','Balde']
contratante=['Moça','Padre','Construtor']
local=['Capital','Campos Verdejantes','Gabara']
local_esp=['Residência Mill','Igreja','Ponte Strefield']

quest_entregar='Entregue {} para {} na {} na {}.' #its cts lces lcs
quest_eliminar='Eliminar {} que se encontra em {}.' # cts lcs
quest_construir='Construir {} em {}.' # lces lcs

quest_random=random.randint(qrmin,qrmax)
quest=[
    {'nome':'Entregar','texto':quest_entregar},
    {'nome':'Eliminar','texto':quest_eliminar},
    {'nome':'Construir','texto':quest_construir}
    ]

#randomizer
item_random=random.choice(item)
contratante_random=random.choice(contratante)
local_random=random.choice(local)
local_esp_random=random.choice(local_esp)

var1=item_random
var2=contratante_random
var3=local_esp_random
var4=local_random
vares=[var1,var2,var3,var4]
# -- -- --
#randomização

def randomizando():
    print(ast)
    print(apresentando_quest)
    global var1,var2,var3,var4
    match quest_random:
        case 0: # entregar
            var1=item_random
            var2=contratante_random
            var3=local_esp_random
            var4=local_random
        case 1: # eliminar
            var1=contratante_random
            var2=local_random
        case 2: # construir
            var1=local_esp_random
            var2=local_random
        case _:
            print(ast)
            print('ERRO def randomizando')
            print(ast)
    print(quest[quest_random]['texto'].format(var1,var2,var3,var4))
    print(ast)

def origin_random():
    global item_random
    global contratante_random
    global local_random
    global local_esp_random
    global quest_random

    item_random=random.choice(item)
    contratante_random=random.choice(contratante)
    local_random=random.choice(local)
    local_esp_random=random.choice(local_esp)
    quest_random=random.randint(qrmin,qrmax)

    global selec_item
    global selec_contratante
    global selec_local
    global selec_local_esp
    global selec_quest

    selec_item=False
    selec_contratante=False
    selec_local=False
    selec_local_esp=False
    selec_quest=False

def mostrar_random():
    global quest_random
    global item_random
    global contratante_random
    global local_random
    global local_esp_random
    
    if selec_quest==True:
        quest_random=quest_selec[0]
    if selec_item==True:
        item_random=item[item_selec[0]]
    if selec_contratante==True:
        contratante_random=contratante[contratante_selec[0]]
    if selec_local==True:
        local_random=local[local_selec[0]]
    if selec_local_esp==True:
        local_esp_random=local_esp[local_esp_selec[0]]
    randomizando()
    origin_random()
    voltando('menu principal')


# -- -- --
#cadastrar 2
def cadastrar_cad(cad_cat):
    if cad_cat=='Item':
        novo_item=str(input(novo_cad.format(cad_cat)))
        item.append(novo_item)
        print(cad_cat+adin_lock.format(novo_item))
        input(ret_cad)
        cads()

    elif cad_cat=='Contratante':
        novo_contratante=str(input(novo_cad.format(cad_cat)))
        contratante.append(novo_contratante)
        print(cad_cat+adin_lock.format(novo_contratante))
        input(ret_cad)
        cads()

    elif cad_cat=='Local':
        novo_local=str(input(novo_cad.format(cad_cat)))
        local.append(novo_local)
        print(cad_cat+adin_lock.format(novo_local))
        input(ret_cad)
        cads()

    elif cad_cat=='Local específico':
        novo_local_esp=str(input(novo_cad.format(cad_cat)))
        local_esp.append(novo_local_esp)
        print(cad_cat+adin_lock.format(novo_local_esp))
        input(ret_cad)
        cads()

    else:
        print(ast)
        print('ERRO def cadastrar_cad')
        print(ast)


# -- -- --
#cadastrar
def exibir_cad():
    print('Selecione a variável de que desejar cadastrar:')
    print('\n1. Item')
    print('2. Contratante')
    print('3. Local')
    print('4. Local específico')
    print('5. Voltar...')

def selecionar_cad():
    try:
        print(divisorias)
        opcao_escolhida=int(input('Escolha uma opção: '))
        if opcao_escolhida==1:
            cadastrar_cad('Item')
        elif opcao_escolhida==2:
            cadastrar_cad('Contratante')
        elif opcao_escolhida==3:
            cadastrar_cad('Local')
        elif opcao_escolhida==4:
            cadastrar_cad('Local específico')
        elif opcao_escolhida==5 or opcao_escolhida==0:
            voltando('menu principal')
        else:
            opcao_invalida('cad')
    except:
        opcao_invalida('cad')

#conjunto cads
def cads():
    cleaner()
    exibir_cad()
    selecionar_cad()

# -- -- --
#locks 2
def mostrar_locks(lock_cat):
    if lock_cat=='quest':
        cont_it=1
        print(retorno_ops)
        for quests in quest:
            nome_quest=quests['nome']
            print(f'{cont_it}. {nome_quest}')
            cont_it+=1

    elif lock_cat=='item':
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
        print(ast)
        print('ERRO def mostrar_locks')
        print(ast)


def escolher_locks(lock_cat):
    if lock_cat=='quest':
        verd=int(qrmax+1)
        print(divisorias)
        qts=int(input('Escolha o tipo de quest que irá ser a quest: '))
        if qts>0 and qts<=verd:
            quest_selec[0]=qts-1
            pr=(quest[quest_selec[0]]['nome']).upper()
            print('Quest do tipo {} selecionada!!'.format(pr))
            global selec_quest
            selec_quest=True
            voltando('lockar opções')
        elif qts==0:
            voltando('lockar opções')
        else:
            print(op_inval)
            escolher_locks('quest')
    elif lock_cat=='item':
        verd=len(item)
        print(divisorias)
        its=int(input('Escolha o item que irá fazer a quest: '))
        if its<=verd and its>0:
            item_selec[0]=(its-1)
            pr=(item[item_selec[0]]).upper()
            print('Item {} selecionado!!'.format(pr))
            global selec_item
            selec_item=True
            voltando('lockar opções')
        elif its==0:
            voltando('lockar opções')
        else:
            print(op_inval)
            escolher_locks('item')
    elif lock_cat=='contratante':
        verd=len(contratante)
        print(divisorias)
        cts=int(input('Escolha o contratante que irá fazer a quest: '))
        if cts<=verd and cts>0:
            contratante_selec[0]=(cts-1)
            pr=(contratante[contratante_selec[0]]).upper()
            print('Contratante {} selecionado!!'.format(pr))
            global selec_contratante
            selec_contratante=True
            voltando('lockar opções')
        elif cts==0:
            voltando('lockar opções')
        else:
            print(op_inval)
            escolher_locks('contratante')

    elif lock_cat=='local':
        verd=len(local)
        print(divisorias)
        lcs=int(input('Escolha o local que irá fazer a quest: '))
        if lcs<=verd and lcs>0:
            local_selec[0]=(lcs-1)
            pr=(local[local_selec[0]]).upper()
            print('Local {} selecionado!!'.format(pr))
            global selec_local
            selec_local=True
            voltando('lockar opções')
        elif lcs==0:
            voltando('lockar opções')
        else:
            print(op_inval)
            escolher_locks('local')

    elif lock_cat=='local especifico':
        verd=len(local_esp)
        print(divisorias)
        lces=int(input('Escolha o local específico que irá fazer a quest: '))
        if lces<=verd and lces>0:
            local_esp_selec[0]=(lces-1)
            pr=(local_esp[local_esp_selec[0]]).upper()
            print('Local específico {} selecionado!!'.format(pr))
            global selec_local_esp
            selec_local_esp=True
            voltando('lockar opções')
        elif lces==0:
            voltando('lockar opções')
        else:
            print(op_inval)
            escolher_locks('local especifico')
    else:
        print(ast)
        print('ERRO def escolher_locks')
        print(ast)

def fixar_locks(look_cat):
    cleaner()
    mostrar_locks(look_cat)
    escolher_locks(look_cat)

# -- -- --
#locks

def exibir_locks():
    print('Selecione a variável de que desejar fixar:')
    print('\n1. Tipo de quest')
    print('2. Item')
    print('3. Contratante')
    print('4. Local')
    print('5. Local específico')
    print('6. Voltar...')

def selecionar_locks():
    try:
        print(divisorias)
        opcao_escolhida=int(input('Escolha uma opção: '))
        if opcao_escolhida==1:
            fixar_locks('quest')
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
    cleaner()
    exibir_locks()
    selecionar_locks()


# -- -- --
#UI

def exibir_opcoes():
    print('1. RAnDomIzaR')
    print('2. Lockar opções')
    print('3. Cadastrar opções')
    print('4. Sair...')

def selecionar_opcoes():
    try:
        print(divisorias)
        opcao_escolhida=int(input('\nEscolha uma opção: '))
        if opcao_escolhida==1:
            mostrar_random()
        elif opcao_escolhida==2:
            locks()
        elif opcao_escolhida==3:
            cads()
        elif opcao_escolhida==4 or opcao_escolhida==0:
            finalizar_app()
        else:
            opcao_invalida('menu')
    except:
        opcao_invalida('menu')
    

# -- -- --
#voltar e finalizando  

def cleaner():
    os.system('cls')
    print(titulo)
    print(divisorias)

#voltando
def voltando(volta):
    input(volte_ao.format(volta))
    cleaner()
    if volta=='menu principal':
        main()
    elif volta=='lockar opções':
        locks()
    else:
        print(ast)
        print('ERRO def voltando')
        print(ast)


#reiniciando sessões por invalidez
def opcao_invalida(cat):
    print('\nOpção inválida!\n')
    if cat=='menu':
        voltando('menu principal')
    elif cat=='lock':
        voltando('lockar opções')
    elif cat=='cad':
        voltando('cad')
    else:
        print(ast)
        print('ERRO def opcao_invalida')
        print(ast)

#finalizar app
def finalizar_app():
    print(ast)
    print('Encerrando o programa...\n')


#-- -- --
#famigerada main
def main():
    cleaner()
    exibir_opcoes()
    selecionar_opcoes()


# -- -- --
#iniciando
main()