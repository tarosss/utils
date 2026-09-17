import os
import sys

def rename_images(directory):
    # 対応する画像拡張子（必要に応じて追加）
    extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')

    # ディレクトリが存在するか確認
    if not os.path.isdir(directory):
        print("エラー: 指定されたパスはディレクトリではありません。")
        return

    # ディレクトリ内のファイルを取得し、画像だけを抽出
    files = [f for f in os.listdir(directory) if f.lower().endswith(extensions)]

    if not files:
        print("画像ファイルが見つかりません。")
        return

    # 名前でソート（変更したい場合は別のキーを指定）
    files.sort()

    # リネーム処理
    counter = 1
    for file in files:
        ext = os.path.splitext(file)[1]
        new_name = f"{counter:04d}{ext}"  # 例: 0001.jpg
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name)

        # 同名ファイルが存在する場合はスキップ
        if os.path.exists(new_path):
            print(f"スキップ: {new_name} は既に存在します。")
            continue

        os.rename(old_path, new_path)
        print(f"{file} -> {new_name}")
        counter += 1

    print("完了しました。")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法: python rename_images.py <ディレクトリパス>")
    else:
        rename_images(sys.argv[1])
