# Ghidra Scripting: References
# @category: GhidraScripting
# @author: Junjie Zhang

# enumerate all references from and to an address
addr = askAddress("Ghidra Scripting - References", "Please input an address:")

refManager = currentProgram.getReferenceManager()

for i in refManager.getReferencesFrom(addr):
    print("a ref from this address: {}".format(i))
for i in refManager.getReferencesTo(addr):
    print("a ref to this address: {}".format(i))