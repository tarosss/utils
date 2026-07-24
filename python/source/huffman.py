# ハフマン木のノードを定義
class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol  # シンボル（文字）
        self.freq = freq      # 頻度（重み）
        self.left = None      # 左の子ノード
        self.right = None     # 右の子ノード

# 優先度付きキューを模倣する関数
def sort_nodes(nodes):
    # 頻度で昇順にソート
    nodes.sort(key=lambda x: x.freq)

# ハフマン木を構築
def build_huffman_tree(symbols):
    # シンボルと頻度をノードに変換
    nodes = [Node(symbol, freq) for symbol, freq in symbols]

    # ハフマン木の構築
    while len(nodes) > 1:
        # 頻度が最小の2つのノードを取得
        sort_nodes(nodes)
        left = nodes.pop(0)
        right = nodes.pop(0)

        # 新しいノードを作成
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # 新しいノードをリストに追加
        nodes.append(merged)
    # 最終的なハフマン木のルートを返す
    return nodes[0]

# ハフマン符号を生成
def generate_huffman_codes(node, current_code="", codes={}):
    if node is None:
        return

    # 葉ノードの場合は符号を記録
    print(node.symbol)
    if node.symbol is not None:
        codes[node.symbol] = current_code
        return

    # 左の子に進む場合は "0" を追加
    generate_huffman_codes(node.left, current_code + "0", codes)

    # 右の子に進む場合は "1" を追加
    generate_huffman_codes(node.right, current_code + "1", codes)

# メイン処理
def huffman_coding(symbols):
    # ハフマン木の構築
    root = build_huffman_tree(symbols)
    # ハフマン符号の生成
    codes = {}
    generate_huffman_codes(root, "", codes)

    return codes

# 例: シンボルと頻度
symbols = [("A", 5), ("B", 9), ("C", 12), ("D", 13), ("E", 16), ("F", 45)]

# ハフマン符号を計算
huffman_codes = huffman_coding(symbols)

# 結果を出力
print("ハフマン符号:")
for symbol, code in huffman_codes.items():
    print(f"{symbol}: {code}")
