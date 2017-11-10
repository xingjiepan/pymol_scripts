from pymol import cmd

objs = cmd.get_object_list()

for i in range(1, len(objs)):
    cmd.super(objs[i], objs[0])

