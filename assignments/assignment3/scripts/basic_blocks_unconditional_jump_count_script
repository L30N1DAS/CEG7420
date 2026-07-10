# Assignment 3: Unconditional Jump Basic Blocks Count
# @category: assignment3_scripts
# @author: Anmol Saini

from ghidra.program.model.block import BasicBlockModel

myBlockModel = BasicBlockModel(currentProgram)
myBasicBlocks = myBlockModel.getCodeBlocks(monitor)
unconditionalJumpBasicBlocksCount = 0

for i in myBasicBlocks:
    if i.getFlowType() == FlowType.UNCONDITIONAL_JUMP:
        print(i)
        unconditionalJumpBasicBlocksCount += 1

print('Total unconditional jump basic blocks in the binary: {}'.format(unconditionalJumpBasicBlocksCount))