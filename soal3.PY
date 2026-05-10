fname = input("Masukkan nama file : ")

try:
    fhand = open(fname)
except:
    print("File tidak bisa dibuka:", fname)
    exit()

counts = {}

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

print(counts)


