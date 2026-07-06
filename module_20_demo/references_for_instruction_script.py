# Ghidra Scripting: References
# @category: GhidraScripting
# @author: Junjie Zhang

myFunc = getFunctionContaining(currentAddress)
if myFunc:
    inst = getFirstInstruction(myFunc)
    if inst:
        addr = inst.getAddress()
        for i in getReferencesFrom(addr):
            print("a ref from this address {}: {}".format(addr, i))
        for i in getReferencesTo(addr):
            print("a ref to this address {}: {}".format(addr, i))