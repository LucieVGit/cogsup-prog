import expyriment

# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, C_DARKGREY

control.set_develop_mode()

# Initialize the experiment
exp = design.Experiment(name = "Kanizsa Square", background_colour = C_DARKGREY)
control.initialize(exp)

width, height = exp.screen.size 

# Stimuli and design
s_size = int(height//2) 
c_size = int(width * 0.05) 
square = stimuli.Rectangle(size=(s_size,s_size), colour=(C_DARKGREY), position=(0, 0))
circle1 = stimuli.Circle(radius=(c_size), colour=(C_BLACK), position=(-height//4, height//4))
circle2 = stimuli.Circle(radius=(c_size), colour=(C_WHITE), position=(height//4, -height//4))
circle3 = stimuli.Circle(radius=(c_size), colour=(C_WHITE), position=(-height//4, -height//4))
circle4 = stimuli.Circle(radius=(c_size), colour=(C_BLACK), position=(height//4, height//4))

control.start(subject_id=1)

# Conduction of experiment


circle1.present(clear=True, update=False)
circle2.present(clear=False, update=False)
circle3.present(clear=False, update=False)
circle4.present(clear=False, update=False)
square.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

control.end()

# voir sur git pour automatiser les positions