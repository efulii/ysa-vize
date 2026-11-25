# YSA Vize Projesi – MLP ile Sınıflandırma (Bank Marketing)

**Elif Öztürk** · Öğrenci No: 244329059 · Temel seed: **31085** (= 29059 + 2026)

PyTorch MLP ile UCI Bank Marketing (`bank-additional.csv`) veri setinde ikili sınıflandırma:
development-only EDA, kat-içi (fold-local) ön işleme, 6 manuel + 6 rastgele hiperparametre adayı,
3×3 nested cross-validation, GitHub'da kilitlenmiş bağımsız test, bootstrap güven aralıkları.
Teknik rapor: [`report.pdf`](report.pdf).

## Veri
Ham veri repoya eklenmedi. Kaynak: Moro, Rita ve Cortez (2014), UCI Machine Learning Repository,
https://archive.ics.uci.edu/dataset/222/bank+marketing (DOI 10.24432/C5K306).
Yalnızca `bank-additional/bank-additional.csv` kullanılır (4.119 satır, 451 "yes"); `-full` sürümü kullanılmaz.
Notebook'ların ilk hücresi dosya çalışma klasöründe yoksa resmi zip'ten otomatik indirir.

## Çalıştırma (Google Colab)
Notebook'ları sırayla, aynı Colab oturumunda çalıştırın (Çalışma zamanı → Tümünü çalıştır):

| Sıra | Notebook | Ne yapar | Ana çıktılar |
|---|---|---|---|
| 1 | `01_eda.ipynb` | Veri okuma, `duration`'ı çıkarma, %80/%20 stratified bölünme, development-only EDA, hipotezler | `dataset_split.csv` |
| 2 | `02_nested_cv.ipynb` | Kat-içi ön işleme, PyTorch MLP, M1–M6 ve R1–R6 adayları, 3×3 nested CV, referans modeller, tam development iç CV ile nihai seçim | `manual_configs.json`, `random_configs.json`, `inner_cv_results.csv`, `outer_cv_results.csv`, `final_selection.json` |
| 3 | `03_final_test.ipynb` | Nihai model (3 seed), etiketsiz kilitli tahminler, **kilit kontrolü**, test metrikleri, bootstrap %95 GA, confusion matrix, ROC/PR, hata analizi, rapor tabloları ve şekilleri | `test_predictions_locked.csv`, `final_hyperparameters.json`, `results/*`, `figures/*` |

`02` ve `03`, Drive'daki `MyDrive/YSA_Vize_cikti` klasörünü ara sonuçlar için kullanır (Google Drive bağlama izni istenir).
Şekil 1 (akış şeması) ve Şekil 3 (MLP mimarisi) `tools/sekil1_3_uret.py` ile üretilir: `python tools/sekil1_3_uret.py figures`.

## Kilitli test (zaman sıralı kayıt)
| Commit | Tarih (UTC) | İçerik |
|---|---|---|
| `5a850c5` | 23.11.2026 11:06 | Split, EDA, M1–M6 / R1–R6 adayları, nested CV sonuçları, nihai seçim (R3) |
| `e1dde65` | 23.11.2026 11:19 | **KİLİT:** `kilit/test_predictions_locked.csv` (etiketsiz), `final_hyperparameters.json`, eğitim geçmişleri |
| sonraki | — | Test metrikleri, şekiller, rapor, notebook düzeni |

Test etiketleri yalnızca kilit commit'inden sonra okunmuştur. `03_final_test.ipynb`, yeniden ürettiği tahminleri
GitHub'daki kilitli dosyayla karşılaştırır (en büyük fark < 1e-6). Test etiketleri kamuya açık olduğundan bu, kör test değil,
zaman sıralı bir deney kaydıdır. Not: aday konfigürasyonlar nested CV'den önceki ayrı bir notebook hücresinde üretilmiş,
ancak nested CV'den önce ayrı bir commit ile kaydedilmemiştir (ilk commit'te sonuçlarla birlikte yüklenmiştir).

## Seed politikası
| Amaç | Seed |
|---|---|
| Dev/test bölünmesi | 31085 |
| PyTorch ağırlık başlangıcı (ana) | 31087 (= +2) |
| Dış CV · İç CV | 31089 (+4) · 31090 (+5) |
| Erken durdurma alt kümesi (%15) | 31091 (+6) |
| Random Search (sgd / adam / adamw) | 31092 / 31093 / 31094 (+7+i) |
| Bootstrap | 31093 (+8) |
| Nihai kararlılık seed'leri | 31087 (ana), 31187, 31287 |

CPU'da `torch.use_deterministic_algorithms(True)` ve tek iş parçacığı kullanılır.

## Klasörler
| Yol | İçerik |
|---|---|
| `01_eda.ipynb`, `02_nested_cv.ipynb`, `03_final_test.ipynb` | Ödevin istediği üç notebook (Colab çıktılarıyla) |
| `Yapay_Sinir_Aglari_Vize.ipynb` | Tüm adımları içeren ilk geliştirme notebook'u (ilk commit) |
| `configs/` | M1–M6, R1–R6 ve arama uzayı / eğitim ayarları |
| kök dizindeki `*.csv`, `*.json` | Nested CV aşamasının çıktıları (ilk commit): `dataset_split.csv`, `inner_cv_results.csv`, `outer_cv_results.csv`, `final_selection.json` |
| `kilit/` | Kilitli test tahminleri ve kilit anındaki notebook (commit `e1dde65`) |
| `results/` | Test metrikleri, bootstrap GA, seed kararlılığı, hata analizi, rapor tabloları (Excel), ortam sürümleri |
| `figures/` | Rapordaki şekiller |
| `tools/` | Şekil 1 ve 3'ü üreten betik |
| `report.pdf` | Teknik rapor |

Rapordaki şekil numaraları ↔ dosyalar: Şekil 1 `sekil2a`, 2 `sekil2b`, 3 `sekil2c`, 4 `sekil1_akis_semasi`,
5 `sekil3_mlp_mimari`, 6 `sekil5_manuel_vs_rastgele`, 7 `sekil4_egitim_egrileri`, 8 `sekil5b_dis_cv`,
9 `sekil6_confusion_matrix`, 10 `sekil7_roc_pr`.

## Özet sonuçlar
| | AP | ROC-AUC |
|---|---|---|
| Dış CV – MLP manuel arama | 0,397 ± 0,017 | 0,758 ± 0,030 |
| Dış CV – MLP rastgele arama | 0,396 ± 0,015 | 0,755 ± 0,032 |
| Dış CV – Logistic Regression | 0,422 ± 0,030 | 0,762 ± 0,009 |
| Test – MLP R3 (seed 31087) | 0,401 [0,306; 0,510] | 0,766 [0,707; 0,826] |
| Test – MLP R3, 3 seed | 0,394 ± 0,006 | 0,761 ± 0,005 |
| Test – Logistic Regression | 0,390 [0,295; 0,506] | 0,770 [0,712; 0,829] |

## Ortam
Google Colab (CPU): Python 3.13.18, PyTorch 2.14.1, scikit-learn 1.6.1, NumPy 2.4.6, pandas 2.2.3,
SciPy 1.16.3, matplotlib 3.10.0 (`results/ortam_surumleri.json`). Tam akış CPU'da birkaç dakika sürer.

## Yapay zekâ kullanımı
Deney düzeninin öğrenilmesi, kodun hazırlanması ve rapor metninin taslağı için yapay zekâ asistanından
(Anthropic Claude) destek alınmıştır. Deneyler Google Colab'da çalıştırılmış; tüm sayılar kodun gerçek çıktılarıdır.
