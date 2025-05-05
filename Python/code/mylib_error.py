def vraag_coureur(nummer):
    while True:
        coureur = input(f"Gebruiker {nummer}: Welke coureur ben jij? ")
        if coureur not in lst_coureur:
            return(coureur)
        print(f"Coureur {coureur} is al in de lijst")
