#!/usr/bin/python3
import cmd, sys



class HBNBCommand(cmd.Cmd):
    intro = "An intro"
    prompt = "(hbnb) "
    file = None
           
    def do_quit(self, arg):
        self.close()
        return True
    
    def do_EOF(self, arg):
        self.close()
        print()
        return True
      
    
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    HBNBCommand().cmdloop()