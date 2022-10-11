# Arrays

+[Squares of sorted array](#squares-of-sorted-array)

+[Merge two sorted array](#merge-two-sorted-array)

+[Sum of diagonal elem in matrix](#sum-of-diagonal-elem-in-matrix)

+[Compress](#compress)

## Squares of sorted array 

Дан отсортированный список в неубавющем порядке. Вернуть элементы этого списка возведенные в квадрат в неубывающем порядке. Элементы списка это целые числа. O(n)

```python
def squares(s):
    i = 0
    a = 0
    b = 0
    while i < len(s) and s[i] < 0:
        i += 1
    for cur in range(i - 1, -1, -1):
        a = s[cur] ** 2
    for cur in range(i, len(s)):
        b = s[cur] ** 2

    return merge(a, b)

```

## Merge two sorted array

На входе два отсортированных массива (списка), на выходе получить 1 отсортированный массив. Элементы списка это целые числа. o(n)

```python

def merge(arr1, arr2):
    res = []
    x = 0
    y = 0

    while x < len(arr1) and y < len(arr2):
        if arr1[x] < arr2[y]:
            res.append(arr1[x])
            x += 1
        else:
            res.append(arr2[y])
            y += 1

    if y < len(arr2):
        while y < len(arr2):
            res.append(arr2[y])
            y += 1

    else:
        while x < len(arr1):
            res.append(arr1[x])
            x += 1

    return res

```

## Sum of diagonal elem in matrix

Сумма диагональных элементов матрицы.

```python

def diagonalSum(mat):
    res = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i == j:
                res += mat[i][j]

    return res

```

## Compress

Два вложеннных цикла.

```python

def compress(x):
    res = []
    cur_sum = 0
    if len(x) > 0:
        res.append(x[0])
        cur_sum = 1
    for i in range(1, len(x)):
        if x[i] == x[i - 1]:
            cur_sum += 1
        else:
            if cur_sum > 1:
                res.append(str(cur_sum))
                cur_sum = 1
            res.append(x[i])

    if (cur_sum > 1):
        res.append(str(cur_sum))

    return "".join(res)

```
