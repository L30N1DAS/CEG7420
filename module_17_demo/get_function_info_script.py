# Ghidra Scripting: Functions
# @category: GhidraScripting
# @author: Junjie Zhang

myFuncManager = currentProgram.getFunctionManager()
allFuncs = myFuncManager.getFunctions(True)
for f in allFuncs:
    print("-"*10)
    print("name:\t\t{}".format(f.getName()))
    print("calling convention:\t\t{}".format(f.getCallingConventionName()))
    print("signature:\t\t{}".format(f.getSignature()))
    print("entry address:\t\t{}".format(f.getEntryPoint()))
    # print("exit address:\t\t{}".format(f_body().getMaxAddress()))
    # print("size of function body:\t\t{}".format(f_body().getNumAddresses()))
    print("internal function:\t\t{}".format(not f.isExternal()))
    print("external function:\t\t{}".format(f.isExternal()))
    print("inline function:\t\t{}".format(f.isInline()))
    print("thunk function:\t\t{}".format(f.isThunk()))
