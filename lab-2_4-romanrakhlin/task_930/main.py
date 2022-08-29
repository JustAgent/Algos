with open("input.txt", "r") as input_file:
    dad = input_file.readline()
    mom = input_file.readline()

name = ""
commom = list(set(dad) & set(mom))

if len(commom) != 0:
    commom.sort()
    commom.reverse()

    while len(commom) != 0:
        length = min(dad.count(commom[0]), mom.count(commom[0]))
        name += commom[0] * length

        for _ in range(min(dad.count(commom[0]), mom.count(commom[0]))):
            dad = dad[dad.find(commom[0]) + 1:]
            mom = mom[mom.find(commom[0]) + 1:]

        commom.pop(0)

with open("output.txt", "w") as output_file:
    output_file.write(name)
        
