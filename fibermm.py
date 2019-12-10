import time
tid=0.5
tid2=4
def udregnmm():

    konnektering = 0.5 #db
    splidsning = 0.1 #db 1 pr 4km # (km/4)*0.1=
    smfiber1310 = 0.35 #db/km
    smfiber1550 = 0.2 #db/km
    mmfiber850 = 2.2 #db/km
    mmfiber1300 = 0.6 #db/km
    sikkerhedsmargin = 1 #pr 10km
    fastsikkerhedmargin = 3 #fast værdi
    reperarion = 0.5 #fast værdi

    taller=2

    time.sleep(tid)

    print("")
    print("Du har valgt Multi Mode Fiber")
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
    print("Udregningerne på Mulkti Mode er lavet ud fra worst case")
    print("- Attenauation at 850nm 2,2dB/km")
    print("- Attenauation at 1500nm 0,6dB/km")
    print("")

    time.sleep(tid)

    km = float(input("Indtast tallet for km: "))
    splidsninger = int(input("Indtast antal forventet splidsninger: "))
    konnekteringer = int(input("Indtast antal forventet konnekteringer: "))

    kmmmfiber850 = km*mmfiber850
    kmmmfiber1300 = km*mmfiber1300
    #print("kmmm850", kmmmfiber850)
    #print("kmmm1300", kmmmfiber1300)

    splidsningmm850 = km/4*0.1
    splidsningmm1300 = km/4*0.1
    #print("splids850", splidsningmm850)
    #print("splids1300", splidsningmm1300)

    konnekteringmm850 = konnekteringer*0.5
    konnekteringmm1300 = konnekteringer*0.5
    #print("Kone850", konnekteringmm850)
    #print("Kone1300", konnekteringmm1300)

    sikmargin = km/10
    #print("sikmargin", sikmargin)

    fast_værdi = reperarion + fastsikkerhedmargin
    #print("fast_værdi", fast_værdi)

    linkmmfiber850 = konnekteringmm850+splidsningmm850+kmmmfiber850+sikmargin+fast_værdi
    #print("links850", linkmmfiber850)

    linkmmfiber1300 = konnekteringmm1300+splidsningmm1300+kmmmfiber1300+sikmargin+fast_værdi
    #print("links1300", linkmmfiber1300)

    time.sleep(tid)

    print("")
    print("Ved brug af MM850 skal den valgte mediekonverter understøtte ", linkmmfiber850,"dB")
    print("Ved brug af MM1500 skal den valgte mediekonverter understøtte ", linkmmfiber1300,"dB")
    print("")

    time.sleep(tid2)
