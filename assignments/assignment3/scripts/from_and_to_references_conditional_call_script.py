# Assignment 3: Conditional Call From and To References for Function
# @category: assignment3_scripts
# @author: Anmol Saini

from ghidra.program.model.symbol import RefType

myFunc = getFunctionContaining(currentAddress)

if myFunc:
	print(myFunc.getName())
	fbody = myFunc.getBody()
	conditionalCallFromRefsCount = 0
	conditionalCallToRefsCount = 0

	for addr in fbody.getAddresses(True):
		for i in getReferencesFrom(addr):
			print("a ref from this address {}: {}".format(addr, i))
			if i.getReferenceType() == RefType.CONDITIONAL_CALL:
				conditionalCallFromRefsCount += 1
		for i in getReferencesTo(addr):
			print("a ref to this address {}: {}".format(addr, i))
			if i.getReferenceType() == RefType.CONDITIONAL_CALL:
				conditionalCallToRefsCount += 1

	print("Conditional Call References from this function {}: {}".format(myFunc.getName(), conditionalCallFromRefsCount))
	print("Conditional Call References to this function {}: {}".format(myFunc.getName(), conditionalCallToRefsCount))