# Archivio iniziale di studenti
archivio = {
    1: {"nome": "Mario", "cognome": "Rossi", "voti": [8.5, 7.0], "media": 7.75},
    2: {"nome": "Anna", "cognome": "Bianchi", "voti": [9.2, 10.0, 8.8], "media": 9.0}
}

# Contatore per gli ID degli studenti
id_contatore = len(archivio) + 1

# Funzione per calcolare la media dei voti
def calcola_media(voti):
    if len(voti) > 0:
        return sum(voti) / len(voti)
    return 0  # Se non ci sono voti, la media è 0

# Funzione per inserire uno studente
def inserisci_studente():
    global id_contatore 
    nome = input("Inserisci il nome dello studente: ")
    cognome = input("Inserisci il cognome dello studente: ")
    voti = []

    while True:
        try:
            voto = float(input("Inserisci un voto (0-10), -1 per terminare: "))
            if voto == -1:
                break
            elif 0 <= voto <= 10:
                voti.append(voto)
            else:
                print("Il voto deve essere tra 0 e 10.")
        except ValueError:
            print("Errore: inserisci un numero valido.")

    media = calcola_media(voti)  # Calcolo della media
    archivio[id_contatore] = {"nome": nome, "cognome": cognome, "voti": voti, "media": media}
    print(f"Studente {nome} {cognome} inserito con ID {id_contatore}.")
    id_contatore += 1  # Incremento dell'ID per il prossimo studente

# Funzione per visualizzare l'elenco degli studenti
def visualizza_studenti():
    if not archivio:
        print("Nessuno studente presente.")
    else:
        for id_studente, info in archivio.items():
            print(f"ID: {id_studente}, Nome: {info['nome']}, Cognome: {info['cognome']}, Voti: {info['voti']}, Media: {info['media']}")

# Funzione per calcolare e visualizzare la media dei voti
def calcola_media_studente():
    for id_studente, info in archivio.items():
        print(f"ID: {id_studente}, Nome: {info['nome']}, Media: {info['media']}")

# Funzione per visualizzare gli studenti con media maggiore o uguale a una soglia
def visualizza_speciali():
    soglia = float(input("Inserisci la soglia della media: "))
    trovato = False
    for id_studente, info in archivio.items():
        if info["media"] >= soglia:
            print(f"ID: {id_studente}, Nome: {info['nome']}, Media: {info['media']}")
            trovato = True
    if not trovato:
        print(f"Nessun studente ha una media superiore o uguale a {soglia}.")

# Funzione per rimuovere uno studente
def rimuovi_studente():
    try:
        id_studente = int(input("Inserisci l'ID dello studente da rimuovere: "))
        if id_studente in archivio:
            del archivio[id_studente]
            print(f"Studente con ID {id_studente} rimosso.")
        else:
            print("Errore: ID studente non trovato.")
    except ValueError:
        print("Errore: inserisci un ID valido.")

# Funzione per il menu di navigazione
def menu():
    while True:
        print("\nMenu:")
        print("1. Inserisci uno studente")
        print("2. Visualizza elenco studenti")
        print("3. Calcola la media dei voti")
        print("4. Visualizza studenti con media superiore a una soglia")
        print("5. Rimuovi uno studente")
        print("0. Esci")

        try:
            scelta = int(input("Fai la tua scelta: "))
            if scelta == 1:
                inserisci_studente()
            elif scelta == 2:
                visualizza_studenti()
            elif scelta == 3:
                calcola_media_studente()
            elif scelta == 4:
                visualizza_speciali()
            elif scelta == 5:
                rimuovi_studente()
            elif scelta == 0:
                print("Esci dal programma.")
                break
            else:
                print("Errore: opzione non valida.")
        except ValueError:
            print("Errore: inserisci un numero valido per l'opzione.")

# Avvio del programma
if __name__ == "__main__":
    menu()
