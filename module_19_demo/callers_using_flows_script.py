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
        # CALL = bl;
        if inst.getMnemonicString().startswith("bl"):
            addrFlowTo = inst.getFlows()
            for calleeAddr in addrFlowTo:
                if myFunc.getEntryPoint() == calleeAddr:
                    callerFunc = getFunctionContaining(inst.getAddress())
                    if callerFunc:
                        print("Caller: {} at {} calls {}".format(callerFunc, inst.getAddress(), myFunc))
                        callers.add(callerFunc)

    print("callers of {}".format(myFunc))
    for i in callers:
        print(i)