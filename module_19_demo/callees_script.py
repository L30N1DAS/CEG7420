# Ghidra Scripting: Instructions
# @category: GhidraScripting
# @author: Junjie Zhang

# Enumerate all callees of the current function.

myFunc = getFunctionContaining(currentAddress)
if myFunc:
    print(myFunc)
    fbody = myFunc.getBody() #fbody is an object of AddressSetView
    myListing = currentProgram.getListing()
    instructionIterator = myListing.getInstructions(fbody, True)
    for inst in instructionIterator:

        # CALL = bl
        if inst.getMnemonicString().startswith("bl"):

            calleeAddress = inst.getOpObjects(0)[0]
            callee = getFunctionAt(calleeAddress)
            print("{} calls {}.".format(myFunc, callee))