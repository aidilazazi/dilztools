import pyfiglet

def tools():
    tools = ["PENDETEKSI JUMLAH KOLOM UNION", "PENDETEKSI STRING PADA KOLOM UNION"]

    return tools

def welcome():
    from libs import tools
    tools = tools()
    banner = pyfiglet.figlet_format("DILZTOOLS")
    ucapan = "SELAMAT DATANG, silahkan pilih tools yang kamu inginkan?\n"
    pilihan = f"TOOLS:\n1. {tools[0]} \n2. {tools[1]}\n"

    print(banner)
    print(ucapan)
    print(pilihan)

    pilihan_user = int(input(": "))
    print("\n\n")

    return pilihan_user