archivio = {
    1: {"nome": "Mario", "cognome": "Rossi", "voti": [8.5, 7.0]},
    2: {"nome": "Anna", "cognome": "Bianchi", "voti": [9.2, 10.0, 8.8]}
}

id = 3

def inserisci_studente():
    global id
    while True:
        nome = input("Insersci il nome dello studente: ")
        if nome == "" or not nome.isalpha():
            print("Nome non valido reinseriscilo")
        else:
            break
    
    while True:
        cognome = input("Inserisci il cognome dello studente: ")
        if cognome == "" or not cognome.isalpha():
            print("Cognome non valido reinseriscilo")
        else:
            break
    lista_voti = []
    while True:
        try:
            voto = float(input("Inserisci il voto dello studente, scrivi -1 per terminare: "))
            if voto == -1:
                break
            else:
                if voto >0 and voto <11:
                    lista_voti.append(voto)
                else:
                    print("Devi inserire voti compresi tra 0 e 10")
        except ValueError:
            print("Valore inserito errato, deve essere un numero intero")
    archivio[id] = {"nome": nome, "cognome": cognome, "voti": lista_voti}
    print("Studente inserito")
    id += 1
   
def visualizza_studenti():
    print("Elenco studenti")
    for id in archivio:
        print( id, archivio[id])
       
def media_voti():
    for chiave in archivio:
        voto_medio = 0
        numero_voto = 0
        for voto in archivio[chiave]["voti"]:
            voto_medio += voto
            numero_voto +=1
        media = voto_medio/numero_voto
        stampa_media(media, chiave)

def stampa_media(media, chiave):
    print("Media voti di", archivio[chiave]["nome"], media)

def visualizza_speciali():
    try: 
        media_visuallizare = float(input("Inserisci la media da visualizzare o più alta: "))
        for chiave in archivio:
            voto_medio = 0
            numero_voto = 0
            for voto in archivio[chiave]["voti"]:
                voto_medio += voto
                numero_voto +=1
            media = voto_medio/numero_voto
            if media_visuallizare <= media:
                stampa_media(media, chiave)
    except ValueError:
        print("Valore inserito errato, deve essere un numero con la virgola")

def elimina_studente():
    print(archivio.keys())
    try:
        id_rimuovere = int(input("Inserisci l'ID dell'utente da eliminare: "))

        if id_rimuovere in archivio.keys():
            archivio.pop(id_rimuovere)
        else:
            print("Id inesistente")
    except ValueError:
        print("Valore inserito errato, deve essere un numero intero")

def menu():
    while True:
        print("------------------------------------")
        print("1. Inserisci uno studente")
        print("2. Visualizza elenco studenti")
        print("3. Calcola la media dei voti")
        print("4. Visualizza studenti con media superiore a una soglia")
        print("5. Rimuovi uno studente")
        print("0. Esci")
        print("------------------------------------")
       
        try:
            scelta = int(input("Fai la tua scelta: "))
            if scelta == 1:
                inserisci_studente()
            elif scelta ==2:
                visualizza_studenti()
            elif scelta == 3:
                media_voti()
            elif scelta == 4:
                visualizza_speciali()   
            elif scelta == 5:
                elimina_studente()   
            elif scelta == 0:
                break
            else:
                print("Sei stato poco chiaro, reinserisci il valore")
        except ValueError:
            print("Valore inserito errato, deve essere un numero intero")
menu()
