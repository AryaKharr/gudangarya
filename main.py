

kontak1 = {'nama' : 'Andi', 'HP': '19020133', 'Email': 'Andiprasetyo@gmail.com'}
kontak2 = {'nama' : 'Amad', 'HP': '19020133', 'Email': 'Andiprasetyo@gmail.com'}
kontak =  [kontak1, kontak2]
while True :
    print('\nMenu Kontak ')
    print('1. Melihat Semua Kontak ')
    print('2. Menambahkan Kontak Baru ')
    print('3. Menghapus Kontak ')
    print('4. Keluar Dari Kontak')

    pilihan = input('Masukkan pilihan menu kontak (1 - 4): ')
    
    if pilihan == '1':
        # Melihat semua kontak
        # kalau tidak ada nilainya maka nilainya false
        if kontak:
         for num, item in enumerate(kontak, start=1):
            print(f'\n{num}, {item ["nama"]} ({item["HP"]}, {item["Email"]})')
    elif pilihan == '2':
        # menambahkan kontak
        nama =input("Masukkan nama kontak yang baru: ")
        Hp = input("Masukkan no HP: ")
        Email = input("Masukkan email kontak yang baru: ")
        kontak_baru = {'nama': nama, 'HP' : Hp, 'Email' : Email}
        kontak.append(kontak_baru)
        print('Kontak baru berhasil di tambahkan ')
    elif pilihan == '3':
        if kontak:
         for num, item in enumerate(kontak, start=1):
          print(f'\n{num}, {item ["nama"]} ({item["HP"]}, {item["Email"]})')
        else:
            print('Kontak masih kosong ')
            continue
        
        i_hapus = int(input('Masukkan kontak yang ingin di hapus: '))
        # del untuk menghapus object
        del kontak[i_hapus-1]
        # -1 karena indeks di mulainya dari 0
        print('Kontak berhasil di hapus ')
        
    elif pilihan == '4':
        break
    else:
        print('Pilihan yang anda masukkan salah ')
    

