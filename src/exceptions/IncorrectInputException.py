from src.exceptions.BashException import BashException


class IncorrectInputException(BashException):
    name:str = "IncorrectInputException"