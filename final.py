# ½ character'i 189 olarak alınmıştır
# k, turnuvaya katılan toplam kişi sayısını belirtir.
import math
import re
def tr_upper(self):
    self = re.sub(r"i", "İ", self)
    self = re.sub(r"ı", "I", self)
    self = re.sub(r"ç", "Ç", self)
    self = re.sub(r"ş", "Ş", self)
    self = re.sub(r"ü", "Ü", self)
    self = re.sub(r"ğ", "Ğ", self)
    self = self.upper() # for the rest use default upper
    return self
def sayac(renkler,anahtar,renk):
    if renk == 'b':
        renkler[anahtar][3] = renkler[anahtar][3] +1
        renkler[anahtar][4] = 0
    elif renk  == 's':
        renkler[anahtar][4] = renkler[anahtar][4] + 1
        renkler[anahtar][3] = 0
    elif renk == 'x':
        renkler[anahtar][3] = 0
        renkler[anahtar][4] = 0
def turbasma(turpuans,masalar,k,mydict,renk):
    print("      Beyazlar           Siyahlar")
    print("MNo BSNo   LNo Puan - Puan   LNo BSNo")
    print("--- ---- ----- ----   ---- ----- ----")
    for i in range(int(k/2)):
        beyazz = str(i+1) + 'b'
        siyahh = str(i+1) + 's'
        print("{:>3} {:>4} {:>5} {:>4.2f} - {:>4.2f} {:>5} {:>4}".format(i+1,mydict[masalar[beyazz]],masalar[beyazz],turpuans[masalar[beyazz]],turpuans[masalar[siyahh]],masalar[siyahh],mydict[masalar[siyahh]]))
    if k%2 == 1:
        bs = str(int(k/2)+1) + renk#########################renkkkk
        print("{:>3} {:>4} {:>5} {:>4.2f} - {}  ".format(int(k/2)+1,mydict[masalar[bs]],masalar[bs],turpuans[masalar[bs]],"BYE"))

def sorting(b,k,turpuans,hesaps):
    i=0
    j=0
    while i<k-i-1:
        j=0
        while j<k-i-1:
            if turpuans[b[j][0]] < turpuans[b[j+1][0]]:
                temp = b[j]
                b[j] = b[j+1]
                b[j+1] = temp
            elif turpuans[b[j][0]] == turpuans[b[j+1][0]]:
                if hesaps[b[j][0]][0] < hesaps[b[j+1][0]][0]:
                    temp = b[j]
                    b[j] = b[j+1]
                    b[j+1] = temp
                elif hesaps[b[j][0]][0] == hesaps[b[j+1][0]][0]:
                    if hesaps[b[j][0]][1] < hesaps[b[j+1][0]][1]:
                        temp = b[j]
                        b[j] = b[j+1]
                        b[j+1] = temp
                    elif hesaps[b[j][0]][1] == hesaps[b[j+1][0]][1]:
                        if hesaps[b[j][0]][2] < hesaps[b[j+1][0]][2]:
                            temp = b[j]
                            b[j] = b[j+1]
                            b[j+1] = temp
                        elif hesaps[b[j][0]][2] == hesaps[b[j+1][0]][2]:
                            if hesaps[b[j][0]][3] < hesaps[b[j+1][0]][3]:
                                temp = b[j]
                                b[j] = b[j+1]
                                b[j+1] = temp
            j = j + 1
        i = i + 1
        
def sortmylist(b,k,turpuans):
    i=0
    j=0
    while i<k-1:
        j=0
        while j<k-i-1:
            if turpuans[b[j][0]] < turpuans[b[j+1][0]]:
                temp = b[j]
                b[j] = b[j+1]
                b[j+1] = temp
            elif turpuans[b[j][0]] == turpuans[b[j+1][0]]:
                if b[j][2] < b[j+1][2]:
                        
                        temp = b[j]
                        b[j] = b[j+1]
                        b[j+1] = temp
                
                elif b[j][2] == b[j+1][2]:
                    
                    
                    if b[j][3] < b[j+1][3]:
                        temp = b[j]
                        b[j] = b[j+1]
                        b[j+1] = temp
                            

                    elif b[j][3] == b[j+1][3]:
                        if b[j][1] < b[j+1][1]:
                            
                            temp = b[j]
                            b[j] = b[j+1]
                            b[j+1] = temp
                        elif b[j][1] == b[j+1][1]:
                            if b[j][0] < b[j+1][0]:
                                
                                temp = b[j]
                                b[j] = b[j+1]
                                b[j+1] = temp
            j= j + 1
        i = i +1  
def tursonuc(masalar,turpuans,k,tur,renk,byeler,bh,sb,gs,tptur,son,mydict):
    if k%2 == 1:
        masasayisi = int(k/2)
        masabs = str(int((k/2)+1)) + renk
        turpuans[masalar[masabs]] = turpuans[masalar[masabs]] + 1
        #capraz[masalar[masabs]][3] = 1
        #capraz[masalar[masabs]][4] = (turpuans[masalar[masabs]]-1) + (0.5*(tptur-tur))
        bh[masalar[masabs]][0].append((turpuans[masalar[masabs]]-1) + (0.5*(tptur-tur)))
        sb[masalar[masabs]][0].append((turpuans[masalar[masabs]]-1) + (0.5*(tptur-tur)))
        son[masalar[masabs]][0].append("-")
        son[masalar[masabs]][1].append("-")
        son[masalar[masabs]][2].append(1)

    else:
        masasayisi = int(k/2)
    for i in range(masasayisi):
        while True:
            print('{}. turda {}. masada oynanan macin sonucunu giriniz (0-5):'.format(tur,i+1))
            sonuc = int(input())
            if sonuc >= 0 and sonuc <= 5:
                break
        if sonuc == 0:
            siyah = str(i+1) + 's'
            beyaz = str(i+1) + 'b'
            turpuans[masalar[siyah]] = turpuans[masalar[siyah]]  + 0.5
            turpuans[masalar[beyaz]] = turpuans[masalar[beyaz]]  + 0.5
            bh[masalar[siyah]][1].append(masalar[beyaz])
            bh[masalar[beyaz]][1].append(masalar[siyah])
            sb[masalar[siyah]][2].append(masalar[beyaz])
            sb[masalar[beyaz]][2].append(masalar[siyah])

            son[masalar[siyah]][0].append(mydict[masalar[beyaz]])
            son[masalar[siyah]][1].append('s')
            son[masalar[siyah]][2].append(chr(189))

            son[masalar[beyaz]][0].append(mydict[masalar[siyah]])
            son[masalar[beyaz]][1].append('b')
            son[masalar[beyaz]][2].append(chr(189))
            #capraz[masalar[siyah]][1].append(turpuans[masalar[beyaz]])
            #capraz[masalar[beyaz]][1].append(turpuans[masalar[siyah]])
        elif sonuc == 1:
            beyaz = str(i+1) + 'b'
            siy = str(i+1) + 's'
            turpuans[masalar[beyaz]] = turpuans[masalar[beyaz]]  + 1
            bh[masalar[beyaz]][1].append(masalar[siy])
            bh[masalar[siy]][1].append(masalar[beyaz])
            sb[masalar[beyaz]][1].append(masalar[siy])
            gs[masalar[beyaz]] = gs[masalar[beyaz]] + 1

            son[masalar[beyaz]][0].append(mydict[masalar[siy]])
            son[masalar[beyaz]][1].append('b')
            son[masalar[beyaz]][2].append(1)

            son[masalar[siy]][0].append(mydict[masalar[beyaz]])
            son[masalar[siy]][1].append('s')
            son[masalar[siy]][2].append(0)
            #capraz[masalar[beyaz]][0].append(turpuans[masalar[siy]]) 
            #capraz[masalar[beyaz]][2] =  capraz[masalar[beyaz]][2] +1
        elif sonuc == 2:
            siyah = str(i+1) + 's'
            bey = str(i+1) + 'b'
            turpuans[masalar[siyah]] = turpuans[masalar[siyah]]  + 1
            bh[masalar[siyah]][1].append(masalar[bey])
            bh[masalar[bey]][1].append(masalar[siyah])
            sb[masalar[siyah]][1].append(masalar[bey])
            gs[masalar[siyah]] = gs[masalar[siyah]] + 1

            son[masalar[siyah]][0].append(mydict[masalar[bey]])
            son[masalar[siyah]][1].append('s')
            son[masalar[siyah]][2].append(1)

            son[masalar[bey]][0].append(mydict[masalar[siyah]])
            son[masalar[bey]][1].append('b')
            son[masalar[bey]][2].append(0)
            #capraz[masalar[siyah]][0].append(turpuans[masalar[bey]]) 
            #capraz[masalar[siyah]][2] = capraz[masalar[siyah]][2] +1 
        elif sonuc == 3:
            beyaz = str(i+1) + 'b'
            siyh = str(i+1) + 's'
            turpuans[masalar[beyaz]] = turpuans[masalar[beyaz]] + 1
            byeler[masalar[beyaz]] = 1
            bh[masalar[beyaz]][0].append(turpuans[masalar[beyaz]] - 1 + (0.5*(tptur-tur)))
            bh[masalar[siyh]][0].append(turpuans[masalar[siyh]] + (0.5*(tptur-tur)))
            sb[masalar[beyaz]][0].append(turpuans[masalar[beyaz]] - 1 + (0.5*(tptur-tur)))
            gs[masalar[beyaz]] = gs[masalar[beyaz]] + 1

            son[masalar[beyaz]][0].append(mydict[masalar[siyh]])
            son[masalar[beyaz]][1].append('b')
            son[masalar[beyaz]][2].append('+')

            son[masalar[siyh]][0].append(mydict[masalar[beyaz]])
            son[masalar[siyh]][1].append('s')
            son[masalar[siyh]][2].append('-')
            #capraz[masalar[beyaz]][3] = 1
            #capraz[masalar[beyaz]][4] = turpuans[masalar[beyaz]] - 1 + (0.5*(tptur-tur)) 
            #capraz[masalar[beyaz]][2] = capraz[masalar[beyaz]][2] + 1
            
        elif sonuc == 4:
            siyah = str(i+1) + 's'
            byz = str(i+1) + 'b'
            turpuans[masalar[siyah]] = turpuans[masalar[siyah]]  + 1
            byeler[masalar[siyah]] = 1
            bh[masalar[siyah]][0].append(turpuans[masalar[siyah]]  - 1 + (0.5*(tptur-tur)))
            bh[masalar[byz]][0].append(turpuans[masalar[byz]] + (0.5*(tptur-tur)))
            sb[masalar[siyah]][0].append(turpuans[masalar[siyah]]  - 1 + (0.5*(tptur-tur)))
            gs[masalar[siyah]] = gs[masalar[siyah]] + 1 

            son[masalar[siyah]][0].append(mydict[masalar[byz]])
            son[masalar[siyah]][1].append('s')
            son[masalar[siyah]][2].append('+')

            son[masalar[byz]][0].append(mydict[masalar[siyah]])
            son[masalar[byz]][1].append('b')
            son[masalar[byz]][2].append('-')
            #capraz[masalar[siyah]][3] = 1
            #capraz[masalar[siyah]][4] = turpuans[masalar[siyah]] - 1 + (0.5*(tptur-tur))
            #capraz[masalar[siyah]][2] = capraz[masalar[siyah]][2] + 1
            
        elif sonuc == 5:
            siy = str(i+1) + 's'
            byz = str(i+1) + 'b'
            bh[masalar[siy]][0].append(turpuans[masalar[siy]] + (0.5*(tptur-tur)))
            bh[masalar[byz]][0].append(turpuans[masalar[byz]] + (0.5*(tptur-tur)))
           
            son[masalar[siy]][0].append(mydict[masalar[byz]])
            son[masalar[siy]][1].append('s')
            son[masalar[siy]][2].append('-')

            son[masalar[byz]][0].append(mydict[masalar[siy]])
            son[masalar[byz]][1].append('b')
            son[masalar[byz]][2].append('-')


def tureslestirme(b,renkler,masalar,turpuans,k,maclar,byeler,renk):
    t = k
    masanum = 1
    kopyab = b.copy()
    target = kopyab[0]
    
    if k%2 == 1:
        masason = str(int(k/2)+1) + renk
        for j in range(k):
            if byeler[b[k-1-j][0]] == 0:
                masalar[masason] = b[k-1-j][0]
                renkler[b[k-1-j][0]][2] = 'x'
                sayac(renkler,b[k-1-j][0],'x')
                #kopyab[k-1-j] , kopyab[k-1]= kopyab[k-1], kopyab[k-1-j]
                kopyab.pop(k-1-j)
                t = t-1 
                byeler[b[k-1-j][0]] = 1
                
                
                break
        
    i = 1
    kod = kopyab[0][0]
    point = turpuans[kopyab[0][0]]
    islem  = 0
    while i < t:
        #print("--------------")
        #print(kopyab)
        #print(renkler)
        #print(turpuans)
        #print("1 --")
        #print(kopyab[0][0])
        #print("2 -- ")

        #print(kopyab[i][0])
        #print(point)
        if point == turpuans[kopyab[i][0]]:
            if (renkler[kopyab[0][0]][2] != renkler[kopyab[i][0]][2]) and (islem == 0) and (not(kopyab[i][0] in maclar[kopyab[0][0]])) and (not(kod == kopyab[i][0])): # aranan zıt renk bulunan zıt renk

                if renkler[kopyab[i][0]][2] == 'x':  #(renkler[kopyab[i][0]][2] != 'b') and (renkler[kopyab[i][0]][2] != 's')
                    if renkler[kopyab[0][0]][2] == 's':
                        renkler[kopyab[i][0]][2] = 'b'
                    else:
                        renkler[kopyab[i][0]][2] = 's'
                elif renkler[kopyab[0][0]][2] == 'x':
                    if renkler[kopyab[i][0]][2] == 's':
                        renkler[kopyab[0][0]][2] = 'b'
                    else:
                        renkler[kopyab[0][0]][2]  = 's'  
                masa1 = str(masanum) + renkler[kopyab[i][0]][2]
                masa2 = str(masanum) +  renkler[kopyab[0][0]][2]
                
                temp = renkler[kopyab[0][0]][2]
                renkler[kopyab[0][0]][2] =renkler[kopyab[i][0]][2] 
                renkler[kopyab[i][0]][2] = temp
                sayac(renkler,kopyab[i][0],renkler[kopyab[i][0]][2])
                sayac(renkler,kopyab[0][0],renkler[kopyab[0][0]][2])

                masalar[masa1] = kopyab[0][0]
                masalar[masa2] = kopyab[i][0]
                #print('Turnuvadaki tur sayisini giriniz ({}-{}): '.format(masa1,masa2))
                kopyab.pop(i)
                kopyab.pop(0)
                
                
                if kopyab != []:
                    point = turpuans[kopyab[0][0]]
                    kod = kopyab[0][0]
                    #print("kod {} ".format(kod))
                i = 1
                t = t -2
                masanum = masanum + 1
                # daha islem var
            elif islem == 0:
                if ((i+1) == t) and not(kopyab == []):
                    islem = 1
                    i = 1
                else:
                    i = i + 1
            elif (renkler[kopyab[0][0]][2] == renkler[kopyab[i][0]][2]) and (islem == 1) and (not(kopyab[i][0] in maclar[kopyab[0][0]])) and (kod != kopyab[i][0]):
                if ((renkler[kopyab[i][0]][2] == 'b') and (renkler[kopyab[i][0]][3] < 2)) or ((renkler[kopyab[i][0]][2] == 's') and (renkler[kopyab[i][0]][4] < 2)):

                    if renkler[kopyab[0][0]][2] == 'b':
                        renkler[kopyab[0][0]][2] = 's'
                        sayac(renkler,kopyab[0][0],'s')
                    else :
                        renkler[kopyab[0][0]][2] = 'b'
                        sayac(renkler,kopyab[0][0],'b')
                    masa1 = str(masanum) + renkler[kopyab[0][0]][2]
                    masa2 = str(masanum) + renkler[kopyab[i][0]][2]
                    sayac(renkler,kopyab[i][0],renkler[kopyab[i][0]][2])
                    masalar[masa1] = kopyab[0][0]
                    masalar[masa2] = kopyab[i][0]
                    
                    
                    kopyab.pop(i)
                    kopyab.pop(0)
                    if kopyab != []:
                        point = turpuans[kopyab[0][0]]
                        kod = kopyab[0][0]
                    i=1
                    t = t-2
                    masanum = masanum  + 1
                    islem = 0
                else:
                    i = i + 1
            elif islem == 1:
                i = i +1
            elif (renkler[kopyab[0][0]][2] == renkler[kopyab[i][0]][2]) and (islem == 2) and (not(kopyab[i][0] in maclar[kopyab[0][0]])) and (kod != kopyab[i][0]):
                if ((renkler[kopyab[0][0]][2] == 'b') and (renkler[kopyab[0][0]][3] < 2)) or ((renkler[kopyab[0][0]][2] == 's') and (renkler[kopyab[0][0]][4] < 2)):
                    if renkler[kopyab[i][0]][2] == 'b':
                        renkler[kopyab[i][0]][2] = 's'
                        sayac(renkler,kopyab[i][0],'s')
                    else:
                        renkler[kopyab[i][0]][2] = 'b'
                        sayac(renkler,kopyab[i][0],'b')
                    masa1 = str(masanum) + renkler[kopyab[0][0]][2]
                    masa2 = str(masanum) + renkler[kopyab[i][0]][2]
                    sayac(renkler,kopyab[0][0],renkler[kopyab[0][0]][2])
                    masalar[masa1] = kopyab[0][0]
                    masalar[masa2] = kopyab[i][0]
                    
                    kopyab.pop(i)               
                    kopyab.pop(0)
                    if kopyab != []:
                        point = turpuans[kopyab[0][0]]
                        kod = kopyab[0][0]
                    i = 1 
                    t = t-2
                    masanum = masanum + 1
                    islem = 0
                else:
                    i = i + 1
            elif islem == 2:
                i = i +1
        elif point > turpuans[kopyab[i][0]]:
           
            if islem == 0:
                
                i = 1
                islem = 1
            elif islem == 1:
                i = 1
                islem = 2
            elif islem == 2:
                
                islem = 0
                point = turpuans[kopyab[i][0]]
                kod = kopyab[i-1][0]
                
        else:
            i = i +1
    

def mactablosu(maclar,masalar,k):
    for i in range(int(k/2)):
        masab = str(i+1) + 'b'
        masas = str(i+1) + 's'
        maclar[masalar[masab]].append(masalar[masas])
        maclar[masalar[masas]].append(masalar[masab])       
        

def hesaplamalar(bh,sb,gs,b,k,hesaps,maclar,turpuans):
    for i in range(k):
        
        bh1 = bh[b[i][0]].copy()
        for j in range(len(bh1[1])):
            bh1[0].append(turpuans[bh1[1][j]])
        bh1[0].remove(min(bh1[0]))
        hesaps[b[i][0]][0] = sum(bh1[0])
        bh1[0].remove(min(bh1[0]))
        hesaps[b[i][0]][1] = sum(bh1[0])
        
        sb1 = sb[b[i][0]].copy()
        for j in range(len(sb1[2])):
            sb1[0].append(turpuans[sb1[2][j]]/2)
        for v in range(len(sb1[1])):
            sb1[0].append(turpuans[sb1[1][v]])
        hesaps[b[i][0]][2] = sum(sb1[0])
        hesaps[b[i][0]][3] = gs[b[i][0]] 
        #sb = capraz[b[i][0]][0].copy()
        #sb2 =capraz[b[i][0]][1].copy()
        #hesaps[b[i][0]][2] = sum(sb) + (sum(sb2)/2) +capraz[b[i][0]][4]
        #hesaps[b[i][0]][3] = capraz[b[i][0]][2] 


i = 1
k = 0 #total person number
b = []
mydict = {}
renkler = {}
maclar = {}
byeler = {}
tekrarlar = {}
#capraz = {}
hesaps = {}
bh = {}
sb = {}
gs = {}
son = {}
flag=0

while i > 0:
    print("Oyuncunun lisans numarasini giriniz (bitirmek için 0 ya da negatif giriniz):")
    i = int(input())
    flag = 0
    for m in range(k):
        if (i in b[m]) and (i > 0) :
            flag= 1
        m = m + 1
    if (flag == 0) and (i > 0):
        b.append([i])
        print("Oyuncunun adini-soyadini giriniz:")
        name = input()
        #name = tr_upper(name)
        b[k].append(name)
        while True:
            print("Oyuncunun ELO’sunu giriniz (en az 1000, yoksa 0):")
            elonum = int(input())
            if elonum >= 1000 or elonum == 0:
                b[k].append(elonum)
                break
        while True:
            print("Oyuncunun UKD’sini giriniz (en az 1000, yoksa 0):")
            ukdnum = int(input())
            if ukdnum >= 1000 or ukdnum == 0:
                b[k].append(ukdnum)
                break
        k = k+1

 
turpuans = {}
for c in range(k):
    son[b[c][0]] = [[],[],[]]
    gs[b[c][0]] = 0
    hesaps[b[c][0]] = [0,0,0,0]
    bh[b[c][0]] = [[],[]]
    sb[b[c][0]] = [[],[],[]]
    #capraz[b[c][0]] = [[],[],0,0,0]
    tekrarlar[b[c][0]] = {'s':0,'b':0}
    byeler[b[c][0]] = 0
    maclar[b[c][0]] = []
    turpuans[b[c][0]] = 0
    renkler[b[c][0]] = [0,0,"x",0,0]
    b[c].append(0)      
sortmylist(b,k,turpuans)                



counter = 0
print("Başlangıç Sıralama Listesi:")
print("BSNo   LNo Ad-Soyad      ELO  UKD")
print("---- ----- ------------ ---- ----")

for c in range(k):
    mydict[b[c][0]] = c+1
    
    print('{:>4} {:>5} {:12} {:>4} {:>4}'.format(c+1, b[c][0],tr_upper(b[c][1]),b[c][2],b[c][3]))

tursayisi = math.ceil(math.log(k,2)) #tur sayisi alt limit

tursayisi2 = k-1 #tur sayisi üst limit



while True:
    print('Turnuvadaki tur sayisini giriniz ({}-{}): '.format(tursayisi,tursayisi2))
    turnuva = int(input())
    if turnuva >=tursayisi and turnuva <= tursayisi2:
        break
while True:
    print("Baslangic siralamasina gore ilk oyuncunun ilk turdaki rengini giriniz (b/s):")
    renk = input()
    if renk == 's' or renk == 'b':
        break
masalar = {}
for i in range(k):
    
    if mydict[b[i][0]]%2 == 1: #mydict Lisans numarası:BsNo
  
        masakod = str(int(i/2+1)) + renk
        masalar[masakod] = b[i][0]
        renkler[b[i][0]][2] = str(renk)
        sayac(renkler,b[i][0],renkler[b[i][0]][2])
        if renk=='b':
            renkler[b[i][0]][0] = renkler[b[i][0]][0] + 1
        elif renk=='s':
            renkler[b[i][0]][1] = renkler[b[i][0]][1] + 1
    else:
        if renk == 's':
            renk2 = 'b'
        else:
            renk2 = 's'
        masakod = str(int(i/2+1)) + renk2
        masalar[masakod] = b[i][0] 
       
        renkler[b[i][0]][2] = str(renk2)
        sayac(renkler,b[i][0],renkler[b[i][0]][2])
        if renk2=='b':
            renkler[b[i][0]][0] = renkler[b[i][0]][0] + 1
        elif renk2=='s':
            renkler[b[i][0]][1] = renkler[b[i][0]][1] + 1
if k%2 == 1:
    byeler[b[k-1][0]] = 1 #################################################
if k%2 == 1:
    renkler[b[k-1][0]][0] = 0
    renkler[b[k-1][0]][1] = 0
    renkler[b[k-1][0]][2] = 'x'

mactablosu(maclar,masalar,k)
if k % 2 == 0:

    for i in range(int(k/2)):
        masas = str(i+1) + 's'
        masab = str(i+1) + 'b'
        print('{} {} {} {} - {} {} {}'.format(i+1, mydict[masalar[masab]],masalar[masab],turpuans[masalar[masab]],turpuans[masalar[masas]],masalar[masas],mydict[masalar[masas]]))
elif k % 2 == 1:
    for i in range(int(k/2)):
        masas = str(i+1) + 's'
        masab = str(i+1) + 'b'
        #print('{} {} {} {} - {} {} {}'.format(i+1, mydict[masalar[masab]],masalar[masab],turpuans[masalar[masab]],turpuans[masalar[masas]],masalar[masas],mydict[masalar[masas]]))
    masabs = str(int((k+1)/2)) + renk
    #print('{} {} {} {} - {} '.format(int((k+1)/2), mydict[masalar[masabs]],masalar[masabs],turpuans[masalar[masabs]],"BYE"))  
print("{}. Tur Eşleştirme Listesi:".format(1))
turbasma(turpuans,masalar,k,mydict,renk)
for i in range(turnuva):
    #print("{}. Tur Eşleştirme Listesi:".format(i+1))
    tursonuc(masalar,turpuans,k,i+1,renk,byeler,bh,sb,gs,turnuva,son,mydict)
    sortmylist(b,k,turpuans)
    tureslestirme(b,renkler,masalar,turpuans,k,maclar,byeler,renk)
    
    if (i+1) < turnuva: 
        mactablosu(maclar,masalar,k)

    if i < turnuva-1:
        print("{}. Tur Eşleştirme Listesi:".format(i+2))
        turbasma(turpuans,masalar,k,mydict,renk)

#print(maclar)
#print(capraz)
hesaplamalar(bh,sb,gs,b,k,hesaps,maclar,turpuans)

sorting(b,k,turpuans,hesaps)

sno = {}
print("Nihai Sıralama Listesi:")
print("SNo BSNo   LNo Ad-Soyad      ELO  UKD Puan  BH-1  BH-2    SB GS")
print("--- ---- ----- ------------ ---- ---- ---- ----- ----- ----- --")
for i in range(k):
    sno[b[i][0]] = i+1
    print("{:3} {:4} {:5} {:<12} {:4} {:4} {:>4.2f} {:>4.2f} {:>4.2f} {:>4.2f} {:2}".format(i+1,mydict[b[i][0]],b[i][0],tr_upper(b[i][1]),b[i][2],b[i][3],turpuans[b[i][0]],hesaps[b[i][0]][0],hesaps[b[i][0]][1],hesaps[b[i][0]][2],hesaps[b[i][0]][3]))
print("Capraz Tablo:")
a = "BSNo "+ "SNo  " + " LNo " + "Ad-Soyad      " + "ELO  " + "UKD "
for i in range(turnuva):
    a = a+ " "+str(i+1) +  ". Tur " 
a = a+ "Puan  BH-1  BH-2    SB GS"
print(a)
a = "---- --- ----- ------------ ---- ---- "
for i in range(turnuva):
    a = a + "------- "
a = a + "---- ----- ----- ----- --"
print(a)
mydict2 = {}
mydict3 = {}
for i in range(k):
    mydict2[mydict[b[i][0]]] = b[i][0]
    mydict3[mydict[b[i][0]]] = b[i]
m = ""
for i in range(k):
    m = "  "
    for j in range(turnuva):
        
        m = m + str(son[mydict3[i+1][0]][0][j]) + " " + str(son[mydict3[i+1][0]][1][j]) + " " + str(son[mydict3[i+1][0]][2][j])
        
        if j == turnuva-2:
            m = m + "  "
        elif j < turnuva-1:
            m = m + "   "

    print("{:4} {:3} {:5} {:<12} {:4} {:4} {:<36}  {:<4.2f} {:<4.2f} {:<4.2f} {:<4.2f}  {:>1}".format(i+1,sno[mydict2[i+1]],mydict3[i+1][0],tr_upper(mydict3[i+1][1]),mydict3[i+1][2],mydict3[i+1][3],m,turpuans[mydict3[i+1][0]],hesaps[mydict3[i+1][0]][0],hesaps[mydict3[i+1][0]][1],hesaps[mydict3[i+1][0]][2],hesaps[mydict3[i+1][0]][3]))
    #print"%4d %3d %5d %12s %4d %4d %36s %4f %4.2f %4.2f %4.2f %1" % (i+1,sno[mydict2[i+1]],mydict3[i+1][0],tr_upper(mydict3[i+1][1]),mydict3[i+1][2],mydict3[i+1][3],m,turpuans[mydict3[i+1][0]],hesaps[mydict3[i+1][0]][0],hesaps[mydict3[i+1][0]][1],hesaps[mydict3[i+1][0]][2],hesaps[mydict3[i+1][0]][3])
    #,mydict3[mydict2[i+1]][0]