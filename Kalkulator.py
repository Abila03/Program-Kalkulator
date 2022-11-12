

print('=' * 25)
print('Operasi Matematika')
print('  1. Penjumlahan  [+]')
print('  2. Pengurangan  [-]')
print('  3. Perkalian    [*]')
print('  4. Pembagian    [/]')
print('=' * 25)

operasi = input('Pilih operasi (1/2/3/4): ')
bilangan_1 = float(input('Masukkan bilangan pertama: '))
bilangan_2 = float(input('Masukkan bilangan kedua: '))


if operasi == '1':
  hasil = bilangan_1 + bilangan_2
  print(f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}')
elif operasi == '2':
  hasil = bilangan_1 - bilangan_2
  print(f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}')
elif operasi == '3':
  hasil = bilangan_1 * bilangan_2
  print(f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}')
elif operasi == '4':
    if bilangan_2==0:
        print("Tidak bisa dibagi 0")
    else:
        hasil = bilangan_1 / bilangan_2
        print(f'Hasil operasi dari {bilangan_1} : {bilangan_2} = {hasil}')
else:
  print('Tidak valid')