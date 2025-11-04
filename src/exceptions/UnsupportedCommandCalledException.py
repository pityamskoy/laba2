from src.exceptions.BashException import BashException


class UnsupportedCommandCalledException(BashException):
    name = "UnsupportedCommandCalledException"