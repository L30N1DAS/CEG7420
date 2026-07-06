# Ghidra Scripting: References
# @category: GhidraScripting
# @author: Junjie Zhang

cnt = 0

myFunc = getFunctionContaining(currentAddress)
if myFunc:
    print(myFunc.getName())
    fbody = myFunc.getBody()
    for addr in fbody.getAddresses(True):
        for i in getReferencesFrom(addr):
            print("a ref from this address {}: {}".format(addr, i))
        for i in getReferencesTo(addr):
            print("a ref to this address {}: {}".format(addr, i))

        cnt += 1
        if cnt > 9:
            break