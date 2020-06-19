import pymysql.cursors
# Veritabanı bağlantı bilgileri
db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='biyomedic',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
baglanti = db.cursor()
# Veritabanı bağlantı bilgileri


giris_hak = 3
print("Lütfen giriş yapınız!")
kul_ad = input("Kullanıcı Adı: ")
kul_pass = input("Kullanıcı Şifre: ")
baglanti.execute("SELECT * FROM personel WHERE personel_username='"+kul_ad+"' AND personel_sifre ='"+kul_pass+"'")
kullanicilar = baglanti.fetchall()
for i in kullanicilar:
      if kullanicilar:
        print("Giriş Yapıldı! Çıkış yapmak için -Q-")
        print('1-Personel İşlemleri\n2- Servis Talep İşlemleri\n3- Müşteri İşlemleri\n4-Cari Hesap İşlemleri\n5-Çıkış')
        anamenu = input("Menü Seçiniz: ")
        if anamenu == "1":
            print('1-Personel Ekleme\n2- Personel Listeleme\n3- Personel Silme')
            personelalt = input("Alt Menü Seçiniz: ")
            if personelalt == "1":
                baglanti.execute("SELECT * FROM personel ORDER BY personel_id DESC LIMIT 1")
                sonpersonel = baglanti.fetchall()
                for p in sonpersonel:
                    lastusername = p['personel_username']
                    lastpassword = p['personel_sifre']
                    sondeger = lastusername[7:10]
                    sifresondeger = lastpassword[3:8]
                    intdeger = int(sondeger)
                    intdegersifre = int(sifresondeger)
                    sondeger2 = intdeger + 1
                    sondeger2sifre = intdegersifre + 1
                    strd = str(sondeger2)
                    strd2 = str(sondeger2sifre)
                    sonuc = baglanti.execute('INSERT INTO personel VALUES(%s,%s,%s)',(None,'biyoser'+strd,'bct'+strd2))
                    db.commit()
                    print(str(sonuc) + " kullanıcı eklendi")
            if personelalt == "2":
                baglanti.execute("SELECT * FROM personel")
                sonpersonel = baglanti.fetchall()
                for p2 in sonpersonel:
                    print("Kullanıcı Adı: " + p2['personel_username'] + " --- " + "Şifre: " + p2['personel_sifre'])
            if personelalt == "3": 
                silid = input("Kullanıcı Adı Seçiniz: ")
                personelsil = baglanti.execute('DELETE FROM personel WHERE personel_username = %s',(silid,))
                db.commit()
                print(str(personelsil) + " kullanıcı silindi")

        if anamenu == "2":
            print('1-Servis Talep Ekleme\n2- Servis Talepleri Görüntüleme (Listeleme)\n3- Servis Talepleri Kapatma (Silme)')
            servisalt = input("Alt Menü Seçiniz: ")
            if servisalt == "1":
                talep = input("Talep Giriniz: ")
                talepnot = input("Not Giriniz: ")
                servistalebi = baglanti.execute('INSERT INTO servistalepleri VALUES(%s,%s,%s)',(None,talepnot,talep))
                db.commit()
                servistalebidevam = baglanti.execute('INSERT INTO servistalepleridevam VALUES(%s,%s,%s)',(None,talepnot,talep))
                db.commit()
                print(str(servistalebi) + " servis talebi eklendi")
            if servisalt == "2":
                baglanti.execute("SELECT * FROM servistalepleri")
                sonpersonel = baglanti.fetchall()
                for t1 in sonpersonel:
                    print("Talep: " +  t1['servistalepleri_talep']+ " --- " + "Not: " +  t1['servistalepleri_not'])
            if servisalt == "3":
                siltalep = input("Silmek İstediğiniz Talep Id siniz yazınız: ")
                baglanti.execute("SELECT * FROM servistalepleridevam WHERE servistalepleridevam_id ='"+siltalep+"'")
                devamtalebi = baglanti.fetchall()
                for t1 in devamtalebi:
                    sonuc = baglanti.execute('INSERT INTO servistalepleribiten VALUES(%s,%s,%s)',(None,t1['servistalepleridevam_not'],t1['servistalepleridevam_talep']))
                    db.commit()
                    print(str(sonuc) + "talep bitmiş olarak güncellendi")
                sonuc = baglanti.execute('DELETE FROM servistalepleridevam WHERE servistalepleridevam_id = %s',(siltalep,))
                db.commit()
                print(str(sonuc) + " kullanıcı silindi")
        if anamenu == "3":
            print('1-Müşteri Kaydı Ekleme\n2- Müşteri Kaydı Listeleme\n3- Müşteri Kaydı Silme')
            musterialt = input("Alt Menü Seçiniz: ")
            if musterialt == "1":
                musterilistesi_hastanead = input("Hastane Ad Giriniz: ")
                musterilistesi_yetkiliad = input("Yetkili Ad Giriniz: ")
                musterilistesi_telno = input("Tel No Giriniz: ")
                musterilistesi_mail = input("Mail Giriniz: ")
                musterilistesi_adres = input("Adres Giriniz: ")
                servistalebi = baglanti.execute('INSERT INTO musterilistesi VALUES(%s,%s,%s,%s,%s,%s)',(None,musterilistesi_hastanead,musterilistesi_yetkiliad,musterilistesi_telno,musterilistesi_mail,musterilistesi_adres))
                db.commit()
                print(str(servistalebi) + " Müşteri eklendi")
            if musterialt == "2":
                baglanti.execute("SELECT * FROM musterilistesi")
                sonpersonel = baglanti.fetchall()
                for t1 in sonpersonel:
                    print("Hastane Ad: " +  t1['musterilistesi_hastanead']+ " --- " + "Yetkili Ad: " +  t1['musterilistesi_yetkiliad']+ " --- " + "Tel No: " +  t1['musterilistesi_telno']+ " --- " + "Mail: " +  t1['musterilistesi_mail']+ " --- " + "Adres: " +  t1['musterilistesi_adres'])
            if musterialt == "3":
                silmusteri = input("Silmek İstediğiniz Müşteri Id siniz yazınız: ")
                sonuc = baglanti.execute('DELETE FROM musterilistesi WHERE musterilistesi_id = %s',(silmusteri,))
                db.commit()
                print(str(sonuc) + " müşteri silindi")
        if anamenu == "4":
            print('1-Müşteri Bakiye Sorgulama\n2- Müşteri Bakiyeleri Listeleme (Toplu Listeleme)')
            carialt = input("Alt Menü Seçiniz: ")
        if anamenu == "5" or anamenu == "q" or anamenu == "Q":
            print("Çıkış Yapıldı")
            quit()
    
       