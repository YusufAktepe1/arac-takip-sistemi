from filo import FiloYonetimi
def main():
    filo=FiloYonetimi()

    while True:
        print("\n--- ARAÇ FİLO VE BAKIM YÖNETİM SİSTEMİ ---")
        print("1. Araç Ekle (Create)")
        print("2. Araçları Listele (Read)")
        print("3. Araç Güncelle - KM veya Durum (Update)")
        print("4. Araç Sil (Delete)")
        print("5. Çıkış")
        
        secim = input("Lütfen bir işlem seçiniz (1-5): ")

        if secim =="1":
            plaka=input("plaka: ")
            marka=input("marka: ")
            model=input("model: ")
            kilometre=input("kilometre: ")
            durum=input("Durum (Aktif / Serviste / Parkta - Boş bırakırsan 'Parkta' olur): ")
            if durum.split():
                sonuc=filo.arac_ekle(plaka,marka,model,kilometre)
            else:
                sonuc=filo.arac_ekle(plaka,marka,model,kilometre,durum)
            print(f"\n{sonuc}")

        elif secim =="2":
            print(filo.araclari_listele())
        elif secim == "3":
            plaka = input("Güncellenecek Araç Plakası: ")
            yeni_durum = input("Yeni Durum (Aktif/Serviste/Parkta - Değiştirmek istemiyorsan Enter'a bas): ")
            yeni_km = input("Yeni Kilometre (Değiştirmek istemiyorsan Enter'a bas): ")
            
            # Boş bırakılan alanları None yapıyoruz ki arka planda eski veriler bozulmasın
            durum_arg = yeni_durum if yeni_durum.strip() != "" else None
            km_arg = yeni_km if yeni_km.strip() != "" else None

            sonuc = filo.arac_guncelle(plaka, yeni_durum=durum_arg, yeni_km=km_arg)
            print(f"\n👉 {sonuc}")

        elif secim =="4":
            plaka =input("silinecek Arac Plakası:")
            sonuc=filo.arac_sil(plaka)
            print(f"\n{sonuc}")

        elif secim=="5":
            print("sistemden çıkılıyor iyi günler.")
            break
        else:
            print("yanlış secim lütfen tekrar deneyin...")

if __name__ =="__main__":
    main()


