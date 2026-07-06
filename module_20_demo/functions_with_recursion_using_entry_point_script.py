# Ghidra Scripting: References
# @category: GhidraScripting
# @author: Junjie Zhang

# find all functions with recursion.

funcsWithRecursion = set()

myListing = currentProgram.getListing()
fm = currentProgram.getFunctionManager()
allFuncs = fm.getFunctions(True)

for f in allFuncs:

    entryPoint = f.getEntryPoint()
    f_body = f.getBody()

    allRefsToEntryPoint = getReferencesTo(entryPoint)
    allCallRefsToEntryPoint = filter(lambda x: x.getReferenceType().isCall(), allRefsToEntryPoint)
    allSelfCallRefsToEntryPoint = filter(lambda x: f_body.contains(x.getFromAddress()), allCallRefsToEntryPoint)

    # if len(allSelfCallRefsToEntryPoint) > 0:
    # doesn't work because filter returns a filter object, not a list
    # so we need to convert it to a list first
    if len(list(allSelfCallRefsToEntryPoint)) > 0:
        funcsWithRecursion.add(f)

print("Functions with recursion:")
for f in funcsWithRecursion:
    print(f)