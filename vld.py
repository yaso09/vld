import os, sys, requests

print("""
    Veledd CLI 1.0.0
    Daha fazla bilgi için `-y` veya `yardım` yazın
""")

if not len(sys.argv) > 1: os._exit(0)

param = sys.argv[1]

if not param: os._exit(0)

if param == "çalıştır" or param == "-ç":
    try:
        res = requests.get(
            "https://raw.githubusercontent.com/yaso09/vld/main/packages/{}.py".format(sys.argv[2])
        )
        if res:
            f = open("run.py", "w")
            f.write(res.text)
            f.close()
            os.system("python run.py")
            os.remove("run.py")
        else: print("""
    Lütfen geçerli bir paket adı girin
        """)
    except IndexError: print("""
    Lütfen paket adı girin
    """)
elif param == "listele" or param == "-l":
    url = "https://api.github.com/repos/yaso09/vld/contents/packages"
    res = requests.get(url)
    files = res.json
    print("""
    PAKET ADI
    """)
    for file in files:
        print("""
    {}
        """.format(file["name"]))
elif param == "yardım" or param == "-y":
    print("""
    KOMUT\tKULLANIM\tÖRNEK

    çalıştır    (-ç)\tPaketi kur\tvld -k disp
    listele     (-l)\tÇevrimiçi paketleri listele\tvld -l
    yardım      (-y)\tYardım al\tvld -y\n

    Github deposu: https://github.com/yaso09/vld
    """)
else: print("""
    Bilinmeyen komut
""")

