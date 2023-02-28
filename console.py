#!/usr/bin/python3
"""Needed modules."""
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Console class."""

    prompt = "(hbnb) "
    file = None
    classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
               'City': City, 'Amenity': Amenity, 'Place': Place,
               'Review': Review}

    def do_quit(self, arg):
        """Apply quit to the console."""
        return True

    def do_EOF(self, arg):
        """Exit when eof method."""
        print()
        return True

    def emptyline(self):
        """Pass when no command found."""
        pass

    def do_create(self, argv):
        """Create a new class and asigns it an id."""
        inputs = argv.split()
        if not inputs:
            print("** class name missing **")
        elif inputs[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            instance = HBNBCommand.classes[inputs[0]]()
            print(instance.id)
            instance.save()

    def do_show(self, argv):
        """Show all contents based on id or all if dont specified."""
        inputs = argv.split()
        if not inputs:
            print("** class name missing **")
        elif inputs[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            key = inputs[0] + '.' + inputs[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                all_objs = storage.all()
                key = inputs[0] + '.' + inputs[1]
                if key in all_objs.keys():
                    print(all_objs[key])

    def do_all(self, argv):
        """Show all contents based on id or all if dont specified."""
        inputs = argv.split()
        if not inputs:
            print(list((storage.all())))
        elif inputs[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            list_all = []
            storage.reload()
            for obj_id in storage.all().keys():
                if obj_id.split(".")[0] == inputs[0]:
                    list_all.append(str(storage.all()[obj_id]))
            print(list_all)

    def do_destroy(self, argv):
        """Destroy a class method."""
        inputs = argv.split()
        if not inputs:
            print("** class name missing **")
        elif inputs[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            key = inputs[0] + '.' + inputs[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(key)
                storage.save()

    def do_update(self, argv):
        """Add an attribute in a class."""
        inputs = argv.split()
        if not inputs:
            print("** class name missing **")
        elif inputs[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            key = inputs[0] + '.' + inputs[1]
            if key not in storage.all():
                print("** no instance found **")
            elif len(inputs) < 3:
                print("** attribute name missing **")
            elif len(inputs) < 4:
                print("** value missing **")
            else:
                setattr(storage.all()[key], inputs[2], inputs[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
