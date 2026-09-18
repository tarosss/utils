from PIL import Image
import os

# 画像フォルダのパス
folder = "image"
output_pdf = "output.pdf"

# フォルダ内のファイルを取得し、拡張子でフィルタ
files = sorted([f for f in os.listdir(folder) if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))])

# 最初の画像を開いてPDF化開始
image_list = []
for f in files[1:]:
    img = Image.open(os.path.join(folder, f)).convert("RGB")
    image_list.append(img)

first_image = Image.open(os.path.join(folder, files[0])).convert("RGB")
first_image.save(output_pdf, save_all=True, append_images=image_list)

print(f"✅ {output_pdf} を作成しました")
