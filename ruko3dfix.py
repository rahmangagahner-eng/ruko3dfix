#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SYDNEY 3D PRO v10.0
✅ Hanya pakai 3D terpanas
✅ Backtest akurasi tinggi
✅ Simpel & efektif
"""

import os
import json
from collections import Counter
from typing import List

# ──────────────────────────────────────────────────────────────
# Warna
# ──────────────────────────────────────────────────────────────
def colored(text, color="white", style="normal"):
    colors = {
        "red": 31, "green": 32, "yellow": 33, "blue": 34,
        "bright_red": 91, "bright_green": 92, "bright_yellow": 93,
    }
    styles = {"normal": 0, "bold": 1}
    c = colors.get(color, 37)
    s = styles.get(style, 0)
    return f"\033[{s};{c}m{text}\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ──────────────────────────────────────────────────────────────
# Simpan & Load
# ──────────────────────────────────────────────────────────────
DATA_FILE = "sydney_data.json"

def load() -> List[str]:
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f).get("results", [])
        except:
            pass
    return []

def save(history: List[str]):
    with open(DATA_FILE, "w") as f:
        json.dump({"results": history}, f)

# ──────────────────────────────────────────────────────────────
# Prediksi 3D Terpanas
# ──────────────────────────────────────────────────────────────
def prediksi_3d(history: List[str]) -> List[str]:
    if len(history) < 5:
        return ["123", "456", "789", "012", "345"]
    all_3d = [r[1:] for r in history]
    freq = Counter(all_3d)
    return [item[0] for item in freq.most_common(10)]

# ──────────────────────────────────────────────────────────────
# Backtest Otomatis
# ──────────────────────────────────────────────────────────────
def backtest(history: List[str]):
    if len(history) < 2:
        print(colored("Butuh minimal 2 data!", "red"))
        return
    correct = 0
    for i in range(1, len(history)):
        train = history[:i]
        actual = history[i][1:]
        pred = prediksi_3d(train)
        if actual in pred:
            correct += 1
    acc = correct / (len(history)-1) * 100
    print(colored(f"🎯 Akurasi: {correct}/{len(history)-1} → {acc:.1f}%", "green", "bold"))

# ──────────────────────────────────────────────────────────────
# Menu
# ──────────────────────────────────────────────────────────────
def menu():
    while True:
        clear()
        print(colored("🎯 SYDNEY 3D PRO v10.0", "yellow", "bold"))
        history = load()
        print(f"\n📁 Data: {len(history)} hasil")
        print("\n1. Tambah hasil manual")
        print("2. Prediksi 3D")
        print("3. Backtest otomatis")
        print("4. Hapus data")
        print("5. Keluar")

        choice = input("\nPilih: ").strip()
        if choice == "1":
            while True:
                inp = input("Hasil 4D (kosongkan selesai): ").strip()
                if not inp: break
                if inp.isdigit() and len(inp) == 4:
                    history.append(inp)
                    save(history)
                else:
                    print(colored("Format salah!", "red"))
        elif choice == "2":
            if len(history) < 5:
                print(colored("Butuh 5+ data!", "yellow"))
            else:
                pred = prediksi_3d(history)
                print(colored("\n🔥 10 ANGKA 3D KUAT:", "bright_yellow", "bold"))
                for i, p in enumerate(pred, 1):
                    print(f"{i:2}. {colored(p, 'green', 'bold')}")
            input("\nEnter...")
        elif choice == "3":
            backtest(history)
            input("\nEnter...")
        elif choice == "4":
            if input("Hapus semua? (y/t): ").lower() == 'y':
                if os.path.exists(DATA_FILE):
                    os.remove(DATA_FILE)
                print("Dihapus")
                time.sleep(1)
        elif choice == "5":
            print("Semoga tembus! 🍀")
            break

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nDihentikan.")
