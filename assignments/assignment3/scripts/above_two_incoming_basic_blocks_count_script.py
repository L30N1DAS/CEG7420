# Assignment 3: Count of Basic Blocks with More than Two Incoming Basic Blocks
# @category: assignment3_scripts
# @author: Anmol Saini

from ghidra.program.model.block import BasicBlockModel

myBlockModel = BasicBlockModel(currentProgram)
myBasicBlocks = myBlockModel.getCodeBlocks(monitor)
countOfBasicBlocksWithMoreThanTwoIncomingBlocks = 0

for i in myBasicBlocks:
    incomingEdgesCount = i.getNumSources(monitor)
    if incomingEdgesCount > 2:
        countOfBasicBlocksWithMoreThanTwoIncomingBlocks += 1

print('Total basic blocks with more than two incoming blocks: {}'.format(countOfBasicBlocksWithMoreThanTwoIncomingBlocks))