#awal = A
#tujuan = G
#jalur

peta1 =  {'A':set(['B']),
         'B':set(['C','A']),
         'C':set(['B','I','H','D']),
         'D':set(['C','E','H','F']),
         'E':set(['D']),
         'F':set(['D','G']),
         'G':set(['F','H']),
         'H':set(['D','C','G','L']),
         'I':set(['C','J','K']),
         'J':set(['I']),
         'K':set(['L','I']),
         'L':set(['K','H'])}

def bfs(graf, mulai, tujuan):
    queue = [[mulai]]
    visited = set()
    print('Visited = ',visited)
    while queue:     
        # masukkan antrian paling depan ke variabel jalur
        jalur = queue.pop(0)
        print('Jalur = ',jalur)
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
                jalur_baru.append(cabang)#update/tambah isi jalur_baru dengan cabang
                print('jalur baru 2 = ',jalur_baru)
                queue.append(jalur_baru) #update/tambah queue dengan jalur_baru
                print('queue = ',queue)
                i=i+1
            # tandai state yang sudah dikunjungi sebagai visited
            visited.add(state)

        #cek isi antrian
        isi = len(queue)
        if isi == 0:
            print("Tidak ditemukan")

print(bfs(peta1,'A','D'))
