import time
tid=0.5
tid2=4
def udregnsm():

    konnektering = 0.5 #db
    splidsning = 0.1 #db 1 pr 4km # (km/4)*0.1=
    smfiber1310 = 0.35 #db/km
    smfiber1550 = 0.2 #db/km
    mmfiber850 = 2.2 #db/km
    mmfiber1300 = 0.6 #db/km
    sikkerhedsmargin = 1 #pr 10km
    fastsikkerhedmargin = 3 #fast værdi
    reperarion = 0.5 #fast værdi

    taller=1
    time.sleep(tid)
    print("")
    print("Du har valgt Single Mode Fiber")
    print("Udfyld felterne her under med værdier")
    print(" ")
    print("Som standart er der lagt følgende ind i udregningen")
    print("- Reperation: 1 stk")
    print("- Sikkerhedsmargin")
    print(" ")
    print("Følgende værdier er sat til")
    print("- Sikkerhedsmargin 3dB")
    print("- Konnekteringer 0,5dB")
    print("- Splidsning 0,1dB")
    print("- Reperation 0,5dB")
    print("")
    print("Udregningerne på Single Mode er lavet ud fra worst case")
    print("- Attenauation at 1310nm 0,35dB/km")
    print("- Attenauation at 1550nm 0,21dB/km")
    print("")
    time.sleep(tid)
    km = float(input("Indtast tallet for km: "))
    splidsninger = int(input("Indtast antal forventet splidsninger: "))
    konnekteringer = int(input("Indtast antal forventet konnekteringer: "))
    time.sleep(tid)

    kmsmfiber1310 = km*smfiber1310
    kmsmfiber1550 = km*smfiber1550
    #print("kmsm1312", kmsmfiber1310)
    #print("kmsm1550", kmsmfiber1550)

    splidsningsm1310 = km/4*0.1
    splidsningsm1550 = km/4*0.1
    #print("splids1310", splidsningsm1310)
    #print("splids1550", splidsningsm1550)

    konnekteringsm1310 = konnekteringer*0.5
    konnekteringsm1550 = konnekteringer*0.5
    #print("Kone1310", konnekteringsm1310)
    #print("Kone1550", konnekteringsm1550)

    sikmargin = km/10
    #print("sikmargin", sikmargin)

    fast_værdi = reperarion + fastsikkerhedmargin
    #print("fast_værdi", fast_værdi)

    linksmfiber1310 = konnekteringsm1310+splidsningsm1310+kmsmfiber1310+sikmargin+ fast_værdi
    #print("links1310", linksmfiber1310)

    linksmfiber1550 = konnekteringsm1550+splidsningsm1550+kmsmfiber1550+sikmargin+fast_værdi
    #print("links1550", linksmfiber1550)

    print("")
    print("Ved brug af SM1310 skal den valgte mediekonverter understøtte ", linksmfiber1310,"dB")
    print("Ved brug af SM1550 skal den valgte mediekonverter understøtte ", linksmfiber1550,"dB")
    print("")

    time.sleep(tid2)
