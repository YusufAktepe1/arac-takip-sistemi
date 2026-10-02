# 🚗 Araç Filo ve Bakım Yönetim Sistemi (Fleet Management System)

Python kullanarak nesne yönelimli programlama (OOP) ilkeleriyle geliştirilmiş, konsol tabanlı ve modüler bir **Araç Filo ve Bakım Yönetim Sistemi**dir. Proje, temel CRUD (Create, Read, Update, Delete) operasyonlarını ve otomatik test süreçlerini barındırmaktadır.

## 📂 Proje Mimarisi

Proje, sorumlulukların ayrılması (separation of concerns) prensibine uygun olarak modüler bir yapıda tasarlanmıştır:

* **`arac.py`**: Araç nesnesinin niteliklerini (Plaka, marka, model, kilometre, durum) ve bilgi verme metodunu barındıran sınıf.
* **`filo.py`**: Araçların listelendiği, eklendiği, güncellendiği ve silindiği tüm CRUD mantığını yöneten arka plan sınıfı.
* **`main.py`**: Kullanıcının terminal üzerinden menü aracılığıyla sistemi yönetmesini sağlayan konsol arayüzü.
* **`test_filo.py`**: Pytest kütüphanesi kullanılarak yazılmış otomatik test dosyası.

## 🚀 Özellikler

* **Mükerrer Kayıt Koruması:** Aynı plakaya sahip araçların sisteme ikinci kez eklenmesi engellenir.
* **Otomatik Standardizasyon:** Plakalar otomatik olarak büyük harfe (`upper()`) çevrilerek veri tutarlılığı sağlanır.
* **Esnek Güncelleme:** Araçların kilometre ve durum (Aktif, Serviste, Parkta) bilgileri dinamik olarak güncellenebilir.
* **Otomatik Testler:** Pytest ile iş mantığının doğruluğu test edilir.

## 🛠️ Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. Depoyu klonlayın veya indirin:
   ```bash
   git clone <repo-linkiniz>
   cd arac-takip-sistemi