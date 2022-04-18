# Network_Infection_Simulation
  My approach to this problem was to create a simulation class in python to house the necessary functions to run the simulation. To have a Monte Carlo type simulation,   a random value is drawn for each event in our simulation. NumPy’s random.rand() method is used to sample a random number from a uniform distribution between 0 and 1. A   new number is generated and if it is less than the infection likelihood (default=0.1) a computer gets infected. Once this process finishes, the maximum number of         computers repaired per day (default=5) are repaired, and a full day will have been completed.
  
## Instructions:
  1.	To run this code, you will need python installed on your computer and NumPy and Matplotlib. If you do not have python installed on your computer see: https://www.python.org/downloads/ Once installed type into your terminal or command prompt: “pip install matplotlib” and “pip install numpy” to install those modules
  2.	Open up the terminal (macOS) or command prompt (Windows). 
  3.	Type “cd”  (change directory) and then the folder the program is in. Example: I downloaded  finalproject.py and now it is in the downloads folder, so I type “cd Downloads” and hit enter. If everything works correctly you should see the folder name before you type.
  4.	Type “python finalproject.py” and the program should run. When prompted by the program, type your response as requested. 

