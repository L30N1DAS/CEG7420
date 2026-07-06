# Ghidra Scripting: References
# @category: GhidraScripting
# @author: Junjie Zhang

# find all callers of the current function.

myFunc = getFunctionContaining(currentAddress)
if myFunc:
    entryPoint = myFunc.getEntryPoint()
    for ref in getReferencesTo(entryPoint):
        if ref.getReferenceType().isCall():
            callerInstAddr = ref.getFromAddress()
            callerFunc = getFunctionContaining(callerInstAddr)
            print("{} is called by {} at {}".format(myFunc, callerFunc, callerInstAddr))