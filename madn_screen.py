import os
import sys
import time


# ========================= Globale Werte und listen =========================

INFO_LINE = 0

INFO_BOX = {'y': 1, 'x': 70, 'h': 23, 'w': 30}

PLAYER_BOX_COLORS = {
    1: 'Ry',
    2: 'Rr',
    3: 'Rb',
    4: 'Rg'
}

COLOR_CODES = {
    "Rr": "\033[0m\033[31m",
    "Rg": "\033[0m\033[32m",
    "Ry": "\033[0m\033[33m",
    "Rb": "\033[0m\033[34m",
    "B": "\033[38;5;231;40m",
    "r": "\033[38;5;231;41m",
    "g": "\033[38;5;231;42m",
    "y": "\033[38;5;16;48;5;220m",
    "b": "\033[38;5;231;44m",
    "m": "\033[38;5;231;45m",
    "c": "\033[38;5;231;46m",
    "yl": "\033[30m\033[48;5;227m",
    "w": "\033[30m\033[48;5;231m",
    "R": "\033[0m"  # Standardfarbe
}


# ============= Schreiben und Leeren von inhalten auf der Konsole =============

def write_pos(y: int, x: int, text: str, newline: bool = False):
    """
    Schreibt den Text an der angegebenen Stelle in der Konsole.
    :param y: Die Zeile in der Konsole.
    :param x: Die Spalte in der Konsole.
    :param text: Der Text, der in die Konsole geschrieben werden soll.
    :param newline: Soll nach der Ausgabe eine neue Zeile geschieben werden.
    :return: None
    """

    write = f"\033[{y};{x}H{text}"

    if newline:
        print(write, sep=' ', end='\n', file=None, flush=False)
    else:
        print(write, sep=' ', end='', file=None, flush=False)


def clear():
    """
    Reinigt die Konsole.
    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# ========================= Infobox rechts =========================
def draw_info_box(color: str, clear_box: bool = True, write_from_top: bool = True):
    """
    Zeichnet die Infobox rechts.
    :param color: Farbcode aus COLOR_CODES.
    :param clear_box: Wenn der Inhalt bleiben soll, kann ein False übergeben werden.
    :param write_from_top: Soll nach dem vorhandenen Text weitergeschrieben werden?
    :return: None
    """
    global INFO_LINE
    if write_from_top:
        INFO_LINE = 0
    y, x, h, w = INFO_BOX['y'], INFO_BOX['x'], INFO_BOX['h'], INFO_BOX['w']

    # Rahmen oben
    write_pos(y, x, f'{COLOR_CODES[color]}  ╔{"═" * w}╗ ')

    if clear_box:
        # Leert die Infobox
        for i in range(y + 1, h + 1):
            write_pos(i, x, f'  ║{" " * w}║ ')
    else:
        # Malt den Rahmen neu, um die Rahmenfarbe zu ändern
        for i in range(y + 1, h + 1):
            write_pos(i, x, '  ║')
        for i in range(y + 1, h + 1):
            write_pos(i, x + w + 3, '║ ')

    # Rahmen unten
    write_pos(h, x, f'  ╚{"═" * w}╝ {COLOR_CODES["R"]}')


def info_text(text: str):
    """
    Schreibt bei jedem Aufruf eine neue Zeile in die Infobox.
    :param text: Der auszugebende Text.
    :return: None
    """
    global INFO_LINE
    y, x, h, w = INFO_BOX['y'], INFO_BOX['x'], INFO_BOX['h'], INFO_BOX['w']
    INFO_LINE += 1
    write_pos(y + INFO_LINE, x + 4, text)


def info_box_blink(player_number: int, finish_white: bool = False):
    """
    gewinner Farbe blinkt
    """
    loops = 8
    if finish_white:
        loops = 9
    for i in range(0, loops):
        if i % 2 == 0:
            draw_info_box('R', False, False)
        else:
            draw_info_box(PLAYER_BOX_COLORS[player_number], False, False)

        # Flush des Speichers ausgeben bevor eine Pause eingeleitet wird.
        # Da die ausgabe auch pausiert wird und eine Animation dadurch verhindert wird.
        sys.stdout.flush()
        time.sleep(0.2)


def get_player_name(player_number: int, player_list):
    """
    Gibt den Namen des Spielers zurück, ansonsten die Nummer.
    :param player_number: Die Nummer des Spielers.
    :param player_list: Die Liste der Spieler.
    :return: Der Name und nummer des Spielers oder die Spieler-Nummer.
    """
    if player_number in player_list:
        return f'{player_number} ({player_list[player_number]})'
    return player_number


def draw_player_box(player: int, player_list=None):
    """
    Zeichnet die Spieler-Box mit Anrede an den Spieler.
    :param player: Die Nummer des Spielers.
    :param player_list: Die Liste der Spieler.
    :return: None
    """
    draw_info_box(PLAYER_BOX_COLORS[player])
    info_text(f'Spieler {get_player_name(player, player_list)}')
    info_text('ist an der Reihe.')
    info_text('')


# ========================= Weißes Spielbrett mit Texten und Rahmen =========================

def draw_board():
    """
    Zeichnet das weiße Spielbrett mit Texten und Rahmen.
    """
    clear()
    # Farbe Setzen
    write_pos(1, 1, f'{COLOR_CODES["yl"]}')
    # Weißes Spielfeld
    write_pos(1, 1, f' ╔{"═" * 65}╗ ')
    for i in range(2, 23):
        write_pos(i, 1, f' ║{" " * 65}║ ')
    write_pos(23, 1, f' ╚{"═" * 65}╝ ')
    # Beschriftung
    write_pos(21, 8, '1')
    write_pos(3, 8, '2')
    write_pos(21, 62, '3')
    write_pos(3, 62, '4')
    write_pos(22, 26, '↑')
    write_pos(9, 5, '→')
    write_pos(2, 44, '↓')
    write_pos(15, 65, '←')
    write_pos(7, 14, 'Mensch')
    write_pos(7, 50, 'ärgere')
    write_pos(17, 15, 'dich')
    write_pos(17, 51, 'nicht')
    # Farbe zurücksetzen
    write_pos(23, 1, f'{COLOR_CODES["R"]}')
    # Infobox Rechts Zeichnen
    draw_info_box('R')


def write_player_names(player_names):
    """
    Schreibt die Namen der Spieler auf das Spielbrett.
    :param player_names: Ein Dictionary mit den Namen der Spieler.
    :return: None
    """
    player_name_y = {1: 19, 2: 5, 3: 5, 4: 19}
    player_name_x = {1: 4, 2: 4, 3: 58, 4: 58}
    write_pos(23, 1, f'{COLOR_CODES["yl"]}')
    for key, value in player_names.items():
        write_pos(player_name_y[key], player_name_x[key], value)
    write_pos(23, 1, f'{COLOR_CODES["R"]}')


# ========================= Spielfelder (Positionen und Farben) =========================

# Gelb (Spieler 1) Start, Ziel
Y_X_LIST = [1, 3, 1, 3, 11, 11, 11, 11]
Y_Y_LIST = [20, 20, 22, 22, 20, 18, 16, 14]

# Rot (Spieler 2) Start, Ziel
R_X_LIST = [1, 3, 1, 3, 3, 5, 7, 9]
R_Y_LIST = [2, 2, 4, 4, 12, 12, 12, 12]

# Blau (Spieler 3) Start, Ziel
B_X_LIST = [19, 21, 19, 21, 11, 11, 11, 11]
B_Y_LIST = [2, 2, 4, 4, 4, 6, 8, 10]

# Grün (Spieler 4) Start, Ziel
G_X_LIST = [19, 21, 19, 21, 19, 17, 15, 13]
G_Y_LIST = [20, 20, 22, 22, 12, 12, 12, 12]

# Spielfelder
X_LIST = [9, 9, 9, 9, 9, 7, 5, 3, 1, 1, 1, 3, 5, 7, 9, 9, 9, 9, 9, 11, 13, 13, 13,
          13, 13, 15, 17, 19, 21, 21, 21, 19, 17, 15, 13, 13, 13, 13, 13, 11]
Y_LIST = [22, 20, 18, 16, 14, 14, 14, 14, 14, 12, 10, 10, 10, 10, 10, 8, 6, 4, 2, 2,
          2, 4, 6, 8, 10, 10, 10, 10, 10, 12, 14, 14, 14, 14, 14, 16, 18, 20, 22, 22]


def field_colors(number):
    """
    Gibt die Farbe des Spielfeldes anhand seiner Nummer zurück.
    :param number: Die Nummer des Spielfeldes.
    :return: Die Farbe des Spielfeldes ('y', 'r', 'b', 'g', 'R').
    """
    color_map = {1: 'y', 11: 'r', 21: 'b', 31: 'g'}
    return color_map.get(number, 'w')


def draw_field_bg():
    """
    Zeichnet die Hintergrundfarben für die Spielfelder (Start, Ziel und Spielfelder).
    :return: None
    """
    player_data = (
        (Y_X_LIST, Y_Y_LIST, 'y'),
        (R_X_LIST, R_Y_LIST, 'r'),
        (B_X_LIST, B_Y_LIST, 'b'),
        (G_X_LIST, G_Y_LIST, 'g')
    )

    # Start- und Zielfelder
    for temp_x_list, temp_y_list, color_code in player_data:
        for x, y in zip(temp_x_list, temp_y_list):
            write_pos(y, (x * 3) + 1, f"{COLOR_CODES[color_code]}   {COLOR_CODES['R']}")

    # Spielfelder
    i_list = [x for x in range(1, 41)]
    for i, x, y in zip(i_list, X_LIST, Y_LIST):
        write_pos(y, (x * 3) + 1, f"{COLOR_CODES[field_colors(i)]}   {COLOR_CODES['R']}")


def draw_fields(pieces):
    """
    Zeichnet die Spielfiguren auf den Spielfeldern.
    :param pieces: Ein Dictionary mit den Positionen der Spielfiguren.
    :return: None
    """
    draw_field_bg()

    player_color = {1: 'y', 2: 'r', 3: 'b', 4: 'g'}

    p_x_list, p_y_list = [], []

    # Liste des aktuellen Spielers laden
    for key, value in pieces.items():
        if key[0] == '1':
            p_x_list, p_y_list = Y_X_LIST, Y_Y_LIST
        elif key[0] == '2':
            p_x_list, p_y_list = R_X_LIST, R_Y_LIST
        elif key[0] == '3':
            p_x_list, p_y_list = B_X_LIST, B_Y_LIST
        elif key[0] == '4':
            p_x_list, p_y_list = G_X_LIST, G_Y_LIST

        # Start Positionen
        if value == 0:
            write_pos(
                p_y_list[int(key[1]) - 1],
                p_x_list[int(key[1]) - 1] * 3 + 2,
                f"{COLOR_CODES[player_color[int(key[0])]]}{key[1]}",
                newline=False)

        # End Positionen
        elif value > 40:
            write_pos(
                p_y_list[value - 37],
                p_x_list[value - 37] * 3 + 2,
                f"{COLOR_CODES[player_color[int(key[0])]]}{key[1]}",
                newline=False)

        # Im Spiel Positionen
        else:
            write_pos(
                Y_LIST[value - 1],
                X_LIST[value - 1] * 3 + 2,
                f"{COLOR_CODES[player_color[int(key[0])]]}{key[1]}",
                newline=False)

    write_pos(23, 1, f'{COLOR_CODES["R"]}')


# ========================= Würfel =========================
def draw_dice(diced_number: int):
    """
    Zeichnet den Würfel mit der gewürfelten Zahl.
    :param diced_number: Die gewürfelte nummer (0-6).
    :return: None
    """

    dice_lines = (
        '           ',
        '┏━━━━━━━━━┓',
        '┃ ■       ┃',
        '┃    ■    ┃',
        '┃       ■ ┃',
        '┃ ■     ■ ┃',
        '┃         ┃',
        '┗━━━━━━━━━┛'
    )

    dice_pattern = (
        [0, 0, 0, 0, 0],
        [1, 6, 3, 6, 7],
        [1, 2, 6, 4, 7],
        [1, 2, 3, 4, 7],
        [1, 5, 6, 5, 7],
        [1, 5, 3, 5, 7],
        [1, 5, 5, 5, 7]
    )

    y, x = 16, 82

    for line, line_pattern in enumerate(dice_pattern[diced_number]):
        write_pos(y + line, x, dice_lines[line_pattern])
