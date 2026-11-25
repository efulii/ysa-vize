# Şekil 1 (nested CV akış şeması) ve Şekil 3 (MLP mimarisi) — rapor için kodla üretilir.
import sys, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
OUT = sys.argv[1] if len(sys.argv) > 1 else "."

# ---------------- Şekil 1 ----------------
fig, ax = plt.subplots(figsize=(11, 5.8)); ax.axis("off"); ax.set_xlim(0, 110); ax.set_ylim(0, 62)
def kutu(x, y, w, h, t, fc):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4", fc=fc, ec="#333", lw=.8))
    ax.text(x + w / 2, y + h / 2, t, ha="center", va="center", fontsize=8)
def ok(x1, y1, x2, y2): ax.annotate("", (x2, y2), (x1, y1), arrowprops=dict(arrowstyle="->", lw=.9))
kutu(2, 52, 22, 7, "bank-additional.csv\n4.119 gözlem\nduration çıkarıldı", "#eeeeee")
kutu(31, 54, 23, 5, "Development %80 (3.295)\nEDA, nested CV, nihai eğitim", "#cfe3f1")
kutu(31, 45.5, 23, 5, "Bağımsız Test %20 (824)\nkilitli; yalnızca son ölçüm", "#f4c7c3")
ok(24, 56, 31, 56.5); ok(24, 54, 31, 48)
kutu(60, 52, 24, 7, "Outer StratifiedKFold (3)\nOuter-Train | Outer-Eval", "#cfe3f1"); ok(54, 56.5, 60, 55.5)
kutu(60, 38, 24, 9, "Inner StratifiedKFold (3)\nMANUEL M1–M6 | RASTGELE R1–R6\n(iki ayrı arama, aynı katlar)", "#e3f0d8"); ok(72, 52, 72, 47)
kutu(57, 20, 30, 12, "Her eğitimde stratified ayrım:\n%85 fit → ön işleme fit + ağırlıklar\n%15 early-stop → BCE izlenir\nEarlyStopping(15) + ReduceLROnPlateau", "#fff2cc"); ok(72, 38, 72, 32)
kutu(90, 38, 18, 9, "İç doğrulama: AP\n→ yöntem başına\nen iyi aday", "#e3f0d8"); ok(84, 42.5, 90, 42.5)
kutu(90, 20, 18, 10, "Outer-Train'de refit\nOuter-Eval'de 1 ölçüm\n→ Mean ± SD (n=3)", "#cfe3f1"); ok(99, 38, 99, 30)
kutu(2, 22, 36, 13, "Tam development'ta iç CV (3) × 12 aday\n→ en yüksek mean AP = nihai (R3)\n→ 3 seed ile nihai eğitim\n(early-stop alt kümesi development içinden)", "#d9d2e9")
ok(31, 54, 22, 35.5)
kutu(2, 4, 52, 10, "test_predictions_locked.csv (etiketsiz) → ayrı GitHub commit'i (KİLİT)\n→ ancak sonra test metrikleri, ROC/PR, confusion matrix, bootstrap %95 GA", "#f4c7c3")
ok(20, 22, 20, 14.5); ok(47, 45.5, 47, 14.5)
fig.savefig(f"{OUT}/sekil1_akis_semasi.png", dpi=200, bbox_inches="tight"); plt.close(fig)

# ---------------- Şekil 3 ----------------
d, h = 61, 32
katman = [d, h, 1]
ad = [f"Girdi\n{d} özellik", f"Gizli katman\n{h} nöron × ReLU", "Çıkış\n1 logit → sigmoid"]
fig, ax = plt.subplots(figsize=(8, 4)); ax.axis("off"); ax.set_xlim(0, 1); ax.set_ylim(-.14, 1.05)
xs = [.12, .5, .88]
ys = [np.linspace(.08, .78, min(n, 8)) if n > 1 else np.array([.43]) for n in katman]
for k in range(2):
    for a in ys[k]:
        for b in ys[k + 1]: ax.plot([xs[k], xs[k + 1]], [a, b], c="#bbb", lw=.3, zorder=1)
for k in range(3):
    ax.scatter([xs[k]] * len(ys[k]), ys[k], s=120, c="#cfe3f1", edgecolors="#333", linewidths=.7, zorder=2)
    if katman[k] > 8: ax.text(xs[k], .0, "⋮", ha="center", fontsize=13)
    ax.text(xs[k], .99, ad[k], ha="center", va="top", fontsize=9)
ax.text(.5, -.11, f"Öğrenilebilir parametre: {d}×{h} + {h} = {d*h+h}  ve  {h}×1 + 1 = {h+1}  →  toplam {d*h+h+h+1}", ha="center", fontsize=9)
fig.savefig(f"{OUT}/sekil3_mlp_mimari.png", dpi=200, bbox_inches="tight"); plt.close(fig)
print("ok")
