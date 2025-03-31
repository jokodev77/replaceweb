def replace_website_code(input_file, output_file, replacements):
    try:
        # Baca isi file input
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Lakukan penggantian untuk setiap pasangan dalam dictionary replacements
        modified_content = content
        for old_text, new_text in replacements.items():
            modified_content = modified_content.replace(old_text, new_text)

        # Simpan hasil ke file output
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        return "Proses penggantian selesai! File baru disimpan sebagai: " + output_file
    
    except FileNotFoundError:
        return "Error: File input tidak ditemukan!"
    except Exception as e:
        return f"Error: Terjadi kesalahan - {str(e)}"

# Contoh penggunaan
def main():
    # Nama file input dan output
    input_file = "website_source.html"  # Ganti dengan nama file source code Anda
    output_file = "website_modified.html"  # Nama file hasil

    # Dictionary berisi teks yang ingin diganti
    replacements = {
        'old_text1': 'new_text1',  # Contoh: ganti teks lama dengan teks baru
        '<title>Old Title</title>': '<title>New Awesome Title</title>',  # Ganti judul
        'http://old-domain.com': 'http://new-domain.com'  # Ganti URL
        # Tambahkan pasangan penggantian lain sesuai kebutuhan
    }

    # Jalankan fungsi
    result = replace_website_code(input_file, output_file, replacements)
    print(result)

# Contoh fungsi dengan input dari pengguna
def interactive_mode():
    input_file = input("Masukkan nama file input (contoh: source.html): ")
    output_file = input("Masukkan nama file output (contoh: modified.html): ")
    
    # Inisialisasi dictionary replacements
    replacements = {}
    print("Masukkan teks yang ingin diganti (kosongkan 'teks lama' untuk selesai):")
    
    while True:
        old_text = input("Teks lama: ")
        if not old_text:
            break
        new_text = input("Teks baru: ")
        replacements[old_text] = new_text
    
    if replacements:
        result = replace_website_code(input_file, output_file, replacements)
        print(result)
    else:
        print("Tidak ada penggantian yang dimasukkan!")

if __name__ == "__main__":
    print("Pilih mode:")
    print("1. Mode default (contoh)")
    print("2. Mode interaktif")
    choice = input("Masukkan pilihan (1/2): ")
    
    if choice == "1":
        main()
    elif choice == "2":
        interactive_mode()
    else:
        print("Pilihan tidak valid!")