# Ghidra Scripting: Functions
# @category: GhidraScripting
# @author: Junjie Zhang

myFuncManager = currentProgram.getFunctionManager()
allFuncs = myFuncManager.getFunctions(True)
for i in allFuncs:
    print(i)