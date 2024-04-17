#!/usr/bin/python3
""" Console Module class"""

import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contain functionality for HBNB console"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:
            pline = line[:]  # parsed line

            _cls = pline[:pline.find('.')]

            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                pline = pline.partition(', ')

                _id = pline[0].replace('\"', '')

                pline = pline[2].strip()
                if pline:
                    if pline[0] == '{' and pline[-1] == '}' \
                            and type(eval(pline)) == dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Print if is atty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ Method to allow exit HBNB console"""
        exit()

    def help_quit(self):
        """ Prints help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides emptyline method of CMD """
        pass

    def do_create(self, args):
        """ Create an object of any class"""
        args = args.split()
        if args == []:
            print("** class name is not found **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            cls = args[0]
		
        new_instance = HBNBCommand.classes[cls]()
        if len(args[1:]) != 0:
            args = args[1:]
        else:
            new_instance.save()
            print(new_instance.id)
            return
		
        for argument in args:
            sa = argument.split("=")
            key = sa[0]
            value = sa[1]
			
            for i in range(len(value)):
                if value[i] == "_":
                    value = value[:i] + " " + value[i+1:]
					
            if (key[0] == "'" and key[-1] == "'") or (
                    key[0] == "\"" and key[-1] == "\""):
                key = key[1:-1]
            if (value[0] == "'" and value[-1] == "'") or (
                    value[0] == "\"" and value[-1] == "\""):
                value = value[1:-1]
			
            setattr(new_instance, key, value)
		
        new_instance.save()
        print(new_instance.id)

    def help_create(self):
        """ Help information for class creation """
        print("Create a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method to show individual object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name is not found **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id is not found **")
            return

        key = c_name + "." + c_id
        __objects = storage.all()
        try:
            print(__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ Help information for show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ Destroy specified object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name is not found **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id is not found **")
            return

        key = c_name + "." + c_id

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help information for destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ Shows all objects """
        print_list = []

        __objects = storage.all()
        if args:
            args = args.split(' ')[0]
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in __objects.items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in __objects.items():
                print_list.append(str(v))

        print(print_list)

    def help_all(self):
        """ Help information for all command """
        print("Shows all objects or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instance"""
        count = 0
        __objects = storage.all()
        for k, v in __objects.items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """ help count function """
        print("Usage: count <class_name>")

    def do_update(self, args):
        """ Update a certain object with new info """
        c_name = c_id = att_name = att_val = kwargs = ''

        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:
            print("** class name is not found **")
            return
        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:
            print("** instance id is not found **")
            return

        key = c_name + "." + c_id

        if key not in storage.all():
            print("** no instance found **")
            return

        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:
            args = args[2]
            if args and args[0] == '\"':
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            if not att_name and args[0] != ' ':
                att_name = args[0]
			
            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        new_dict = storage.all()[key]

        for i, att_name in enumerate(args):
            if (i % 2 == 0):
                att_val = args[i + 1]
                if not att_name:
                    print("** attribute name is not found **")
                    return
                if not att_val:
                    print("** value is not found **")
                    return
				
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()

    def help_update(self):
        """ Help info for update class """
        print("Update the object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
