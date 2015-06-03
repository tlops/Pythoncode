def removespec(johan):
        specialChar = ["/", "(", ")", "%", "'", "?", "[", "]", "!", ":", ";", ",", ".", "-", "_", '"']
        for c in specialChar:
                if c in johan:
                        johan = johan.replace(c,"")
        for x in specialChar:
                if x in johan:
                        return johan.replace(x,"")
                else:
                        return johan



pase = {}
fhandler =open('aohf.txt')
count = 0
for lines in fhandler:
	count +=1
	lines = lines.rstrip()
	words = lines.split()
	for word in words:
		#if word ==[]: continue
		reg = removespec(word)
		if word not in pase:
			pase[reg] = 1
		else:
			pase[reg] +=1
		#pass

new_list=[]
for key,value in pase.items(): # Har skapar vi annu en loop som Lagger till ett vardena i nyckeln.
		new_list.append((value, key)) # Printing out the value of
new_list.sort(reverse=False)
for elements in new_list:
	print "{} {} ".format(elements[0],elements[1])
print "\nThese number of line ", count




"""def removespec(johan):
	specialChar = ["/", "(", ")", "%", "'", "?", "[", "]", "!", ":", ";", ",", ".", "-", "_", '"']
	for c in specialChar:
		if c in johan:
			johan = johan.replace(c,"")
	for x in specialChar:
		if x in johan:
			return johan.replace(x,"")
		else:
			return johan"""
