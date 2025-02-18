votaram = {}
def verifica_eleitor(nome):
    if votaram.get(nome):
        print('Mande embora!')
    else:
        votaram[nome] = True
        print('Deixe votar!')

verifica_eleitor('Tom')
verifica_eleitor('Mike')
verifica_eleitor('Mike')