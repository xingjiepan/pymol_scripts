from pymol import cmd

objs = cmd.get_object_list()

for i in range(1, len(objs)):
    cmd.super(objs[i] + ' and (ss s)', objs[0] + ' and (ss s)')

