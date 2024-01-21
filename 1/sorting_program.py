def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def save_to_file(filename, arr):
    with open(filename, "w") as file:
        file.write(", ".join(map(str, arr)))


def read_from_file(filename):
    with open(filename, "r") as file:
        line = file.readline()
        arr = list(map(int, line.split(", ")))
    return arr


def main():
    nums = []
    while True:
        print("MENU PILIHAN")
        print("1. Input angka")
        print("2. Tampil hasil pengurutan")
        print("3. Selesai")

        choice = input("Masukkan pilihan [1/2/3]: ")

        if choice == "1":
            n = int(input("Masukkan jumlah angka yang akan diinput: "))
            print("Input Angka Secara Acak")
            print("---------------------------------")
            for i in range(n):
                num = int(input("Angka {}: ".format(i + 1)))
                nums.append(num)
            print()
        elif choice == "2":
            bubble_sort(nums)
            save_to_file(
                "hasil_pengurutan.txt",
                nums,
            )
            sorted_nums = read_from_file("hasil_pengurutan.txt")
            print("TAMPIL HASIL PENGURUTAN")
            print("Nilai tugas:", ", ".join(map(str, sorted_nums)))
            print()
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih [1/2/3].")
            print()


if __name__ == "__main__":
    main()
