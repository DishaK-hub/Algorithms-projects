import time
def editDistance(str1,str2):

    # Declaring array 'D' with rows = len(a) + 1 and columns = len(b) + 1:
    D = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]

    # Initialising first row:
    for i in range(len(str1) + 1):
        D[i][0] = i

    # Initialising first column:
    for j in range(len(str2) + 1):
        D[0][j] = j

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                D[i][j] = D[i - 1][j - 1]
            else:
                # Adding 1 to account for the cost of operation
                insertion = 1 + D[i][j - 1]
                deletion = 1 + D[i - 1][j]
                replacement = 1 + D[i - 1][j - 1]

                # Choosing the best option:
                D[i][j] = min(insertion, deletion, replacement)
    return D[len(str1)][len(str2)]

if __name__ == "__main__":
    print(editDistance("ATCAT", "ATTATC"))
    print(editDistance("taacttctagtacatacccgggttgagcccccatttcttggttggatgcgaggaacattacgctagaggaacaacaaggtcagaggcctgttactcctat", "taacttctagtacatacccgggttgagcccccatttccgaggaacattacgctagaggaacaacaaggtcagaggcctgttactcctat"))
    print(editDistance("CGCAATTCTGAAGCGCTGGGGAAGACGGGT", "TATCCCATCGAACGCCTATTCTAGGAT"))
    print(editDistance("tatttacccaccacttctcccgttctcgaatcaggaatagactactgcaatcgacgtagggataggaaactccccgagtttccacagaccgcgcgcgatattgctcgccggcatacagcccttgcgggaaatcggcaaccagttgagtagttcattggcttaagacgctttaagtacttaggatggtcgcgtcgtgccaa", "atggtctccccgcaagataccctaattccttcactctctcacctagagcaccttaacgtgaaagatggctttaggatggcatagctatgccgtggtgctatgagatcaaacaccgctttctttttagaacgggtcctaatacgacgtgccgtgcacagcattgtaataacactggacgacgcgggctcggttagtaagtt"))






