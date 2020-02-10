# CALCULATING PRESSURE DROP
# condition: RADIAL, TRANSIENT flow, and SLIGHTLY COMPRESSIBLE fluid
# Craft & Hawkins, 1959

# initialize Python library
import math
import matplotlib.pyplot as plt

# initialize empty array
p_drop = []
x = []
E = []

t = []
r = []

pi = float(2500)
q = float(300)
B = float(1.32)
mu = float(0.44)
k = float(25)
h = float(45)
c = float(18E-6)
phi = float(0.16)

def x_func(phi, mu, c, r, k, t):
	return round(float(phi * mu * c * r**2 / (0.00105 * k * t * 24)), 10)

def E_func(x, approx = 100):
	sum = math.log(-1 * x)

	if (-1 * x <= 10):
		for i in range(1,  approx + 1):
			sum += (math.pow(-1 * x, i) * math.pow(-1, i) / (i * math.factorial(i)))
	elif (-1 * x > 10):
		sum += 0
	else:
		sum += 0.577

	return round(-1 * sum, 10)

def PressureDrop(pi, q, mu, B, k, h, E):
	return round(pi - (70.6 * q * mu * B / (k * h) * E), 10)

nt = int(input('masukkan banyak t: '))

for i in range(0, nt):
	t.append(float(input('masukkan nilai t ke-' + str(i + 1) + ': ')))

nr = int(input('masukkan banyak r: '))

for i in range(0, nr):
	r.append(float(input('masukkan nilai t ke-' + str(i + 1) + ': ')))

# print(nr)


for i in range(0, nt):
	# init empty list for pressure drop and x for integral function
	p_drop.append([])
	x.append([])
	E.append([])

	# filling the x value for integral function
	for j in range(0, nr):
		x[i].append(x_func(phi, mu, c, r[j], k, t[i]))
		E[i].append(E_func(-1 * x[i][j]))
		p_drop[i].append(PressureDrop(pi, q, mu, B, k, h, E[i][j]))
		print(t[i], r[j], x[i][j], E[i][j], p_drop[i][j])

# for i in range(0, nt):
# 	row = ""
# 	for j in range(0, nt):
# 		row += str(x[i][j]) + " "
# 	print(row)

# print()

# for i in range(0, nt):
# 	row = ""
# 	for j in range(0, nr):
# 		row += str(E[i][j]) + " "
# 	print(row)

# print()

# for i in range(0, nt):
# 	row = ""
# 	for j in range(0, nr):
# 		row += str(p_drop[i][j]) + " "
# 	print(row)

fig = plt.figure()

ax = fig.add_subplot(111)

for i in range(0, nt):
	ax.scatter(r, p_drop[i], label="t = " + str(t[i]) + " days")

plt.legend()
plt.show()