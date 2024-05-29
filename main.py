import random

# lock em caracteristicas

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
    print('Entregue {} para {} na {} na {}.'.format(item_random,contratante_random,local_random,localE_random))

# -- -- --
#teste

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
    if its<=verd:
        item_selec[0]=(its-1)
        pr=(item[item_selec[0]]).upper()
        print('Item {} selecionado!!'.format(pr))
    else:
        print('Opção inválida!\n')
        escolher_item()

#testes
mostrar_item()
escolher_item()
print("-- -- --")
#mostrar_random()
