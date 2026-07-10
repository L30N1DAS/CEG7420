# Ghidra Scripting: Basic Blocks
# @category: GhidraScripting
# @author: Junjie Zhang

# To enumerate all basic blocks in a binary.

from ghidra.program.model.block import BasicBlockModel

myBlockModel = BasicBlockModel(currentProgram)
myBasicBlocks = myBlockModel.getCodeBlocks(monitor)
for i in myBasicBlocks:
    print(i)