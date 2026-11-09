from laptop import Laptop
from pelanggan import Pelanggan

class SistemToko:
    """Class pengendali untuk mengelola katalog data laptop serta algoritma rekomendasi."""
    def __init__(self):
        self.daftar_laptop = []  # Menyimpan kumpulan objek Laptop

    def tambah_laptop(self, laptop: Laptop):
        """Method untuk memasukkan data laptop baru ke dalam katalog toko."""
        self.daftar_laptop.append(laptop)

    def cari_rekomendasi(self, pelanggan: Pelanggan):
        """
        Method logika rekomendasi berdasarkan kriteria:
        - Harga laptop <= Budget maksimal pelanggan
        - Kategori laptop == Kebutuhan pelanggan
        - Stok laptop > 0 (Tersedia)
        """
        rekomendasi = []
        for laptop in self.daftar_laptop:
            if (laptop.harga <= pelanggan.budget_maksimal and 
                laptop.kategori == pelanggan.kebutuhan and 
                laptop.stok > 0):
                rekomendasi.append(laptop)
        
        return rekomendasi

    def tampilkan_semua_katalog(self):
        """Method untuk menampilkan seluruh daftar produk laptop yang ada di toko."""
        print("\n================ DAFTAR KATALOG LAPTOP ================")
        if not self.daftar_laptop:
            print("Katalog laptop masih kosong.")
            return
        
        for idx, laptop in enumerate(self.daftar_laptop, start=1):
            print(f"No. {idx}")
            laptop.tampilkan_info()

rahel 
