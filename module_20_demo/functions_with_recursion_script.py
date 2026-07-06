# Ghidra Scripting: References
# @category: GhidraScripting
# @author: Junjie Zhang

# find all functions with recursion.

funcsWithRecursion = set()

myListing = currentProgram.getListing()
fm = currentProgram.getFunctionManager()
allFuncs = fm.getFunctions(True)

for f in allFuncs:
    f_body = f.getBody()

    instructionIterator = myListing.getInstructions(f_body, True)

    for inst in instructionIterator:
        allRefsFromInst = getReferencesFrom(inst.getAddress())
        allCallRefsFromInst = filter(lambda x: x.getReferenceType().isCall(), allRefsFromInst)
        allSelfCallRefsFromInst = filter(lambda x: x.getToAddress() == f.getEntryPoint(), allCallRefsFromInst)
        # if len(allSelfCallRefsFromInst) > 0:
        # doesn't work because filter returns a filter object, not a list
        # so we need to convert it to a list first
        if len(list(allSelfCallRefsFromInst)) > 0:
            funcsWithRecursion.add(f)

print("Functions with recursion:")
for f in funcsWithRecursion:
    print(f)