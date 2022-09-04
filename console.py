#!/usr/bin/python3
"""This is a class HBNBCommand"""
import cmd
import shlex
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This is a class HBNBCommand"""
    prompt = '(hbnb) '

    def do_quit(self, argv):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, argv):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing"""
        pass

    def do_create(self, argv):
        """Creates a new instance of BaseModel"""
        argv = shlex.split(argv)
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, argv):
        """Prints the string representation of an instance"""
        if argv == "":
            print("** class name missing **")
        else:
            argv = shlex.split(argv)
            if argv[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(argv) == 1:
                print("** instance id missing **")
            else:
                key = argv[0] + "." + argv[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, argv):
        """Deletes an instance based on the class name and id"""
        argv = shlex.split(argv)
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            try:
                key = argv[0] + "." + argv[1]
                del storage.all()[key]
                storage.save()
            except NoInstanceError:
                print("** no instance found **")

    def do_all(self, argv):
        """Prints all string representation of all instances"""
        argv = shlex.split(argv)
        if len(argv) == 0:
            print([str(v) for k, v in models.storage.all().items()])
        elif argv[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in models.storage.all().items()
                   if argv[0] in k])

    def do_update(self, argv):
        """Updates an instance based on the class name and id"""
        argv = shlex.split(argv)
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        elif argv[0] + "." + argv[1] not in models.storage.all():
            print("** no instance found **")
        elif len(argv) == 2:
            print("** attribute name missing **")
        elif len(argv) == 3:
            print("** value missing **")
        else:
            key = argv[0] + "." + argv[1]
            setattr(models.storage.all()[key], argv[2], argv[3])
            models.storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()


