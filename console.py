#!/usr/bin/python3
""" Module doc"""
import cmd, json, inspect, readline
from models.base_model import BaseModel
from sys import argv
from models.engine.file_storage import FileStorage
from models import storage
class HBNBCommand(cmd.Cmd):
    """ Class doc"""
    prompt = "(hbnb) "
    file = None

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
        elif inputs[0] != 'BaseModel':
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            print(instance.id)
            instance.save()

    def do_show(self, argv):
        """ do_show doc"""
        inputs = argv.split()
        if not inputs:
            print("** class name missing **")
        elif inputs[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            key = inputs[0] + '.' + inputs[1]
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
        if not inputs or inputs[0] != 'BaseModel':
            print("** class doesn't exist **")
        else:
            list = []
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                list.append(str(all_objs[obj_id]))
            print(list)

    def do_destroy(self, argv):
        """ do_destroy doc"""
        inputs = argv.split()
        if not inputs:
            print("** class name missing **")
        elif inputs[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            key = inputs[0] + '.' + inputs[1]
            if not key in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(key)
                with open('file.json') as f:
                    d = json.load(f)
                del d[key]
                with open('file.json', 'w') as f:
                    json.dump(d, f)

    def do_update(self, argv):
        """ do_update doc"""
        inputs = argv.split()
        if not inputs:
            print("** class name missing **")
        elif inputs[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            key = inputs[0] + '.' + inputs[1]
            if not key in storage.all():
                print("** no instance found **")
            elif len(inputs) < 3:
                print("** attribute name missing **")
            elif len(inputs) < 4:
                print("** value missing **")
            else:
                all_objs = storage.all()
                setattr(all_objs[key], inputs[2], inputs[3])
                with open('file.json') as f:
                    d = json.load(f)
                d[key][inputs[2]] = inputs[3]
                with open('file.json', 'w') as f:
                    json.dump(d, f)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
