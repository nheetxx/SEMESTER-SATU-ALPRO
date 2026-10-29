package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var reader = bufio.NewReader(os.Stdin)

func bacaInt(prompt string) int {
	for {
		fmt.Print(prompt)
		teks, err := reader.ReadString('\n')
		if err != nil && teks == "" {
			os.Exit(0)
		}
		n, err := strconv.Atoi(strings.TrimSpace(teks))
		if err != nil {
			fmt.Println("Input harus berupa bilangan bulat.")
			continue
		}
		return n
	}
}

func bacaUkuran(prompt string) int {
	for {
		n := bacaInt(prompt)
		if n <= 0 {
			fmt.Println("Ukuran harus lebih dari 0.")
			continue
		}
		return n
	}
}

func isiMatriks(nama string, baris, kolom int) [][]int {
	m := make([][]int, baris)
	for i := range m {
		m[i] = make([]int, kolom)
		for j := range m[i] {
			m[i][j] = bacaInt(fmt.Sprintf("Isi matriks %s [Baris %d][Kolom %d]: ", nama, i+1, j+1))
		}
	}
	return m
}

func cetak(m [][]int) {
	for _, baris := range m {
		fmt.Println(baris)
	}
}

func tambah(a, b [][]int) [][]int {
	hasil := make([][]int, len(a))
	for i := range a {
		hasil[i] = make([]int, len(a[i]))
		for j := range a[i] {
			hasil[i][j] = a[i][j] + b[i][j]
		}
	}
	return hasil
}

func kali(a, b [][]int) [][]int {
	hasil := make([][]int, len(a))
	for i := range a {
		hasil[i] = make([]int, len(b[0]))
		for j := range b[0] {
			for k := range b {
				hasil[i][j] += a[i][k] * b[k][j]
			}
		}
	}
	return hasil
}

func main() {
	for {
		barisA := bacaUkuran("Jumlah baris matriks A: ")
		kolomA := bacaUkuran("Jumlah kolom matriks A: ")
		barisB := bacaUkuran("Jumlah baris matriks B: ")
		kolomB := bacaUkuran("Jumlah kolom matriks B: ")

		matriksA := isiMatriks("A", barisA, kolomA)
		matriksB := isiMatriks("B", barisB, kolomB)

		fmt.Println("Hasil matriks A")
		cetak(matriksA)
		fmt.Println("Hasil matriks B")
		cetak(matriksB)

		fmt.Print("Pilih opsi\n1. Penjumlahan\n2. Perkalian\n(1/2): ")
		pilihan, _ := reader.ReadString('\n')
		pilihan = strings.TrimSpace(pilihan)

		switch pilihan {
		case "1":
			if barisA != barisB || kolomA != kolomB {
				fmt.Printf("%dx%d dan %dx%d tidak sama, penjumlahan tidak bisa dilakukan.\n",
					barisA, kolomA, barisB, kolomB)
				continue
			}
			fmt.Println("Hasil penjumlahan matriks A dan matriks B adalah:")
			cetak(tambah(matriksA, matriksB))
		case "2":
			if kolomA != barisB {
				fmt.Printf("%dx%d dan %dx%d tidak memenuhi syarat perkalian.\n",
					barisA, kolomA, barisB, kolomB)
				continue
			}
			fmt.Println("Hasil perkalian matriks A dan matriks B adalah:")
			cetak(kali(matriksA, matriksB))
		default:
			fmt.Println("Pilihan tidak sesuai.")
			continue
		}
		break
	}
}