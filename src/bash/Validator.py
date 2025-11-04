from src.constants import COMMANDS
from src.constants import UNSUPPORTED_SYMBOLS_IN_PATH
from src.exceptions.IncorrectInputException import IncorrectInputException
from src.exceptions.UnsupportedCommandCalledException import UnsupportedCommandCalledException

"""
Validator checks if an input string is initially correct
"""


class Validator:
    """
    This method checks if an incorrect symbol is in a string
    """

    def is_input_string_correct(self, string: str) -> None:
        for symbol in UNSUPPORTED_SYMBOLS_IN_PATH:
            if string.find(symbol) != -1:
                raise IncorrectInputException(f"Error: unsupported symbol '{symbol}' was provided in the input string")

    """
    This method checks if a called command is correct
    """

    def is_command_correct(self, command: str) -> None:
        if command not in COMMANDS:
            raise UnsupportedCommandCalledException("Error: command '" + command + "' is not supported")
