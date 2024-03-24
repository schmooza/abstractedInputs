# functions to be abstracted
def adder(inputIs):
	# key 0
	inputIs = inputIs * 5
	return inputIs, "key 0"

def markup(inputIs):
	# key 1
	inputIs += 10
	return inputIs, "key 1"

def zipMethods(*args):
	# create a list of functions saved as arguments
	unpackList = list(args)
	print(unpackList)
	return unpackList

unpackList = zipMethods(adder, markup)

def makeDict (unpackList):
	my_dict = {}

	# uses enumerate to create a dictionary
	for index, element in enumerate(unpackList):
		my_dict[index] = element

	print(my_dict)
	return my_dict
# creates_a_dictionary_of_methods
cdm1 = makeDict(unpackList)


def useMethods(keyValue, cdm1):
	print(cdm1[keyValue],"it works")
	# instantiate the method
	methodIs = cdm1[keyValue]
	return methodIs


a1 = useMethods(0,cdm1)
a2 = useMethods(1,cdm1)

print(a1(5),a2(20))
