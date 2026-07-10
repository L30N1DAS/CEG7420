# Assignment 3: Basic Blocks in Function Count
# @category: assignment3_scripts
# @author: Anmol Saini

from ghidra.program.model.block import BasicBlockModel

myBlockModel = BasicBlockModel(currentProgram)
currentFunc = getFunctionContaining(currentAddress)

if currentFunc:
    fbody = currentFunc.getBody()
    myBasicBlocks = myBlockModel.getCodeBlocksContaining(fbody, monitor) #fbody is an instance of the AddressSetView class
    basicBlocksCount = 0

    for i in myBasicBlocks:
        name = i.getName()
        print('Name: {}, Starting Address: {}'.format(name, i.getFirstStartAddress()))
        basicBlocksCount += 1

    print('Total basic blocks in function {}: {}'.format(currentFunc.getName(), basicBlocksCount))