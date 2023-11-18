#import os
#
## 設定檔案所在的目錄和新名稱的格式
#directory = r"E:\yolov7\data\datasets1\train1"  # 將這裡的路徑替換為您的目錄路徑
#new_filename_format = "{0:02d}.jpg"  #"{:02d}.jpg"
#
## 獲取目錄中的所有檔案
#files = os.listdir(directory)
#
## 迭代處理每個檔案
#for index, old_filename in enumerate(files):
#    if old_filename.endswith(".jpg"):
#        new_filename = new_filename_format.format(index)
#        new_filepath = os.path.join(directory, new_filename)
#        old_filepath = os.path.join(directory, old_filename)
#        
#        # 使用rename函式來將檔案重新命名
#        os.rename(old_filepath, new_filepath)
#        print(f"將 {old_filename} 重新命名為 {new_filename}")





import os

# 設定檔案所在的目錄
directory = r"E:\yolov7\data\datasets1\胡蘿蔔"  # 將這裡的路徑替換為您的目錄路徑
start_number = 0  # 開始的數字

# 獲取目錄中的所有檔案
files = os.listdir(directory)

# 迭代處理每個檔案
for old_filename in files:
    if old_filename.upper().endswith((".JPG","JPEG")):  # 確保只處理 .JPG 檔案，忽略大小寫
        new_number = start_number
        new_filename = "{:02d}.jpg".format(new_number)
        new_filepath = os.path.join(directory, new_filename)
        old_filepath = os.path.join(directory, old_filename)
        
        # 避免檔案名稱衝突，檢查新的檔案是否已存在，如果存在，就增加數字直到找到一個可用的名稱
        while os.path.exists(new_filepath):
            new_number += 1
            new_filename = "{:02d}.jpg".format(new_number)
            new_filepath = os.path.join(directory, new_filename)
        
        # 使用rename函式來將檔案重新命名
        os.rename(old_filepath, new_filepath)
        print(f"將 {old_filename} 重新命名為 {new_filename}")




#import os
#
## 設定檔案所在的目錄
#directory = r"E:\yolov7\data\datasets1\Toyota\Corolla Cross"  # 將這裡的路徑替換為您的目錄路徑
#start_number = 43  # 開始的數字
#
## 獲取目錄中的所有檔案
#files = os.listdir(directory)
#
## 迭代處理每個檔案
#for old_filename in files:
#    if old_filename.upper().endswith(".TXT"):  # 確保只處理 .TXT 檔案，忽略大小寫
#        new_number = start_number
#        new_filename = "{:02d}.txt".format(new_number)
#        new_filepath = os.path.join(directory, new_filename)
#        old_filepath = os.path.join(directory, old_filename)
#        
#        # 避免檔案名稱衝突，檢查新的檔案是否已存在，如果存在，就增加數字直到找到一個可用的名稱
#        while os.path.exists(new_filepath):
#            new_number += 1
#            new_filename = "{:02d}.txt".format(new_number)
#            new_filepath = os.path.join(directory, new_filename)
#        
#        # 使用rename函式來將檔案重新命名
#        os.rename(old_filepath, new_filepath)
#        print(f"將 {old_filename} 重新命名為 {new_filename}")
#