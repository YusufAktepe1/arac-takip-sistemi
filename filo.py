from arac import Arac

class FiloYonetimi:
    def __init__(self):
        self.araclar=[]

    #araç ekleme fonksiyonu
    def arac_ekle(self,plaka,marka,model,kilometre,durum="parkta"):
        #aynı plakadan araç var mı.
        for arac in self.araclar:
            if arac.plaka == plaka.upper():
                return f"Hata: {plaka.upper()} plakalı araç filoda zaten mevcut!"
        yeni_arac=Arac(plaka,marka,model,kilometre,durum)
        self.araclar.append(yeni_arac)
        return f"Başarılı: {yeni_arac.plaka} plakalı araç filoya eklendi."

    def araclari_listele(self):
        if not self.araclar:
            return "filoda kayıtlı araç bulunamadı!"
        liste="\n--- ARAÇ FİLOSu LİSTESİ ---\n"
        for i,arac in enumerate(self.araclar, 1):
            liste +=f"{i}. {arac.arac_bilgisi()}\n"
        return liste

    def arac_guncelle(self,plaka,yeni_durum=None,yeni_km=None):
        for arac in self.araclar:
            if arac.plaka ==plaka.upper():
                if yeni_durum:
                    arac.durum = yeni_durum
                if yeni_km is not None:
                    arac.kilometre =int(yeni_km)
                return f"Başarılı: {arac.plaka} plakalı araç güncellendi."
        return "Hata: Belirtilen plaka numarasına sahip araç bulunamadı."

    def arac_sil(self,plaka):
        for arac in self.araclar:
            if arac.plaka== plaka.upper():
                self.araclar.remove(arac)
                return f"Başarılı: {arac.plaka} plakalı araç filodan silindi."
        return "Hata: Silinmek istenen araç bulunamadı."


        