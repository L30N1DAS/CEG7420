# Assignment 4: Refined P-code instructions in main
# @category: assignment4_scripts
# @author: Anmol Saini

from ghidra.app.decompiler import *

# We will get refined p-code for the current function.
func = getFunctionContaining(currentAddress)
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

cnt = 0
pcode_seq = results_highFunction.getPcodeOps() # This pcode_seq is refined pcode!
for op in pcode_seq:
    print("{}".format(op.toString()))
    cnt += 1

print("Total refined p-code instructions found: {}".format(cnt))