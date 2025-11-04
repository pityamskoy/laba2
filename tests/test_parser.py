import pytest

from src.bash.Parser import Parser
from src.exceptions.IncorrectInputException import IncorrectInputException


def test_execute_true():
    parser = Parser()

    assert parser.execute("cd C:\\") == ("cd", ["C:\\"])
    assert parser.execute("rm C:\\users\someuser\downloads\laba.txt -r") == ("rm", ["C:\\users\someuser\downloads\laba.txt","-r"])
    assert parser.execute("cd 'my folder with spaces'") == ("cd", ["my folder with spaces"])
    assert parser.execute("ls") == ("ls", [])

def test_execute_false():
    parser = Parser()

    with pytest.raises(IncorrectInputException):
        parser.execute("cd something something something")

    assert parser.execute("cd something") != ("cat", ["my_folder"])
    assert parser.execute("ls") != "ls"
