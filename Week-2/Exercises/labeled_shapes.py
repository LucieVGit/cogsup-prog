# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc import geometry

control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Triangle and hexagon")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

tri = stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(3, 50), colour = (128,0,128), position = (-125, 0))
hex = stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(6, 25), colour = (225,225,0), position = (125, 0))

left = stimuli.Line(start_point = (-125, 0), end_point = (-125, 50), line_width = 3, colour= (225,225,225))
right = stimuli.Line(start_point = (125, 0), end_point = (125, 50), line_width = 3, colour= (225,225,225))

text_t = stimuli.TextLine("triangle", position=(-125, 50), text_colour=(225,225,225), background_colour = (0,0,0))
text_h = stimuli.TextLine("hexagon", position=(125, 50), text_colour=(225,225,225), background_colour = (0,0,0))

# Start running the experiment
control.start(subject_id=1)

# Present the shapes
left.present(clear=True, update=False)
right.present(clear=False, update=False)
tri.present(clear=False, update=False)
text_t.present(clear=False, update=False)
text_h.present(clear=False, update=False)
hex.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()
 
# End the current session and quit expyriment
control.end()