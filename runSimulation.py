import subprocess
import os
import glob

def getNextFileNumber(base_name):
    # find next file num
    existing_files = glob.glob(f"{base_name}[0-9]*.txt")
    numbers = [int(f[len(base_name):-4]) for f in existing_files if f[len(base_name):-4].isdigit()]
    return max(numbers, default=0) + 1

def runGenerateInput():
    # run generator script
    try:
        subprocess.run(["python3", "generateTMInput.py"], check=True)
        print("TMInputs.txt has been generated with 250 Turing Machine inputs.\n")
    except subprocess.CalledProcessError:
        print("Error running input generator.")
        return False
    return True

def runSimulate():
    # run simulation script
    print("Running Turing Machine simulator...")
    try:
        subprocess.run(["python3", "simulateTuringMachine.py"], check=True)
        print("Turing Machine simulation complete.")
        print(" ")
    except subprocess.CalledProcessError:
        print("Error running simulator.")
        return False
    return True

def saveResults(file_number):
    # saving info
    input_file = "TMInputs.txt"
    output_file = "TMOutputs.txt"
    new_input_file = f"TMInputs{file_number}.txt"
    new_output_file = f"TMOutputs{file_number}.txt"
    
    # save inputs
    if os.path.exists(input_file):
        with open(input_file, 'r') as infile, open(new_input_file, 'w') as outfile:
            outfile.write("INPUT:\n")
            outfile.write(infile.read())
        print(f"Saved inputs to {new_input_file}")
    
    # saves outputs
    if os.path.exists(output_file):
        with open(output_file, 'r') as outfile, open(new_output_file, 'w') as outfile_new:
            outfile_new.write("OUTPUT:\n")
            outfile_new.write(outfile.read())
        print(f"Saved outputs to {new_output_file}")
    
    # cleanup
    if os.path.exists(input_file):
        os.remove(input_file)
    if os.path.exists(output_file):
        os.remove(output_file)
    print("Deleted TMInputs.txt and TMOutputs.txt for cleaning purposes.\n")

def main():
    if not runGenerateInput():
        return

    if not runSimulate():
        return

    file_number = getNextFileNumber("TMInputs")
    saveResults(file_number)
    print("Entire simulation and write complete.")

if __name__ == "__main__":
    main()
