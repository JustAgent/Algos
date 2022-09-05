import random

def RabinKarp(text, pattern):
	p = 1000000009
	x = random.randint(1, p - 1)

	result = []
	# pHash = PolyHash(P, p, x)

	H = PrecomputeHashes(text, len(pattern), p, x)

	for i in range(0, len(text) - len(pattern)):
		if pHash != H[i]:
			continue

		if text[i:i+len(pattern)] == pattern:
			result.append(i)

	return result

def PrecomputeHashes(text, pattern_length, p, x):
	H = [0 for _ in range(len(text) - pattern_length + 1)]

	S = text[len(text) - pattern_length:len(text)]
	# H[len(text) - pattern_length] = PolyHash(S,p,x)
	y = 1

	for i in range(1, pattern_length):
		y = (y * x) % p

	for i in range(len(text) - pattern_length - 1, -1, -1):
		H[i] = (x * H[i + 1] + text[i] - y * text[i + pattern_length]) % p

	return H

with open("input.txt", "r") as input_file:
	pattern = input_file.readline().strip()
	text = input_file.readline()

result = RabinKarp(text, pattern)
print(result)

with open("output.txt", "w") as output_file:
	output_file.write(str(len(result)) + "\n")

	output_indeces = ""
	for index in result:
		output_indeces += str(index + 1) + " "
	output_file.write(output_indeces)

	