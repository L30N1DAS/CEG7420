# Assignment 3: Conditional Jump From and To References for Function
# @category: assignment3_scripts
# @author: Anmol Saini

from ghidra.program.model.symbol import RefType

myFunc = getFunctionContaining(currentAddress)

if myFunc:
	print(myFunc.getName())
	fbody = myFunc.getBody()
	conditionalJumpFromRefsCount = 0
	conditionalJumpToRefsCount = 0

	for addr in fbody.getAddresses(True):
		for i in getReferencesFrom(addr):
			print("a ref from this address {}: {}".format(addr, i))
			if i.getReferenceType() == RefType.CONDITIONAL_JUMP:
				conditionalJumpFromRefsCount += 1
		for i in getReferencesTo(addr):
			print("a ref to this address {}: {}".format(addr, i))
			if i.getReferenceType() == RefType.CONDITIONAL_JUMP:
				conditionalJumpToRefsCount += 1

	print("Conditional Jump References from this function {}: {}".format(myFunc.getName(), conditionalJumpFromRefsCount))
	print("Conditional Jump References to this function {}: {}".format(myFunc.getName(), conditionalJumpToRefsCount))