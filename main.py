def funzione_aura(parola: str):
    arrParola = list(parola)
    arrFinale = []
    arrParola.append("$")

    for i in range(0, len(arrParola)):
        arrFinale.append(arrParola)
        arrParola.insert(len(arrParola), arrParola[0])
        arrParola.pop(0)
        
    print("\nrotazione parola: ")
    print(arrFinale)
    arrFinale.sort()

    print("\nrotazioni ordinate: ")
    print(arrFinale)

    risultato = ""

    for j in range(len(arrFinale)):
        risultato = risultato + arrFinale[j][len(arrParola)-1]

    print("\nrisultato della trasformazione BWT: ")
    print(risultato)
    return risultato



if __name__ == "__main__":
    parola = input("Inserisci una parola da trasformare con il Burrows-Wheeler: ")
    funzione_aura(parola)