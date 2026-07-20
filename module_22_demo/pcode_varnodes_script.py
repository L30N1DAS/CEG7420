# Ghidra Scripting: P-Code
# @category: GhidraScripting
# @author: Junjie Zhang

# to explore varnodes

from ghidra.program.model.pcode import PcodeOp
cnt = 0
myListing = currentProgram.getListing()
instructionIterator = myListing.getInstructions(True)
for inst in instructionIterator:
    pcodeList = inst.getPcode()
    print("{}".format(inst))
    for pcode in pcodeList:
        print("\t{}".format(pcode))
        output = pcode.getOutput()
        inputs = pcode.getInputs()
        if output:
            print("\t\toutput: {}".format(output))
            print("\t\t\tRam/Address Space?: {}".format(output.isAddress()))
            print("\t\t\tConstant Space?: {}".format(output.isConstant()))
            print("\t\t\tRegister Space?: {}".format(output.isRegister()))
            print("\t\t\tTemporary/Unique Space?: {}".format(output.isUnique()))
            print("\t\t\tOffset: {}, with size: {}".format(output.getOffset(), output.getSize()))
        for vn in inputs:
            print("\t\tinput: {}".format(vn))
            print("\t\t\tRam/Address Space?: {}".format(vn.isAddress()))
            print("\t\t\tConstant Space?: {}".format(vn.isConstant()))
            print("\t\t\tRegister Space?: {}".format(vn.isRegister()))
            print("\t\t\tTemporary/Unique Space?: {}".format(vn.isUnique()))
            print("\t\t\tOffset: {}, with size: {}".format(vn.getOffset(), vn.getSize()))