# Ghidra Scripting: P-Code
# @category: GhidraScripting
# @author: Junjie Zhang

from ghidra.program.model.pcode import PcodeOp

myListing = currentProgram.getListing()
instructionIterator = myListing.getInstructions(True)
for inst in instructionIterator:
    pcodeList = inst.getPcode()
    print("{} : {}".format(inst.getAddress(), inst))
    for pcode in pcodeList:
        print("\t{}".format(pcode))
        seq = pcode.getSeqnum()
        print("\t\tseq number: {}".format(seq))
        print("\t\t\taddress of the assembly instruction this pcode is from: {} with the index of {}".format(seq.getTarget(), seq.getTime()))