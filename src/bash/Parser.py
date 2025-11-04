from src.exceptions.IncorrectInputException import IncorrectInputException

"""
Parses handles extracting commands and
specific arguments in an input string.

It also supports arguments with spaces,
they should be written in quotes. 
"""


class Parser:
    """
    It's the main high-leveled method of this class.

    It gets just a string and returns only command and raw arguments.
    """

    def execute(self, string: str) -> tuple:
        command: str
        args: list = list()
        string = self.remove_redundant_spaces_before_and_after_args(string)

        if string == "":
            return string,

        try:
            var = self.define_indexes_of_args(string)
        except ValueError:
            raise IncorrectInputException("Error: commands with more than 2 arguments are not supported")

        indexes_of_parameters: tuple[int, int, int] = var[0]
        indexes_of_first_spaces_after_args: tuple[int, int, int] = var[1]
        is_parameters_with_spaces: tuple[bool, bool] = var[2]

        if indexes_of_parameters[0] != -1:
            if indexes_of_first_spaces_after_args[0] == -1:
                command = string
            else:
                command = string[:indexes_of_first_spaces_after_args[0]]
        else:
            command = ""

        if indexes_of_parameters[1] != -1:
            if is_parameters_with_spaces[0]:
                if indexes_of_first_spaces_after_args[1] == -1:
                    args.append(string[indexes_of_parameters[1]:indexes_of_first_spaces_after_args[1]])
                else:
                    args.append(string[indexes_of_parameters[1]:indexes_of_first_spaces_after_args[1] - 1])
            else:
                if indexes_of_first_spaces_after_args[1] == -1:
                    args.append(string[indexes_of_parameters[1]:])
                else:
                    args.append(string[indexes_of_parameters[1]:indexes_of_first_spaces_after_args[1]])

        if indexes_of_parameters[2] != -1:
            if is_parameters_with_spaces[1]:
                args.append(string[indexes_of_parameters[2]:-1])
            else:
                args.append(string[indexes_of_parameters[2]:])

        return command, args

    def remove_redundant_spaces_before_and_after_args(self, string: str) -> str:
        while string[0] == " ":
            string = string[1:]

        while string[-1] == " ":
            string = string[:-1]

        return string

    """
    It's the scariest and the most dangerous part of program... but it works)
    
    So, there is a bunch of lists each of them contains parameters for 3 arguments
    corresponding to their name.
    For example, indexes_of_parameters contains first index of each parameter in
    a string if it is represented. It contains -1 by default, excluding first,
    which is simply zero.
    The exactly same thing goes for indexes_of_first_spaces_after_args and
    is_parameters_with_spaces, which names represent what they contain.
    
    define_indexes_of_args returns tuple of tuples for high-level handling.
    Tuples in tuple were returned in the same order as they have been initialized.
    """

    def define_indexes_of_args(self, string: str) -> tuple[tuple, tuple, tuple]:
        indexes_of_parameters: list = [0, -1, -1]
        indexes_of_first_spaces_after_args: list = [-1, -1, -1]
        is_parameters_with_spaces: list = [False, False]

        for i in range(len(string)):
            if string[i] == " ":
                indexes_of_first_spaces_after_args[0] = i
                break

        if indexes_of_first_spaces_after_args[0] != -1:
            for i in range(len(string[indexes_of_first_spaces_after_args[0]:])):
                if string[indexes_of_first_spaces_after_args[0] + i] != " ":
                    if string[indexes_of_first_spaces_after_args[0] + i] == "'":
                        is_parameters_with_spaces[0] = True

                    indexes_of_parameters[1] = indexes_of_first_spaces_after_args[0] + i
                    if is_parameters_with_spaces[0]:
                        indexes_of_parameters[1] += 1
                    break

        check: str = " "
        if indexes_of_parameters[1] != -1:
            if is_parameters_with_spaces[0]:
                check = "'"
            for i in range(len(string[indexes_of_parameters[1]:])):
                if string[indexes_of_parameters[1] + i] == check:
                    if check == " ":
                        indexes_of_first_spaces_after_args[1] = indexes_of_parameters[1] + i
                        break
                    elif check == "'":
                        if indexes_of_parameters[1] + i + 1 != len(string):
                            if indexes_of_parameters[1] + i + 1 == ' ':
                                indexes_of_first_spaces_after_args[1] = indexes_of_parameters[1] + i + 1
                                break

        if indexes_of_first_spaces_after_args[1] != -1:
            for i in range(len(string[indexes_of_first_spaces_after_args[1]:])):
                if string[indexes_of_first_spaces_after_args[1] + i] != " ":
                    if string[indexes_of_first_spaces_after_args[1] + i] == "'":
                        is_parameters_with_spaces[1] = True

                    indexes_of_parameters[2] = indexes_of_first_spaces_after_args[1] + i
                    if is_parameters_with_spaces[1]:
                        indexes_of_parameters[2] += 1
                    break

        check = " "
        if indexes_of_parameters[2] != -1:
            if is_parameters_with_spaces[1]:
                check = "'"
            for i in range(len(string[indexes_of_parameters[2]:])):
                if string[indexes_of_parameters[2] + i] == check:
                    if check == " ":
                        indexes_of_first_spaces_after_args[2] = indexes_of_parameters[2] + i
                        break
                    elif check == "'":
                        if indexes_of_parameters[2] + i + 1 != len(string):
                            if string[indexes_of_parameters[2] + i + 1] == ' ':
                                indexes_of_first_spaces_after_args[2] = indexes_of_parameters[2] + i + 1
                                break

        if indexes_of_first_spaces_after_args[2] != -1:
            for i in range(len(string[indexes_of_first_spaces_after_args[2]:])):
                if string[indexes_of_first_spaces_after_args[2] + i] != " ":
                    raise ValueError()

        return tuple(indexes_of_parameters), tuple(indexes_of_first_spaces_after_args), tuple(is_parameters_with_spaces)
