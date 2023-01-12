def cek_bilangan(angka):
    list_bilangan = ['bulat']

    if angka < 0:
        list_bilangan.append('negatif')
    else:
        list_bilangan.append('cacah')
        if angka == 0:
            list_bilangan.append('nol')
        else:
            list_bilangan.append('asli')
            if angka %2 != 0:
                list_bilangan.append('ganjil')
                if angka > 1:
                    for i in range(2, angka):
                        if angka % i == 0:
                            list_bilangan.append('komposit')
                            break
                    else:
                        list_bilangan.append('prima')
                        
            else:
                list_bilangan.append('genap')
                for i in range(2, angka):
                    if angka % i == 0:
                        list_bilangan.append('komposit')
                        break
                else:
                    list_bilangan.append('prima')
    return list_bilangan

angka = int(input('Masukkan angka: '))
print(cek_bilangan(angka))