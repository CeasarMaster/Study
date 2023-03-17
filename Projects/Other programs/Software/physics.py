import tkinter as tk
import random

waves_questions = [
    "What is the characteristic of a wave that corresponds to its frequency?",
    "What is the law of conservation of energy?",
    "What type of wave is characterized by the direction of its vibration and what property determines its speed?",
    "What is the bending of waves around an obstacle called?",
    "What property of a wave is directly proportional to its energy?",
    "What is the interference of waves that results in their amplification or cancellation called?",
    "What type of wave is characterized by the oscillation of the medium perpendicular to the direction of propagation?",
    "What is the property of waves that determines the extent of their spreading or focusing?",
    "What is the phenomenon of a wave bouncing off a surface called?",
    "What is the change in the direction of a wave as it passes from one medium to another?"]


energy_questions = [
    "What is the law of conservation of energy?",
    "What is the formula for kinetic energy and how is it related to mass and velocity?",
    "What is the difference between potential and kinetic energy and how are they related?",
    "What is the unit of measurement for energy?",
    "What is the formula for calculating work and how is it related to energy?",
    "What is the difference between renewable and nonrenewable sources of energy?",
    "What is the process by which plants convert sunlight into chemical energy?",
    "What is the energy required to raise the temperature of one gram of water by one degree Celsius?",
    "What is the amount of energy needed to change the state of a substance called?",
    "What is the energy released by the nucleus of an atom called?"]

astrophysics_questions = [
    "What is the explosive death of a star called?",
    "What is the theory that describes the origin and evolution of the universe, and what is the evidence for it?",
    "What is the phenomenon of light bending around massive objects in space called?",
    "What is a black hole and how is it formed?",
    "What is the temperature of the cosmic microwave background radiation?",
    "What is the study of the distribution and motion of galaxies called?",
    "What is the source of energy that powers the sun?",
    "What is the process by which a star fuses hydrogen into helium?",
    "What is the term for the time it takes for a planet to complete one orbit around the sun?",
    "What is the measurement of the amount of matter in an object called?"]

atomic_questions = [
    "What is the fundamental unit of matter?",
    "What is ionization and how does it affect the properties of an atom?",
    "What is the difference between mass number and atomic number and how do they determine the identity and properties of an atom?",
    "What is the difference between a molecule and an atom?",
    "What is the process by which an unstable nucleus emits radiation and decays into a more stable state?",
    "What is the measurement of the time it takes for half of the atoms in a sample to decay called?",
    "What is the phenomenon of electrons behaving like waves and particles called?",
    "What is the property of particles that determines their behavior in a magnetic field?",
    "What is the process by which electrons are transferred between atoms called?",
    "What is the measurement of the amount of electrical charge in an object called?"]

forces_questions = [
    "What is the force that opposes motion between two surfaces in contact?",
    "What is Newton's second law of motion and how is it related to force, mass, and acceleration?",
    "What is the force that causes an object to move in a circle called?",
    "What is the difference between weight and mass?",
    "What is the force that pulls objects towards each other called?",
    "What is the terminal velocity and how does it relate to air resistance?",
    "What is the difference between elastic and inelastic collisions?",
    "What is the force that acts on an object due to its position in a gravitational field?",
    "What is the difference between static and kinetic friction?",
    "What is the principle that states that every action has an equal and opposite reaction?",
]

electricity_questions = [
    "What is the difference between an electric conductor and an insulator?",
    "What is Ohm's law and how is it used to calculate the current, voltage, and resistance in an electrical circuit?",
    "What is the difference between direct current (DC) and alternating current (AC)?",
    "What is the phenomenon of electrons moving from one atom to another in a material called?",
    "What is the difference between series and parallel circuits?",
    "What is the unit of measurement for electric power?",
    "What is the property of a material that determines its resistance to the flow of electric current?",
    "What is the difference between a magnet and an electromagnet?",
    "What is the phenomenon of an electric current inducing a magnetic field called?",
    "What is the principle behind the operation of an electric generator?"]

# define the function to display a random question for a given category
def display_question(category):
    rand_num = random.randint(0, len(category)-1)
    question = category[rand_num]
    question_label.config(text=question)

# create the main window
root = tk.Tk()
root.title("Super Physics Party")
root.geometry("1080x800")

# add a title label
title_label = tk.Label(root, text="Super Physics Party", font=("Arial Bold", 36))
title_label.pack(side=tk.TOP, pady=20)

# create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, pady=20)

# add buttons for each category
waves_button = tk.Button(button_frame, text="Blue", command=lambda: display_question(waves_questions))
waves_button.pack(side=tk.LEFT, padx=20)
energy_button = tk.Button(button_frame, text="Green", command=lambda: display_question(energy_questions))
energy_button.pack(side=tk.LEFT, padx=20)
astrophysics_button = tk.Button(button_frame, text="Purple", command=lambda: display_question(astrophysics_questions))
astrophysics_button.pack(side=tk.LEFT, padx=20)
atomic_button = tk.Button(button_frame, text="Orange", command=lambda: display_question(atomic_questions))
atomic_button.pack(side=tk.LEFT, padx=20)
forces_button = tk.Button(button_frame, text="Red", command=lambda: display_question(forces_questions))
forces_button.pack(side=tk.LEFT, padx=20)
electricity_button = tk.Button(button_frame, text="Yellow", command=lambda: display_question(electricity_questions))
electricity_button.pack(side=tk.LEFT, padx=20)

# add a label to display the questions
question_label = tk.Label(root, text="", font=("Arial", 20), wraplength=800)
question_label.pack(pady=20)

# run the main loop
root.mainloop()