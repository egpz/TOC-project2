# TOC-project2
Turing machine project. Emulates NTM execution and traces all possible execution paths that a nondeterministic TM might take up until the time when it either accepts or rejects.

# Project 2 Readme Team EGPZ

## 1. Team Name:
EGPZ

## 2. Team members' names and netids:
EG Gonzalez - egonza26

## 3. Overall project attempted, with sub-projects:
Program 2: K-Tape Turing Machine

## 4. Overall success of the project:
Successful as far as I evaluated. The program anazlyzed the inputs well and it ran succesfull after all final code commits.

## 5. Approximately total time (in hours) to complete:
6 hours

## 6. Link to GitHub repository:
[https://github.com/egpz/TOC-project2](https://github.com/egpz/TOC-project2)

## 7. List of included files:
**Code Files**
- [X] TMInput.py (Generates random Turing Machine input data)
- [X] runSimulation.py (Automates the entire process, assigns filenames, and manages file cleanup. Handles input/output naming for each run)
- [X] simulateTM.py (Runs the simulation on input data and writes result to an output file)
 
  
**Test Files**
- [X] TMInputs.txt  (Initial input file created by generateTMInput.py)
- [X] TMInputs1.txt (Generated input file, used for the Turing machine simulation)
- [X] TMInputs2.txt (Generated input file, used for the Turing machine simulation)
- [X] TMInputs3.txt (Generated input file, used for the Turing machine simulation)
- [X] TMInputs4.txt (Generated input file, used for the Turing machine simulation)
- [X] TMInputs5.txt (Generated input file, used for the Turing machine simulation)

**Output Files**
- [X] TMOutputs1.txt (Output file for TMInputs1.txt)
- [X] TMOutputs2.txt  (Output file for TMInputs2.txt)
- [X] TMOutputs3.txt  (Output file for TMInputs3.txt)
- [X] TMOutputs4.txt  (Output file for TMInputs4.txt)
- [X] TMOutputs5.txt  (Output file for TMInputs5.txt)

## 8. Programming languages used, and associated libraries:
- Python:
    - Subprocess: To execute scripts in the directory.
    - Sys: For argument parsing.
    - Os: Used for file existence checks and deleting files.


## 9. Key data structures:
Lists, Dictionaries, Strings

## 10. General explination of each program:
- **generateTMInput.py**: Generates input data for the Turing machine.
- **simulateTuringMachine.py**: Parses inputs and generates simulation output.
- **runTMSimulation.py**: Automates both input generation and simulation, saves results with new filenames, and performs cleanup.

## 11. What test cases you used/added, why you used them, what did they tell you about the correctness of your code:
I used test cases with varying input sizes and edge cases, such as multiple tapes and transitions, to make sure that the Turing Machine simulator handled different configurations correctly.

## 13. How team was organized and dynamics:
I worked on this project alone. As such, I followed a similar structure used for project 1. I decided  what inputs would be needed and what I wanted them to look like. I used this to start  writing **generateTMInput.py**. Then I tackled actually creating the Turing Machine, which took the longest. I made sure the logic was correct by referencing the textbook. Finally, I made everything run automatically, assigning file names and cleaning up unnecessary files.

## 14. What you might do differently if you did the project again:
If I were to do the project again, I would of course start ealier. Hoenstly debuggin it was super difficult at certain points so I would implement more detailed logging to track each step of the simulation to make debugging and testing easier.

