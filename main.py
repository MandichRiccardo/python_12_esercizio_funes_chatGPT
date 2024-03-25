# funzione che prende come parametro una lista e ritorna la sua somma
def somma_lista(lista):
    """

    :type lista: list
    """
    somma = 0
    for i in lista:
        somma += i
    return somma


# funzione che conta quante volte una parola è uguale all'elemento di una lista
def conteggio_parola(lista, stringa):
    """

    :type lista: list
    :type stringa: string
    """
    count = 0
    for i in lista:
        if i == stringa:
            count += 1
    return count


# corpo del programma
for i in range(1, 11, 1):
    listaInt = list(range(1, i + 1, 1))
    print("la somma degli elementi della lista " + str(listaInt) + " è " + str(somma_lista(listaInt)))
listaString = ["mario", "luigi", "luca", "gianni", "giovanni", "mario", "luca", "gianni", "giovanni", ]
print("nella lista " + str(listaString) + "la stringa \"mario\" è contenuta " + str(conteggio_parola(listaString, "mario")) + " volte")
