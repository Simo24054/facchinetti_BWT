if __name__ == "__main__":


    stringa = input("Inserisci una parola da trasformare con il Burrows-Wheeler: ")

    array_parola = list(stringa)

    for i in range(len(array_parola) -1, -1 , -1 ) : 
        print(array_parola[i] , end = "")



