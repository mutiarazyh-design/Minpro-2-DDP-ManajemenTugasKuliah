from prettytable import PrettyTable
import getpass
from datetime import datetime


# DATA USER

users = {
    "admin": {
        "password": "admin26",
        "role": "admin"
    },
    "user": {
        "password": "user26",
        "role": "user"
    }
}


data_tugas = {}


def login():

    print("======================================")
    print("        LOGIN SISTEM TUGAS")
    print("======================================")

    kesempatan = 3

    while kesempatan > 0:

        username = input("Username : ").strip()
        password = getpass.getpass("Password : ")

        if username in users and users[username]["password"] == password:

            role = users[username]["role"]

            print("\nLogin berhasil!")
            print(f"Selamat datang, {username}.")
            print(f"Role : {role}")

            input("\nTekan Enter untuk melanjutkan...")
            return username, role

        else:

            kesempatan -= 1

            print("\nUsername atau password salah!")
            print(f"Sisa percobaan: {kesempatan}")

    print("\nAnda gagal login.")
    print("Program selesai.")

    return None, None



def tambah_tugas():

    print("\n======================================")
    print("        TAMBAH TUGAS KULIAH")
    print("======================================")

    while True:

        mata_kuliah = input("Mata Kuliah : ").strip()

        if mata_kuliah == "":
            print("Mata kuliah tidak boleh kosong!")
        else:
            break

    while True:

        nama_tugas = input("Nama Tugas  : ").strip()

        if nama_tugas == "":
            print("Nama tugas tidak boleh kosong!")
        else:
            break

    while True:

        deadline = input("Deadline (DD-MM-YYYY) : ").strip()

        try:
            datetime.strptime(deadline, "%d-%m-%Y")
            break

        except ValueError:
            print("Format deadline salah!")
            print("Gunakan format DD-MM-YYYY.")

    while True:

        status = input(
            "Status (Belum/Selesai): "
        ).strip().lower()

        if status == "belum":
            status = "Belum"
            break

        elif status == "selesai":
            status = "Selesai"
            break

        else:
            print("Status hanya boleh Belum atau Selesai!")

    if len(data_tugas) == 0:
        id_tugas = 1
    else:
        id_tugas = max(data_tugas.keys()) + 1

    # Dictionary untuk menyimpan tugas
    data_tugas[id_tugas] = {
        "mata_kuliah": mata_kuliah,
        "nama_tugas": nama_tugas,
        "deadline": deadline,
        "status": status
    }

    print("\nTugas berhasil ditambahkan!")

    input("\nTekan Enter untuk kembali...")


def lihat_tugas():

    print("\n======================================")
    print("          DAFTAR TUGAS KULIAH")
    print("======================================")

    if len(data_tugas) == 0:

        print("Belum ada tugas.")

    else:

        tabel = PrettyTable()

        tabel.field_names = [
            "ID",
            "Mata Kuliah",
            "Nama Tugas",
            "Deadline",
            "Status"
        ]

        for id_tugas, tugas in data_tugas.items():
            tabel.add_row([
                id_tugas,
                tugas["mata_kuliah"],
                tugas["nama_tugas"],
                tugas["deadline"],
                tugas["status"]
            ])

        print(tabel)

    input("\nTekan Enter untuk keluar...")


def ubah_tugas():

    print("\n======================================")
    print("            UBAH DATA TUGAS")
    print("======================================")

    if len(data_tugas) == 0:

        print("Belum ada tugas.")
        input("\nTekan Enter untuk keluar...")
        return

    lihat_tugas()

    while True:

        try:

            id_tugas = int(input("Masukkan ID tugas: "))

            if id_tugas <= 0:
                print("ID harus lebih dari 0!")

            elif id_tugas not in data_tugas:
                print("Tugas tidak ditemukan!")
                input("\nTekan Enter untuk keluar...")
                return

            else:
                break

        except ValueError:

            print("ID harus berupa angka!")

    while True:

        print("\n======================================")
        print("       PILIH DATA YANG INGIN DIUBAH")
        print("======================================")
        print("1. Mata Kuliah")
        print("2. Nama Tugas")
        print("3. Deadline")
        print("4. Status")
        print("5. Kembali")
        print("======================================")

        pilihan = input("Pilih: ").strip()

        if pilihan == "1":

            while True:

                mata_kuliah = input(
                    "Mata Kuliah baru: "
                ).strip()

                if mata_kuliah == "":
                    print("Mata kuliah tidak boleh kosong!")

                else:
                    data_tugas[id_tugas]["mata_kuliah"] = mata_kuliah
                    print("Mata kuliah berhasil diubah!")
                    break

            break


        elif pilihan == "2":

            while True:

                nama_tugas = input(
                    "Nama Tugas baru: "
                ).strip()

                if nama_tugas == "":
                    print("Nama tugas tidak boleh kosong!")

                else:
                    data_tugas[id_tugas]["nama_tugas"] = nama_tugas
                    print("Nama tugas berhasil diubah!")
                    break

            break

        # UBAH DEADLINE
    
        elif pilihan == "3":

            while True:

                deadline = input(
                    "Deadline baru (DD-MM-YYYY): "
                ).strip()

                try:

                    datetime.strptime(
                        deadline,
                        "%d-%m-%Y"
                    )

                    data_tugas[id_tugas]["deadline"] = deadline

                    print("Deadline berhasil diubah!")
                    break

                except ValueError:

                    print(
                        "Format deadline salah!"
                    )
                    print(
                        "Gunakan format DD-MM-YYYY."
                    )

            break

        elif pilihan == "4":

            while True:

                status = input(
                    "Status baru (Belum/Selesai): "
                ).strip().lower()

                if status == "belum":

                    data_tugas[id_tugas]["status"] = "Belum"
                    print("Status berhasil diubah!")
                    break

                elif status == "selesai":

                    data_tugas[id_tugas]["status"] = "Selesai"
                    print("Status berhasil diubah!")
                    break

                else:

                    print(
                        "Status hanya boleh "
                        "Belum atau Selesai!"
                    )

            break


        elif pilihan == "5":

            print("Kembali ke menu utama...")
            return

        else:

            print("Pilihan tidak valid!")



def hapus_tugas():

    print("\n======================================")
    print("            HAPUS DATA TUGAS")
    print("======================================")

    if len(data_tugas) == 0:

        print("Belum ada tugas.")
        input("\nTekan Enter untuk kembali...")
        return

    lihat_tugas()

    while True:

        try:

            id_tugas = int(
                input("Masukkan ID tugas: ")
            )

            if id_tugas <= 0:

                print("ID harus lebih dari 0!")

            elif id_tugas not in data_tugas:

                print("Tugas tidak ditemukan!")
                input("\nTekan Enter untuk kembali...")
                return

            else:

                break

        except ValueError:

            print("ID harus berupa angka!")

    while True:

        konfirmasi = input(
            "Yakin ingin menghapus? (Y/T): "
        ).strip().upper()

        if konfirmasi == "Y":

            del data_tugas[id_tugas]

            print("Tugas berhasil dihapus!")
            break

        elif konfirmasi == "T":

            print("Penghapusan dibatalkan.")
            break

        else:

            print("Masukkan Y atau T!")

    input("\nTekan Enter untuk kembali...")


# MENU ADMIN

def menu_admin():

    while True:


        print("======================================")
        print("       MENU ADMIN - MANAJEMEN TUGAS")
        print("======================================")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Ubah Tugas")
        print("4. Hapus Tugas")
        print("5. Keluar")
        print("======================================")

        pilihan = input(
            "Pilih menu (1-5): "
        ).strip()

        if pilihan == "1":

            tambah_tugas()

        elif pilihan == "2":

            lihat_tugas()

        elif pilihan == "3":

            ubah_tugas()

        elif pilihan == "4":

            hapus_tugas()

        elif pilihan == "5":

            print("Keluar dari menu admin...")
            break

        else:

            print("Pilihan tidak valid!")
            input(
                "\nTekan Enter untuk mencoba lagi..."
            )


# MENU USER
def menu_user():

    while True:

        print("======================================")
        print("         MENU USER - TUGAS KULIAH")
        print("======================================")
        print("1. Lihat Tugas")
        print("2. Keluar")
        print("======================================")

        pilihan = input(
            "Pilih menu (1-2): "
        ).strip()

        if pilihan == "1":

            lihat_tugas()

        elif pilihan == "2":

            print("Keluar dari menu user...")
            break

        else:

            print("Pilihan tidak valid!")
            input(
                "\nTekan Enter untuk mencoba lagi..."
            )


# PROGRAM UTAMA

def main():

    while True:


        username, role = login()

        if username is None:
            break

        if role == "admin":
            menu_admin()

        elif role == "user":
            menu_user()

        print("\nKembali ke halaman login...")
        input("Tekan Enter untuk melanjutkan...")


main()