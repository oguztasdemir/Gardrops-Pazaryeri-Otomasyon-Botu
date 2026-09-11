# 🛍️ Gardrops Otonom Pazaryeri & Takip Suite (2022 Arşivi)

> 📅 **Tarihçe & Geliştirme Notu:** Bu repo, **2022 yılında** e-ticaret pazaryerinde (Gardrops) mağaza görünürlüğünü artırmak, geri takip (follow-for-follow) süreçlerini otonomlaştırmak ve platformun o dönemki teknik kısıtlarını aşmak amacıyla geliştirilmiş 3 farklı otomasyon modülünün orijinal klasör hiyerarşisiyle korunmuş arşiv sürümüdür.

---

## 📁 Proje Klasör Hiyerarşisi & Modüller

Bu depoda 2022 yılında geliştirilen **3 bağımsız yaklaşım** yer almaktadır:

```text
Gardrops-Otomasyon-Botu/
├── Gardrops Fonksiyonel Bot (BS4)/       # BeautifulSoup4 & Requests tabanlı hızlı DOM kazıyıcı
│   ├── search.py                        # Hedef kitleyi hızla tarayıp listelere ayrıştıran motor
│   ├── follow.py                        # Filtrelenen profillere otonom istek gönderici
│   ├── Lists/                           # Taranan ve takip edilen kullanıcı önbellekleri
│   └── kullanici.py                     # Hesap ve hedef mağaza parametreleri
│
├── Gardrops Fonksiyonel Bot (Selenium)/  # Tam otonom tarayıcı simülasyonu
│   ├── follow.py                        # Canlı Chrome oturumuyla gerçek kullanıcı aksiyonları
│   └── Lists/                           # Oturum listeleri
│
└── Gardrops Geri Takip Botu/             # Karşılıklı takip (GT) kontrolü ve takibi bırakanlar
    ├── search.py                        # Takipçi ve takip edilen diferansiyel analizi
    ├── main.py                          # Otomasyon başlatıcı
    └── Lists/                           # Analiz sonuç listeleri
```

---

## 🎯 2022 Vaka Analizi & Çözülen Problemler

2022 döneminde Gardrops platformunda butik satıcıların karşılaştığı darboğazlar:
1. **Görünürlük & Satış Limiti:** Mağazadaki ürünlerin öne çıkması için her gün yüzlerce potansiyel alıcının profiline manuel girip takip etme zorunluluğu.
2. **Platform Arayüz Eksikliği (DOM Bug):** Takipçiler sayfasında aşağı kaydırma yapıldığında platformun DOM güncelleme hatasından dolayı daha önce takip edilen kullanıcıların sanki takip edilmemiş gibi görünmesi.
3. **Sayfalama Limiti (Pagination):** Gardrops arayüzünün tek oturumda en fazla 3030 kullanıcıyı listelemesi; kalan kullanıcıların arayüzde kaybolması.

### 💡 Mühendislik Çözümü: Diferansiyel Önbellekleme
Yukarıdaki hataları aşmak için `Lists/` dizininde **diferansiyel metin önbelleği** kurgulanmıştır:
- Taranan her kullanıcı anlık kaydedilir (`Gardrops_tur.txt`).
- Genel havuzla (`Gardrops_total.txt`) karşılaştırılarak daha önce taranmış olanlar elenir.
- Sadece yeni ve benzersiz profillere etkileşim uygulanarak mükerrer işlem yapılması engellenir.

---

## 🚀 Kurulum & Çalıştırma

### Bağımlılıkları Yükleyin:
```bash
pip install -r requirements.txt
```

### Modülleri Çalıştırma:
İlgili modülün klasörüne girerek ayarları yapıp çalıştırabilirsiniz:

```bash
# 1. Hızlı BS4 Kazıyıcı Modülü:
cd "Gardrops Fonksiyonel Bot (BS4)"
python search.py

# 2. Selenium Otonom Takip Modülü:
cd "../Gardrops Fonksiyonel Bot (Selenium)"
python follow.py

# 3. Geri Takip Kontrol Modülü:
cd "../Gardrops Geri Takip Botu"
python main.py
```

---

## ⚠️ Arşiv & Sorumluluk Reddi
*Bu proje yazılım mimarisi, veri analitiği ve web otomasyonu tarihçesi amacıyla eğitim amaçlı açık kaynak olarak paylaşılmıştır. 2022 yılındaki DOM mimarisine göre kodlanmıştır.*
