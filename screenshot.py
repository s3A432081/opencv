# please install opencv-python first
# pip install opencv-python

import cv2
import time
from datetime import datetime

def screenshot():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Can't open camera")
        exit()

    while True:
        # 擷取影像
        ret,frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # 顯示攝像頭畫面
        cv2.imshow('capture',frame)

        # 無限迴圈截圖
        now = datetime.now().strftime('%Y%m%d_%H%M%S')
        cv2.imwrite(f"D:/training data/{now}.png",frame) # 路徑請自行轉換
        print("截圖成功")

        # 按下 q 鍵離開迴圈
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("離開攝像頭")
            break

    # 釋放該攝影機裝置
    cap.release()
    cv2.destroyAllWindows()

screenshot()
        