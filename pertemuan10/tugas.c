#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAKS 50

int bacaInt(const char *prompt) {
    char buf[64], *end;
    while (1) {
        printf("%s", prompt);
        if (!fgets(buf, sizeof buf, stdin)) exit(0);
        long n = strtol(buf, &end, 10);
        while (isspace((unsigned char)*end)) end++;
        if (end == buf || *end != '\0') {
            printf("Input harus berupa bilangan bulat.\n");
            continue;
        }
        return (int)n;
    }
}

int bacaUkuran(const char *prompt) {
    while (1) {
        int n = bacaInt(prompt);
        if (n <= 0 || n > MAKS) {
            printf("Ukuran harus 1 sampai %d.\n", MAKS);
            continue;
        }
        return n;
    }
}

void isiMatriks(const char *nama, int m[MAKS][MAKS], int baris, int kolom) {
    char prompt[64];
    for (int i = 0; i < baris; i++)
        for (int j = 0; j < kolom; j++) {
            snprintf(prompt, sizeof prompt,
                     "Isi matriks %s [Baris %d][Kolom %d]: ", nama, i + 1, j + 1);
            m[i][j] = bacaInt(prompt);
        }
}

void cetak(int m[MAKS][MAKS], int baris, int kolom) {
    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < kolom; j++)
            printf("%d ", m[i][j]);
        printf("\n");
    }
}

int main(void) {
    static int A[MAKS][MAKS], B[MAKS][MAKS], C[MAKS][MAKS];
    char buf[16];

    while (1) {
        int barisA = bacaUkuran("Jumlah baris matriks A: ");
        int kolomA = bacaUkuran("Jumlah kolom matriks A: ");
        int barisB = bacaUkuran("Jumlah baris matriks B: ");
        int kolomB = bacaUkuran("Jumlah kolom matriks B: ");

        isiMatriks("A", A, barisA, kolomA);
        isiMatriks("B", B, barisB, kolomB);

        printf("Hasil matriks A\n");
        cetak(A, barisA, kolomA);
        printf("Hasil matriks B\n");
        cetak(B, barisB, kolomB);

        printf("Pilih opsi\n1. Penjumlahan\n2. Perkalian\n(1/2): ");
        if (!fgets(buf, sizeof buf, stdin)) return 0;
        buf[strcspn(buf, "\n")] = '\0';

        if (strcmp(buf, "1") == 0) {
            if (barisA != barisB || kolomA != kolomB) {
                printf("%dx%d dan %dx%d tidak sama, penjumlahan tidak bisa dilakukan.\n",
                       barisA, kolomA, barisB, kolomB);
                continue;
            }
            for (int i = 0; i < barisA; i++)
                for (int j = 0; j < kolomA; j++)
                    C[i][j] = A[i][j] + B[i][j];
            printf("Hasil penjumlahan matriks A dan matriks B adalah:\n");
            cetak(C, barisA, kolomA);

        } else if (strcmp(buf, "2") == 0) {
            if (kolomA != barisB) {
                printf("%dx%d dan %dx%d tidak memenuhi syarat perkalian.\n",
                       barisA, kolomA, barisB, kolomB);
                continue;
            }
            for (int i = 0; i < barisA; i++)
                for (int j = 0; j < kolomB; j++) {
                    C[i][j] = 0;
                    for (int k = 0; k < kolomA; k++)
                        C[i][j] += A[i][k] * B[k][j];
                }
            printf("Hasil perkalian matriks A dan matriks B adalah:\n");
            cetak(C, barisA, kolomB);

        } else {
            printf("Pilihan tidak sesuai.\n");
            continue;
        }
        break;
    }
    return 0;
}