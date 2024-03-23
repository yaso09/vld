import os, sys, requests

print("""
    Veledd CLI 1.0.0
    Daha fazla bilgi için `-y` veya `yardım` yazın
""")

param = sys.argv[1]

if not param: os._exit(0)

if param == "kur" or "-k":
    try:
        res = requests.get(
            "https://raw.githubusercontent.com/yaso09/vld/main/packages/{}.py".format(sys.argv[2])
        )
        if res: eval(res.content)
        else: print("""
    Lütfen geçerli bir paket adı girin
        """)
    except IndexError: print("""
    Lütfen paket adı girin
    """)
elif param == "yardım" or "-y":
    print("""
    KOMUT\tKULLANIM\tÖRNEK

    kur     (-k)\tPaketi kur\tvld -k disp
    yardım  (-y)\tYardım al\tvld -y

    Github deposu: https://github.com/yaso09/vld
    """)



