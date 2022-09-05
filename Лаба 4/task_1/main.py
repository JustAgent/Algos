def substring_search():
	arr = [0] * len(pattern)
	j = 0
 
	compute_array(arr)
 
	i = 0
	while i < len(text):
		if pattern[j] == text[i]:
			i += 1
			j += 1

		if j == len(pattern):
			result.append(i - j)
			j = arr[j-1]
		else:
			if i < len(text) and pattern[j] != text[i]:
				if j != 0:
					j = arr[j-1]
				else:
					i += 1
 
def compute_array(arr):
	prev_arr = 0

	arr[0]
	i = 1

	while i < len(pattern):
		if pattern[i]== pattern[prev_arr]:
			prev_arr += 1
			arr[i] = prev_arr
			i += 1
		else:
			if prev_arr != 0:
				prev_arr = arr[prev_arr-1]
			else:
				arr[i] = 0
				i += 1

with open("input.txt", "r") as input_file:
	pattern = input_file.readline().strip()
	text = input_file.readline()

result = []
substring_search()

with open("output.txt", "w") as output_file:
	output_file.write(str(len(result)) + "\n")

	output = ""
	for index in result:
		output += str(index + 1) + " "
	output_file.write(output)

substring_search()

