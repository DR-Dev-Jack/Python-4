import random
from termcolor import colored

Config = {"EXTENSIE": ".wrd", "SCHEIDER": "=", "SCHERMBREEDTE": 80}
Keys = {"DELETE": "d",  "OPSLAAN": "w", "OVERHOREN": "o", "STOPPEN": "q", "TOEVOEGEN": "t", "IMPORTEREN": "i", "EXPORTEREN": "e"}

standaard_lijst = {}


def print_regel(regel):
    if regel != "NONE":
        print(("| {:" + str(Config["SCHERMBREEDTE"] - 4) + "} |").format(regel))
    else:
        print("|" + (Config["SCHERMBREEDTE"] - 2) * " " + "|")


def print_warning(regel):
    if regel != "NONE":
        print(("| {:" + str(Config["SCHERMBREEDTE"] - 4) + "} |").format(colored(regel, 'red')))
    else:
        print("|" + (Config["SCHERMBREEDTE"] - 2) * " " + "|")


def print_opener(name):
    output = name.center(Config["SCHERMBREEDTE"], '=')
    print(output)
    print_regel("NONE")


def print_closer():
    print_regel("NONE")
    print("=" * int(Config["SCHERMBREEDTE"]))


def choose(method):
    choise = input("Choise? : ")
    if method == "normal":
        if choise == "Main":
            main()
        elif choise == Keys["IMPORTEREN"]:
            importeren()
        elif choise == Keys["TOEVOEGEN"]:
            toevoegen()
        elif choise == Keys["EXPORTEREN"]:
            exporteren()
        elif choise == Keys["OVERHOREN"]:
            overhoren()
        elif choise == Keys["STOPPEN"]:
            quit("Program stopped by user")
        else:
            print(choise, "is not a valid key input.")
            choose("normal")
    elif method == "nieuwe lijst":
        if choise == Keys["TOEVOEGEN"]:
            return "toevoegen"
        elif choise == Keys["IMPORTEREN"]:
            return "importeren"
        elif choise == Keys["DELETE"]:
            return "verwijderen"
        else:
            print(choise, "is not a valid key input.")
            choose("nieuwe lijst")


def main():
    print_opener("MENU")
    print_regel(Keys["IMPORTEREN"] + " - lijst importeren")
    print_regel(Keys["EXPORTEREN"] + " - lijst exporteren/opslaan")
    print_regel(Keys["TOEVOEGEN"] + " - woorden toevoegen aan lijst")
    print_regel(Keys["OVERHOREN"] + " - woordenlijsten overhoren")
    print_regel(Keys["STOPPEN"] + " - stoppen met het programma")
    print_closer()
    choose("normal")


def importeren():
    standaard_lijst.clear()
    print_opener("importeren")
    print_regel("Wat is de filepath van het bestand dat je wil importeren?")
    print_closer()
    filepath = input("Filepath : ")
    with open(filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split('=')
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                standaard_lijst[key] = value
    main()


def toevoegen():
    print_opener("woorden toevoegen")
    print_regel("welke woorden wil je toevoegen aan de lijst?")
    print_regel("type eerst het woord en dan de vertaling")
    print_closer()
    standaard_lijst[input("woord : ")] = input("vertaling : ")
    main()


def exporteren():
    print_opener("exporteren")
    print_regel("hoe moet de lijst die je wil exporteren heten? : ")
    print_warning("WARNING: als er al een bestand met deze naam bestaat word deze verwijderd")
    print_closer()
    filepath = input("Filepath : ")
    with open(filepath, 'w') as file:
        for key, value in standaard_lijst.items():
            line = f"{key} = {value}\n"
            file.write(line)
    standaard_lijst.clear()
    main()


def overhoren():
    sleutels = list(standaard_lijst.keys())
    while sleutels:
        sleutel = random.choice(sleutels)
        juiste_antwoord = standaard_lijst[sleutel]
        print_opener("Overhoren")
        print_regel("Wat is de vertaling van:")
        print_regel(sleutel)
        print_closer()
        guess = input("Jouw antwoord: ")
        if guess == juiste_antwoord:
            print("Correct! Goed gedaan.")
        else:
            print("Helaas, het juiste antwoord is", juiste_antwoord + ".")
        sleutels.remove(sleutel)
    main()


main()
