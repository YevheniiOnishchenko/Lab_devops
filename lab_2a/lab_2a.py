print("First const", True)
print("Second const", False)

print(ord('a'))
print(oct(8))

a = True
if a == True:
	print("a")
else:
	print("not a")

for i in range (5):
	print("I like devops")

l = ['a', 'b', 'c', 'd']
try:
	print(l[4])
except Exception as e:
	print(e)
finally:
	print("Point is done")

with open("README.md", "w") as f:
	f.write("some data")

calc = lambda a, b, c: a+c 
print(calc(4, '+', 67))
