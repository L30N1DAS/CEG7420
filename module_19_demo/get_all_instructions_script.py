# Ghidra Scripting: Instructions
# @category: GhidraScripting
# @author: Junjie Zhang

inst = getFirstInstruction()
while inst:
    print("{} : {}".format(inst.getAddress(), inst))
    inst = getInstructionAfter(inst)