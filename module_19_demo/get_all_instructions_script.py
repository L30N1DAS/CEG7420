# Ghidra Scripting: Instructions
# @category: GhidraScripting
# @author: Junjie Zhang

cnt = 0

inst = getFirstInstruction()
while inst:
    cnt += 1
    print("{} : {}".format(inst.getAddress(), inst))
    inst = getInstructionAfter(inst)
    if cnt > 10:
        break