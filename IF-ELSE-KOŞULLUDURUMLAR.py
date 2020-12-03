

seçim = int(input("MERHABA HESAP MAKİNESİNE HOŞGELDİNİZ TOPLAMA İÇİN 1 , ÇIKARMA İÇİN 2 ÇARPMA İÇİN 3 BÖLME İÇİN 4 SAYISINI TUŞLAYINIZ"))
if seçim > 0 and seçim <= 4 :
   sayı1 = int(input("ilk sayıyı giriniz"))
   sayı2 = int(input("ikinci sayıyı giriniz"))

if seçim == 1 :
    print("toplama işleminin sonucu" , (sayı1+sayı2))
    print("beni kullandığınız için teşekkür ederim " , "\n", "CREATED BY FATİH KARATEKİN ")

if seçim == 2 :
    print("çıkarma işleminin sonucu" , (sayı1-sayı2))
    print("beni kullandığınız için teşekkür ederim " , "\n", "CREATED BY FATİH KARATEKİN ")


if seçim == 3 :
    print("çarpma işleminin sonucu" , (sayı1*sayı2))
    print("beni kullandığınız için teşekkür ederim " , "\n", "CREATED BY FATİH KARATEKİN ")

if seçim == 4 :
    print("bölme işleminin sonucu" , (sayı1//sayı2))
    print("beni kullandığınız için teşekkür ederim " , "\n", "CREATED BY FATİH KARATEKİN ")
