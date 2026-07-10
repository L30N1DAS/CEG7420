# Assignment 3: Basic Blocks Count
# @category: assignment3_scripts
# @author: Anmol Saini

# To enumerate all basic blocks in a binary.

from ghidra.program.model.block import BasicBlockModel

myBlockModel = BasicBlockModel(currentProgram)
myBasicBlocks = myBlockModel.getCodeBlocks(monitor)
basicBlocksCount = 0

for i in myBasicBlocks:
    print(i)
    basicBlocksCount += 1

print('Total basic blocks in the binary: {}'.format(basicBlocksCount))