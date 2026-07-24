def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # 初期のギャップを配列の長さの半分に設定
    # ギャップを徐々に小さくしながらソート
    debug = 0
    while gap > 0:
        print(f"ギャップ: {gap}")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        print(f"中間結果: {arr}")
        gap //= 2


# 使用例
if __name__ == "__main__":
    arr = [99, 97, 94, 92,-1, 10, 8, 6 , 4, 100 ]
    print("ソート前の配列:", arr)
    shell_sort(arr)
    print("ソート後の配列:", arr)
