__author__ = 'Mohit'

"""
# This is a script that simulates a rolling
# Die Game with a Die of 6 sides.
# The minimium is 1 and maximum is 6 on the Die.
#
# In order to play the Game, number of players
# and number of times die would be rolled is decided.
#
# The user presses any key and gets a number.
# This number is then added to the player's total.
#
# Their are maximum of five players that can play
# this simple game.
# The maximum turns that one can roll the die for
# any player is 1000.
"""

import random
import os, sys
import time


class Die(object):
    def __init__(self):
        # This function initialises the necessary
        # parameters for a Die to be rolled.
        # The parameters are
        # 1. Minimium value for a Die.
        # 2. Maximum value for a Die
        self._min = 1
        self._max = 6

    @property
    def min(self):
        """
        This function defines the minimium
        of a Die as a property.

        """
        return self._min

    @min.setter
    def min(self,number):
        raise TypeError("Can't reset minimium of Die")

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self,number):
        raise TypeError("Can't reset maximum of Die")

    def run(self):
        """This method when called gives a random number
        between 1 and 6.
        """
        return random.randint(self.min, self.max)


class RollingDieGame(object):
    max_players = 5
    max_turns = 1000
    seconds_to_sleep = 4
    min_time_to_sleep = 3

    def __init__(self, number_of_players, number_of_turns):
        # This function initialises the necessary
        # parameters for a game to be played.
        # These parameters are:
        # 1.number of players.
        # 2.Number of turns for each player.
        # 3. The rolling die
        self.number_of_players = RollingDieGame.max_players if number_of_players > RollingDieGame.max_players else number_of_players
        self.number_of_turns = RollingDieGame.max_turns if number_of_turns > RollingDieGame.max_turns else number_of_turns
        self.rolling_die = Die()
        self.players = [Player(counter + 1) for counter in xrange(number_of_players)]

    def clear(self):
        """
        This method detects the os and accordingly runs the
        command to clear the screen.
        The supported OS are Windows, Linux.
        If other OS is found, it returns error.
        Return Values: True, False
        """
        #operating_system = platform.system()
        operating_system = "Windows"
        if operating_system == "Windows":
            command = "cls"
        elif operating_system == "Linux":
            command = "clear"
        else:
            print "Unknown Operating System."
            return False

        os.system(command)
        sys.stdout.flush()
        return True

    def run_die(self):
        """
        This function runs the die of the game when a key is pressed.
        """
        return self.rolling_die.run()

    def press_any_key(self):
        return raw_input("Hit enter.")

    def run(self):
        """
        This function will run the game.
        At first we initialise the turns to zero.
        Then we get each player to press any key.
        For each player, we print his unique identifier
        After he presses any key, we print the number on screen
        and adds the number to its existing score.
        Then we wait for ten seconds to account for any additional
        keys pressed and iterates to next player.
        """

        turn_number = 1
        while turn_number <= self.number_of_turns:
            for player in self.players:
                if not self.clear():
                    break
                print("The player to play is: {}".format(player.identifier) )
                self.press_any_key()
                random_number = self.run_die()
                print("The number generated for yourself is: {}".format(random_number) )
                player.score += random_number
                #Now we sleep for 10 seconds.
                time.sleep(RollingDieGame.seconds_to_sleep)
            print("All players have played for turn number {}".format(turn_number) )
            time_to_sleep = max(RollingDieGame.min_time_to_sleep, RollingDieGame.seconds_to_sleep - 5)
            time.sleep(time_to_sleep)
            turn_number += 1

    def announce_winner(self):
        if not self.clear():
            print("The game could not be played.OS not supported.")
            return
        winner_player_identifiers = []
        max_value_of_winning_player = 0

        for player in self.players:
            if player.score >= max_value_of_winning_player:
                max_value_of_winning_player = player.score

        for player in self.players:
            if player.score == max_value_of_winning_player:
                winner_player_identifiers.append(str(player.identifier))

        print("The identifiers of players that have won are:" +  ",".join(winner_player_identifiers) )
        return






class Player(object):
    def __init__(self, number):
        """
        This function initialises the necessary
        parameters for a player to operate.
        These parameters are:
        1. sum total of turns.
        """
        self._total = 0
        self._identifier = number

    @property
    def score(self):
        """
        This function returns the total of
        the player as a score property.
        """
        return self._total

    @score.setter
    def score(self,number):
        """
        This function adds the die value to the total of
        the player.
        """
        self._total = number

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self,number):
        raise TypeError("Can't reset identifier.")


if __name__ == "__main__":
    try:
        number_of_players = int(raw_input("Input number of players.Defaults/maximum to 5.") )
    except:
        number_of_players = 5

    try:
        number_of_turns = int(raw_input("Input number of turns.Defaults/maximum to 1000.") )
    except:
        number_of_turns = 1000

    if number_of_players <= 0 or number_of_players > 5:
        number_of_players = 5
    if number_of_turns <= 0 or number_of_turns > 1000:
        number_of_turns = 1000
    print ("The number of players are {}".format(number_of_players) )
    print("The maximum turns are {}".format(number_of_turns) )
    game = RollingDieGame(number_of_players,number_of_turns)
    game.run()
    game.announce_winner()

