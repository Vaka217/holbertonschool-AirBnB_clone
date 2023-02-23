#!/usr/bin/python3
""" Module doc"""
import cmd, json, inspect, readline
from models.base_model import BaseModel
from sys import argv


class HBNBCommand(cmd.Cmd):
    """ Class doc"""
    prompt = "(hbnb) "
    file = None

    def do_quit(self, arg):
        """ do_quit doc"""
        self.close()
        return True

    def do_EOF(self, arg):
        """ do_EOF doc"""
        self.close()
        print()
        return True

    def close(self):
        """ do_close doc"""
        if self.file:
            self.file.close()
            self.file = None

    def emptyline(self):
        pass

    def do_create(self, argv):
        inputs = argv.split()
        if not inputs:
            print("** class name missing **")
        elif inputs[0] != 'BaseModel':
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            print(instance.id)
            instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
