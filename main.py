field_list = [i for i in range(1, 10)]

def print_field(field_list):
    print(f" {field_list[0]} | {field_list[1]} | {field_list[2]}")
    print(f" {field_list[3]} | {field_list[4]} | {field_list[5]}")
    print(f" {field_list[6]} | {field_list[7]} | {field_list[8]}")
    print()

def check_win(field_list):
    # Gewinne Horizontal
    if field_list[0] == field_list[1] == field_list[2]:
        return f"Spieler '{field_list[0]}' hat gewonnen!!!"

    if field_list[3] == field_list[4] == field_list[5]:
        return f"Spieler '{field_list[3]}' hat gewonnen!!!"
    if field_list[6] == field_list[7] == field_list[8]:
        return f"Spieler '{field_list[6]}' hat gewonnen!!!"
    # Gewinne Vertikal
    if field_list[0] == field_list[3] == field_list[6]:
        return f"Spieler '{field_list[0]}' hat gewonnen!!!"
    if field_list[1] == field_list[4] == field_list[7]:
        return f"Spieler '{field_list[1]}' hat gewonnen!!!"
    if field_list[2] == field_list[5] == field_list[8]:
        return f"Spieler '{field_list[2]}' hat gewonnen!!!"
    # Gewinne Schräg
    if field_list[0] == field_list[4] == field_list[8]:
        return f"Spieler '{field_list[0]}' hat gewonnen!!!"
    if field_list[6] == field_list[4] == field_list[2]:
        return f"Spieler '{field_list[6]}' hat gewonnen!!!"

    # unentschieden
    unentschieden = True
    for i in field_list:
        if type(i) == int:
            unentschieden = False

    if unentschieden:
        return "Unentschieden!"

    return False

playing = True
user = "O"
while playing:
    print_field(field_list)
    index_in = input(f"Spieler '{user}', gebe die Zahl des Feldes ein, auf das du setzen möchstest: ")
    # Überprüfe ob die Eingabe gültig ist
    while not index_in.isdigit() or int(index_in) > 9 or int(index_in) < 1 or str(field_list[int(index_in) - 1]) in "XO":
        index_in = input(f"Spieler '{user}', deine Eingabe war nicht gültig! Gebe erneut eine Zahl ein: ")
    index = int(index_in)
    field_list[index - 1] = user

    if check_win(field_list):
        playing = False
        print_field(field_list)
        print(check_win(field_list))

    if user == "O":
        user = "X"
    else:
        user = "O"
