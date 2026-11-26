from abc import ABC, abstractmethod


class BarangToko(ABC):
    """Kontrak dasar barang di toko (mendukung OCP & LSP)."""

    def __init__(self, merk: str, harga: float, stok: int):
        if harga < 0 or stok < 0:
            raise ValueError("Harga dan stok awal tidak boleh negatif.")
        self.merk = merk.strip()
        self.harga = float(harga)
        self.stok = int(stok)

    def kurangi_stok(self, jumlah: int = 1) -> bool:
        """Kontrak: mengembalikan bool; hanya mengurangi stok jika jumlah valid & cukup."""
        if not isinstance(jumlah, int) or jumlah <= 0:
            return False
        if self.stok >= jumlah:
            self.stok -= jumlah
            return True
        return False

    @abstractmethod
    def tampilkan_info(self) -> str:
        """Kontrak: setiap turunan wajib mengembalikan string ringkasan informasi."""
        pass


class Laptop(BarangToko):
    """Turunan BarangToko khusus laptop yang mematuhi kontrak induk (LSP)."""

    def __init__(self, merk: str, tipe: str, kategori: str, harga: float, stok: int):
        super().__init__(merk, harga, stok)
        self.tipe = tipe.strip()
        self.kategori = kategori.lower().strip()

    def tampilkan_info(self) -> str:
        info = (
            f"[{self.merk.upper()} - {self.tipe}]\n"
            f"   Kategori : {self.kategori.capitalize()}\n"
            f"   Harga    : Rp {self.harga:,.0f}\n"
            f"   Stok     : {self.stok} unit\n"
            + ("-" * 40)
        )
        print(info)
        return info

bintang
