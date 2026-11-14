import os
from laptop import Laptop
from pelanggan import Pelanggan
from sistem_toko import SistemToko

def inisialisasi_data_toko(toko: SistemToko):
    """Fungsi untuk mengisi data awal (katalog dummy) ke dalam sistem."""
    toko.tambah_laptop(Laptop("Asus", "Vivobook Go 14", "office", 6500000, 5))
    toko.tambah_laptop(Laptop("Lenovo", "IdeaPad Slim 3", "office", 7200000, 3))
    toko.tambah_laptop(Laptop("Acer", "Aspire 5", "office", 8000000, 0))  # Stok habis (uji validasi)
    toko.tambah_laptop(Laptop("Asus", "TUF Gaming F15", "gaming", 12500000, 4))
    toko.tambah_laptop(Laptop("Lenovo", "Legion Slim 5", "gaming", 16000000, 2))
    toko.tambah_laptop(Laptop("HP", "Victus 15", "gaming", 11000000, 3))
    toko.tambah_laptop(Laptop("Apple", "MacBook Air M1", "editing", 11500000, 2))
    toko.tambah_laptop(Laptop("MSI", "Prestige 14", "editing", 13500000, 1))

def main():
    toko = SistemToko()
    inisialisasi_data_toko(toko)

    while True:
        print("\n==================================================")
        print("   SISTEM KASIR & REKOMENDASI LAPTOP TOKO OFFLINE  ")
        print("==================================================")
        print("1. Lihat Semua Katalog Laptop")
        print("2. Cari Rekomendasi Laptop untuk Pembeli")
        print("3. Proses Transaksi Kasir (Pembayaran)")
        print("4. Keluar Sistem")
        print("==================================================")
        
        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            toko.tampilkan_semua_katalog()

        elif pilihan == "2":
            print("\n--- INPUT DATA PREFERENSI PEMBELI ---")
            nama = input("Masukkan Nama Pembeli: ").strip()
            
            # Validasi input budget agar program tidak crash jika salah ketik huruf
            while True:
                try:
                    budget = float(input("Masukkan Batas Budget Maksimal (Rp): "))
                    if budget <= 0:
                        print(">> Nominal budget harus lebih dari 0!")
                        continue
                    break
                except ValueError:
                    print(">> Error: Harap masukkan angka yang valid untuk budget!")

            print("\nPilihan Kategori Kebutuhan: [Office / Gaming / Editing]")
            kebutuhan = input("Masukkan Kategori Kebutuhan: ").strip()

            # Membuat objek Pelanggan
            pelanggan = Pelanggan(nama, budget, kebutuhan)
            pelanggan.input_preferensi()

            # Memproses pencarian rekomendasi
            hasil_rekomendasi = toko.cari_rekomendasi(pelanggan)

            # Menampilkan hasil output ke layar terminal
            print(f"\n================ HASIL REKOMENDASI UNTUK {nama.upper()} ================")
            if hasil_rekomendasi:
                print(f"Ditemukan {len(hasil_rekomendasi)} laptop yang sesuai kriteria:\n")
                for laptop in hasil_rekomendasi:
                    laptop.tampilkan_info()
            else:
                print(">> Maaf, tidak ada laptop yang sesuai kriteria budget/kategori atau stok sedang kosong.")

        elif pilihan == "3":
            print("\n================ MENU KASIR & PEMBAYARAN ================")
            toko.tampilkan_semua_katalog()
            
            if not toko.daftar_laptop:
                continue

            try:
                indeks_pilih = int(input("Masukkan nomor urut laptop yang ingin dibeli: ")) - 1
                if indeks_pilih < 0 or indeks_pilih >= len(toko.daftar_laptop):
                    print(">> Nomor urut laptop tidak valid!")
                    continue
                
                laptop_terpilih = toko.daftar_laptop[indeks_pilih]
                
                jumlah_beli = int(input(f"Masukkan jumlah unit yang ingin dibeli: "))
                uang_bayar = float(input("Masukkan nominal uang tunai dari pembeli (Rp): "))

                # Eksekusi transaksi kasir
                toko.proses_transaksi(laptop_terpilih, jumlah_beli, uang_bayar)

            except ValueError:
                print(">> Error: Masukkan angka yang valid untuk nomor, jumlah, atau uang bayar!")

        elif pilihan == "4":
            print("\nTerima kasih! Program selesai dijalankan.")
            break
        else:
            print(">> Pilihan menu tidak valid. Silakan pilih angka 1 sampai 4!")

if __name__ == "__main__":
    main()
