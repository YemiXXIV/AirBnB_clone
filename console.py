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
    classes = ['BaseModel']


    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        """
        if arg == "":
            print("** class name missing **")
            return

        try:
            class_name = arg.split()[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return

            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """
        Prints the string representation of an instance.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = class_name + "." + args[1]
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = class_name + "." + args[1]
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances.
        """
        if arg == "":
            print("** class name missing **")
            return

        try:
            class_name = arg.split()[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return

            objects = storage.all()
            class_objects = [str(obj) for obj in objects.values()
                         if type(obj).__name__ == class_name]
            print(class_objects)
        except IndexError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = class_name + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(storage.all()[key], args[2], eval(args[3]))
            storage.save()
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")
        except AttributeError:
            print("** no instance found **")
        except SyntaxError:
            print("** invalid syntax **")
            
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
