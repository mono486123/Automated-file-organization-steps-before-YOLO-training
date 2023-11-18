import subprocess

def run_yolo_detection():
    # 使用絕對路徑指定detect.py的位置
    command = r'python E:\yolov7\detect.py --weights "E:\yolov7\runs\train\yolov7-custom23\weights\best.pt" --source "E:\yolov7\inference\images\03.jpg" --save-txt'
    
    try:
        # 使用subprocess模組執行命令行指令
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"執行Yolo時出現錯誤：{e}")
    except Exception as e:
        print(f"執行Yolo時發生未知錯誤：{e}")

if __name__ == "__main__":
    run_yolo_detection()




#anaconda環境激活方法>>  Set-Location -Path "E:\yolov7"  >>conda env list>>conda activate my_yolo_env(D:\Anaconda\envs\torch)>>conda activate D:\Anaconda\envs\torch
