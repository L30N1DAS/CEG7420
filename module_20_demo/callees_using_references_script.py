# Ghidra Scripting: References
# @category: GhidraScripting
# @author: Junjie Zhang

# find all callees of the current function.
myFunc = getFunctionContaining(currentAddress)
if myFunc:
    print(myFunc)

    fbody = myFunc.getBody() # fbody is an object of AddressSetView
    myListing = currentProgram.getListing()
    instructionIterator = myListing.getInstructions(fbody, True)

    for inst in instructionIterator:
        addr = inst.getAddress()
        for ref in getReferencesFrom(addr):
            if ref.getReferenceType().isCall():
                calleeAddr = ref.getToAddress()
                calleeFunc = getFunctionAt(calleeAddr)
                print("{} at {} calls {}".format(myFunc, addr, calleeFunc))