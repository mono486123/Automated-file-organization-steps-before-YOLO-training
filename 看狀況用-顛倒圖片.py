from PIL import Image
import os

# 要處理的原始圖片所在文件夾路徑
input_folder = r"E:\yolov7\data\datasets1\照片分類\Toyota\Corolla Altis 2.0"


# 存儲鏡像翻轉後的圖片的文件夾路徑
output_folder = input_folder

# 遍歷輸入文件夾中的每張圖片
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # 假設處理的是常見的圖片格式
        input_path = os.path.join(input_folder, filename)
        img = Image.open(input_path)

        # 将图像转换为RGB模式
        img = img.convert("RGB")
        
        # 將圖片進行顛倒旋轉（旋轉180度）
        rotated_img = img.rotate(36)
        
        # 構造輸出文件路徑
        output_path = os.path.join(input_folder, "rotated_" + filename)

        
        
        # 儲存旋轉後的圖片
        rotated_img.save(output_path)
        
        # 儲存鏡像翻轉後的圖片
        rotated_img.save(output_path)

print("顛倒旋轉完成並保存圖片",output_folder)
