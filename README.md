# YSA Vize Projesi – MLP ile Sınıflandırma (Bank Marketing)

Öğrenci: Elif Öztürk · No: 244329059 · Temel seed: 31085 (= 29059 + 2026)

Veri: UCI Bank Marketing, yalnızca `bank-additional.csv` (repoya eklenmedi).
Kaynak: https://archive.ics.uci.edu/dataset/222/bank+marketing (DOI 10.24432/C5K306)

## Bu aşamadaki dosyalar
| Dosya | İçerik |
|---|---|
| `Yapay_Sinir_Aglari_Vize.ipynb` | Split, development-only EDA, kat-içi ön işleme, PyTorch MLP, nested CV |
| `dataset_split.csv` | Orijinal satır indeksleri ve development/test ataması |
| `manual_configs.json`, `random_configs.json` | M1–M6 manuel ve R1–R6 rastgele adaylar |
| `inner_cv_results.csv` | Her aday ve iç kat için AP, en iyi epoch, süre |
| `outer_cv_results.csv` | Dış CV kat sonuçları (MLP-manuel, MLP-rastgele, LogReg, Dummy) |
| `final_selection.json` | Tam development iç CV'si ile seçilen nihai konfigürasyon (R3) |

Not: Adaylar nested CV'den önceki ayrı bir notebook hücresinde üretildi ve değiştirilmedi;
ancak nested CV'den önce ayrı bir commit ile kaydedilmedi.
