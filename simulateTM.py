class TuringMachine:
    def __init__(self, inputFile):
        # initialize machine parameters
        self.name = None
        self.numTapes = 1
        self.tapes = []
        self.tapeHeads = []
        self.states = set()
        self.currentState = None
        self.transitions = []
        
        # pare input
        self._parseInputFile(inputFile)
    
    def _parseInputFile(self, filename):
        with open(filename, 'r') as f:
            # 0arse first line w machine name and number of tapes
            firstLine = f.readline().strip().split()
            self.name = firstLine[0]
            self.numTapes = int(firstLine[1]) if len(firstLine) > 1 else 1
            
            # initialize tapes
            self.tapes = [list(f.readline().strip() + 'n' * 100) for _ in range(self.numTapes)]
            self.tapeHeads = [0] * self.numTapes
            self.currentState = None
            
            # parse transitions
            for line in f:
                transition = line.strip().split()
                if not transition:
                    continue
                
                # first state
                if self.currentState is None:
                    self.currentState = transition[0]
                
                # check num of elements
                expectedLength = 2 * self.numTapes + 3
                if len(transition) < expectedLength:
                    continue

                # state tracking 
                self.transitions.append(transition)
                self.states.update([transition[0], transition[self.numTapes + 1]])

    
    def _findMatchingTransition(self, currentSymbols):
        # find transitions
        for transition in self.transitions:
            # check for start state
            if transition[0] != self.currentState:
                continue
            
            # check matches and wildcards
            match = True
            for i in range(self.numTapes):
                inputSymbol = transition[i+1]
                if inputSymbol != '*' and inputSymbol != currentSymbols[i]:
                    match = False
                    break
            
            if match:
                return transition
        
        return None
    
    def simulate(self, maxSteps=1000):
        # output file
        with open('TMOutputs.txt', 'w') as out:
            # write machine name
            out.write(f"{self.name} Simulation\n")
            
            # run turing machine
            for step in range(maxSteps):
                out.write(f"\nStep {step}:\n")
                currentSymbols = []
                
                # get symbols
                for tapeIdx in range(self.numTapes):
                    head = self.tapeHeads[tapeIdx]
                    tape = self.tapes[tapeIdx]
                    
                    # make tape longer if needed
                    if head >= len(tape):
                        tape.extend(['n'] * (head - len(tape) + 1))
                    
                    # head symbol
                    currentSymbol = tape[head]
                    currentSymbols.append(currentSymbol)
                    
                    # write to output
                    tapeDisplay = ''.join(tape)
                    out.write(f"Tape {tapeIdx+1}: {tapeDisplay[:head]} {tapeDisplay[head]} {tapeDisplay[head+1:]}\n")
                
                # find transitions
                transition = self._findMatchingTransition(currentSymbols)
                
                # edge case
                if transition is None:
                    out.write("No matching transition found. Halting.\n")
                    break
                
                # update curr state
                self.currentState = transition[self.numTapes + 1]
                
                # update tapes and tape heads based on transition actions
                for tapeIdx in range(self.numTapes):
                    replacement = transition[self.numTapes + 2 + tapeIdx]
                    if replacement != '*':
                        self.tapes[tapeIdx][self.tapeHeads[tapeIdx]] = replacement
                    
                    # move tape
                    move = transition[2 * self.numTapes + 2 + tapeIdx]
                    if move == 'L':
                        self.tapeHeads[tapeIdx] = max(0, self.tapeHeads[tapeIdx] - 1)
                    elif move == 'R':
                        self.tapeHeads[tapeIdx] += 1
                
                # final state check
                if self.currentState in [t for t in self.states if t.startswith('qf')]:
                    out.write("Reached final state. Halting.\n")
                    break
            
            else:
                out.write("Maximum steps reached. Halting.\n")


if __name__ == "__main__":
    tm = TuringMachine('TMInputs.txt')
    tm.simulate()
    print("Simulation complete. Output written to TMOutputs.txt")
