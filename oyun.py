print("*"*50,"\n\n X O X Oyununa Hoşgeldiniz...\n \n\n)
karar = "e"
while karar == "e" :
    while True :
        tablo = ["___","___","___","___","___","___","___","___","___"]
        yatay = 1
        dikey = 1
        print("\t\t",tablo[0],tablo[1],tablo[2],"\n\t\t",tablo[3],tablo[4],tablo[5],"\n\t\t",tablo[6],tablo[7],tablo[8],"\n")

        print("~~ 1. oyuncu (X) ~~")
        yatay = input("Soldan sağa [1,2,3] : ")
        while yatay != "1" and yatay != "2" and yatay != "3" and yatay != "!bilgi" :
            yatay = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nSoldan sağa [1,2,3] : ")
        if yatay == "!bilgi" :
            print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
            yatay = input("Soldan sağa [1,2,3] : ")
        dikey = input("Yukarıdan aşağıya [1,2,3] : ")
        while dikey != "1" and dikey != "2" and dikey != "3" and dikey != "!bilgi" :
            dikey = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nYukarıdan aşağıya [1,2,3] : ")
        if dikey == "!bilgi" :
            print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
            dikey = input("Yukarıdan aşağıya [1,2,3] : ")
        if dikey == "1" and yatay == "1" :
            tablo[0] = "_X_"
        elif dikey == "1" and yatay == "2" :
            tablo[1] = "_X_"
        elif dikey == "1" and yatay == "3" :
            tablo[2] = "_X_"
        elif dikey == "2" and yatay == "1" :
            tablo[3] = "_X_"
        elif dikey == "2" and yatay == "2" :
            tablo[4] = "_X_"
        elif dikey == "2" and yatay == "3" :
            tablo[5] = "_X_"
        elif dikey == "3" and yatay == "1" :
            tablo[6] = "_X_"
        elif dikey == "3" and yatay == "2" :
            tablo[7] = "_X_"
        elif dikey == "3" and yatay == "3" :
            tablo[8] = "_X_"
        print("\t\t",tablo[0],tablo[1],tablo[2],"\n\t\t",tablo[3],tablo[4],tablo[5],"\n\t\t",tablo[6],tablo[7],tablo[8],"\n")

        while True :
            yatay = input("Soldan sağa [1,2,3] : ")
            while yatay != "1" and yatay != "2" and yatay != "3" and yatay != "!bilgi" :
                yatay = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nSoldan sağa [1,2,3] : ")
            if yatay == "!bilgi" :
                print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
                yatay = input("Soldan sağa [1,2,3] : ")
            dikey = input("Yukarıdan aşağıya [1,2,3] : ")
            while dikey != "1" and dikey != "2" and dikey != "3" and dikey != "!bilgi" :
                dikey = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nYukarıdan aşağıya [1,2,3] : ")
            if dikey == "!bilgi" :
                print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
                dikey = input("Yukarıdan aşağıya [1,2,3] : ")
            if yatay == "1" and dikey == "1" and tablo[0] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "1" and tablo[1] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "1" and tablo[2] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "1" and dikey == "2" and tablo[3] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "2" and tablo[4] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "2" and tablo[5] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "1" and dikey == "3" and tablo[6] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "3" and tablo[7] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "3" and tablo[8] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            else :
                break
        if dikey == "1" and yatay == "1" :
            tablo[0] = "_O_"
        elif dikey == "1" and yatay == "2" :
            tablo[1] = "_O_"
        elif dikey == "1" and yatay == "3" :
            tablo[2] = "_O_"
        elif dikey == "2" and yatay == "1" :
            tablo[3] = "_O_"
        elif dikey == "2" and yatay == "2" :
            tablo[4] = "_O_"
        elif dikey == "2" and yatay == "3" :
            tablo[5] = "_O_"
        elif dikey == "3" and yatay == "1" :
            tablo[6] = "_O_"
        elif dikey == "3" and yatay == "2" :
            tablo[7] = "_O_"
        elif dikey == "3" and yatay == "3" :
            tablo[8] = "_O_"
        print("\t\t",tablo[0],tablo[1],tablo[2],"\n\t\t",tablo[3],tablo[4],tablo[5],"\n\t\t",tablo[6],tablo[7],tablo[8],"\n")

        print("~~ 1. oyuncu (X) ~~")
        while True :
            yatay = input("Soldan sağa [1,2,3] : ")
            while yatay != "1" and yatay != "2" and yatay != "3" and yatay != "!bilgi" :
                yatay = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nSoldan sağa [1,2,3] : ")
            if yatay == "!bilgi" :
                print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
                yatay = input("Soldan sağa [1,2,3] : ")
            dikey = input("Yukarıdan aşağıya [1,2,3] : ")
            while dikey != "1" and dikey != "2" and dikey != "3" and dikey != "!bilgi" :
                dikey = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nYukarıdan aşağıya [1,2,3] : ")
            if dikey == "!bilgi" :
                print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
                dikey = input("Yukarıdan aşağıya [1,2,3] : ")
            if yatay == "1" and dikey == "1" and tablo[0] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "1" and tablo[1] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "1" and tablo[2] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "1" and dikey == "2" and tablo[3] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "2" and tablo[4] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "2" and tablo[5] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "1" and dikey == "3" and tablo[6] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "3" and tablo[7] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "3" and tablo[8] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            else :
                break
        if dikey == "1" and yatay == "1" :
            tablo[0] = "_X_"
        elif dikey == "1" and yatay == "2" :
            tablo[1] = "_X_"
        elif dikey == "1" and yatay == "3" :
            tablo[2] = "_X_"
        elif dikey == "2" and yatay == "1" :
            tablo[3] = "_X_"
        elif dikey == "2" and yatay == "2" :
            tablo[4] = "_X_"
        elif dikey == "2" and yatay == "3" :
            tablo[5] = "_X_"
        elif dikey == "3" and yatay == "1" :
            tablo[6] = "_X_"
        elif dikey == "3" and yatay == "2" :
            tablo[7] = "_X_"
        elif dikey == "3" and yatay == "3" :
            tablo[8] = "_X_"
        print("\t\t",tablo[0],tablo[1],tablo[2],"\n\t\t",tablo[3],tablo[4],tablo[5],"\n\t\t",tablo[6],tablo[7],tablo[8],"\n")

        print("~~ 2. oyuncu (O) ~~")
        while True :
            yatay = input("Soldan sağa [1,2,3] : ")
            while yatay != "1" and yatay != "2" and yatay != "3" and yatay != "!bilgi" :
                yatay = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nSoldan sağa [1,2,3] : ")
            if yatay == "!bilgi" :
                print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
                yatay = input("Soldan sağa [1,2,3] : ")
            dikey = input("Yukarıdan aşağıya [1,2,3] : ")
            while dikey != "1" and dikey != "2" and dikey != "3" and dikey != "!bilgi" :
                dikey = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nYukarıdan aşağıya [1,2,3] : ")
            if dikey == "!bilgi" :
                print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
                dikey = input("Yukarıdan aşağıya [1,2,3] : ")
            if yatay == "1" and dikey == "1" and tablo[0] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "1" and tablo[1] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "1" and tablo[2] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "1" and dikey == "2" and tablo[3] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "2" and tablo[4] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "2" and tablo[5] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "1" and dikey == "3" and tablo[6] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "3" and tablo[7] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "3" and tablo[8] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            else :
                break
        if dikey == "1" and yatay == "1" :
            tablo[0] = "_O_"
        elif dikey == "1" and yatay == "2" :
            tablo[1] = "_O_"
        elif dikey == "1" and yatay == "3" :
            tablo[2] = "_O_"
        elif dikey == "2" and yatay == "1" :
            tablo[3] = "_O_"
        elif dikey == "2" and yatay == "2" :
            tablo[4] = "_O_"
        elif dikey == "2" and yatay == "3" :
            tablo[5] = "_O_"
        elif dikey == "3" and yatay == "1" :
            tablo[6] = "_O_"
        elif dikey == "3" and yatay == "2" :
            tablo[7] = "_O_"
        elif dikey == "3" and yatay == "3" :
            tablo[8] = "_O_"
        print("\t\t",tablo[0],tablo[1],tablo[2],"\n\t\t",tablo[3],tablo[4],tablo[5],"\n\t\t",tablo[6],tablo[7],tablo[8],"\n")
                #       ~~ Dabaddu Software @ 2020 Tüm Hakları Saklıdır ~~
        print("~~ 1. oyuncu (X) ~~")
        while True :
            yatay = input("Soldan sağa [1,2,3] : ")
            while yatay != "1" and yatay != "2" and yatay != "3" and yatay != "!bilgi" :
                yatay = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nSoldan sağa [1,2,3] : ")
            if yatay == "!bilgi" :
                print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
                yatay = input("Soldan sağa [1,2,3] : ")
            dikey = input("Yukarıdan aşağıya [1,2,3] : ")
            while dikey != "1" and dikey != "2" and dikey != "3" and dikey != "!bilgi" :
                dikey = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nYukarıdan aşağıya [1,2,3] : ")
            if dikey == "!bilgi" :
                print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
                dikey = input("Yukarıdan aşağıya [1,2,3] : ")
            if yatay == "1" and dikey == "1" and tablo[0] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "1" and tablo[1] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "1" and tablo[2] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "1" and dikey == "2" and tablo[3] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "2" and tablo[4] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "2" and tablo[5] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "1" and dikey == "3" and tablo[6] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "3" and tablo[7] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "3" and tablo[8] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            else :
                break
        if dikey == "1" and yatay == "1" :
            tablo[0] = "_X_"
        elif dikey == "1" and yatay == "2" :
            tablo[1] = "_X_"
        elif dikey == "1" and yatay == "3" :
            tablo[2] = "_X_"
        elif dikey == "2" and yatay == "1" :
            tablo[3] = "_X_"
        elif dikey == "2" and yatay == "2" :
            tablo[4] = "_X_"
        elif dikey == "2" and yatay == "3" :
            tablo[5] = "_X_"
        elif dikey == "3" and yatay == "1" :
            tablo[6] = "_X_"
        elif dikey == "3" and yatay == "2" :
            tablo[7] = "_X_"
        elif dikey == "3" and yatay == "3" :
            tablo[8] = "_X_"
        print("\t\t",tablo[0],tablo[1],tablo[2],"\n\t\t",tablo[3],tablo[4],tablo[5],"\n\t\t",tablo[6],tablo[7],tablo[8],"\n")
        if tablo[0] == "_X_" and tablo[1] == "_X_" and tablo[2] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[3] == "_X_" and tablo[4] == "_X_" and tablo[5] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[6] == "_X_" and tablo[7] == "_X_" and tablo[8] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[0] == "_X_" and tablo[3] == "_X_" and tablo[6] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[1] == "_X_" and tablo[4] == "_X_" and tablo[7] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[2] == "_X_" and tablo[5] == "_X_" and tablo[8] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[0] == "_X_" and tablo[4] == "_X_" and tablo[8] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[2] == "_X_" and tablo[4] == "_X_" and tablo[6] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
                # Dabaddu38
        print("~~ 2. oyuncu (O) ~~")
        while True :
            yatay = input("Soldan sağa [1,2,3] : ")
            while yatay != "1" and yatay != "2" and yatay != "3" and yatay != "!bilgi" :
                yatay = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nSoldan sağa [1,2,3] : ")
            if yatay == "!bilgi" :
                print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
                yatay = input("Soldan sağa [1,2,3] : ")
            dikey = input("Yukarıdan aşağıya [1,2,3] : ")
            while dikey != "1" and dikey != "2" and dikey != "3" and dikey != "!bilgi" :
                dikey = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nYukarıdan aşağıya [1,2,3] : ")
            if dikey == "!bilgi" :
                print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
                dikey = input("Yukarıdan aşağıya [1,2,3] : ")
            if yatay == "1" and dikey == "1" and tablo[0] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "1" and tablo[1] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "1" and tablo[2] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "1" and dikey == "2" and tablo[3] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "2" and tablo[4] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "2" and tablo[5] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "1" and dikey == "3" and tablo[6] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "3" and tablo[7] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "3" and tablo[8] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            else :
                break
        if dikey == "1" and yatay == "1" :
            tablo[0] = "_O_"
        elif dikey == "1" and yatay == "2" :
            tablo[1] = "_O_"
        elif dikey == "1" and yatay == "3" :
            tablo[2] = "_O_"
        elif dikey == "2" and yatay == "1" :
            tablo[3] = "_O_"
        elif dikey == "2" and yatay == "2" :
            tablo[4] = "_O_"
        elif dikey == "2" and yatay == "3" :
            tablo[5] = "_O_"
        elif dikey == "3" and yatay == "1" :
            tablo[6] = "_O_"
        elif dikey == "3" and yatay == "2" :
            tablo[7] = "_O_"
        elif dikey == "3" and yatay == "3" :
            tablo[8] = "_O_"
        print("\t\t",tablo[0],tablo[1],tablo[2],"\n\t\t",tablo[3],tablo[4],tablo[5],"\n\t\t",tablo[6],tablo[7],tablo[8],"\n")
        if tablo[0] == "_O_" and tablo[1] == "_O_" and tablo[2] == "_O_" :
            print("TEBRİKLER ~~ 2. oyuncu (O) ~~ KAZANDI !!!")
            break
        elif tablo[3] == "_O_" and tablo[4] == "_O_" and tablo[5] == "_O_" :
            print("TEBRİKLER ~~ 2. oyuncu (O) ~~ KAZANDI !!!")
            break
        elif tablo[6] == "_O_" and tablo[7] == "_O_" and tablo[8] == "_O_" :
            print("TEBRİKLER ~~ 2. oyuncu (O) ~~ KAZANDI !!!")
            break
        elif tablo[0] == "_O_" and tablo[3] == "_O_" and tablo[6] == "_O_" :
            print("TEBRİKLER ~~ 2. oyuncu (O) ~~ KAZANDI !!!")
            break
        elif tablo[1] == "_O_" and tablo[4] == "_O_" and tablo[7] == "_O_" :
            print("TEBRİKLER ~~ 2. oyuncu (O) ~~ KAZANDI !!!")
            break
        elif tablo[2] == "_O_" and tablo[5] == "_O_" and tablo[8] == "_O_" :
            print("TEBRİKLER ~~ 2. oyuncu (O) ~~ KAZANDI !!!")
            break
        elif tablo[0] == "_O_" and tablo[4] == "_O_" and tablo[8] == "_O_" :
            print("TEBRİKLER ~~ 2. oyuncu (O) ~~ KAZANDI !!!")
            break
        elif tablo[2] == "_O_" and tablo[4] == "_O_" and tablo[6] == "_O_" :
            print("TEBRİKLER ~~ 2. oyuncu (O) ~~ KAZANDI !!!")
            break

        print("~~ 1. oyuncu (X) ~~")
        while True :
            yatay = input("Soldan sağa [1,2,3] : ")
            while yatay != "1" and yatay != "2" and yatay != "3" and yatay != "!bilgi" :
                yatay = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nSoldan sağa [1,2,3] : ")
            if yatay == "!bilgi" :
                print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
                yatay = input("Soldan sağa [1,2,3] : ")
            dikey = input("Yukarıdan aşağıya [1,2,3] : ")
            while dikey != "1" and dikey != "2" and dikey != "3" and dikey != "!bilgi" :
                dikey = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nYukarıdan aşağıya [1,2,3] : ")
            if dikey == "!bilgi" :
                print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
                dikey = input("Yukarıdan aşağıya [1,2,3] : ")
            if yatay == "1" and dikey == "1" and tablo[0] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "1" and tablo[1] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "1" and tablo[2] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "1" and dikey == "2" and tablo[3] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "2" and tablo[4] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "2" and tablo[5] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "1" and dikey == "3" and tablo[6] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "3" and tablo[7] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "3" and tablo[8] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            else :
                break
        if dikey == "1" and yatay == "1" :
            tablo[0] = "_X_"
        elif dikey == "1" and yatay == "2" :
            tablo[1] = "_X_"
        elif dikey == "1" and yatay == "3" :
            tablo[2] = "_X_"
        elif dikey == "2" and yatay == "1" :
            tablo[3] = "_X_"
        elif dikey == "2" and yatay == "2" :
            tablo[4] = "_X_"
        elif dikey == "2" and yatay == "3" :
            tablo[5] = "_X_"
        elif dikey == "3" and yatay == "1" :
            tablo[6] = "_X_"
        elif dikey == "3" and yatay == "2" :
            tablo[7] = "_X_"
        elif dikey == "3" and yatay == "3" :
            tablo[8] = "_X_"
        print("\t\t",tablo[0],tablo[1],tablo[2],"\n\t\t",tablo[3],tablo[4],tablo[5],"\n\t\t",tablo[6],tablo[7],tablo[8],"\n")
        if tablo[0] == "_X_" and tablo[1] == "_X_" and tablo[2] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[3] == "_X_" and tablo[4] == "_X_" and tablo[5] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[6] == "_X_" and tablo[7] == "_X_" and tablo[8] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[0] == "_X_" and tablo[3] == "_X_" and tablo[6] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[1] == "_X_" and tablo[4] == "_X_" and tablo[7] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[2] == "_X_" and tablo[5] == "_X_" and tablo[8] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[0] == "_X_" and tablo[4] == "_X_" and tablo[8] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[2] == "_X_" and tablo[4] == "_X_" and tablo[6] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
                # Dabaddu38
        print("~~ 2. oyuncu (O) ~~")
        while True :
            yatay = input("Soldan sağa [1,2,3] : ")
            while yatay != "1" and yatay != "2" and yatay != "3" and yatay != "!bilgi" :
                yatay = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nSoldan sağa [1,2,3] : ")
            if yatay == "!bilgi" :
                print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
                yatay = input("Soldan sağa [1,2,3] : ")
            dikey = input("Yukarıdan aşağıya [1,2,3] : ")
            while dikey != "1" and dikey != "2" and dikey != "3" and dikey != "!bilgi" :
                dikey = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nYukarıdan aşağıya [1,2,3] : ")
            if dikey == "!bilgi" :
                print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
                dikey = input("Yukarıdan aşağıya [1,2,3] : ")
            if yatay == "1" and dikey == "1" and tablo[0] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "1" and tablo[1] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "1" and tablo[2] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "1" and dikey == "2" and tablo[3] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "2" and tablo[4] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "2" and tablo[5] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "1" and dikey == "3" and tablo[6] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "3" and tablo[7] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "3" and tablo[8] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            else :
                break
        if dikey == "1" and yatay == "1" :
            tablo[0] = "_O_"
        elif dikey == "1" and yatay == "2" :
            tablo[1] = "_O_"
        elif dikey == "1" and yatay == "3" :
            tablo[2] = "_O_"
        elif dikey == "2" and yatay == "1" :
            tablo[3] = "_O_"
        elif dikey == "2" and yatay == "2" :
            tablo[4] = "_O_"
        elif dikey == "2" and yatay == "3" :
            tablo[5] = "_O_"
        elif dikey == "3" and yatay == "1" :
            tablo[6] = "_O_"
        elif dikey == "3" and yatay == "2" :
            tablo[7] = "_O_"
        elif dikey == "3" and yatay == "3" :
            tablo[8] = "_O_"
        print("\t\t",tablo[0],tablo[1],tablo[2],"\n\t\t",tablo[3],tablo[4],tablo[5],"\n\t\t",tablo[6],tablo[7],tablo[8],"\n")
        if tablo[0] == "_O_" and tablo[1] == "_O_" and tablo[2] == "_O_" :
            print("TEBRİKLER ~~ 2. oyuncu (O) ~~ KAZANDI !!!")
            break
        elif tablo[3] == "_O_" and tablo[4] == "_O_" and tablo[5] == "_O_" :
            print("TEBRİKLER ~~ 2. oyuncu (O) ~~ KAZANDI !!!")
            break
        elif tablo[6] == "_O_" and tablo[7] == "_O_" and tablo[8] == "_O_" :
            print("TEBRİKLER ~~ 2. oyuncu (O) ~~ KAZANDI !!!")
            break
        elif tablo[0] == "_O_" and tablo[3] == "_O_" and tablo[6] == "_O_" :
            print("TEBRİKLER ~~ 2. oyuncu (O) ~~ KAZANDI !!!")
            break
        elif tablo[1] == "_O_" and tablo[4] == "_O_" and tablo[7] == "_O_" :
            print("TEBRİKLER ~~ 2. oyuncu (O) ~~ KAZANDI !!!")
            break
        elif tablo[2] == "_O_" and tablo[5] == "_O_" and tablo[8] == "_O_" :
            print("TEBRİKLER ~~ 2. oyuncu (O) ~~ KAZANDI !!!")
            break
        elif tablo[0] == "_O_" and tablo[4] == "_O_" and tablo[8] == "_O_" :
            print("TEBRİKLER ~~ 2. oyuncu (O) ~~ KAZANDI !!!")
            break
        elif tablo[2] == "_O_" and tablo[4] == "_O_" and tablo[6] == "_O_" :
            print("TEBRİKLER ~~ 2. oyuncu (O) ~~ KAZANDI !!!")
            break

        print("~~ 1. oyuncu (X) ~~")
        while True :
            yatay = input("Soldan sağa [1,2,3] : ")
            while yatay != "1" and yatay != "2" and yatay != "3" and yatay != "!bilgi" :
                yatay = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nSoldan sağa [1,2,3] : ")
            if yatay == "!bilgi" :
                print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
                yatay = input("Soldan sağa [1,2,3] : ")
            dikey = input("Yukarıdan aşağıya [1,2,3] : ")
            while dikey != "1" and dikey != "2" and dikey != "3" and dikey != "!bilgi" :
                dikey = input("Sadece \"1, 2, 3, !bilgi\" kullanılabilir.\nYukarıdan aşağıya [1,2,3] : ")
            if dikey == "!bilgi" :
                print("\n"+"*"*50,"\n\nBu oyunda ana kural, 3 tane x veya 3 tane o harfini birleştirmektir. Herkesin bir kere kullanma hakkı vardır. Yani sırayla birer birer yapılır. 3 tane birleştirilen x veya o harflerinin üstü çizilir. Alttan üste, Üstten alta, Çapraz kullanılabilir. Bu oyunda kimse kimsenin hamlesine karışamaz. Süre yoktur. En fazla harf birleştiren oyunun galibidir.\n\n"+50*"*","\n")
                dikey = input("Yukarıdan aşağıya [1,2,3] : ")
            if yatay == "1" and dikey == "1" and tablo[0] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "1" and tablo[1] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "1" and tablo[2] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "1" and dikey == "2" and tablo[3] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "2" and tablo[4] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "2" and tablo[5] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "1" and dikey == "3" and tablo[6] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "2" and dikey == "3" and tablo[7] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            elif yatay == "3" and dikey == "3" and tablo[8] != "___" :
                print("Orası zaten dolu, lütfen başka bir yer seç.")
                continue
            else :
                break
        if dikey == "1" and yatay == "1" :
            tablo[0] = "_X_"
        elif dikey == "1" and yatay == "2" :
            tablo[1] = "_X_"
        elif dikey == "1" and yatay == "3" :
            tablo[2] = "_X_"
        elif dikey == "2" and yatay == "1" :
            tablo[3] = "_X_"
        elif dikey == "2" and yatay == "2" :
            tablo[4] = "_X_"
        elif dikey == "2" and yatay == "3" :
            tablo[5] = "_X_"
        elif dikey == "3" and yatay == "1" :
            tablo[6] = "_X_"
        elif dikey == "3" and yatay == "2" :
            tablo[7] = "_X_"
        elif dikey == "3" and yatay == "3" :
            tablo[8] = "_X_"
        print("\t\t",tablo[0],tablo[1],tablo[2],"\n\t\t",tablo[3],tablo[4],tablo[5],"\n\t\t",tablo[6],tablo[7],tablo[8],"\n")
        if tablo[0] == "_X_" and tablo[1] == "_X_" and tablo[2] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[3] == "_X_" and tablo[4] == "_X_" and tablo[5] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[6] == "_X_" and tablo[7] == "_X_" and tablo[8] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[0] == "_X_" and tablo[3] == "_X_" and tablo[6] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[1] == "_X_" and tablo[4] == "_X_" and tablo[7] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[2] == "_X_" and tablo[5] == "_X_" and tablo[8] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[0] == "_X_" and tablo[4] == "_X_" and tablo[8] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        elif tablo[2] == "_X_" and tablo[4] == "_X_" and tablo[6] == "_X_" :
            print("TEBRİKLER ~~ 1. oyuncu (X) ~~ KAZANDI !!!")
            break
        print("Malesef kimse kazanamadı :(")
        break
    karar = input("\n******************************\nBizi, yani Dabaddu Software' i tercih ettiğiniz için teşekkür ederiz...\nTekrar oynamak ister misiniz? (e/h) : ")
    while karar != "e" and karar != "h" :
        karar = input("Sadece \"e\" yada \"h\" yazılabilir !\nTekrar oynamak ister misiniz? (e/h) : ")
quit()