#!/usr/bin/env python3
"""Konverter Satuan CLI — panjang, berat, dan suhu (Bahasa Indonesia)."""

# Faktor ke satuan dasar: panjang -> meter, berat -> kilogram
PANJANG = {"km": 1000.0, "m": 1.0, "cm": 0.01, "mm": 0.001, "mi": 1609.344}
BERAT = {"kg": 1.0, "g": 0.001, "ton": 1000.0, "lb": 0.45359237}


def konversi_linear(nilai, asal, tujuan, tabel):
    """Konversi lewat satuan dasar: nilai * faktor_asal / faktor_tujuan."""
    return nilai * tabel[asal] / tabel[tujuan]


def konversi_suhu(nilai, asal, tujuan):
    """Konversi suhu lewat Celsius sebagai satuan perantara."""
    if asal == tujuan:
        return nilai
    # ke Celsius
    if asal == "C":
        c = nilai
    elif asal == "F":
        c = (nilai - 32) * 5 / 9
    elif asal == "K":
        c = nilai - 273.15
    else:
        raise ValueError(f"Satuan suhu tidak dikenal: {asal}")
    # dari Celsius
    if tujuan == "C":
        return c
    if tujuan == "F":
        return c * 9 / 5 + 32
    if tujuan == "K":
        return c + 273.15
    raise ValueError(f"Satuan suhu tidak dikenal: {tujuan}")


def tanya_satuan(prompt, pilihan):
    while True:
        s = input(prompt).strip()
        # suhu pakai huruf besar C/F/K, satuan lain huruf kecil
        s_norm = s.upper() if set(pilihan) <= {"C", "F", "K"} else s.lower()
        if s_norm in pilihan:
            return s_norm
        print(f"  Satuan tidak valid. Pilihan: {', '.join(pilihan)}")


def tanya_angka(prompt):
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("  Masukkan angka yang valid.")


def jalankan_kategori(nama, tabel, fungsi_suhu=False):
    pilihan = list(tabel)
    print(f"\n--- {nama} ---  Satuan: {', '.join(pilihan)}")
    nilai = tanya_angka("Nilai yang mau dikonversi: ")
    asal = tanya_satuan("Satuan asal: ", pilihan)
    tujuan = tanya_satuan("Satuan tujuan: ", pilihan)
    if fungsi_suhu:
        hasil = konversi_suhu(nilai, asal, tujuan)
    else:
        hasil = konversi_linear(nilai, asal, tujuan, tabel)
    print(f"Hasil: {nilai:g} {asal} = {hasil:.6g} {tujuan}")


def main():
    suhu = {"C": None, "F": None, "K": None}
    while True:
        print("\n=== KONVERTER SATUAN ===")
        print("1. Panjang (km/m/cm/mm/mi)")
        print("2. Berat (kg/g/ton/lb)")
        print("3. Suhu (C/F/K)")
        print("0. Keluar")
        pilih = input("Pilih kategori (0-3): ").strip()
        if pilih == "1":
            jalankan_kategori("Panjang", PANJANG)
        elif pilih == "2":
            jalankan_kategori("Berat", BERAT)
        elif pilih == "3":
            jalankan_kategori("Suhu", suhu, fungsi_suhu=True)
        elif pilih == "0":
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()
