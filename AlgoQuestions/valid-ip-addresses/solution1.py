def validIPAddresses(string, numberOfBlocks=4):
	if numberOfBlocks == 1:
		return [string] if IsValidIPAddress(string) else []

	ipAddress = []

	for prefixSize in range(1, 3+1):
		if prefixSize >= (len(string)):
			continue

		prefix, suffix = string[:prefixSize], string[prefixSize:]
		if not IsValidIPAddress(prefix):
			continue

		smallerIPAddress = validIPAddresses(suffix, numberOfBlocks-1)

		for smallIPAddress in smallerIPAddress:
			ipAddress.append(prefix + "." + smallIPAddress)

	return ipAddress


def IsValidIPAddress(String):
	stringAsInt = int(String)
	if stringAsInt > 255:
		return False
	return len(String) == len(str(stringAsInt))


string = "1921680"
print(validIPAddresses(string))
