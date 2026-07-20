# Ghidra Scripting: P-Code
# @category: GhidraScripting
# @author: Junjie Zhang

# to only print p-code instructions that are `CALL` p-code operators/opcodes

from ghidra.program.model.pcode import PcodeOp
cnt = 0
myListing = currentProgram.getListing()
instructionIterator = myListing.getInstructions(True)
for inst in instructionIterator:
    pcodeList = inst.getPcode()
    for pcode in pcodeList:
        if pcode.getOpcode() == PcodeOp.CALL:
            print(pcode)