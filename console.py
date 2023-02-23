""" Module doc"""
#!/usr/bin/python3
import cmd



class HBNBCommand(cmd.Cmd):
    """ Class doc"""
    intro = "An intro"
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
