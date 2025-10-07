from expyriment import design, control, stimuli

exp = design.Experiment(name = "Ternus illusion")

control.set_develop_mode()
control.initialize(exp)





exp.keyboard.wait()
control.end()

