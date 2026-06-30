# Ghidra Scripting: Functions
# @category: GhidraScripting
# @author: Junjie Zhang

myFunc = getFirstFunction()
while myFunc:
    print(myFunc)
    myFunc = getFunctionAfter(myFunc)