from madn_screen import *
import random


PLAYER_ENTRY_POINT = {1: 1, 2: 11, 3: 21, 4: 31}


def sleep(timer):
    """
    Pausiert den Ablauf für die angegebene Zeit.
    Der Speicher der ausgabe wird geflachst,
    um den gesamten Inhalt auszugeben, bevor pausiert wird.
    :param timer: Die Pausendauer in Sekunden.
    """
    sys.stdout.flush()
    time.sleep(timer)


def diced():
    """
    Simuliert das Würfeln und gibt die gewürfelte Zahl zurück.
    :return: Die gewürfelte Zahl (1-6).
    """
    number = random.randint(1, 6)
    draw_dice(number)
    return number


def input_how_many_players():
    """
    Fragt den Benutzer nach der Anzahl der Spieler und gibt diese zurück.
    :return: Die Anzahl der Spieler (1-4).
    """
    while True:
        try:
            info_text('Wie viele Personen')
            info_text('spielen mit? (1 - 4) ')
            info_text('')
            player_number = int(input())
            if 1 <= player_number <= 4:
                return player_number
            else:
                info_text('Ungültige Eingabe.')
                info_text('')
        except ValueError:
            info_text('Ungültige Eingabe.')
            info_text('')


def input_color_and_name_for_players(players):
    """
    Fragt den Benutzer nach der Farbe und dem Namen jedes Spielers und gibt sie als Dictionary zurück.
    :param players: Die Anzahl der Spieler.
    :return: Ein Dictionary mit der Farbe und dem Namen jedes Spielers.
    """
    temp_player_list = {}

    while players > len(temp_player_list):
        draw_info_box('R')
        try:
            info_text(f'Farbe für Mitspieler {len(temp_player_list) + 1}:')
            if 1 not in temp_player_list:
                info_text('1. Gelb')
            if 2 not in temp_player_list:
                info_text('2. Rot')
            if 3 not in temp_player_list:
                info_text('3. Blau')
            if 4 not in temp_player_list:
                info_text('4. Grün')
            info_text('')
            inputted_value = int(input())
            info_text('')
            if 1 <= inputted_value <= 4:
                if inputted_value not in temp_player_list:
                    player_name = ''

                    while player_name == '':
                        info_text('Geben Sie ihren Namen ein: ')
                        info_text('')
                        player_name = input()
                    temp_player_list[inputted_value] = player_name
                    write_player_names(temp_player_list)
                else:
                    info_text('Die Farbe ist')
                    info_text('bereits vergeben.')
                    info_text('')
                    input('[ OK ]')
            else:
                info_text('Bitte geben Sie eine Zahl')
                info_text('zwischen 1 und 4 ein.')
                info_text('')
                input('[ OK ]')
        except ValueError:
            info_text('Ungültige Eingabe.')
            info_text('Bitte geben Sie eine Zahl')
            info_text('zwischen 1 und 4 ein.')
            info_text('')
            input('[ OK ]')

    return temp_player_list


def who_gets_to_play_first():
    """
    Simuliert das Würfeln für alle Spieler und gibt den Spieler zurück, der als erster beginnen darf.
    :return: Die Nummer des Spielers, der beginnen darf (1-4).
    """
    player_diced_list = {1: 0, 2: 0, 3: 0, 4: 0}
    draw_info_box('R')
    info_text('Alle Spieler Würfeln!')
    info_text('')
    sleep(1)

    while True:
        # Spieler Würfeln
        highest_number = max(player_diced_list.values())
        for key, value in player_diced_list.items():
            if value == highest_number:
                draw_info_box(PLAYER_BOX_COLORS[key], False, False)
                diced_number = diced()
                player_diced_list[key] = diced_number
                info_text(f'Spieler {key} Würfelt {diced_number}')
                sleep(1)
            else:
                player_diced_list[key] = 0
        info_text('')

        # Gewinner
        highest_number = max(player_diced_list.values())
        winners = sum(1 for value in player_diced_list.values() if value == highest_number)
        if winners == 1:
            winner = next(key for key, value in player_diced_list.items() if value == highest_number)
            info_text(f'Spieler {winner} fängt an.')
            info_box_blink(winner)
            sleep(1)
            return winner

        # kein eindeutiger Gewinner, neuer durchlauf
        info_text('Gleichstand!')
        sleep(1)
        draw_info_box('R')
        info_text(f'Spieler mit einer {highest_number}')
        info_text('würfeln erneut.')
        info_text('')


def enter_for_new_game(winner):
    draw_info_box('R')
    info_text('Herzlichen glückwunsch!')
    info_text(f'Spieler {winner} hat gewonnen.')
    info_text('')
    info_text('[ Neues Spiel Starten ]')
    input()


def piece_beaten(get_player_list, player_number, position_number, get_pieces):
    """
    Überprüft, ob eine Figur geschlagen wurde, und aktualisiert das Spielfeld.
    :param get_player_list: Ein Dictionary, das die Spielernamen enthält.
    :param player_number: Die Nummer des aktuellen Spielers.
    :param position_number: Die Position der zu überprüfenden Figur.
    :param get_pieces: Ein Dictionary, das die Positionen der Figuren enthält.
    :return: True: wenn die Figur gehen kann,
             False: wenn das Feld von einer eigenen Figur belegt ist.
    """
    for key, value in get_pieces.items():
        if value == position_number:
            if player_number != key[0]:
                info_text(f'Figur von Spieler {get_player_name(key[0], get_player_list)}')
                info_text('wurde geschlagen.')
                info_text('')
                get_pieces[key] = 0
                break
            else:
                info_text('Der zug ist ungültig')
                info_text('Feld von Ihnen besetzt.')
                info_text('')
                return False
    return True


def count_pieces_in_game(player_number, get_pieces):
    """
    Anzahl der Figuren eines Spielers, die sich noch im Spiel befinden.
    :param player_number: Die Nummer des Spielers.
    :param get_pieces: Ein Dictionary, das die Positionen der Figuren enthält.
    :return: Die vorhandenen Figuren des Spielers, die sich noch im Spiel befinden.
    """
    count = 0
    in_goal = [False, False, False, False]

    for piece_number in range(1, 5):
        piece_position = get_pieces[f'{player_number}{piece_number}']

        # Figuren im Spielfeld
        if 0 < piece_position < 41:
            count += 1

        # Figuren im Ziel, die noch nicht aufgerückt haben
        if 41 <= piece_position <= 44:
            in_goal[piece_position - 41] = True

    if in_goal[3] == 0 and sum(in_goal[:3]) > 0 or \
       in_goal[2] == 0 and sum(in_goal[:2]) > 0 or \
       in_goal[1] == 0 and in_goal[0]:
        count += 1

    return count


def move_piece_to_game(get_player_list, player_number, get_pieces):
    for piece_number in range(1, 5):
        if get_pieces[f'{player_number}{piece_number}'] == 0:
            if piece_beaten(get_player_list, player_number, PLAYER_ENTRY_POINT[player_number], get_pieces):
                get_pieces[f'{player_number}{piece_number}'] = PLAYER_ENTRY_POINT[player_number]
                return piece_number
            else:
                return -1
    return -1


def get_valid_user_input(pieces_points):
    """
    Benutzereingabe welche Figur gehen soll.
    :param pieces_points: Ein Dictionary, das die Punkte der Spielfiguren enthält.
    :return: Die Nummer der gewählten Spielfigur.
    """
    valid_numbers = [str(num) for num in pieces_points if pieces_points[num] > -1]
    valid_numbers_str = ", ".join(valid_numbers)

    if len(valid_numbers) > 1:
        while True:
            info_text('Bitte wählen Sie eine')
            info_text(f'Spielfigur ({valid_numbers_str}): ')
            info_text('')
            user_input = input()
            info_text('')
            try:
                chosen_piece = int(user_input)
                if chosen_piece in pieces_points and pieces_points[chosen_piece] > -1:
                    return chosen_piece
                else:
                    info_text('Ungültige Eingabe.')
                    info_text('')
            except ValueError:
                info_text('Ungültige Eingabe.')
                info_text('')
    else:
        return int(valid_numbers[0])


def get_possible_moves(player_number, diced_number, get_pieces):
    """
    Berechnet welche Figur gehen kann, anhand der gewürfelten Zahl.
    :param player_number: Die Nummer des Spielers.
    :param diced_number: Die gewürfelte Zahl.
    :param get_pieces: Das Dictionary mit den Spielfiguren und ihren Positionen.
    :return: Ein Dictionary mit möglichen Zügen und ihren Punktwerten.
    """
    pieces_points = {1: -1, 2: -1, 3: -1, 4: -1}
    pieces_desired_position = {1: -1, 2: -1, 3: -1, 4: -1}

    for piece_number in range(1, 5):
        piece_position = get_pieces[f'{player_number}{piece_number}']

        # Figur bei einer 6 herausholen
        if piece_position == 0 and diced_number == 6:
            pieces_desired_position[piece_number] = PLAYER_ENTRY_POINT[player_number]
            pieces_points[piece_number] += 200

            for key, value in get_pieces.items():
                if value == PLAYER_ENTRY_POINT[player_number]:
                    if player_number != int(key[0]):
                        # Gegner kann geschlagen werden
                        pieces_points[piece_number] += 50
                    else:
                        # Feld durch eigene Figur belegt
                        pieces_desired_position[piece_number] = -1
                        pieces_points[piece_number] = -1

        # Figuren im Ziel
        if 40 < piece_position < 44 and piece_position + diced_number < 45:
            pieces_desired_position[piece_number] = piece_position + diced_number
            pieces_points[piece_number] += 2

            for key, value in get_pieces.items():
                if value == pieces_desired_position[piece_number] and int(key[0]) == player_number:
                    # Spielfeld durch eigene Figur belegt
                    pieces_points[piece_number] = -1

        # Eigene Figuren in der Eintrittsposition
        if piece_position == PLAYER_ENTRY_POINT[player_number]:
            pieces_desired_position[piece_number] = piece_position + diced_number
            pieces_points[piece_number] += 50

            for key, value in get_pieces.items():
                if value == pieces_desired_position[piece_number] and int(key[0]) == player_number:
                    # Spielfeld durch eigene Figur belegt
                    pieces_points[piece_number] = -1

        # Nur figuren aus dem aktiven Bereich
        if 0 < piece_position < 41:
            real_piece_position = piece_position - PLAYER_ENTRY_POINT[player_number] + 1
            if real_piece_position < 1:
                real_piece_position += 40

            # Kann das Ziel erreicht werden?
            if 40 < real_piece_position + diced_number < 45:
                pieces_desired_position[piece_number] = real_piece_position + diced_number
                pieces_points[piece_number] += 150

                # Ist der Platz im Ziel frei?
                for key, value in get_pieces.items():
                    # Spielfeld im Ziel frei
                    if value == real_piece_position + diced_number and int(key[0]) == player_number:
                        # Spielfeld im Ziel belegt
                        pieces_points[piece_number] = -1

            elif real_piece_position + diced_number < 41:

                # nach dem zug ist der Spieler noch im Spielbereich
                new_piece_position = piece_position + diced_number
                if piece_position + diced_number > 40:
                    new_piece_position = piece_position + diced_number - 40

                pieces_desired_position[piece_number] = new_piece_position
                pieces_points[piece_number] += real_piece_position + diced_number

                # Kann ein gegner erreicht werden
                for key, value in get_pieces.items():
                    if value == new_piece_position:
                        if int(key[0]) == player_number:
                            # Spielfeld durch eigene figur belegt
                            pieces_points[piece_number] = -1
                        else:
                            # gegner auf dem Spielfeld
                            pieces_points[piece_number] += 100

    return pieces_points, pieces_desired_position


def piece_turn(player_number, get_diced_number, player_list, get_pieces):
    """
    Führt den Zug für den Spieler durch.
    :param player_number: Die Nummer des Spielers.
    :param get_diced_number: Die gewürfelte Zahl.
    :param player_list: Liste der Spieler die Aktiv mitspielen.
    :param get_pieces: Das Dictionary mit den Spielfiguren und ihren Positionen.
    :return winner: Gibt einen Gewinner zurück, wobei die 0 aussagt das noch kein Gewinner vorhanden ist.
    """
    pieces_points, pieces_desired_position = get_possible_moves(player_number, get_diced_number, get_pieces)

    # Wenn eine Figur genutzt werden kann, wird dem Spieler oder Computer eine eingabe ermöglicht
    if max(pieces_points.values()) > -1:
        piece_to_move = -1
        if player_number in player_list:
            # Spieler
            piece_to_move = get_valid_user_input(pieces_points)
            draw_player_box(player_number, player_list)
        else:
            # Computer
            piece_to_move = max(pieces_points, key=pieces_points.get)

        if pieces_desired_position[piece_to_move] < 41:
            piece_beaten(player_list, player_number, pieces_desired_position[piece_to_move], get_pieces)
        get_pieces[f'{player_number}{piece_to_move}'] = pieces_desired_position[piece_to_move]

    # Hat jemand Gewonnen
    player_points = 0
    winner = 0
    for key, value in get_pieces.items():
        if value > 40 and int(key[0]) == player_number:
            player_points += 1
    if player_points == 4:
        winner = player_number
        info_text('')
        info_text(f'Spieler {player_number}')
        info_text('hat das Spiel gewonnen!')
    return winner


def piece_goes_in(player_number, player_list, pieces_list):
    """
    Zieht die Figur aus der Startzone.
    :param player_number: Die Nummer des Spielers.
    :param player_list: Die Liste der Spieler.
    :param pieces_list: Liste der Spielfiguren.
    """
    if count_pieces_in_game(player_number, pieces_list) == 0:
        for i in range(3):
            # Der Spieler darf 3-mal Würfeln bis eine 6 dabei ist, um eine Figur herauszuholen
            diced_number = diced()
            info_text(f'Es wurde eine {diced_number} gewürfelt')
            sleep(1)
            if diced_number == 6:
                info_text(f'Spieler {player_number} darf eine')
                info_text('Figur rausstellen.')
                info_text('')
                move_piece_to_game(player_list, player_number, pieces_list)
                sleep(0.5)
                draw_fields(pieces_list)
                sleep(1)
                break


def piece_in_game_turn(player_number, player_list, pieces_list):
    """
    Der Spieler darf Würfeln um zu gehen, wenn eine Figur draußen ist
    :param player_number: Spieler Nummer.
    :param player_list: Die Liste der Spieler.
    :param pieces_list: Die Liste der Spielfiguren.
    :return: Gibt den gewinner zurück.
    """
    winner = 0
    if count_pieces_in_game(player_number, pieces_list) > 0:
        for i in range(3):

            # Der Spieler darf maximal 3-mal Würfeln, falls eine 6 gewürfelt wurde
            diced_number = diced()
            info_text(f'Es wurde eine {diced_number} gewürfelt')
            sleep(2)

            # 3-mal hintereinander eine 6 würfeln ist ungültig
            if i == 3 and diced_number == 6:
                info_text('3 mal die die 6 gewürfelt.')
                info_text('Du setzt aus.')
                info_text('')
                sleep(3)
                break

            winner = piece_turn(player_number, diced_number, player_list, pieces_list)

            sleep(1)
            draw_fields(pieces_list)
            sleep(1)
            if diced_number != 6:
                break

            info_text('Du darfst nochmal würfeln.')
            info_text('')
            sleep(3)
    return winner
