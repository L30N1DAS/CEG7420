# Assignment 4: Refined P-code instructions with input varnodes in main
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

pcode_seq = results_highFunction.getPcodeOps() # This pcode_seq is refined pcode!

paramSet = set()

for op in pcode_seq:
    inputs = op.getInputs()
    for invar in inputs:
        hv = invar.getHigh()
        if hv:
            hs = hv.getSymbol()
            if hs and hs.isParameter():
                # Add the formatted string to the set instead of the Varnode object
                # This ensures Python evaluates uniqueness based on the text values
                paramSet.add("varnode: {}, high variable name: {} with type {}, symbol name: {}".format(invar, hv.getName(), hv.getDataType(), hs.getName()))

print("all varnodes in refined pcode that are identified as parameters.")
for unique_param in paramSet:
    print(unique_param)