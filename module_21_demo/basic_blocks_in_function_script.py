# Ghidra Scripting: Basic Blocks
# @category: GhidraScripting
# @author: Junjie Zhang

# To enumerate all basic blocks in the current function.

from ghidra.program.model.block import BasicBlockModel

myBlockModel = BasicBlockModel(currentProgram)
currentFunc = getFunctionContaining(currentAddress)
if currentFunc:
    fbody = currentFunc.getBody()
    myBasicBlocks = myBlockModel.getCodeBlocksContaining(fbody, monitor) #fbody is an instance of the AddressSetView class
    for i in myBasicBlocks:
        name = i.getName()
        print('Name: {}, Starting Address: {}'.format(name, i.getFirstStartAddress()))