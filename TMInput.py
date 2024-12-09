import random
import string

def randomString(length=10):
    # generates a random string of given length consisting of 'a', 'b', and 'c'
    return ''.join(random.choice('abc') for _ in range(length))

def generateTransition(numTapes):
    # curr state for the Turing Machine
    currentState = random.choice(['q0', 'q1', 'q2', 'q3', 'q4', 'qf0', 'qf1'])
    # random input symbols or wildcard '*'
    inputSymbols = [random.choice('abc*') for _ in range(numTapes)]
    # select the next state
    nextState = random.choice(['q0', 'q1', 'q2', 'q3', 'q4', 'qf0', 'qf1'])
    # symbols or wildcard '*' for each tape
    replacements = [random.choice('abc*') for _ in range(numTapes)]
    # select movement ('L', 'R', or '*') for each tape head
    moves = [random.choice(['L', 'R', '*']) for _ in range(numTapes)]
    
    # return what we made
    return [currentState] + inputSymbols + [nextState] + replacements + moves

def generateTuringMachineInput(numTapes=3, numTransitions=10):
    name = "MultiTapeMachine"
    tapes = [randomString(random.randint(5, 15)) + 'n' * 100 for _ in range(numTapes)]
    transitions = [generateTransition(numTapes) for _ in range(numTransitions)]
    
    # generates Turing Machine input string
    tmInput = f"{name} {numTapes}\n"
    tmInput += "\n".join(tapes) + "\n"
    for transition in transitions:
        tmInput += " ".join(transition) + "\n"
    
    return tmInput

def generateMultipleTMInputs(numCases=250, numTapes=3, numTransitions=10, outputFile="TMInputs.txt"):
    # writing
    with open(outputFile, 'w') as f:
        for _ in range(numCases):
            tmInput = generateTuringMachineInput(numTapes, numTransitions)
            f.write(tmInput + "\n")

if __name__ == "__main__":
    generateMultipleTMInputs(numCases=250, numTapes=3, numTransitions=10, outputFile="TMInputs.txt")
