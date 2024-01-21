def bubble_sort(arr):
    """Menyimpan array ke file, memisahkan nilai dengan koma."""

    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Tukar elemen


def save_to_file(filename, arr):
    """Menyimpan array ke file, memisahkan nilai dengan koma."""

    with open(filename, "w") as file:
        file.write(",".join(map(str, arr)))


def read_from_file(filename):
    """Membaca array dari file, dengan asumsi nilai dipisahkan dengan koma."""

    with open(filename, "r") as file:
        line = file.readline()
        arr = list(map(int, line.split(",")))
    return arr


def main():
    """Menyediakan antarmuka berbasis menu untuk mengurutkan nomor."""

    numbers = []

    while True:
        print("\nMENU PILIHAN")
        print("1. Input angka")
        print("2. Tampil hasil pengurutan")
        print("3. Selesai")

        choice = input("Masukkan pilihan [1/2/3]: ")

        if choice == "1":
            num_count = int(input("Masukkan jumlah angka yang akan diinput: "))
            print("Input Angka Secara Acak")
            print("---------------------------------")
            for i in range(num_count):
                number = int(input("Angka {}: ".format(i + 1)))
                numbers.append(number)
        elif choice == "2":
            bubble_sort(numbers)
            save_to_file("hasil_pengurutan.txt", numbers)
            sorted_numbers = read_from_file("hasil_pengurutan.txt")
            print("\nTAMPIL HASIL PENGURUTAN")
            print("Nilai tugas:", ", ".join(map(str, sorted_numbers)))
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih [1/2/3].")


if __name__ == "__main__":
    main()
