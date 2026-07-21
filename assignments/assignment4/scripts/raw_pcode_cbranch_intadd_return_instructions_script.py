# Assignment 4: Raw P-code CBRANCH, INT_ADD, and RETURN instructions in main
# @category: assignment4_scripts
# @author: Anmol Saini

from ghidra.program.model.pcode import PcodeOp

addr = currentAddress # currentAddress is the address indicated by your cursor.
func = getFunctionContaining(addr)
cnt_cbranch = 0
cnt_intadd = 0
cnt_return = 0

if func:
    fbody = func.getBody() # fbody is an object of AddressSetView
    myListing = currentProgram.getListing()
    instructionIterator = myListing.getInstructions(fbody, True) # myListing.getInstructions(AddressSetView, Boolean) will return instructions that are inside this set of addresses
    for inst in instructionIterator:
        pcodeList = inst.getPcode()
        for pcode in pcodeList:
            if pcode.getOpcode() == PcodeOp.CBRANCH:
                print(pcode)
                cnt_cbranch += 1
            elif pcode.getOpcode() == PcodeOp.INT_ADD:
                print(pcode)
                cnt_intadd += 1
            elif pcode.getOpcode() == PcodeOp.RETURN:
                print(pcode)
                cnt_return += 1

print("Total CBRANCH instructions found: {}".format(cnt_cbranch))
print("Total INT_ADD instructions found: {}".format(cnt_intadd))
print("Total RETURN instructions found: {}".format(cnt_return))