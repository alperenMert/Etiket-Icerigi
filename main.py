import urllib.request
import re

#html kodu icerisindeki title etiketinin içeriğini almak
try:
    adress=input("Site adresi girin: ") #Kaynak kodun alınacagı site adresi
    print("\n")

    #siteye bağlanarak kaynak kodlar alındı
    html= urllib.request.urlopen(adress)
    html =html.read()
    html = str(html)

    #REGEX ile etiketin tanımı
    tanim= "<title>(.*?)</title>"

    #REGEX ile etiketi kaynak kodların içine aldık
    ara= re.search(tanim,html)

    #etiket kaynak kod içerisinde ise
    if ara:
        etiket= ara.group(0) # etiket html kodu ile beraber geldi
        icerik= ara.group(1) # etiketin sadece içeriği geldi

        print("etiket: "+ etiket)
        print("içerik: "+ icerik)

    #eger kaynak kodlar içerisinde etiket bulunmuyorsa
    else:
        print("İstediğiniz etiket kaynak kodlar arasında bulunamadı")

except:

    print("Beklenmeyen bir hata oluştu")