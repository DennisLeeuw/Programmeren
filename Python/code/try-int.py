while True:
    try:
        x = int(input("Geef een nummer op: "))
        break
    except ValueError:
        print(f"Dat is geen geldig nummer, probeer het nog eens")
