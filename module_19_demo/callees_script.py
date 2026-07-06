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

        # CALL = bl; NOTE: this doesn't work great on ARM due to indirect calls like blx, but it works for most cases
        if inst.getMnemonicString().startswith("bl"):

            calleeAddress = inst.getOpObjects(0)[0]
            callee = getFunctionAt(calleeAddress)
            calleeSet.add(callee)

print("{} has following callees:".format(myFunc))

for i in calleeSet:
    print("\t{}".format(i))