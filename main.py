from logo import logo

print(logo)


def addition(number1, number2):
    return number1 + number2


def soustraction(number1, number2):
    return number1 + number2


def multiplication(number1, number2):
    return number1 + number2


def division(number1, number2):
    if number2 == 0:
        print("Impossible de diviser un nombre par zero")
    return number1 / number2

operateur = {
    "+": addition,
    "-": soustraction,
    "*": multiplication,
    "/": division
}

def calculer():
    number_1 = int(input("Entrez le premier nombre\n"))
    for symbole in operateur:
        print(symbole)

    continuer_executer = True
    while continuer_executer:
        dans_operateur = input("Choisissez entre les operateurs ci-dessus: ").lower()
        number_2 = int(input("Entrez le deuxieme nombre\n"))
        calculer_fonction = operateur[dans_operateur]
        reponse = calculer_fonction(number_1, number_2)

        print(f"{number_1} {dans_operateur} {number_2} = {reponse}")

        if input(f"Tapez 'o' pour continuer à calculer avec {reponse} 'n' pour commencer une nouvelle calculatrice: ") == "o":
            number_1 = reponse
        else:
            continuer_executer = False
            calculer()


calculer()
