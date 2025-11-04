import pytest

from src.bash.Validator import Validator
from src.exceptions.IncorrectInputException import IncorrectInputException
from src.exceptions.UnsupportedCommandCalledException import UnsupportedCommandCalledException


@pytest.mark.parametrize("string", ["cd \downloads", "cd downloads", "cd C:\\users\someuser\downloads"])
def test_is_input_string_correct_true(string: str):
    validator = Validator()
    assert validator.is_input_string_correct(string) is None


@pytest.mark.parametrize("string", ["cd C:\\***", "cat <file>", 'cp "file" to "file"'])
def test_is_input_string_correct_false(string: str):
    with pytest.raises(IncorrectInputException):
        validator = Validator()
        validator.is_input_string_correct(string)


@pytest.mark.parametrize("string", ["cd", "cp", "cat", "mv"])
def test_is_command_correct_true(string: str):
    validator = Validator()
    assert validator.is_command_correct(string) is None


@pytest.mark.parametrize("string", ["aasdasd", "caaaaat", "Samir", "football"])
def test_is_command_correct_false(string: str):
    with pytest.raises(UnsupportedCommandCalledException):
        validator = Validator()
        validator.is_command_correct(string)
