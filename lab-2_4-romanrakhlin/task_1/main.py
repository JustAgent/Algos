def KMPSearch():
    lps = [0] * len(pattern)
    j = 0
 
    computeLPSArray(lps)
 
    i = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
 
        if j == len(pattern):
        	result.append(i - j)
        	j = lps[j-1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
 
def computeLPSArray(lps):
	prev_lps = 0

	lps[0]
	i = 1

	while i < len(pattern):
		if pattern[i]== pattern[prev_lps]:
			prev_lps += 1
			lps[i] = prev_lps
			i += 1
		else:
			if prev_lps != 0:
				prev_lps = lps[prev_lps-1]
			else:
				lps[i] = 0
				i += 1

with open("input.txt", "r") as input_file:
	pattern = input_file.readline().strip()
	text = input_file.readline()

result = []
KMPSearch()

with open("output.txt", "w") as output_file:
	output_file.write(str(len(result)) + "\n")

	output_indeces = ""
	for index in result:
		output_indeces += str(index + 1) + " "
	output_file.write(output_indeces)


