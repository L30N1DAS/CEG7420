# Ghidra Scripting: References
# @category: GhidraScripting
# @author: Junjie Zhang

# find all callers of the current function.

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

        if len(allBackwardJumpRefsFromInst) > 0:
            funcsWithLoop.add(f)

print("Functions with loop:")
for f in funcsWithLoop:
    print(f)


# jumpRefs = filter(lambda x: x.getReferenceType().isJump() and f_body.contains(x.getToAddress()) and x.getToAddress().subtract(inst.getAddress()) < 0, getReferencesFrom(inst.getAddress()))
# if len(list(jumpRefs)) > 0:
#     funcsWithLoop.add(f)
