# Ghidra Scripting: Instructions
# @category: GhidraScripting
# @author: Junjie Zhang

# Enumerate all callees of the current function.

calleeSet = set()

myFunc = getFunctionContaining(currentAddress)
if myFunc:
    print(myFunc)
    fbody = myFunc.getBody() #fbody is an object of AddressSetView
    myListing = currentProgram.getListing()
    instructionIterator = myListing.getInstructions(fbody, True)
    for inst in instructionIterator:

        # CALL = bl;
        if inst.getMnemonicString().startswith("bl"):

            addrFlowTo = inst.getFlows() # addrFlowTo is the callee's entry point.
            for addr in addrFlowTo:
                callee = getFunctionAt(addr)
                calleeSet.add(callee)

print("{} has following callees:".format(myFunc))

for i in calleeSet:
    print("\t{}".format(i))