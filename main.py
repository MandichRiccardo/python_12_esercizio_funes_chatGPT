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


def unisci_dizionari(dizionario1, dizionario2):
    """
    :type dizionario1: dict
    :type dizionario2: dict
    :return: nuovo_dizionario: dict
    """
    nuovo_dizionario = {}
    for i in dizionario1:
        nuovo_dizionario[i] = dizionario1[i]
    for i in dizionario2:
        nuovo_dizionario[i] = dizionario2[i]
    return nuovo_dizionario


def rimuovi_duplicati(old_list):
    """
    :type old_list: list
    :return: new_lista: list
    """
    new_list = []
    for i in old_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


# corpo del programma
listaInt = list(range(1, 10 + 1, 1))
print("la somma degli elementi della lista " + str(listaInt) + " è " + str(somma_lista(listaInt)))

listaString = ["mario", "luigi", "luca", "gianni", "giovanni", "mario", "luca", "gianni", "giovanni", ]
print("nella lista " + str(listaString) + "la stringa \"mario\" è contenuta " + str(conteggio_parola(listaString, "mario")) + " volte")

persona1 = {"nome": "Mario", "cognome": "Rossi", "età": 30}
persona2 = {"nome": "luigi", "cognome": "bianchi", "età": 25}
persone = unisci_dizionari(persona1, persona2)
print(persona1)
print(persona2)
print(persone)

lista = ["mario", "luigi", "mario", "luigi"]
print(lista)
lista = rimuovi_duplicati(lista)
print(lista)
