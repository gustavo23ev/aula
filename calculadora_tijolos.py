def calcular_tijolo(ml,ma,b1,b2,eh,ev):
    tijolo = (ml*ma)/((b1+eh)*(b2+ev))
    print(f"****************RESULTADO**************")
    print(f"Vai ser necessário : nº {tijolo} tijolos.")
    print(f"****************DADOS******************")
    print(f"Largura do muro: {ml}m a altura do muro : {ma}m.")
    print(f"Espessura horizontal argamassa: {ev}mm \nEspessura vertical argamassa:  {eh}mm.")
    print(f"comprimento do tijolo {b1}cm \nLargura do tijolo:  {b2}cm.")
calcular_tijolo(4,3,0.29,0.19,0.01,0.01)