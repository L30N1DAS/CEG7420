# Assignment 3: Unconditional Call From and To References for Function
# @category: assignment3_scripts
# @author: Anmol Saini

from ghidra.program.model.symbol import RefType

myFunc = getFunctionContaining(currentAddress)

if myFunc:
	print(myFunc.getName())
	fbody = myFunc.getBody()
	unconditionalCallFromRefsCount = 0
	unconditionalCallToRefsCount = 0

	for addr in fbody.getAddresses(True):
		for i in getReferencesFrom(addr):
			print("a ref from this address {}: {}".format(addr, i))
			if i.getReferenceType() == RefType.UNCONDITIONAL_CALL:
				unconditionalCallFromRefsCount += 1
		for i in getReferencesTo(addr):
			print("a ref to this address {}: {}".format(addr, i))
			if i.getReferenceType() == RefType.UNCONDITIONAL_CALL:
				unconditionalCallToRefsCount += 1

	print("Unconditional Call References from this function {}: {}".format(myFunc.getName(), unconditionalCallFromRefsCount))
	print("Unconditional Call References to this function {}: {}".format(myFunc.getName(), unconditionalCallToRefsCount))