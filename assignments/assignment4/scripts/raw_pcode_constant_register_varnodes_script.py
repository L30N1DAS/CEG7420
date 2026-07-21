# Assignment 4: Raw P-code instructions with input and output constant and register varnodes in main
# @category: assignment4_scripts
# @author: Anmol Saini

from ghidra.program.model.pcode import PcodeOp

addr = currentAddress # currentAddress is the address indicated by your cursor.
func = getFunctionContaining(addr)
cnt_constant_output = 0
cnt_register_output = 0
cnt_constant_input = 0
cnt_register_input = 0

if func:
    fbody = func.getBody() # fbody is an object of AddressSetView
    myListing = currentProgram.getListing()
    instructionIterator = myListing.getInstructions(fbody, True) # myListing.getInstructions(AddressSetView, Boolean) will return instructions that are inside this set of addresses
    for inst in instructionIterator:
        pcodeList = inst.getPcode()
        for pcode in pcodeList:
            print("\t{}".format(pcode))
            output = pcode.getOutput()
            inputs = pcode.getInputs()
            if output:
                if output.isConstant():
                    print("\t\toutput: {}; Constant Space?: {}".format(output, output.isConstant()))
                    cnt_constant_output += 1
                elif output.isRegister():
                    print("\t\toutput: {}; Register Space?: {}".format(output, output.isRegister()))
                    cnt_register_output += 1
            for vn in inputs:
                if vn.isConstant():
                    print("\t\tinput: {}; Constant Space?: {}".format(vn, vn.isConstant()))
                    cnt_constant_input += 1
                elif vn.isRegister():
                    print("\t\tinput: {}; Register Space?: {}".format(vn, vn.isRegister()))
                    cnt_register_input += 1

print("Total constant output varnodes found: {}".format(cnt_constant_output))
print("Total register output varnodes found: {}".format(cnt_register_output))
print("Total constant input varnodes found: {}".format(cnt_constant_input))
print("Total register input varnodes found: {}".format(cnt_register_input))