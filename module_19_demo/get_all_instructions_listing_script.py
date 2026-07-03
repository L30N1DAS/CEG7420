# Ghidra Scripting: Instructions
# @category: GhidraScripting
# @author: Junjie Zhang

# currentProgram <- Program
myListing = currentProgram.getListing()
instructionIterator = myListing.getInstructions(True)
for inst in instructionIterator:
    print(inst)