# Ghidra Scripting: References
# @category: GhidraScripting
# @author: Junjie Zhang

myListing = currentProgram.getListing()
instructionIterator = myListing.getInstructions(True)
for inst in instructionIterator:
    addr = inst.getAddress()
    allRefsFromAddr = getReferencesFrom(addr)
    for ref in allRefsFromAddr:
        if ref.getReferenceType() == RefType.UNCONDITIONAL_JUMP:
            print("{} with the specific type of {}".format(ref, ref.getReferenceType().getName()))