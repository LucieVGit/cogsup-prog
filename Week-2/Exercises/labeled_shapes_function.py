# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc import geometry

# CONSTANTS
label = {3: 'triangle', 4: 'square', 5: 'pentagon', 6: 'hexagon', 7: 'heptagon', 8: 'octagon', 10: 'decagon', 12: 'dodecagon'}
# interesting to put more constants like colours or lenghts to not repeat yourself !!

# FUNCTIONS
def create_polygon(n, length, colour, position):

    polygon = stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(n, length), colour = colour, position = position)

    x, y = polygon.position
    text_shape = label.get(n, "polygon")

    text = stimuli.TextLine(text_shape, position=(x, y + 50), text_colour=(225,225,225), background_colour = (0,0,0))
    line = stimuli.Line(start_point = polygon.position, end_point = text.position, line_width = 3, colour= (225,225,225))

    return (line, polygon, text)

# we can't use a for loop because we have different stimuli, present only work for one variable
# Tuples in Python don’t have methods like .present()
def draw(create_polygon):
    for stim in create_polygon:
        stim.present(clear=False, update=False)

# start expyriment
control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Triangle and hexagon")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

triangle_def = create_polygon(3, 50, (128,0,128), (-125, 0))
hex_def = create_polygon(6, 25, (225,225,0), (125, 0))

# Start running the experiment
control.start(subject_id=1)

# Present the shapes
for bundle in (triangle_def, hex_def):
    draw(bundle)
exp.screen.update()

# Leave it on-screen until a key is pressed
exp.keyboard.wait()
 
# End the current session and quit expyriment
control.end()