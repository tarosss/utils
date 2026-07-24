def boyer_moore_search(text, pattern):
    # ステップ 1: 不一致文字表の構築
    def build_bad_char_table(pattern):
        bad_char_table = {}
        for i, char in enumerate(pattern):
            bad_char_table[char] = i  # 各文字の最後の出現位置
        return bad_char_table

    # ステップ 2: 良い接尾辞表の構築（簡略化版）
    def build_good_suffix_table(pattern):
        m = len(pattern)
        good_suffix_table = [0] * m
        last_prefix_position = m

        for i in range(m - 1, -1, -1):
            # print(is_prefix(pattern, i + 1))
            if is_prefix(pattern, i + 1):
                last_prefix_position = i + 1
            good_suffix_table[m - 1 - i] = last_prefix_position - i + m - 1
        for i in range(m - 1):
            slen = suffix_length(pattern, i)
            print(slen)
            good_suffix_table[slen] = m - 1 - i + slen
        return good_suffix_table

    def is_prefix(pattern, p):
        return pattern[p:] == pattern[:len(pattern) - p]

    def suffix_length(pattern, p):
        length = 0
        while p >= 0 and pattern[p] == pattern[len(pattern) - 1 - length]:
            length += 1
            p -= 1
        return length

    # ステップ 3: 検索プロセス
    bad_char_table = build_bad_char_table(pattern)
    good_suffix_table = build_good_suffix_table(pattern)
    print(good_suffix_table)
    n, m = len(text), len(pattern)
    i = 0

    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            print(f"パターンが見つかりました: {i}")
            i += good_suffix_table[0]
        else:
            bad_char_shift = j - bad_char_table.get(text[i + j], -1)
            good_suffix_shift = good_suffix_table[j]
            i += max(bad_char_shift, good_suffix_shift)

boyer_moore_search('ABCABABACABABAC', 'ABABACA')
