#!/usr/bin/python3

"""

This module provides a command line interface for
the AirBnB clone project

"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    Gives the program CLI methods to handle commands
    """

    prompt = "(hbnb) "

    classes = [
        "BaseModel", "User", "State", "Amenity",
        "Place", "City", "Review" 
    ]


    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        """
        args = arg.split(" ")
        if arg == "":
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            if args[0] == "BaseModel":
                base = BaseModel()
            elif args[0] == "User":
                base = User()
            elif args[0] == "State":
                base = State()
            elif args[0] == "Amenity":
                base = Amenity()
            elif args[0] == "Place":
                base = Place()
            elif args[0] == "City":
                base = City()
            elif args[0] == "Review":
                base = Review()
            print(base.id)
            storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance.
        """
        objs = storage.all()
        args = arg.split()
        if arg == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            args[1] = args[1].replace('"', '') \
                    if args[1][0] == '"' else args[1]
            classname_id = args[0] + "." + args[1]
            if classname_id not in objs.keys():
                print("** no instance found **")
            else:
                print(objs[classname_id])
        
            
    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        
        objs = storage.all()
        args = arg.split(" ")
        if arg == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            args[1] = args[1].replace('"', '') \
                if args[1][0] == '"' else args[1]
            classname_id = args[0] + "." + args[1]
            if classname_id not in objs.keys():
                print("** no instance found **")
            else:
                del objs[classname_id]
                storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances.
        """
        objs = storage.all()
        args = arg.split(" ")
        if args[0] != "":
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                all_items = []
                for obj in objs:
                    if obj.startswith(args[0]):
                        all_items.append(str(objs[obj]))
                print(all_items)
        else:
            all_items = []
            for obj in objs:
                all_items.append(str(objs[obj]))
            print(all_items)

            
    def do_update(self, arg):
        """
        Updates an instance based on the class name and id.
        """
        objs = storage.all()
        args = arg.split(" ")
        if arg == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            args[1] = args[1].replace('"', '') \
                if args[1][0] == '"' else args[1]
            classname_id = args[0] + "." + args[1]
            if classname_id not in objs.keys():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                args[2] = args[2].replace('"', '').replace("'", "")
                obj = objs[classname_id]
                if args[3].startswith('"') and args[3].endswith('"') or \
                   args[3].startswith("'") and args[3].endswith("'"):
                    setattr(obj, args[2], str(args[3][1:-1]))
                elif args[3].startswith('"') and not args[3].endswith('"') or \
                     args[3].startswith("'") and not args[3].endswith("'"):
                    str_val = ""
                    for arg in args[3:]:
                        str_val += " " + arg
                        if arg.endswith('"') or arg.endswith("'"):
                            break
                        setattr(obj, args[2], str(str_value[2:-1]))
                elif "." in args[3]:
                    setattr(obj, args[2], float(args[3]))
                else:
                    setattr(obj, args[2], int(args[3]))
                    storage.save()
    
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
