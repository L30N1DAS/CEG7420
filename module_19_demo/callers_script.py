# Ghidra Scripting: Instructions
# @category: GhidraScripting
# @author: Junjie Zhang

# Enumerate all callers of the current function.

callers = set()

myFunc = getFunctionContaining(currentAddress)

if myFunc:
    # getInstructions returns an iterator of instructions inside this binary
    myListing = currentProgram.getListing()
    instructionIterator = myListing.getInstructions(True)
    for inst in instructionIterator:
        # CALL = bl; NOTE: this doesn't work great on ARM due to indirect calls like blx, but it works for most cases
        if inst.getMnemonicString().startswith("bl"):
            calleeAddr = inst.getOpObjects(0)[0]
            if myFunc.getEntryPoint() == calleeAddr:
                callerFunc = getFunctionContaining(inst.getAddress())
                if callerFunc:
                    print("Caller: {} at {} calls {}".format(callerFunc, inst.getAddress(), myFunc))
                    callers.add(callerFunc)
    print("callers of {}".format(myFunc))
    for i in callers:
        print(i)