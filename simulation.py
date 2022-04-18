# Code by: Jack Ericson
# Date: 4/6/22
# GSU MATH3020 Final Project

# Importing packages
import numpy as np
import matplotlib.pyplot as plt


# Creating Network class
class Simulation:

    # Initializing network with number of computers, number of infected, probability of infecting another computer, and
    # the maximum number of computers that can be cured per day
    def __init__(self, num_comps=20, num_infected=1, infect_prob=.1, num_sims=10000, repaired_day=5):

        # Set input variables
        self.num_comps = num_comps
        self.init_infected = num_infected
        self.infect_prob = infect_prob
        self.num_sims = num_sims
        self.repaired_day = repaired_day

        # List of our computers: Boolean list, whether the system is infected or not: Bool
        self.comp_list = []
        self.infected_list = []

    # Define our plot method. Since it does not call on the object we declare it as a static method
    def plot(self, avg, sim_length_arr, avg_arr, num_infected_list, every_prob, exp_num_comps):

        # Plot the number of days for each simulation to run
        fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(15, 5))
        sims = np.linspace(1, self.num_sims, self.num_sims)

        # ax0 = Text box subplot
        ax0.text(0, 0.95, "Results:", fontsize=15)
        ax0.text(0.1, 0.70, "\nExpected time to remove virus = {} days\n\nProbability that each computer gets infected "
                            "= {}\n\nExpected number of infected computers = {}".format(round(avg, 5),
                                                                                        round(every_prob, 5),
                                                                                        round(exp_num_comps, 5)),
                 fontsize=10)
        ax0.text(0, 0.45, "Settings:\n\n", fontsize=15)
        ax0.text(0.1, 0.30, "1. Number of computers = {}\n2. Initially infected computers = {}\n3. Infection Rate = {}"
                            "\n4. Number of simulations = {}\n5. Number of computers repaired daily = {}"
                            .format(self.num_comps, self.init_infected, self.infect_prob, self.num_sims,
                                    self.repaired_day),
                 fontsize=10)
        ax0.set_axis_off()

        # ax1: Simulation Plot
        ax1.plot(sims, avg_arr, c='grey', linewidth=2.0, linestyle='--')
        ax1.scatter(sims, sim_length_arr, marker ='.', c='k')
        # Set plot attributes
        ax1.set_xlabel("Simulation Number")
        ax1.set_ylabel("Time to clear network (days)")
        ax1.legend(["Average", "Time per sim", "Number of infected computers"])
        ax1.set_title("%i Simulated Network Infections" % self.num_sims)
        if max(sim_length_arr) - min(sim_length_arr) > 1000:
            ax1.set_yscale('log')

        # Infected computers plot
        ax2.scatter(sims, num_infected_list, marker='.', c='k')
        # Set plot attributes
        ax2.set_xlabel("Simulation Number")
        ax2.set_ylabel("NUmber of computers")
        ax2.set_title("Number of computers that have been infected")

        # Spread the subplots
        plt.tight_layout()

        # Show the plot
        plt.show()

    # Define our choices method
    def choices(self):

        # Ask the user if they want to make any changes with the simulation
        choices = input("\n Current settings: \n    1. Number of computers = {}\n    2. Initially infected computers"
                        " = {}\n    3. Infection Rate = {}\n    4. Number of simulations = {}\n    5. Number of "
                        "computers repaired daily = {}\n\nWould you like to change any of the above settings? If so, "
                        "which setting(s)? (use numbers separated by commas or 'all') Type 'n' if not.\n"
                        .format(self.num_comps, self.init_infected, self.infect_prob, self.num_sims,
                                self.repaired_day)).lower()

        # If user inputs 'y' ask them which settings they want to change
        if choices == 'y':
            choices = input("Which setting(s)? (use numbers separated by commas or 'all')\n")

        # Create a list of changes from users input string
        choice_list = choices.replace(" ", "").split(',')  # Replaces spaces and splits at the commas

        # List of request that can be called by index
        inputs = ["1. Number of computers?\n",
                  "2. Initially infected computers?\n",
                  "3. Infection rate?\n",
                  "4. Number of simulations?\n",
                  "5. Number of computers repaired daily?\n"]

        # If the input is 'n' exit
        if choice_list[0].lower() == 'n':
            return

        # All is in the choice list we go through the entire list of settings
        elif choice_list[0] == 'all':
            for i in range(len(inputs)):
                # Go through all settings
                if i == 0:
                    self.num_comps = int(input(inputs[i]))
                elif i == 1:
                    self.init_infected = int(input(inputs[i]))
                elif i == 2:
                    self.infect_prob = float(input(inputs[i]))
                elif i == 3:
                    self.num_sims = int(input(inputs[i]))
                elif i == 4:
                    self.repaired_day = int(input(inputs[i]))
                else:
                    return
            return

        # Go through all of the settings that the user requested be changed
        for i in range(len(choice_list)):
            # Set our choice to be the first item in the choice list
            choice = choice_list[0]

            # If the choice is a digit and less than the size of our settings list go through the current input and
            # remove it from the choice list
            if choice.isdigit() and i <= len(inputs) - 1 and int(choice) <= len(inputs):

                if int(choice) == 1:
                    self.num_comps = int(input(inputs[int(choice) - 1]))
                elif int(choice) == 2:
                    self.init_infected = int(input(inputs[int(choice) - 1]))
                elif int(choice) == 3:
                    self.infect_prob = float(input(inputs[int(choice) - 1]))
                elif int(choice) == 4:
                    self.num_sims = int(input(inputs[int(choice) - 1]))
                elif int(choice) == 5:
                    self.repaired_day = int(input(inputs[int(choice) - 1]))

                choice_list.pop(0)

            # If the item is not a valid entry ask if the user wants to continue anyways
            else:
                cont = input("\"{}\" is not a valid entry at this point. Would you like to continue anyways? (y/n)"
                             .format(choice_list.pop(0))).lower()
                if cont.lower() == 'n':
                    self.choices()

    # Method to simulate a day
    def day(self):

        # Infection process:
        # Go through the infected computer list
        for i in range(len(self.infected_list)):

            # For each infected computer try to infect all other non-infected computers
            for num in range(len(self.comp_list)):

                # If the computer is already infected or a random number between 0 and 0.99 is larger than our set
                # infection threshold move to the next step in the loop
                if self.comp_list[num] or np.random.rand(1) >= self.infect_prob:
                    continue

                # Change the computer list entry for this computer to True (i.e. infected) and add it's index to the
                # infected list
                self.comp_list[num] = True
                self.infected_list.append(num)

        # Cure process:

        cured = 0

        # Keep curing computers until we reach the desired number of cured computers or all computers are healthy
        while cured <= self.repaired_day and len(self.infected_list) > 0:
            # Choose a random index from our infected computer list, remove that index (pop) and cure the
            # corresponding computer (i.e. set it's value to False) and increment our tally
            self.comp_list[self.infected_list.pop(np.random.randint(len(self.infected_list)))] = False
            cured += 1

    # Method for running the simulation
    def run(self):

        self.choices()

        # Set our average back to 0 and reset our data arrays
        avg = 0
        sim_length_arr = []
        avg_arr = []

        # Set our number of infected computers per simulation and related averages back to 0
        num_infected_list = []
        num_all_infected = 0  # The number of times all computers become infected
        exp_num_comps = 0

        # Run the number of simulations specified
        for i in range(self.num_sims):

            # Reset our lists and day counter for each simulation
            self.comp_list = [True] * self.init_infected + [False] * (self.num_comps - self.init_infected)
            self.infected_list = list(range(0, self.init_infected, 1))
            days = 0

            been_infected = []
            # Keep running days until all computers are cured
            while len(self.infected_list) > 0 and days <= 10000:

                # Record what computers have been infected
                for x in self.infected_list:
                    if x not in been_infected:
                        been_infected.append(x)

                # Call the day method and add a day to our counter
                self.day()
                days += 1

                # Update running print statement to show the current sim number, current sim length & running average
                print("\rSimulation #: %6d, length = %3d days, average = %3f days per simulation" % (i + 1, days, avg),
                      end='')

            # Update our length data
            sim_length_arr.append(days)
            avg = (i * avg + days) / (i + 1)
            avg_arr.append(avg)

            # Update our number of infected computers data
            num_infected_list.append(len(been_infected))
            if len(been_infected) == self.num_comps:
                num_all_infected += 1
            exp_num_comps = (i * exp_num_comps + len(been_infected)) / (i + 1)

        every_prob = num_all_infected / self.num_sims

        # Plot the results
        self.plot(avg, sim_length_arr, avg_arr, num_infected_list, every_prob, exp_num_comps)

        # Ask the user if they would like to run another simulation.
        cont = input("\n\nWould you like to run another simulation?\n")
        if cont.lower() == 'y':
            self.run()


# Driver code
mySim = Simulation()
mySim.run()