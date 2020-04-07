for number in range(1, 21):
	print(number)
	
ten = list(range(1, 11))
for n in ten:
	print(n)
	
hundred = range(1, 101)
for h in hundred:
	print(h)
	
million = list(range(1, 1000001))
print(min(million))
print(max(million))
print(sum(million))

for n in range(1, 21, 2):
	print(n)
	
for n in range(3, 31, 3):
	print(n)
	
for n in range(1, 11):
	print(n ** 3)
	
cubes = list(range(1, 11))
empty_cubes = []
for c in cubes:
	empty_cubes.append(c ** 3)
print(empty_cubes)


