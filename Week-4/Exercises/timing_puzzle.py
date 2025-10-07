from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

control.initialize(exp)

exp.keyboard.wait()

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")

# t0 = exp.clock.time
# fixation.present()
# dt = exp.clock.time - t0
# fix_duration = exp.clock.wait(1000 - dt)

exp.clock.reset_stopwatch()
t0 = exp.clock.time
fixation.present()
dt = exp.clock.time - t0
exp.clock.wait(1000 - dt)
fix_duration = exp.clock.stopwatch_time / 1000

text.present()
exp.clock.wait(1000)

units = "second" if fix_duration == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {fix_duration} {units}"

text2 = stimuli.TextLine(duration_text)
text2.present()

exp.keyboard.wait()
control.end()