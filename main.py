from UNION import jumlahKolomUnion, tipeDataKolom
from libs import welcome

pilihan_user = welcome()

if pilihan_user == 1:
    jumlahKolomUnion()
elif pilihan_user == 2:
    tipeDataKolom()