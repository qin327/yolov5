import cv2
import numpy as np

# 載入車道辨識結果影片
lane_video_path = 'video\output_solidWhiteRight_with_lines.mp4'
lane_cap = cv2.VideoCapture(lane_video_path)

# 載入車輛辨識結果影片
vehicle_video_path = 'runs\detect\exp29\solidWhiteRight.mp4'
vehicle_cap = cv2.VideoCapture(vehicle_video_path)

# 檢查影片是否成功打開
if not lane_cap.isOpened() or not vehicle_cap.isOpened():
    print("Error: Unable to open videos.")
    exit()

# 獲取影片的基本資訊
fps = lane_cap.get(cv2.CAP_PROP_FPS)
width = int(lane_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(lane_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 建立輸出影片
output_video_path = 'video\merge_output.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

while True:
    # 讀取車道辨識影片的一帧
    ret_lane, frame_lane = lane_cap.read()

    # 讀取車輛辨識影片的一帧
    ret_vehicle, frame_vehicle = vehicle_cap.read()

    # 檢查是否成功讀取影片帧
    if not ret_lane or not ret_vehicle:
        break

    # 將兩個影片進行合併
    combined_frame = cv2.addWeighted(frame_lane, 0.4, frame_vehicle, 0.8, 0)

    # 將合併結果寫入輸出影片
    output_video.write(combined_frame)

    # 顯示合併結果
    cv2.imshow('Combined Video', combined_frame)

    # 按下 'q' 鍵退出迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放資源
lane_cap.release()
vehicle_cap.release()
output_video.release()
cv2.destroyAllWindows()
