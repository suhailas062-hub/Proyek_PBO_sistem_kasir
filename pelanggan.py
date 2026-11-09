class Pelanggan:
    """Class untuk mengelola data preferensi pembeli yang dilayani oleh staf toko."""
    def __init__(self, nama: str, budget_maksimal: float, kebutuhan: str):
        self.nama = nama
        self.budget_maksimal = budget_maksimal
        self.kebutuhan = kebutuhan.lower().strip()  # Membersihkan spasi dan menyeragamkan teks

    def input_preferensi(self):
        """Method untuk menampilkan ringkasan data preferensi pembeli."""
        print(f"\n--- Data Preferensi Pembeli ---")
        print(f"Nama Pelanggan  : {self.nama}")
        print(f"Budget Maksimal : Rp {self.budget_maksimal:,.0f}")
        print(f"Kebutuhan Utama : {self.kebutuhan.capitalize()}")
        print("-" * 35)
