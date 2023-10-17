import os
alimentos = [] 
indice_salvo = []
while True: 
    print("Selecione para começar : ") #PERGUNTA 
    op = input("(I)nserir - (D)eletar - (L)istar  ") #LEITURA 
    opcao = op.upper() #FORMATA 
    
    if len(opcao) != 1 : #CALCULO SE ESTÁ DIFERENTE DAQUILO QUE PEDI
        os.system("cls")    
        print("Não permitido!") #EXIBIÇÃO 
        continue    #VOLTA PARA O INICIO 
 
    if opcao == "I" : #VERIFICA A LETRA 
        os.system("cls")
        adds = input("Valor: ") #LEIA
        if adds in alimentos: #VERIFICA SE ESTÁ DENTRO
            print(f"Já foi adicionado {adds}.") #EXIBA 
            continue #VOLTA PARA O INICIO
        else:  #CASO CONTRARIO 
            print(f"Foi adicionado {adds}.") #EXIBA QUE FOI ADICIONA  
            alimentos.append(adds) #E ADICIONE O VALOR
    
    for indice in list(enumerate(alimentos)):   #EXIBA O INDICE E O VALOR
        indice_salvo = indice
        
    if opcao == "D" :  #VERIFICA A LETRA
        os.system("cls")
        remover = input("Fala algo para remover: ") #LEIA
        try:
            indice = int(remover)
            del alimentos[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    if opcao == "L" : #LEIA
        os.system("cls")
        if alimentos != []: #SE ESTIVER DIFERENTE DE VAZIA
            for i, item in enumerate(alimentos): #PARA I DE INDICE E ITEM DE NOME ENUMERATE(ALIMENTOS)
                print(f" {i} {item}") #EXIBA
        else: #SE ESTIVER VAZIA
            print("Lista vazia!  ") #EXIBA



