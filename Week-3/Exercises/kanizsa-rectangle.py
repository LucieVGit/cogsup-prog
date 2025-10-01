import expyriment

# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, C_DARKGREY

control.set_develop_mode()

# Initialize the experiment
exp = design.Experiment(name = "Kanizsa Recatngle", background_colour = C_DARKGREY)
control.initialize(exp)

# scaling factor = échelle

def kanizsa_rectangle(aspect_ratio, rectangle_scaling_factor, circle_scaling_factor):

    largeur, _ = exp.screen.size 

    # RECTANGLE
    width = largeur // rectangle_scaling_factor
    height = width // aspect_ratio
    rectangle = stimuli.Rectangle(size=(width, height), colour=C_DARKGREY, corner_anti_aliasing=10)

    half_width = width // 2
    half_height = height // 2

    # CIRCLES
    radius = largeur // circle_scaling_factor
    edges = []
    colors = []

    for x in (-half_width, half_width):
        for y in (-half_height, half_height):  
            edges.append((x, y))
            colors.append(C_WHITE if y < 0 else C_BLACK)
    
    circles = [stimuli.Circle(radius=radius, position=edge, colour=color, anti_aliasing=10) for edge, color in zip(edges, colors)]

    return circles + [rectangle]

stim_list = kanizsa_rectangle(aspect_ratio=1.5, rectangle_scaling_factor=2, circle_scaling_factor=12)

""" RUN EXPERIMENT """

# DRAW
exp.screen.clear()
for stim in stim_list:
    stim.present(False, False)
exp.screen.update()

# WAIT
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()

# The aspect ratio is the ratio between the rectangle’s width and its height:
# If aspect_ratio = 1, the rectangle is a square (width = height).
# If aspect_ratio = 1.5, the rectangle is wider than tall (width is 1.5 times its height).
# If aspect_ratio = 0.5, the rectangle is taller than wide (height is twice the width).
# So in this code, aspect_ratio directly controls the proportions of the Kanizsa rectangle illusion.

