# Assignment 4: Refined P-code instructions with specific varnodes in main
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

for op in pcode_seq:
    print(op)
    output = op.getOutput()
    if output:
        print("\toutput varnode: {}".format(output))

        inst_def = output.getDef()
        print("\t\t It is defined by: {}".format(inst_def))

        inst_descendants = output.getDescendants()
        for i in inst_descendants:
            print("\t\t It is used by: {}".format(i))
            
    inputs = op.getInputs()
    for invar in inputs:
        print("\tinput varnode: {}".format(invar))
        inst_def = invar.getDef()
        print("\t\t It is defined by: {}".format(inst_def))

        inst_descendants = invar.getDescendants()
        for i in inst_descendants:
            print("\t\t It is used by: {}".format(i))