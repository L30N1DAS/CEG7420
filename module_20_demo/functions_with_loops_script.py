# Ghidra Scripting: References
# @category: GhidraScripting
# @author: Junjie Zhang

# find all functions with loops.

funcsWithLoop = set()

myListing = currentProgram.getListing()
fm = currentProgram.getFunctionManager()
allFuncs = fm.getFunctions(True)

for f in allFuncs:
    f_body = f.getBody()

    instructionIterator = myListing.getInstructions(f_body, True)

    for inst in instructionIterator:
        allRefsFromInst = getReferencesFrom(inst.getAddress())
        allJumpRefsFromInst = filter(lambda x: x.getReferenceType().isJump(), allRefsFromInst)
        allBackwardJumpRefsFromInst = filter(lambda x: x.getFromAddress() > x.getToAddress(), allJumpRefsFromInst)
        # if len(allBackwardJumpRefsFromInst) > 0:
        # doesn't work because filter returns a filter object, not a list
        # so we need to convert it to a list first
        if len(list(allBackwardJumpRefsFromInst)) > 0:
            funcsWithLoop.add(f)

print("Functions with loop:")
for f in funcsWithLoop:
    print(f)