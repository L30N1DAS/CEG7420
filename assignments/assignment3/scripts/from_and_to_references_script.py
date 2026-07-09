# Assignment 3: From and To References for Function
# @category: assignment3_scripts
# @author: Anmol Saini

myFunc = getFunctionContaining(currentAddress)

if myFunc:
	print(myFunc.getName())
	fbody = myFunc.getBody()
	fromRefsCount = 0
    toRefsCount = 0

	for addr in fbody.getAddresses(True):
		for i in getReferencesFrom(addr):
			print("a ref from this address {}: {}".format(addr, i))
			fromRefsCount += 1
		for i in getReferencesTo(addr):
			print("a ref to this address {}: {}".format(addr, i))
			toRefsCount += 1

	print("References from this function {}: {}".format(myFunc.getName(), fromRefsCount))
	print("References to this function {}: {}".format(myFunc.getName(), toRefsCount))