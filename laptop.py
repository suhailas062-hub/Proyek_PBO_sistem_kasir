class Laptop:
    """Class untuk merepresentasikan entitas barang/laptop di toko."""
    def __init__(self, merk: str, tipe: str, kategori: str, harga: float, stok: int):
        self.merk = merk
        self.tipe = tipe
        self.kategori = kategori.lower()  # Diseragamkan ke huruf kecil agar pencarian tidak case-sensitive
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        """Method untuk menampilkan detail spesifikasi dan informasi laptop."""
        print(f"[{self.merk.upper()} - {self.tipe}]")
        print(f"   Kategori : {self.kategori.capitalize()}")
        print(f"   Harga    : Rp {self.harga:,.0f}")
        print(f"   Stok     : {self.stok} unit")
        print("-" * 40)

    def kurangi_stok(self, jumlah: int = 1) -> bool:
        """Method untuk mengurangi stok jika laptop terjual."""
        if self.stok >= jumlah:
            self.stok -= jumlah
            return True
        return False
