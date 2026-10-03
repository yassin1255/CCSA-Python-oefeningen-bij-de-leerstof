def selection_sort_vooraan(a):

 n = len(a)

 for i in range(0, n -1,1) :
    pos = i #index van de min
    min = a[i]
    for j in range(i+1,n,1):
        if a[j] < min:
          min = a[j]
          pos = j
        #min voorraan zetten
        a[pos] = a[i]
        a[i] = min 







if __name__ == "__main__":
    a = [int(_) for _ in input().split()]
    selection_sort_vooraan(a)

