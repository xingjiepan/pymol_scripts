# Make a pymol movie that shows all objects in turn

from pymol import cmd

objs = cmd.get_object_list()

n_frame_per_obj = 5

# Initialize the frames

cmd.mset('1', n_frame_per_obj * len(objs))

# Create a scene for each frame

cmd.scene(key='*', action='clear')
cmd.scene(key='original_scene', action='store')

for obj in objs:

    # Hide everything but this object

    cmd.scene(key='original_scene', action='recall')
    cmd.hide('everything', 'not ' + obj)
    cmd.scene(key=obj + '_scene', action='store')

# Make the movie

cmd.mview(action='clear', first=1, last=n_frame_per_obj * len(objs))

for i, obj in enumerate(objs):
    frame_start = i * n_frame_per_obj + 1
    #frame_stop = (i + 1) * n_frame_per_obj

    cmd.scene(key=obj + '_scene', action='recall')
    cmd.mview(action='store', first=frame_start)
