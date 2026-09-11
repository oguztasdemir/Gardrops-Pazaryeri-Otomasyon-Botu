# 🛍️ Gardrops Otonom Pazaryeri & Takip Suite (2022 Arşivi)

> 📅 **Tarihçe & Geliştirme Notu:** Bu proje, **2022 yılında** e-ticaret pazaryerinde (Gardrops) mağaza etkileşimini ve satış dönüşümlerini artırmak, geri takip (follow-for-follow) süreçlerini otonomlaştırmak ve platformun o dönemki teknik arayüz kısıtlarını aşmak amacıyla geliştirilmiş en kapsamlı (V3 - BeautifulSoup4 + Selenium Hibrit) otomasyon çalışmasıdır.

---

## 🎯 2022 Vaka Analizi & Çözülen Problemler

2022 döneminde Gardrops platformunda butik satıcıların karşılaştığı temel darboğazlar:
1. **Görünürlük Sınırı:** Mağazadaki ürünlerin hedef kitleye ulaşması için her gün yüzlerce potansiyel alıcının profiline manuel girip takip etme zorunluluğu.
2. **Platform Arayüz Eksikliği (DOM Bug):** Takipçiler sayfasında aşağı kaydırma yapıldığında platformun DOM güncelleme hatasından dolayı daha önce takip edilen kullanıcıların durumunun listede hatalı yansıması.
3. **Sayfalama Limiti (Pagination):** Gardrops arayüzünün tek oturumda en fazla 3030 kullanıcıyı listelemesi; kalan kullanıcıların arayüzde kaybolması.

---

## 🏗️ Sistem Mimarisi & Gelişmiş Özellikler (V3 Hibrit Model)

Bu sürüm, önceki saf Selenium botlarının yavaşlığını aşmak üzere **hibrit** olarak kurgulanmıştır:

1. **Hızlı DOM Kazıyıcı (`search.py` - BeautifulSoup4 & Requests):**
   - Hedef mağazaların potansiyel müşteri listesini saniyeler içinde tarar ve listelere ayrıştırır.
2. **Otonom Tarayıcı Motoru (`follow.py` - Selenium WebDriver):**
   - Ayrıştırılan kullanıcı profillerine otonom girerek "Takip Et" butonunu tetikler.
3. **Mükerrerlik Önleyici Diferansiyel Önbellek (`Lists/`):**
   - `Gardrops_tur.txt` ve `Gardrops_total.txt` karşılaştırması yaparak daha önce taranan veya takip edilen profillere mükerrer işlem yapılmasını %100 engeller.
4. **Çok Kanallı Bildirim Sistemi (E-Posta & Mobil Push):**
   - İşlemler tamamlandığında Gmail (SMTP) ve mobil bildirim servisi üzerinden geliştiriciye anlık durum raporu gönderir.

---

## 📁 Proje Dosya Yapısı

```text
Gardrops-Otomasyon-Botu/
├── search.py          # Hızlı BeautifulSoup4 kullanıcı kazıma motoru
├── follow.py          # Selenium otonom profil takip motoru
├── search_main.py     # Kazıma başlatıcı
├── follow_main.py     # Takip başlatıcı
├── kullanici.py       # Hesap, hedef mağaza ve filtreleme ayarları
├── bildirim.txt       # Mobil push bildirim servis konfigürasyonu
├── Lists/             # Taranan, takip edilen ve GT durum önbellekleri
├── requirements.txt   # Python kütüphane bağımlılıkları
└── README.md          # 2022 vaka analizi ve dokümantasyon
```

---

## 🚀 Kurulum & Çalıştırma

### 1. Bağımlılıkları Yükleyin:
```bash
pip install -r requirements.txt
```

### 2. Yapılandırma:
`kullanici.py` dosyasını açarak giriş bilgilerinizi ve hedef mağaza kullanıcı adını girin.

### 3. Başlatma:
```bash
# Adım 1: Hedef kullanıcıları hızlıca listeye çıkarın:
python search_main.py

# Adım 2: Otonom takip sürecini başlatın:
python follow_main.py
```

---

## ⚠️ Arşiv & Sorumluluk Reddi
*Bu yazılım eğitim, veri madenciliği ve web otomasyonu tarihçesi amacıyla açık kaynak olarak paylaşılmıştır. 2022 yılındaki DOM yapısına göre tasarlanmıştır.*
