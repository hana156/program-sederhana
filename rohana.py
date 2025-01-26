def display_menu():
    print("\n=== Sistem Manajemen File dan Folder ===")
    print("1. Buat Folder")
    print("2. Hapus Folder")
    print("3. Buat File")
    print("4. Hapus File")
    print("5. Tampilkan Isi Folder")
    print("6. Keluar")

def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' berhasil dibuat.")
    except FileExistsError:
        print(f"Folder '{folder_name}' sudah ada.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def delete_folder(folder_name):
    try:
        os.rmdir(folder_name)
        print(f"Folder '{folder_name}' berhasil dihapus.")
    except FileNotFoundError:
        print(f"Folder '{folder_name}' tidak ditemukan.")
    except OSError:
        print(f"Folder '{folder_name}' tidak kosong.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write("")  # Membuat file kosong
        print(f"File '{file_name}' berhasil dibuat.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' berhasil dihapus.")
    except FileNotFoundError:
        print(f"File '{file_name}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def list_directory_contents(path):
    try:
        items = os.listdir(path)
        print(f"Isi folder '{path}':")
        for item in items:
            print(f"- {item}")
    except FileNotFoundError:
        print(f"Folder '{path}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def main():
    while True:
        display_menu()
        choice = input("Pilih opsi (1-6): ")

        if choice == '1':
            folder_name = input("Masukkan nama folder: ")
            create_folder(folder_name)
        elif choice == '2':
            folder_name = input("Masukkan nama folder yang ingin dihapus: ")
            delete_folder(folder_name)
        elif choice == '3':
            file_name = input("Masukkan nama file: ")
            create_file(file_name)
        elif choice == '4':
            file_name = input("Masukkan nama file yang ingin dihapus: ")
            delete_file(file_name)
        elif choice == '5':
            path = input("Masukkan path folder: ")
            list_directory_contents(path)
        elif choice == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if _name_ == "_main_":
    main()
