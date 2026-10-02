from filo import FiloYonetimi
from arac import Arac
def test_arac_ekleme():
    #test icin nesne
    filo=FiloYonetimi()

    mesaj=filo.arac_ekle("34ABC34","Toyota","Corolla",50000)

    assert len(filo.araclar) ==1
    assert filo.araclar[0].plaka =="34ABC34"
    assert "Başarılı" in mesaj

def Girilmiş_plakaEngeli():
    filo= FiloYonetimi()

    filo.arac_ekle("06ANK06","Renault","Megane",30000)
    mesaj =filo.arac_ekle("06ANK06","Honda","Civic",45000)
    #doğrulama
    assert "Hata " in mesaj
    assert len(filo.araclar)==1