def fpb(a, b):
  if b == 0: 
    return a
  else: 
    return fpb(b, a % b)

def kpk(a, b):
  return a * b / fpb(a, b)

angka1=int(input('Masukkan angka pertama :'))
angka2=int(input('Masukkan angka kedua   :'))

print('FPB dari ',angka1,' dan ',angka2,' adalah ',fpb(angka1,angka2))
print('KPK dari ',angka1,' dan ',angka2,' adalah ',kpk(angka1,angka2))