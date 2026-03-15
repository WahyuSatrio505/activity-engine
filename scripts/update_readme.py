import random
import os
from datetime import datetime

quotes = [
"Kode yang baik bukan hanya berjalan, tapi mudah dipahami. -- wahyu ",
"Debugging adalah seni menemukan kesalahan yang kita buat sendiri.",
"Fokus + Konsisten = Keahlian ,Tercapainya Tujuan",
"Konsisten diatas segalanya..."
]

tips_ai = [
"Pelajari Python jika ingin masuk dunia AI.",
"Pahami konsep data structure sebelum machine learning.",
"Model AI bagus berasal dari data yang bagus.",
"Biasakan membaca dokumentasi."
]

catatan = [
"Hari ini belajar tentang GitHub Actions  (GIT). ",
"Mencoba memahami automation workflow.",
"Belajar sedikit tentang scripting Python.",
"Menjelajahi cara kerja CI/CD."
]

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

quote = random.choice(quotes)
tip = random.choice(tips_ai)
note = random.choice(catatan)

readme = f"""
# Activity Engine Wahyu 🚀

Repository ini melakukan update otomatis setiap hari menggunakan GitHub Actions.

## Update Terakhir
{now}

## Quote Programming Hari Ini
{quote}

## Tips AI
{tip}

## Catatan Belajar
{note}

---

Repository ini diperbarui otomatis oleh sistem automation.
"""

with open("README.md","w") as f:
    f.write(readme)

os.makedirs("data", exist_ok=True)

with open("data/log.md","a") as f:
    f.write(f"\n{now} - Update otomatis berhasil.")