import cv2
import os

# 先导入openCV
# 将一个长的视频缩短，按照比例缩短，只保存其中的一部分
# 如下面代码就是将一个长视频每20秒取5秒，合并成一个短视频

cap = cv2.VideoCapture('myvideo.avi')
if not cap.isOpened():
    print('video is not opened')
else:
    # 每秒25帧
    num = 0
    # 取5秒
    needTime = 125
    # 每20秒
    timeSpace = 500
    # 获取视频帧率
    fps = cap.get(cv2.CAP_PROP_FPS)
    # AVI格式编码输出XVID
    videoWriter = cv2.VideoWriter('result//resultVideo_2.avi',cv2.VideoWriter_fourcc('X','V','I','D'),fps,frameSize=(320,288))
    while(1):
        success,frame = cap.read()
        if (num%timeSpace <= needTime):
            videoWriter.write(frame)
            print('write'+ str(num))
        num = num + 1
        if not success:
            print('finished')
            break
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cap.release()