# CALCULATING Z-FACTOR
# using virial coefficient EOS of Van-der-Waals equation

## initialize Python library
import math

## initialize chemical properties
chem_name = ["CH4", "C2H6", "C3H8", "C4H10", "C5H12", "C6H14", "C7H16", "CO2", "H2S", "N2"]		# chemical name
mol = []																						# mol percentage
Tc = [343.33, 549.92, 666.06, 765.62, 845.8, 913.6, 972.7, 547.91, 672.45, 227.49]				# critical temperature for chemicals
Pc = [866.4, 706.5, 615.0, 550.8, 468.6, 436.9, 396.8, 1071, 1300, 493.1]						# critical pressure for chemicals
acc_factor = [0.0104, 0.0879, 0.1522, 0.1995, 0.2514, 0.2994, 0.3494, 0.2997, 0.0948, 0.0372]	# accentric factor

## define functions
def B0(T, Tc):
	return (0.083 - (0.422 / math.pow(T / Tc, 1.6)))

def B1(T, Tc):
	return (0.139 - (0.172 / math.pow(T / Tc, 4.2)))

def B(T, Tc, Pc, acc_factor):
	return Tc / Pc * (B0(T, Tc) + (acc_factor * B1(T, Tc)))

## receiving input
P = float(input("masukkan nilai tekanan P (dalam psia): "))		# pressure (psia)
T = float(input("masukkan nilai temperatur T (dalam oR): "))	# temperature (oR)

sum = 0																							# sum for normalization

for i in range(len(chem_name)):
	mol.append(float(input("masukkan nilai persen mol utk " + chem_name[i] + ": ")))
	sum += mol[i]

if (sum != 100):
	print("HASIL NORMALISASI:")
	for i in range(len(chem_name)):
		mol[i] = round(mol[i] / sum * 100, 2)
		print(chem_name[i] + ": " + str(mol[i]) + "%")	


## processing
z = 1			# init'd z-factor
x = P / T	# init'd reciproc. volume (1/V)
for i in range(0, len(chem_name)):
	z += B(T, Tc[i], Pc[i], acc_factor[i]) * math.pow(x, i+1)

print(z)