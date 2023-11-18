#import os
#import re
#
#def replace_start_of_lines_in_directory(directory_path, new_integer):
#    try:
#        for filename in os.listdir(directory_path):
#            if filename.endswith('.txt'):
#                file_path = os.path.join(directory_path, filename)
#                with open(file_path, 'r') as file:
#                    lines = file.readlines()
#
#                new_lines = []
#                for line in lines:
#                    # Use regular expressions to find the first integer at the start of the line 
#                    match = re.match(r'^\d+', line) #'^'表示尋找開頭
#                    if match:
#                        # Replace the found integer with the new integer
#                        line = re.sub(r'^\d+', str(new_integer), line, count=1)
#                    new_lines.append(line)
#
#                with open(file_path, 'w') as file:
#                    file.writelines(new_lines)
#
#                print(f'已成功處理文件：{filename}')
#    
#    except Exception as e:
#        print(f'出現錯誤：{str(e)}')
#
#if __name__ == "__main__":
#    # 設置文件路徑和要替換的新整數
#    directory_path = r"E:\yolov7\data\datasets1\完成txt的照片\10.Kuga-還要整理\labels"
#    new_integer = 13  # Replace with the new integer you want to use
#
#
#    # 調用替換函數
#    replace_start_of_lines_in_directory(directory_path, new_integer)
#


 




##只又改76-79段的程式碼就好
##迴圈處裡多個檔案(txt)
import os
import re

def replace_start_of_lines_in_directory(directory_path, new_integer):
    try:
        for filename in os.listdir(directory_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(directory_path, filename)
                with open(file_path, 'r') as file:
                    lines = file.readlines()

                new_lines = []
                for line in lines:
                    # Use regular expressions to find the first integer at the start of the line 
                    match = re.match(r'^\d+', line) #'^'表示尋找開頭
                    if match:
                        # Replace the found integer with the new integer
                        line = re.sub(r'^\d+', str(new_integer), line, count=1)
                    new_lines.append(line)

                with open(file_path, 'w') as file:
                    file.writelines(new_lines)

                print(f'已成功處理文件：{filename}')
    
    except Exception as e:
        print(f'出現錯誤：{str(e)}')

if __name__ == "__main__":
    # 定義多個資料夾路徑和相對應的整數
    folder_info = [
        
        (r"E:\yolov7\data\datasets1\完成txt的照片\29.Corolla Altis\labels", 0),
        (r"E:\yolov7\data\datasets1\完成txt的照片\30.Corolla Cross\labels", 1),
        (r"E:\yolov7\data\datasets1\完成txt的照片\31.RAV4\labels",2),
        (r"E:\yolov7\data\datasets1\完成txt的照片\32.Yaris\labels", 3),
    ]

    # 依次處理每個資料夾
    for folder_path, new_int in folder_info:
        replace_start_of_lines_in_directory(folder_path, new_int)









##選擇特定檔案
#def replace_start_of_lines(file_path, old_text, new_text):
#    try:
#        with open(file_path, 'r') as file:
#            lines = file.readlines()
#
#        # 替換每行的開頭 "2"
#        new_lines = [line.replace(old_text, new_text, 1) if line.startswith(old_text) else line for line in lines]
#
#        with open(file_path, 'w') as file:
#            file.writelines(new_lines)
#
#        print(f'已成功將每行開頭的 "{old_text}" 替換為 "{new_text}"。')
#    except FileNotFoundError:
#        print(f'找不到文件：{file_path}')
#    except Exception as e:
#        print(f'出現錯誤：{str(e)}')
#
#if __name__ == "__main__":
#    # 設置文件路徑、要替換的內容和新的內容
#    file_path = r'E:\yolov7\data\datasets1\完成txt的照片\1.A250 AMG-還要整理\labels\00.txt'
#    old_text = '2'
#    new_text = '3'
#
#    # 調用替換函數
#    replace_start_of_lines(file_path, old_text, new_text)
#



