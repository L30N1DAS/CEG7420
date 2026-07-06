# Ghidra Scripting: Instructions
# @category: GhidraScripting
# @author: Junjie Zhang

# get the fallthrough instructions and non-fallthrough/target instructions for J, CALL, and RET instructions.

myFunc = getFunctionContaining(currentAddress)
if myFunc:
    print(myFunc)
    fbody = myFunc.getBody() #fbody is an object of AddressSetView
    myListing = currentProgram.getListing()
    instructionIterator = myListing.getInstructions(fbody, True)
    for inst in instructionIterator:

        # J = b, CALL = bl, RET = ret
        if inst.getMnemonicString().startswith("b") or inst.getMnemonicString().startswith("ret"):

            print("-"*10)
            
            print("{}\t{}".format(inst.getAddress(), inst))

            addrFallThrough = inst.getFallThrough()
            if addrFallThrough:
                fallThroughtInst = getInstructionAt(addrFallThrough)
                print("        fallthrough to: {}\t{}".format(addrFallThrough, fallThroughtInst))

            addrOtherThanFallThrough = inst.getFlows()
            for one in addrOtherThanFallThrough:
                notFallThroughtInst = getInstructionAt(one)
                print("        notfallthrough/targe/flow to: {}\t{}".format(one, notFallThroughtInst))