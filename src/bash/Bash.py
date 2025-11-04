import os
import shutil
import time
import logging

from typing import TextIO

from src.bash.Validator import Validator
from src.bash.Parser import Parser
from src.exceptions.BashException import BashException
from src.exceptions.IncorrectInputException import IncorrectInputException
from src.exceptions.SamirILoveYouException import SamirILoveYouException

"""
Bash is the main class of the program,
which controls each command to be executed.

It logs all called commands and exceptions if they happen
"""


class Bash:
    validator = Validator()
    parser = Parser()
    parameter: str

    def __init__(self):
        logging.basicConfig(level=logging.INFO,
                            filename="shell.log",
                            filemode="a",
                            encoding="utf-8",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        os.chdir(os.path.expanduser("~"))
        self.execute()

    """
    execute matches each command with corresponding method of this class
    """

    def execute(self) -> None:
        flag: bool = True

        while flag:
            string: str = input(os.getcwd() + ">")
            logging.info(string)

            try:
                self.validator.is_input_string_correct(string)
                input_args: tuple = self.parser.execute(string)

                args = input_args[1]
                command: str = input_args[0]
                self.validator.is_command_correct(command)
                if command == "":
                    continue

                match command:
                    case "ls":
                        self.ls(args)
                    case "cd":
                        self.cd(args)
                    case "cat":
                        self.cat(args)
                    case "cp":
                        self.cp(args)
                    case "mv":
                        self.mv(args)
                    case "rm":
                        self.rm(args)
                    case "zip":
                        self.archive("zip", args)
                    case "tar":
                        self.archive("tar", args)
                    case "unzip":
                        self.extract("zip", args)
                    case "untar":
                        self.extract("tar", args)
                    case "quit":
                        flag = False

            except BashException as bash:
                logging.error(bash.message)
                print(bash.message)
                continue

    """
    ls command is similar to ls command in linux.
    However, it only supports -l flag
    """

    def ls(self, args: tuple) -> None:
        if len(args) == 0:
            print(os.listdir(os.getcwd()))
            return

        flag: str = None
        paths: list = list()

        for i in args:
            if args[i] == "-l":
                flag = i
            else:
                paths.append(i)

        if len(paths) == 2:
            raise IncorrectInputException("Error: 2 arguments without flag was provided or flag is incorrect")

        try:
            if flag is not None:
                past_dir: str = None
                if len(paths) == 1:
                    past_dir = os.getcwd()
                    os.chdir(paths[0])

                for i in os.listdir(os.getcwd()):
                    print(os.stat(i).st_uid, i, os.stat(i).st_size, time.ctime(os.path.getctime(i)),
                          time.ctime(os.path.getmtime(i)))

                if len(paths) == 1:
                    os.chdir(past_dir)

                return

            print(os.listdir(paths[0]))
        except FileNotFoundError:
            raise SamirILoveYouException(f"Error: cannot find directory {paths[0]}")

    """
    cd command is similar to cd command in linux.
    However, it doesn't support flags
    """

    def cd(self, args: tuple) -> None:
        if len(args) == 0:
            return

        if len(args) == 2:
            raise IncorrectInputException("Error: 2 arguments were provided for 'cd' command")

        if args[0] == "..":
            os.chdir(os.pardir)
        elif args[0] == "~":
            os.chdir(os.path.expanduser("~"))
        else:
            try:
                os.chdir(args[0])
            except FileNotFoundError:
                raise SamirILoveYouException(f"Cannot find directory {args[0]}")
            except NotADirectoryError:
                raise SamirILoveYouException(
                    f"Error: 'cd' cannot handle file {args[0]}, it supports only directories, not files.")

    """
    cat command is similar to cat command in linux.
    However, it doesn't support flags
    """

    def cat(self, args: tuple) -> None:
        if len(args) > 1:
            raise IncorrectInputException("Error: more than 1 argument was provided for 'cat' command")
        if len(args) == 0:
            return

        path: str = args[0]

        try:
            if os.path.isfile(path):
                file: TextIO = open(path, "r")
                print(file.read())
                file.close()
            else:
                raise SamirILoveYouException(
                    "Error: command 'cat' cannot read directories. It only supports readable files")
        except FileNotFoundError:
            raise SamirILoveYouException(f"Error: cannot find directory '{path}'")

    """
    cp command is similar to cp command in linux.
    However, it supports either recursively copying
    in the case a catalog was provided as an input
    or just copying a file.
    """

    def cp(self, args: tuple) -> None:
        if len(args) == 1:
            raise IncorrectInputException("Error: missing destination file")
        if len(args) == 0:
            return

        directory: str = args[0]
        path: str = args[1]

        if os.path.isfile(path):
            raise SamirILoveYouException(f"Error: it is impossible to copy to a file {path}")

        try:
            if not os.path.exists(directory):
                raise SamirILoveYouException(f"Error: no such file or directory {directory}")

            if not os.path.exists(path):
                raise SamirILoveYouException(f"Error: no such file or directory {path}")

            if os.path.isfile(directory):
                shutil.copy2(directory, path)
            else:
                index_of_last_slash: int = directory.rfind("\\")
                directory_name: str = directory[index_of_last_slash + 1:]
                os.mkdir(path + "\\" + directory_name)

                for i in os.listdir(directory):
                    self.cp((directory + "\\" + i, path + "\\" + directory_name))

        except PermissionError:
            raise SamirILoveYouException(f"Error: permission denied: '{path}'")
        except FileExistsError:
            raise SamirILoveYouException(
                f"Error: cannot create file that already exists: '{path + "\\" + directory_name}'")

    """
    mv command is similar to mv command in linux.
    However, it doesn't support flags
    """

    def mv(self, args: tuple) -> None:
        if len(args) == 0:
            return

        destination: str
        source: str
        if len(args) == 1:
            source = args[0]
            destination = os.getcwd()
        else:
            source = args[0]
            destination = args[1]

        if not os.path.exists(source):
            raise SamirILoveYouException(f"Error: no such file or directory {source}")

        if not os.path.exists(destination):
            raise SamirILoveYouException(f"Error: no such file or directory {destination}")

        try:
            shutil.move(source, destination)
        except FileExistsError:
            raise SamirILoveYouException(f"Error: file is already exists in directory '{destination}'")
        except PermissionError:
            raise SamirILoveYouException(f"Error: permission denied")

    """
    rm command is similar to rm command in linux.
    However, it support only -r flag.
    """

    def rm(self, args: tuple) -> None:
        if len(args) == 0:
            return

        paths: list = list()
        flag: str = None

        for i in args:
            if i == "-r":
                flag = i
            else:
                paths.append(i)

        if len(paths) == 2:
            raise IncorrectInputException("Error: 2 directories or files were provided for 'rm' command")

        if paths[0] == "C:\\":
            raise IncorrectInputException("Error: 'rm' cannot remove root directory")

        if paths[0] == "..":
            raise IncorrectInputException("Error: 'rm' cannot remove parent directory")

        try:
            if os.path.isdir(paths[0]):
                if flag is not None:
                    shutil.rmtree(paths[0])
                else:
                    raise IncorrectInputException("Error: 'rm' can be used with directories only with '-r' flag")
            else:
                os.remove(paths[0])
        except FileNotFoundError:
            raise SamirILoveYouException(f"Error: cannot find directory {paths[0]}")
        except PermissionError:
            raise SamirILoveYouException(f"Error: permission denied: '{paths[0]}'")

    """
    archive is the method, which executes zip or tar commands.
    
    format_type argument contains the format of archiving,
    namely: 'zip' or 'tar'.
    """

    def archive(self, format_type: str, args: tuple) -> None:
        if len(args) == 0:
            return

        if len(args) == 1:
            raise IncorrectInputException("Error: missing directory of zip archive")

        folder: str = args[0]
        directory_to_save_archive: str = args[1]

        try:
            shutil.make_archive(directory_to_save_archive, format_type, folder)
        except FileNotFoundError:
            raise SamirILoveYouException(f"Error: cannot find directory {folder}")
        except PermissionError:
            raise SamirILoveYouException(f"Error: permission denied {directory_to_save_archive}")

    """
    extract method extracts all files in an archive into provided folder.
    It is able to create new ones if it's necessary.
    
    Similar to archive, format_type contains type of archive provided to.
    """

    def extract(self, format_type: str, args: tuple) -> None:
        if len(args) == 0:
            return

        if len(args) == 2:
            raise IncorrectInputException(f"Error: 2 arguments were provided for '{format_type}' command")

        try:
            shutil.unpack_archive(args[0], os.getcwd(), format_type)
        except FileNotFoundError:
            raise SamirILoveYouException(f"Error: cannot find archive '{args[0]}'")
        except PermissionError:
            raise SamirILoveYouException(f"Error: permission denied '{os.getcwd()}'")
        except shutil.ReadError:
            raise SamirILoveYouException(f"Error: '{args[0]}' is not a '{format_type} file'")
