# Ghidra Scripting: Functions
# @category: GhidraScripting
# @author: Junjie Zhang

myFuncManager = currentProgram.getFunctionManager()
allFuncs = myFuncManager.getFunctions(True)
for f in allFuncs:

    f_body = f.getBody()

    print("-"*10)
    print("name:\t\t{}".format(f.getName()))
    print("calling convention:\t\t{}".format(f.getCallingConventionName()))
    print("signature:\t\t{}".format(f.getSignature()))
    print("entry address:\t\t{}".format(f.getEntryPoint()))
    print("exit address:\t\t{}".format(f_body.getMaxAddress()))
    print("size of function body:\t\t{}".format(f_body.getNumAddresses()))
    print("internal function:\t\t{}".format(not f.isExternal()))
    print("external function:\t\t{}".format(f.isExternal()))
    print("inline function:\t\t{}".format(f.isInline()))
    print("thunk function:\t\t{}".format(f.isThunk()))

    parameter_cnt = f.getParameterCount()
    parameter_list = f.getParameters()
    for i in parameter_list:
        print("parameter:\t\t{}".format(i))

    local_variables = f.getLocalVariables()
    for i in local_variables:
        print("local variable:\t\t{}".format(i))

    ret_variable = f.getReturn()
    ret_variable_type = f.getReturnType()
    print("return variable: {} with the type of {}".format(ret_variable, ret_variable_type))