import math

# fungsi korelasi Dranchuk-Abou Kaseem (z fungsi Rhor)
def DAK(Pr, Tr, z):
    Rhor = 0.27 * Pr / (z * Tr)     # reduced density
    
    # konstanta
    R1 = 0.3265 + (-1.0700 / Tr) + (-0.5339 / Tr**3) + (0.01569 / Tr**4) + (-0.05165 / Tr**5)
    R2 = 0.27 * Pr / Tr
    R3 = 0.5475 + (-0.7361 / Tr) + (0.1844 / Tr**2)
    R4 = 0.1056 * ((-0.7361 / Tr) + (0.1844 / Tr**2))
    R5 = 0.6134 * Rhor**2 / Tr**3

    # output: nilai z sebagai fungsi Rhor f(Rhor)
    return R1 * Rhor + R3 * Rhor**2 - R4 * Rhor**5 + (R5 * (1 + 0.7210 * Rhor**2)) * math.exp(-0.7210 * Rhor**2) + 1 - z

# fungsi turunan Dranchuk-Abou Kaseem
def dDAK(Pr, Tr, z, deltaZ):
    """ mencari nilai turunan dengan menggunakan pendekatan limit """
    return (DAK(Pr, Tr, z + deltaZ) - DAK(Pr, Tr, z)) / deltaZ  # Mengembalikan nilai turunan

# fungsi metode Newton-Raphson
def newton_raphson(z, Pr, Tr, miter, epsilon):
    """ mencari solusi nilai z dengan metode Newton Rhapson """
    i = 0           
    z0 = 0
    deltaZ = 0.001

    # algoritma Newton-Raphson
    while (abs(z - z0) > epsilon and i < miter):
        z0 = z
        z = z - (DAK(Pr, Tr, z) / dDAK(Pr, Tr, z, deltaZ))
        i += 1

    # mengembalikan nilai z
    return float(round(z, 3)) 

z = float(input("masukkan nilai z tebakan: "))
Pr = float(input("masukkan nilai Pr: "))
Tr = float(input("masukan nilai Tr: "))
epsilon = float(input("masukan nilai galat: "))
MI = int(input("masukan jumlah iterasi: "))  # Iterasi maksimum

print("hasil perhitungan z: " + str(newton_raphson(z, Pr, Tr, MI, epsilon)))