# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc import geometry 
control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Two squares")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

triangle = stimuli.Shape(vertices_triangle=[(50,50)], colour = (225,0,225), position = (-125, 0))
hex = stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(5, 50), colour = (0,225,0), position = (125, 0))

# Start running the experiment
control.start(subject_id=1)

# Present the squares
square_left.present(clear=True, update=False)
square_right.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()