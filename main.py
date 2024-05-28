import random

# escolher tipo de missão nosso caso "entregar" # esse é o próximo passo
# escolher item no caso "flor"
# escolher receptor ""
# escolher local específico "taverna"
# escolher local "capital"

item=['flor','cordão','balde']
contratante=['Moça','Padre','Construtor']
local=['Capital','Campos Verdejantes','Gabara']
localE=['residência Mill','Igreja','ponte Strefield']

item_selec=random.choice(item)
contratante_selec=random.choice(contratante)
local_selec=random.choice(local)
localE_selec=random.choice(localE)

def mostrar_item():
    cont=1
    for itens in item:
        nome_item=itens
        print(f'{cont}. {nome_item}')
        cont+=1
        

def escolher_item():
    try:
       opcao_escolhida=int(input('Escolha o item que irá entregar'))
       if opcao_escolhida==1:
           print('oi')
    except:
        print('tchau')



def mostrar_random():
    print('Entregue {} para {} na {} na {}.'.format(item_selec,contratante_selec,local_selec,localE_selec))

mostrar_item()
print("-- -- --")
mostrar_random()
