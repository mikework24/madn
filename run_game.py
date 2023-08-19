from madn_func import *


class Game:
    """
    Die Spiel-Klasse enthält aktuelle eigenschaften des Spieles.
    Initialisiert ein Spiel mit der start_game methode.
    """
    def __init__(self):
        self.__pieces = {
            '11': 0, '12': 0, '13': 0, '14': 0,
            '21': 0, '22': 0, '23': 0, '24': 0,
            '31': 0, '32': 0, '33': 0, '34': 0,
            '41': 0, '42': 0, '43': 0, '44': 0
        }
        self.__players = 0
        self.__player_list = {}
        self.__player = 0

    def __draw_game(self):
        """
        Zeichnet das Initiale aussehen des Spieles.
        """
        draw_board()
        draw_fields(self.__pieces)
        draw_info_box('R')

    def __setup_players(self):
        """
        Die nutzer können sich im Spiel anmelden.
        """
        self.__players = input_how_many_players()
        self.__player_list = input_color_and_name_for_players(self.__players)
        self.__player = who_gets_to_play_first()

    def start_game(self):
        """
        Beginnt die Spielschleife.
        """
        self.__draw_game()
        self.__setup_players()

        winner = 0
        while winner == 0:
            # Boxfarben setzen mit passender Anrede
            draw_player_box(self.__player, self.__player_list)

            # Wenn keine Figur im Aktiven Spielfeld ist, Darf der Spieler 3-mal Würfeln und beginnen.
            piece_goes_in(self.__player, self.__player_list, self.__pieces)

            # Alle Spielzüge, sollten für alle Figuren berechnet werden und gehen.
            # wenn alle Figuren im Ziel ankommen sind, hat der Spieler gewonnen.
            winner = piece_in_game_turn(self.__player, self.__player_list, self.__pieces)

            # Nächster Spieler
            self.__player = (self.__player % 4) + 1

        # Pausiert das Ende des Spieles mit einer Gratulation, bevor ein neues Spiel beginnt
        enter_for_new_game(winner)


def new_game():
    """
    Startet das Spiel: Mensch ärgere Dich nicht.
    """

    # Das Spiel ist in einer Schleife um dem nutzer die möglichkeit zu geben,
    # direkt nach einem Spielende ein neues Spiel zu beginnen.
    while True:
        game = Game()
        game.start_game()


if __name__ == "__main__":
    new_game()
