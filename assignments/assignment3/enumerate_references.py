# Hint: Code to enumerate references in a function:

myFunc = getFunctionContaining(currentAddress)
if myFunc:
	print(myFunc.getName())
	fbody = myFunc.getBody()
	for addr in fbody.getAddresses(True):
		for i in getReferencesFrom(addr):
			print("a ref from this address {}: {}".format(addr, i))
		for i in getReferencesTo(addr):
			print("a ref to this address {}: {}".format(addr, i))