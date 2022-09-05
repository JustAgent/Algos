def rabin_karp(pat, txt, q):
	M = len(pat)
	N = len(txt)
	i = 0
	j = 0
	p = 0 
	t = 0 
	h = 1

	for i in range(M-1):
		h = (h * d)% q

	
	for i in range(M):
		p = (d * p + ord(pat[i]))% q
		t = (d * t + ord(txt[i]))% q

	for i in range(N-M + 1):
		if p == t:
			for j in range(M):
				if txt[i + j] != pat[j]:
					break

			j+= 1
			if j == M:
				print(str(i+1))

		if i < N-M:
			t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q

			
			if t < 0:
				t = t + q


with open("input.txt", "r") as input_file:
	pattern = input_file.readline().strip()
	text = input_file.readline()

d = 256
q = 1000000009 
rabin_karp(pattern, text, q)

