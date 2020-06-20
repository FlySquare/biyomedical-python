#aşağıdaki kütüphaneyi kullanmak için bu dosyanın olduğu klasörde cmd açıp "pip install pymysql" yazman lazım ama tırnakları ekleme
import pymysql.cursors#mysql bağlanmak için bir adet kütüphane ekliyoruz
# Veritabanı bağlantı bilgileri
db = pymysql.connect(host='89.107.228.51',user='bolfpsco_hazal',password='acumk6001**',db='bolfpsco_hazal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)#mysql veri tabanına bağlanıyoruz
baglanti = db.cursor()#bağlanıyoruz
# Veritabanı bağlantı bilgileri
# Fonksiyonlar
def personelalt1():# fonksiyonumuzu oluşturuyoruz
    baglanti.execute("SELECT * FROM personel ORDER BY personel_id DESC LIMIT 1")# veritabanından veriyi çekiyoruz
    sonpersonel = baglanti.fetchall()# değişkene atıyoruz
    for p in sonpersonel:# for döngüsüne alıyoruz
        lastusername = p['personel_username'] # veritabanından personel kullanıcı adını oluşturduğum değşkene atıyorum
        lastpassword = p['personel_sifre']# burda da aynı şekil şifreyi atıyorum
        sondeger = lastusername[7:10]# burada kullanıcı adı biyoser20 ya son 20 sayısını alıyoruz sadece çünkü hocan her kullanıcı eklendiğinde isim sabit sayı artsın dediği için veri geldiğinde kontrol edicek kaç diye sonra üstüne bir ekliycek
        sifresondeger = lastpassword[3:8]# burada da şifreyi aynı şekil bct2020 ya 2020 tarafını alıyoruz sadece
        intdeger = int(sondeger)# burada aldığımız veriyi int yani sayı olduğunu belirtiyoruz ki matematiksel işlemleri yapabilelim
        intdegersifre = int(sifresondeger)# burada da aynı int yapıyoruz işlemler için
        sondeger2 = intdeger + 1# burada son çekilen sayıya 1 ekliyoruz örnek: son kullanıcı adı 2020 ise ona +1 ekleyip 2021 yapıyoruz
        sondeger2sifre = intdegersifre + 1 # burda da şifrenin sayısına ekliyorum
        strd = str(sondeger2) # şimdi +1 ekledik ya onu sayısal değerden metin değerine çeviriyoruz
        strd2 = str(sondeger2sifre) # aynısını burada yapıyoruz şifre için
        sonuc = baglanti.execute('INSERT INTO personel VALUES(%s,%s,%s)',(None,'biyoser'+strd,'bct'+strd2))# burada ise veritabanına kayıt ettiriyoruz son şekilde
        db.commit()# commit çekiyoruz
        print(str(sonuc) + " kullanıcı eklendi")#ekrana sonucu yazdırıyoruz
def personelalt2():#her def yazan yeni bir fonksiyon diğerlerine yazmıycam
    baglanti.execute("SELECT * FROM personel")#veritabanına bağlanıyoruz
    sonpersonel = baglanti.fetchall()# değişkene atıyoruz
    for p2 in sonpersonel:#for döngüsüne alıyoruz
        print("Kullanıcı Adı: " + p2['personel_username'] + " --- " + "Şifre: " + p2['personel_sifre'])# ekrana kullanıcıları bastırıyoruz
def personelalt3():
    silid = input("Kullanıcı Adı Seçiniz: ")#burada yazılan kullanıcı adını değişkene alıyoruz
    personelsil = baglanti.execute('DELETE FROM personel WHERE personel_username = %s',(silid,))#burada veritabanına bağlanıp yazılan kullanıcı adına göre veritabanındansilinmesini sağlıyoruz
    db.commit()#commit çekiyoruz
    print(str(personelsil) + " kullanıcı silindi")#ekrana yazdırıyoruz
def servisalt1():
    talep = input("Talep Giriniz: ")#girilen talep bilgisini alıyoruz
    talepnot = input("Not Giriniz: ")#girilen notu alıyoruz
    servistalebi = baglanti.execute('INSERT INTO servistalepleri VALUES(%s,%s,%s)',(None,talepnot,talep))# veritabanına bağlanıp servistaleplerine veri ekliyoruz
    db.commit()#commit çekiyoruz
    servistalebidevam = baglanti.execute('INSERT INTO servistalepleridevam VALUES(%s,%s,%s)',(None,talepnot,talep))#burda da aktif taleplere ekliyoruz 2 sine eklememizin sebebi servistaleplerinde silinen de devam edende durucak ama burada sadece devam eden duracak ve her eklenen veriyeni olduğundan oto devam eden oluyor
    db.commit()#commit çekiyoruz
    print(str(servistalebi) + " servis talebi eklendi")#ekrana yazdırıyoruz
def servisalt2():
    baglanti.execute("SELECT * FROM servistalepleri")#veritabanına bağlanıyoruz
    sonpersonel = baglanti.fetchall()#değişkene atıyoruz
    for t1 in sonpersonel:#for döngsüne alıyoruz
        print("Talep: " +  t1['servistalepleri_talep']+ " --- " + "Not: " +  t1['servistalepleri_not'])#ekrana yazdırıyoruz          
def servisalt3():
    siltalep = input("Silmek İstediğiniz Talep Id siniz yazınız: ")#silincek talep id sini yazınca değişkene alıyoruz
    baglanti.execute("SELECT * FROM servistalepleridevam WHERE servistalepleridevam_id ='"+siltalep+"'")#şimdi ilk olarak devam eden taleplerden bu id ye sahip talep bilgilerinin hepsini çekiyoruz çünkü biten taleplere ekliycez
    devamtalebi = baglanti.fetchall()#değişkene atıyoruz
    for t1 in devamtalebi:#for döngüsü açıyorum
        sonuc = baglanti.execute('INSERT INTO servistalepleribiten VALUES(%s,%s,%s)',(None,t1['servistalepleridevam_not'],t1['servistalepleridevam_talep']))#şimdi aldığımız bilgileri biten taleplere ekliyoruz
        db.commit()#commit çekiyoruz
        print(str(sonuc) + "talep bitmiş olarak güncellendi")#ekrana yazdırıyoruz eklendiğini
    sonuc = baglanti.execute('DELETE FROM servistalepleridevam WHERE servistalepleridevam_id = %s',(siltalep,))#devam eden talep bittiği için devam tablosundan siliyoruz 
    db.commit()#commit çekiyoruz
    print(str(sonuc) + " kullanıcı silindi")#ekrana ayzdırıyoruz
def musterialt1():
     musterilistesi_hastanead = input("Hastane Ad Giriniz: ")#hastane adını değişkene alıyoruz
     musterilistesi_yetkiliad = input("Yetkili Ad Giriniz: ")#değişkene alıyoruz
     musterilistesi_telno = input("Tel No Giriniz: ")#değişkene alıyoruz
     musterilistesi_mail = input("Mail Giriniz: ")#değişkene alıyoruz
     musterilistesi_adres = input("Adres Giriniz: ")#değişkene alıyoruz
     servistalebi = baglanti.execute('INSERT INTO musterilistesi VALUES(%s,%s,%s,%s,%s,%s)',(None,musterilistesi_hastanead,musterilistesi_yetkiliad,musterilistesi_telno,musterilistesi_mail,musterilistesi_adres))#müşteri listesine verileri ekliyoruz
     db.commit()#commit çekiyoruz
     print(str(servistalebi) + " Müşteri eklendi")#ekrana yazdırıyoruz
def musterialt2():
     baglanti.execute("SELECT * FROM musterilistesi")#veritabanına bağlanıyoruz
     sonpersonel = baglanti.fetchall()#değişkene atıyoruz
     for t1 in sonpersonel:#for döngüsü
        print("Hastane Ad: " +  t1['musterilistesi_hastanead']+ " --- " + "Yetkili Ad: " +  t1['musterilistesi_yetkiliad']+ " --- " + "Tel No: " +  t1['musterilistesi_telno']+ " --- " + "Mail: " +  t1['musterilistesi_mail']+ " --- " + "Adres: " +  t1['musterilistesi_adres'])#ekrana yazdırıyoruz
def musterialt3():
    silmusteri = input("Silmek İstediğiniz Müşteri Id siniz yazınız: ")#veriyi değşkene alıyoruz
    sonuc = baglanti.execute('DELETE FROM musterilistesi WHERE musterilistesi_id = %s',(silmusteri,))#id ye göre veritabanından siliyoruz
    db.commit()#commit çekiyoruz
    print(str(sonuc) + " müşteri silindi")#ekrana yazdırıyoruz
# Fonksiyonlar




print("Lütfen giriş yapınız!")
kul_ad = input("Kullanıcı Adı: ")
kul_pass = input("Kullanıcı Şifre: ")
baglanti.execute("SELECT * FROM personel WHERE personel_username='"+kul_ad+"' AND personel_sifre ='"+kul_pass+"'")#veritabanına bağlanıp girilen kullanıcı adı ve şifre var mı diye bakıyoruz
kullanicilar = baglanti.fetchall()#değşkene atıyoruz
for i in kullanicilar:#for döngüsüne alıyoruz 
      if kullanicilar:#eğer kullanicilar değişkeni = true ise eğer varsa altındakiler çalışıyor
        print("Giriş Yapıldı! Çıkış yapmak için -Q-")
        print('1-Personel İşlemleri\n2- Servis Talep İşlemleri\n3- Müşteri İşlemleri\n4-Cari Hesap İşlemleri\n5-Çıkış')
        anamenu = input("Menü Seçiniz: ")
        if anamenu == "1":
            print('1-Personel Ekleme\n2- Personel Listeleme\n3- Personel Silme')
            personelalt = input("Alt Menü Seçiniz: ")
            if personelalt == "1":
                personelalt1()#bunlar fonksiyon yukarda bulabilirsin
            if personelalt == "2":
                personelalt2()##bunlar fonksiyon yukarda bulabilirsin
            if personelalt == "3": 
                personelalt3()##bunlar fonksiyon yukarda bulabilirsin
        if anamenu == "2":
            print('1-Servis Talep Ekleme\n2- Servis Talepleri Görüntüleme (Listeleme)\n3- Servis Talepleri Kapatma (Silme)')
            servisalt = input("Alt Menü Seçiniz: ")
            if servisalt == "1":
                servisalt1()#bunlar fonksiyon yukarda bulabilirsin
            if servisalt == "2":
                servisalt2()#bunlar fonksiyon yukarda bulabilirsin
            if servisalt == "3":
                servisalt3()#bunlar fonksiyon yukarda bulabilirsin
        if anamenu == "3":
            print('1-Müşteri Kaydı Ekleme\n2- Müşteri Kaydı Listeleme\n3- Müşteri Kaydı Silme')
            musterialt = input("Alt Menü Seçiniz: ")
            if musterialt == "1":
               musterialt1()#bunlar fonksiyon yukarda bulabilirsin
            if musterialt == "2":
               musterialt2()#bunlar fonksiyon yukarda bulabilirsin
            if musterialt == "3":
                musterialt3()#bunlar fonksiyon yukarda bulabilirsin
        if anamenu == "4":
            print('1-Müşteri Bakiye Sorgulama\n2- Müşteri Bakiyeleri Listeleme (Toplu Listeleme)')
            carialt = input("Alt Menü Seçiniz: ")
        if anamenu == "5" or anamenu == "q" or anamenu == "Q":
            print("Çıkış Yapıldı")
            quit()#çıkış yapıyor
      