class Arac:
    def __init__(self,plaka,marka,model,kilometre,durum="parkta"):
        self.plaka=plaka.upper()
        self.marka=marka
        self.model=model
        self.kilometre = int(kilometre)
        self.durum=durum

    def arac_bilgisi(self):
        return f"Plaka: {self.plaka} | Marka/Model: {self.marka} {self.model} | KM: {self.kilometre} | Durum: {self.durum}"

    