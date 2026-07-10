# Assignment 3: Basic Blocks Count
# @category: assignment3_scripts
# @author: Anmol Saini

# To enumerate all basic blocks in a binary.

from ghidra.program.model.block import BasicBlockModel

myBlockModel = BasicBlockModel(currentProgram)
myBasicBlocks = myBlockModel.getCodeBlocks(monitor)
for i in myBasicBlocks:
    print(i)