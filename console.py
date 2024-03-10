#!/usr/bin/python3

"""

This module provides a command line interface for
the AirBnB clone project

"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    Gives the program CLI methods to handle commands
    """

    prompt = "(hbnb) "

    
    def do_quit(self, arg):
        """
        Exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        End the CLI
        """
        return True

    def emptyline(self):
        """
        Called when an empty line is entered
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
