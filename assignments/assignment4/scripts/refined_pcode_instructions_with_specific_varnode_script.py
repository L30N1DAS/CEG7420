# Assignment 4: Refined P-code instructions with specific varnode in main
# @category: assignment4_scripts
# @author: Anmol Saini

from ghidra.app.decompiler import *

# We will get refined p-code for the current function.
func = getFunctionContaining(currentAddress)
fbody = func.getBody() # fbody is an object of AddressSetView
startAddress = fbody.getMinAddress()
endAddress = fbody.getMaxAddress()

myDecomp = DecompInterface()
myDecomp.openProgram(currentProgram)

if func is None:
    print("No function contains this address.")
    exit()

decomp_results = myDecomp.decompileFunction(func, 30, monitor)
if decomp_results is None:
    print("Fail to decompile this function.")
    exit()

results_highFunction = decomp_results.getHighFunction()
if results_highFunction is None:
    print("Fail to get the high function.")
    exit()

varnodes_highFunction = results_highFunction.getVarnodes(startAddress, endAddress) # This will populate the varnode list in the high function

for varnode in varnodes_highFunction:
    if varnode.isRegister():
        print("varnode: {}".format(varnode))

        varnode_def = varnode.getDef()
        print("\t It is defined by: {}".format(varnode_def))

        varnode_descendants = varnode.getDescendants()
        for i in varnode_descendants:
            print("\t It is used by: {}".format(i))