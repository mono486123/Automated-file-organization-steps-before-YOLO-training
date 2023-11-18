import subprocess

def run_yolo_detection():
    # Define the command as a list of strings
    command = [
        'python', 'train.py',
        '--workers', '4',
        '--device', '0',
        '--batch-size', '4',
        '--data', 'data/coco.yaml',
        '--img', '640', '640',
        '--cfg', 'cfg/training/yolov7.yaml',
        '--weights', 'runs\\train\\yolov7-custom23\\weights\\last.pt',
        '--name', 'yolov7-custom2',
        '--hyp', 'data/hyp.scratch.custom.yaml',
        '--epochs', '1000',
        '--early-stopping-patience', '10'
    ]
    
    try:
        # Use subprocess to run the command
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running YOLO: {e}")
    except Exception as e:
        print(f"Unknown error running YOLO: {e}")
 
if __name__ == "__main__":
    run_yolo_detection()


#Set-Location -Path "E:\yolov7"