# Assignment 3: Unconditional Jump From and To References for Function
# @category: assignment3_scripts
# @author: Anmol Saini

myFunc = getFunctionContaining(currentAddress)

if myFunc:
	print(myFunc.getName())
	fbody = myFunc.getBody()
	unconditionalJumpFromRefsCount = 0
	unconditionalJumpToRefsCount = 0

	for addr in fbody.getAddresses(True):
		for i in getReferencesFrom(addr):
			print("a ref from this address {}: {}".format(addr, i))
			if i.getReferenceType() == RefType.UNCONDITIONAL_JUMP:
			    unconditionalJumpFromRefsCount += 1
        for i in getReferencesTo(addr):
			print("a ref to this address {}: {}".format(addr, i))
			if i.getReferenceType() == RefType.UNCONDITIONAL_JUMP:
				unconditionalJumpToRefsCount += 1

	print("Unconditional Jump References from this function {}: {}".format(myFunc.getName(), unconditionalJumpFromRefsCount))
	print("Unconditional Jump References to this function {}: {}".format(myFunc.getName(), unconditionalJumpToRefsCount))