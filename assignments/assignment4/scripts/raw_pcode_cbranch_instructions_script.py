# Assignment 4: Raw P-code CBRANCH instructions in main
# @category: assignment4_scripts
# @author: Anmol Saini

from ghidra.program.model.pcode import PcodeOp

addr = currentAddress # currentAddress is the address indicated by your cursor.
func = getFunctionContaining(addr)
cnt = 0

if func:
    fbody = func.getBody() # fbody is an object of AddressSetView
    myListing = currentProgram.getListing()
    instructionIterator = myListing.getInstructions(fbody, True) # myListing.getInstructions(AddressSetView, Boolean) will return instructions that are inside this set of addresses
    for inst in instructionIterator:
        pcodeList = inst.getPcode()
        for pcode in pcodeList:
            if pcode.getOpcode() == PcodeOp.CBRANCH:
                print(pcode)
                cnt += 1

print("Total CBRANCH instructions found: {}".format(cnt))