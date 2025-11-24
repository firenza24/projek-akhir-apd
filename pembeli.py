from prettytable import PrettyTable

barang = [
    {"id": 1, "nama": "Pensil", "harga": 3000},
    {"id": 2, "nama": "Buku Tulis", "harga": 5000},
    {"id": 3, "nama": "Penghapus", "harga": 2000}
]

keranjang = []


def lihat_barang_tersedia():
    print(" DAFTAR BARANG ")
    for b in barang:
        print(f"{b['id']}. {b['nama']} - Rp{b['harga']}")
    print()


def tambah():
    print(" TAMBAH BARANG KE KERANJANG ")
    lihat_barang_tersedia()

    try:
        id_barang = int(input("Masukkan ID barang: "))
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Input harus berupa angka.")
        return

    found = next((b for b in barang if b["id"] == id_barang), None)

    if not found:
        print("Barang tidak ditemukan.")
        return

    keranjang.append({
        "id": found["id"],
        "nama": found["nama"],
        "harga": found["harga"],
        "jumlah": jumlah
    })

    print("Barang berhasil ditambahkan ke keranjang.")


def ubah():
    print(" UBAH DATA DI KERANJANG ")
    lihat_keranjang()

    if not keranjang:
        return

    try:
        idx = int(input("Pilih nomor barang di keranjang: ")) - 1
        jumlah_baru = int(input("Masukkan jumlah baru: "))
    except ValueError:
        print("Input harus berupa angka.")
        return

    if idx < 0 or idx >= len(keranjang):
        print("Pilihan tidak valid.")
        return

    keranjang[idx]["jumlah"] = jumlah_baru
    print("Data berhasil diubah.")


def hapus():
    print(" HAPUS DATA DARI KERANJANG ")
    lihat_keranjang()

    if not keranjang:
        return

    try:
        idx = int(input("Pilih nomor barang yang ingin dihapus: ")) - 1
    except ValueError:
        print("Input harus berupa angka.")
        return

    if idx < 0 or idx >= len(keranjang):
        print("Pilihan tidak valid.")
        return

    keranjang.pop(idx)
    print("Barang berhasil dihapus.")


def cetak_nota():
    print(" NOTA PEMBELIAN ")

    table = PrettyTable()
    table.field_names = ["No", "Nama Barang", "Harga Satuan", "Jumlah", "Subtotal"]

    total = 0
    for i, item in enumerate(keranjang, start=1):
        subtotal = item["harga"] * item["jumlah"]
        total += subtotal
        table.add_row([i, item["nama"], f"Rp{item['harga']}", item["jumlah"], f"Rp{subtotal}"])

    print(table)
    print(f"TOTAL BAYAR : Rp{total}")


def checkout():
    print(" CHECKOUT ")

    if not keranjang:
        print("Keranjang masih kosong.")
        return

    cetak_nota()
    print("Checkout selesai. Terima kasih telah berbelanja!")

    keranjang.clear()


def lihat_keranjang():
    print(" KERANJANG ")
    if not keranjang:
        print("Keranjang kosong.")
        return

    for i, item in enumerate(keranjang, start=1):
        print(f"{i}. {item['nama']} - Rp{item['harga']} x {item['jumlah']}")
    print()


def menu_keranjang():
    while True:
        print(" MENU KERANJANG ")
        print("1. Tambah barang")
        print("2. Ubah barang")
        print("3. Hapus barang")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            tambah()
        elif pilihan == "2":
            ubah()
        elif pilihan == "3":
            hapus()
        elif pilihan == "4":
            return
        else:
            print("Pilihan tidak valid.\n")


def menu_pembeli():
    while True:
        print(" MENU PEMBELI ")
        print("1. Lihat barang yang ada")
        print("2. keranjang")
        print("3. Checkout")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            lihat_barang_tersedia()
        elif pilihan == "2":
            menu_keranjang()
        elif pilihan == "3":
            checkout()
        elif pilihan == "4":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")


menu_pembeli()
