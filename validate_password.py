
"""
1. Hur mycket tid trodde du att det skulle ta att lösa den här uppgiften?
12 timmar
2. Hur mycket tid har du lagt ned på att lösa uppgiften?
6 timmar

Validate_pwd

"""
def validate_pwd(password):##Våran funktion validate_pwd

    """
    Validate_pwd är en funktion för att kolla om lösenordet innehåller de tecken de ska innehålla
    """
##Om alla dessa är sant, returnera sant på hela funktionen
    if (big_check(password) and
        small_check(password) and
        special_check(password) and
        lenght_check(password) and
        number_check(password)):
        print("Bra val!")
        print("Avslutar programmet...")
        return True

    #Else
    print("Lösenordet duger inte! Försök igen")
    return False

def number_check(password):
    """
    nummer_check är en funktion för att kolla om lösenordet innehåller minst 1 nummer
    """
    for number in '123456789':##en for loop, för alla nummer i 123456789
        if number in password:##Om det nummret finns i password, gör detta
            return True##Returnera sant
    return False

def lenght_check(password):
    """
    lenght_check är en funktion för att kolla om lösenordet innehåller rätt längd
    """
    if len(password) <= 16 and len(password) >= 6:
        return True
    return False

def special_check(password):
    """
    special_check är en funktion för att kolla om lösenordet innehåller minst 1 specialtecken
    """
    for special in "$@!*":##För alla specialtecken i range(for loop)
        if special in password:##Om det specialtecknet finns i password, gör detta
            return True
    return False

def small_check(password):
    """
    small_check är en funktion för att kolla om lösenordet innehåller minst 1 liten bokstav
    """
    for size in password:
        if 'a' <= size <= 'z':##Om det finns något från a till z så returnera sant
            return True
    return False

def big_check(password):
    """
    big_check är en funktion för att kolla om lösenordet innehåller minst 1 stor bokstav
    """
    for size in password:
        if 'A' <= size <= 'Z':##Om det finns något från A till Z så returnera sant
            return True
    return False

def start():
    """
    start är en funktion som fungerar som meny
    """
    ready = False
    while not ready:

        password = str(input("Skriv ditt lösenord: ")) ##En vanlig string input
        if validate_pwd(password):
            ready = True

if __name__ == "__main__":
    print("Välkommen till laboration 1")
    start()
