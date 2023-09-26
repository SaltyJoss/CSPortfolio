S1 = 113
S2 = 175
S3 = 12

S = S1 + S2 + S3
G = S / 24
L = (G % 1) * 12

print("Total amount of full groups is %.f" % G)
print("Total amount of students in the \"left over\" group is %.f" % L)
