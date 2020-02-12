import math

## initialize chemical properties
chem_name = ["CH4", "C2H6", "C3H8", "C4H10", "C5H12", "C6H14", "C7H16", "CO2", "H2S", "N2"]		# chemical name
mol = []																						# mol percentage
Tc = [343.33, 549.92, 666.06, 765.62, 845.8, 913.6, 972.7, 547.91, 672.45, 227.49]				# critical temperature for chemicals
Pc = [866.4, 706.5, 615.0, 550.8, 468.6, 436.9, 396.8, 1071, 1300, 493.1]						# critical pressure for chemicals
acc_factor = [0.0104, 0.0879, 0.1522, 0.1995, 0.2514, 0.2994, 0.3494, 0.2997, 0.0948, 0.0372]	# accentric factor

## define functions
def B0(Tr):
	return (0.083 - (0.422/math.pow(Tr, 1.6)))

def B1(Tr):
	return (0.139 - (0.172/math.pow(Tr, 4.2)))

def B(T, Tc, Pc, acc_factor):
	return Tc/Pc*(B0(T/Tc) + (acc_factor * B1(T/Tc)))

def f_T(z, P, T, Tc, Pc, acc_factor):
	zf = 1		# init'd z-factor
	x = P / T	# init'd reciproc. volume (1/V)
	for i in range(0, len(chem_name)):
		z += B(T, Tc[i], Pc[i], acc_factor[i]) * math.pow(x, i+1)

	return zf - z

def df_T(z, P, T, Tc, Pc, acc_factor, delta_z):
    return (f_T(z + delta_z, P, T, Tc, Pc, acc_factor) - f_T(z, P, T, Tc, Pc, acc_factor)) / delta_z  # Mengembalikan nilai turunan g(Z)

# fungsi metode Newton-Raphson
def newton_raphson(z, P, T, Tc, Pc, acc_factor, MI, epsilon):
    """ mencari solusi z dengan metode Newton-Raphson """
    m = 0
    z0 = 0
    delta_z = 0.001

    while (abs(z - z0) > epsilon and m < MI):
        z0 = z
        z = z - (f_T(z, P, T, Tc, Pc, acc_factor) / df_T(z, P, T, Tc, Pc, acc_factor, delta_z))
        m += 1

    return float(format(z, "0.6f")) # Mengembalikan nilai Z dengan 6 angka di belakang koma

## receiving input
P = float(input("masukkan nilai tekanan P (dalam psia): "))		# pressure (psia)
T = float(input("masukkan nilai temperatur T (dalam oR): "))	# temperature (oR)

sum = 0															# sum for normalization

for i in range(len(chem_name)):
	mol.append(float(input("masukkan nilai persen mol utk " + chem_name[i] + ": ")))
	sum += mol[i]

z = float(input("masukkan tebakan awal z: "))
epsilon = float(input("masukkan nilai galat: "))
MI = int(input("masukkan jumlah iterasi: "))

print(newton_raphson(z, P, T, Tc, Pc, acc_factor, MI, epsilon))