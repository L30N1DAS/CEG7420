# Ghidra Scripting: Basic Blocks
# @category: GhidraScripting
# @author: Junjie Zhang

# For one basic block, enumerate all incoming edges and outgoing edges;
# and for each edge, display the source address and the destination address

from ghidra.program.model.block import BasicBlockModel

myBlockModel = BasicBlockModel(currentProgram)

addr = askAddress("Ghidra Scripting: Basic Blocks", "Give me an address of a basic block:")

myBasicBlock = myBlockModel.getFirstCodeBlockContaining(addr, monitor)

print("Identified Basic Block: {}".format(myBasicBlock.getName()))

incomingEdges = myBasicBlock.getSources(monitor)
outgoingEdges = myBasicBlock.getDestinations(monitor)

for i in incomingEdges:
    print("incoming edge: src: {}, dest: {}".format(i.getSourceAddress(), i.getDestinationAddress()))

for i in outgoingEdges:
    print("outgoing edge: src: {}, dest: {}".format(i.getSourceAddress(), i.getDestinationAddress()))