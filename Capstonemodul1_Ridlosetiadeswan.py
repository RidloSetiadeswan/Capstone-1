inventoryrental= [{
    'mobil': 'xenia',
    'jumlah unit': 5,
    'harga sewa' : 350000
},{
     'mobil': 'ayla',
    'jumlah unit': 3,
    'harga sewa' : 250000
},{
     'mobil': 'terios',
    'jumlah unit': 4,
    'harga sewa' : 400000
}]

                
def melihatjmlunit () :
    print ('\t Rincian Armada Rental Anda')
    print ('Kendaraan\t| jumlahunit\t| Harga Sewa')
    for x in range(len(inventoryrental)):
        print(' {}\t\t| {}\t\t| {}'.format(inventoryrental[x]['mobil'],inventoryrental[x]['jumlah unit'],inventoryrental[x]['harga sewa']))

def menambahunitrental() :
        masukan=str(input('masukan nama unit :'))
        for i in range(len(inventoryrental)) :
            if (masukan==inventoryrental[i]['mobil']) :
                print('''Unit sudah tersedia
                 Nama Kendaraan\t| jumlah unit\t| Harga Sewa
                 {}\t\t| {}\t\t| {}'''.format(inventoryrental[i]['mobil'],inventoryrental[i]['jumlah unit'],inventoryrental[i]['harga sewa']))
                break

            elif i==(len(inventoryrental)-1) :
                fixtambahunit= input('unit belum tersedia apakah anda akan menambah unit baru (ya/tidak)?')
                if (fixtambahunit=='ya') :
                    tambahunit ()
                    break
                else :
                    print('kembali ke menu sebelumnya')
                    break

def tambahunit () :
    namaunit = input('Masukkan Nama Kendaraan : ')
    jumlunit = int(input('Masukkan jumlah unit : '))
    hargasewa = int(input('Masukkan Harga sewa : '))
    print('apakah data tersebut ingin di simpan? \n mobil \t:',namaunit,'\n jumlah unit \t:',jumlunit,'\n harga sewa \t:',hargasewa)
    y=input('ya/tidak :')
    if y== 'ya' :
            inventoryrental.append({
                'mobil': namaunit,
                'jumlah unit': jumlunit,
                'harga sewa': hargasewa
                })
            print( 'selamat atas unit rental terbaru anda!')
            melihatjmlunit()
    else :
        print('Data tidak berhasil disimpan')

def ubahunit () :
        pencarian=str(input('selamat datang di menu ubah data ! \n\n silahkan masukan nama unit yang ingin diubah :'))
        for i in range(len(inventoryrental)) :
            if (pencarian==inventoryrental[i]['mobil']) :
                print('''Unit ditemukan
                Nama Kendaraan\t| jumlah unit\t| Harga Sewa
                {}\t\t| {}\t\t| {}'''.format(inventoryrental[i]['mobil'],inventoryrental[i]['jumlah unit'],inventoryrental[i]['harga sewa']))
                ubah=input('lanjut ubah data (ya/tidak) ? :')
                if ubah == 'ya':
                    while True:
                        pilih=input('''Pilih menu data yang akan di ubah :
                        1. mengubah nama mobil
                        2. mengubah jumlah unit
                        3. mengubah harga sewa
                        4. kembali ke menu sebelumnya
                        
                        masukan angka menu yang diinginkan :''')
                        if pilih == '1' :
                            t=input('masukan nama mobil yang baru:')
                            inventoryrental[i]['mobil']=t
                            print('''nama unit telah berhasil dirubah
                                Nama Kendaraan\t| jumlah unit\t| Harga Sewa
                                {}\t\t| {}\t\t| {}'''.format(inventoryrental[i]['mobil'],inventoryrental[i]['jumlah unit'],inventoryrental[i]['harga sewa']))
                        elif pilih=='2' :
                            t=int(input('masukan jumlah unit yang baru :'))
                            inventoryrental[i]['jumlah unit']=t
                            print('''jumlah unit telah berhasil dirubah
                                Nama Kendaraan\t| jumlah unit\t| Harga Sewa
                                {}\t\t| {}\t\t| {}'''.format(inventoryrental[i]['mobil'],inventoryrental[i]['jumlah unit'],inventoryrental[i]['harga sewa']))
                        elif pilih=='3' :
                            t=int(input('masukan Harga sewa yang baru :'))
                            inventoryrental[i]['harga sewa']=t
                            print('''Harga sewa telah berhasil dirubah
                                Nama Kendaraan\t| jumlah unit\t| Harga Sewa
                                {}\t\t| {}\t\t| {}'''.format(inventoryrental[i]['mobil'],inventoryrental[i]['jumlah unit'],inventoryrental[i]['harga sewa']))
                        elif pilih=='4' :
                            break
                else :
                    break
            elif i==(len(inventoryrental)-1) :
                print('data tidak ditemukan')
                break

def hapusdata() :
    while True:
        pilih=input('''selamat datang di menu hapus data :
                    
            1. menghapus satu set data yang ada
            2. kembali kemenu sebelumnya

            masukan angka menu yang diinginkan :''')
        if pilih == '1' :
            pencarian=str(input('selamat datang di menu ubah data ! \n\n silahkan masukan nama unit yang ingin dihapus :'))
            for i in range(len(inventoryrental)) :
                if (pencarian==inventoryrental[i]['mobil']) :
                    print('''Unit ditemukan
                    Nama Kendaraan\t| jumlah unit\t| Harga Sewa
                    {}\t\t| {}\t\t| {}'''.format(inventoryrental[i]['mobil'],inventoryrental[i]['jumlah unit'],inventoryrental[i]['harga sewa']))                
                    t=input('''Apakah anada yakin untuk menghapus? (ya/tidak) :''')
                    if t =='ya' :
                        del inventoryrental[i]
                        print('!!! Data Berhasil dihapus !!!')
                        melihatjmlunit()
                        break
        elif pilih=='2' :
            break
def database () :
    while True :
        pilihanMenux = input('''
        silahkan pilih menu sesuai kebutuhan anda :

          1. seluruh data unit rental anda
          2. mencari data unit tertentu
          3. kembali kemenu sebelumnya

          Masukkan angka Menu yang ingin dijalankan :''')

        if(pilihanMenux == '1') :
            melihatjmlunit()
        elif(pilihanMenux == '2') :
            menambahunitrental()
        elif(pilihanMenux == '3') :
            break
    
def menambahdata () :
    while True :
        Menutambahdata =input(''' 
            Selamat datang di menu tambah data
        
            1. Tambah Data
            2. kembali ke menu sebelumnya

            Masukkan angka Menu yang ingin dijalankan : ''')

        if (Menutambahdata=='1') :
            menambahunitrental()
        elif (Menutambahdata=='2') :
            break

while True :
    pilihanMenu = input('''
        Selamat Datang di database center Ridlo Rentcar

        List Menu :
        1. Menampilkan  data 
        2. Menambah data 
        3. Merubah data
        4. Menghapus data
        5. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
        database()
    elif(pilihanMenu == '2') :
        menambahdata()
    elif(pilihanMenu == '3') :
        ubahunit()
    elif(pilihanMenu == '4') :
        hapusdata()
    elif(pilihanMenu == '5') :
        break
    else :
        print ('input yang anda masukan salah')