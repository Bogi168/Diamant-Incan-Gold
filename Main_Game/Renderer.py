from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render_game(self, message):
        pass

    @abstractmethod
    def render_system(self, message):
        pass

    @abstractmethod
    def ask_players_amount(self):
        pass

    @abstractmethod
    def re_ask_players_amount(self):
        pass

    @abstractmethod
    def ask_player_name(self, player_num):
        pass

    @abstractmethod
    def ask_bots_amount(self):
        pass

    @abstractmethod
    def re_ask_bots_amount(self):
        pass

    @abstractmethod
    def ask_bot_level(self, bot_num):
        pass

    @abstractmethod
    def re_ask_bot_level(self, bot_num):
        pass

    @abstractmethod
    def ask_games_amount(self):
        pass

    @abstractmethod
    def re_ask_games_amount(self):
        pass

    @abstractmethod
    def ask_continue_or_leave(self, player_name):
        pass

    @abstractmethod
    def re_ask_continue_or_leave(self, player_name):
        pass

    @abstractmethod
    def ask_again(self):
        pass

    @abstractmethod
    def ask_for_save(self):
        pass

class ConsoleRenderer(Renderer):
    def render_game(self, message):
        print(message)

    def render_system(self, message):
        pass

    def ask_players_amount(self):
        return input("How many players?: ")

    def re_ask_players_amount(self):
        return input("That's not a valid number. How many players? ")

    def ask_player_name(self, player_num):
        return input(f"Enter player number {player_num + 1}'s name: ").capitalize()

    def ask_bots_amount(self):
        return input("\nHow many bots? ")

    def re_ask_bots_amount(self):
        return input("That's not a valid number. How many bots? ")

    def ask_bot_level(self, bot_num):
        return input(f"Select a level for Bot {bot_num + 1} (1-13): ")

    def re_ask_bot_level(self, bot_num):
        return input(f"That's not a valid level. Select a level for Bot {bot_num + 1} (1-13): ")

    def ask_games_amount(self):
        pass

    def re_ask_games_amount(self):
        pass

    def ask_continue_or_leave(self, player_name):
        return input(f"{player_name}: Do you want to go home? (Y/N) ").upper()

    def re_ask_continue_or_leave(self, player_name):
        return input(f"{player_name}: That's is not valid. Do you want to go home? (Y/N) ").upper()

    def ask_again(self):
        return input("Do you want to play again? (Y/N) ").upper()

    def ask_for_save(self):
        pass

class SimulationRenderer(Renderer):
    def render_game(self, message):
        pass

    def render_system(self, message):
        print(message)

    def ask_players_amount(self):
        pass

    def re_ask_players_amount(self):
        pass

    def ask_player_name(self, player_num):
        pass

    def ask_bots_amount(self):
        return input("\nHow many bots? ")

    def re_ask_bots_amount(self):
        return input("That's not a valid number. How many bots? ")

    def ask_bot_level(self, bot_num):
        return input(f"Select a level for Bot {bot_num + 1} (1-13): ")

    def re_ask_bot_level(self, bot_num):
        return input(f"That's not valid. Select a level for Bot {bot_num + 1} (1-13): ")

    def ask_games_amount(self):
        return input("How many games? ")

    def re_ask_games_amount(self):
        return input("That's not a valid number. How many games?: ")

    def ask_continue_or_leave(self, player_name):
        pass

    def re_ask_continue_or_leave(self, player_name):
        pass

    def ask_again(self):
        pass

    def ask_for_save(self):
        return input("Do you want to save the game statistics? (Y/N): ").upper()