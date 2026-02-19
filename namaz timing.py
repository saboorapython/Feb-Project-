def fajr(time,salah):
    print(f"{salah} Timings i.e {time}! Offer prayers!")
def zuhar(time,salah):
    print(f"{salah} Timings i.e {time}! Offer prayers!")
def asar(time,salah):
    print(f"{salah} Timings i.e {time}! Offer prayers!")
def magrib(time,salah):
    print(f"{salah} Timings i.e {time}! Offer prayers!")
def isha(time,salah):
    print(f"{salah} Timings i.e {time}! Offer prayers!")
    
time=int(input("Whats your time now? (0-24):"))

if time<=4:
    salah="Zuhar"
    zuhar(time,salah)
elif time<=6:
    salah="Asar"
    asr(time,salah)
elif time<=7:
    salah="Magrib"
    magrib(time,salah)
elif time<=16:
    salah="isha"
    isha(time,salah)
elif time<=19:
    salah="fajr"
    fajr(time,salah)
else:
    print("Invalid time error")