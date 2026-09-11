# Gardrops Otonom Pazaryeri ve Takip Botu (2022 Arsivi)

> **Tarihce ve Gelistirme Notu:** Bu proje **2022 yilinda** e-ticaret pazaryerlerinde (Gardrops) organik magazalarin etkilesimini artirmak, geri takip sureclerini otonomlastirmak ve platformun arayuz sinirlamalarini asmak amaciyla gelistirilmis arsivlik bir otomasyon calismasidir.

---

## Projenin Ortaya Cikis Amaci (2022 Vaka Analizi)
2022 doneminde Gardrops platformu uzerinde satis yapan bireysel saticilarin karsilastigi temel problemler:
1. **Gorunurluk Siniri:** Urunlerin hedef kitleye ulasmasi icin manuel binlerce takip yapma zorunlulugu.
2. **Platform Arayuz Eksikligi:** Takipciler listesinde kaydirma yapildiginda DOM optimizasyonu eksikligi nedeniyle durumun hatali yansimasi.
3. **Sayfalama Limiti:** Platformun tek seferde en fazla ~3030 kullaniciya erisime izin vermesi.

---

## Sistem Mimarisi ve Moduller
- **Hizli Veri Cikarici (search.py - BeautifulSoup4 & Requests):** Magazalarin potansiyel musteri listesini DOM uzerinden hafif ve hizli sekilde kazir.
- **Otonom Etkilesim Motoru (ollow.py - Selenium WebDriver):** Hedef kullanici listesini otonom simulasyonla gezerek Takip Et butonunu tetikler.

---

## Kurulum ve Calistirma
`ash
pip install -r requirements.txt
python follow.py
`

---
## Arsiv ve Sorumluluk Reddi
Bu yazilim egitim ve otomasyon algoritmalarini inceleme amaciyla paylasilmistir. 2022 donemindeki web DOM yapisina gore tasarlanmistir.