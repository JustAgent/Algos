def rabin_karp(pattern, txt, prime):
	M = len(pattern)
	N = len(txt)
	i = 0
	j = 0
	p = 0 
	t = 0 
	h = 1

	for i in range(M-1):
		h = (h * d)% prime

	
	for i in range(M):
		p = (d * p + ord(pattern[i]))% prime
		t = (d * t + ord(txt[i]))% prime

	for i in range(N-M + 1):
		if p == t:
			for j in range(M):
				if txt[i + j] != pattern[j]:
					break

			j+= 1
			if j == M:
				print(str(i+1))

		if i < N-M:
			t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% prime

			
			if t < 0:
				t = t + prime


with open("input.txt", "r") as input_file:
	pattern = input_file.readline().strip()
	text = input_file.readline()

d = 256
prime = 1000000009 
rabin_karp(pattern, text, prime)

