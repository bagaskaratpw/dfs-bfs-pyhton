#contoh peta 
peta =  {'A':set(['B']),
         'B':set(['A','C']),
         'C':set(['B','D','H','I']),
         'D':set(['C','E','F','H']),
         'E':set(['D']),
         'F':set(['D','G']),
         'G':set(['F','H']),
         'H':set(['D','C','G','L']),
         'I':set(['C','J','K']),
         'J':set(['I']),
         'K':set(['L','I']),
         'L':set(['K','H'])}
   

def dfs(graf, mulai, tujuan):
    stack = [[mulai]]
    visited = set()
    print("visited = " ,visited)

    while stack:
        #hitung panjang tumpukan dan masukkan ke variabel panjang_tumpukan
        panjang_tumpukan = len(stack)-1
        # masukkan tumpukan palinif state == tujuan:g atas ke variabel jalur
        jalur = stack.pop(panjang_tumpukan)
        print("jalur = ",jalur)
        # simpan node yang dipilih ke variabel state, misal jalur = C,B maka simpan B ke variabel state
        state = jalur[-1]
        print('state = ',state)
        i = 1;
        # cek state apakah sama dengan tujuan, jika ya maka return jalur
        if state == tujuan:
            return jalur
        # jika state tidak sama dengan tujuan, maka cek apakah state tidak ada di visited
        elif state not in visited:
            # jika state tidak ada di visited maka cek cabang
            for cabang in graf.get(state, []): #cek semua cabang dari state
                print('step : ',i)
                jalur_baru = list(jalur) #masukkan isi dari variabel jalur ke variabel jalur_baru
                print('jalur baru 1 = ',jalur_baru)
                jalur_baru.append(cabang) #update/tambah isi jalur_baru dengan cabang
                print('jalur baru 2 = ',jalur_baru)
                stack.append(jalur_baru) #update/tambah queue dengan jalur_baru
                print('STACK = ',stack)
            # tandai state yang sudah dikunjungi sebagai visited
            visited.add(state)


        #cek isi tumpukan
        isi = len(stack)
        if isi == 0:
            print("Tidak ditemukan")

print(dfs(peta,'A','D'))
