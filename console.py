#!/usr/bin/python3
""" Module doc"""
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
    """ Class doc"""
    prompt = "(hbnb) "
    file = None
    classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                    'City': City, 'Amenity': Amenity, 'Place': Place,
                    'Review': Review}

    def do_quit(self, arg):
        """ do_quit doc"""
        return True

    def do_EOF(self, arg):
        """ do_EOF doc"""
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, argv):
        """ do_create doc"""
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
        """ do_show doc"""
        inputs = argv.split()
        if not inputs:
            print("** class name missing **")
        elif inputs[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            key = inputs[0] + '.' + inputs[1]
            storage.reload()
            if not key in storage.all():
                print("** no instance found **")
            else:
                all_objs = storage.all()
                key = inputs[0] + '.' + inputs[1]
                if key in all_objs.keys():
                    print(all_objs[key])

    def do_all(self, argv):
        """ do_all doc"""
        inputs = argv.split()
        if not inputs or inputs[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            list = []
            storage.reload()
            for obj_id in storage.all().keys():
                if obj_id.split(".")[0] == inputs[0]:
                    list.append(str(storage.all()[obj_id]))
            print(list)

    def do_destroy(self, argv):
        """ do_destroy doc"""
        inputs = argv.split()
        if not inputs:
            print("** class name missing **")
        elif inputs[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            key = inputs[0] + '.' + inputs[1]
            storage.reload()
            if not key in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(key)
                storage.save()

    def do_update(self, argv):
        """ do_update doc"""
        inputs = argv.split()
        if not inputs:
            print("** class name missing **")
        elif inputs[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            key = inputs[0] + '.' + inputs[1]
            storage.reload()
            if not key in storage.all():
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
