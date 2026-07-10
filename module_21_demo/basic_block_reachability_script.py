# Ghidra Scripting: Basic Blocks
# @category: GhidraScripting
# @author: Junjie Zhang

# Given a basic block, identify all basic blocks from which the current basic block is reachable.

from ghidra.program.model.block import BasicBlockModel

myBlockModel = BasicBlockModel(currentProgram)
addr = askAddress("Ghidra Scripting: Basic Blocks", "Give me an address of a basic block:")
targetBasicBlock = myBlockModel.getFirstCodeBlockContaining(addr, monitor)

if not targetBasicBlock:
    exit()

processedBasicBlocks = []
toBeProcessedBasicBlocks = [targetBasicBlock]

while len(toBeProcessedBasicBlocks) > 0:
    one = toBeProcessedBasicBlocks.pop(0) # to dequeue the array
    processedBasicBlocks.append(one)
    incomingEdges = one.getSources(monitor)
    while incomingEdges.hasNext():
        incomingRef = incomingEdges.next()
        srcBasicBlock = incomingRef.getSourceBlock()
        if srcBasicBlock:
            if not (srcBasicBlock in processedBasicBlocks):
                toBeProcessedBasicBlocks.append(srcBasicBlock)

print("The target basic block {} is reachable from the following basic blocks:".format(targetBasicBlock.getName()))
print([i.getName() for i in processedBasicBlocks])