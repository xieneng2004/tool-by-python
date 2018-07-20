import cv2
import os
import numpy as np

# 先导入openCV
# 将一个长的视频缩短，按照比例缩短，只保存其中的一部分
# 如下面代码就是将一个长视频每80秒取60秒，再消除其中帧差较小的帧，再并成一个短视频
def short_cut_video():
    cap = cv2.VideoCapture('myvideo.avi')
    if not cap.isOpened():
        print('video is not opened')
    else:
        # 每秒25帧
        num = 0
        # 取80秒
        needTime = 1500
        # 每80秒
        timeSpace = 2000
        # 获取视频帧率
        fps = cap.get(cv2.CAP_PROP_FPS)
        # AVI格式编码输出XVID
        videoWriter = cv2.VideoWriter('result//resultVideo.avi',cv2.VideoWriter_fourcc('X','V','I','D'),fps,frameSize=(320,288))
        success, frame = cap.read()
        pre_frame = frame
        while(1):
            success,frame = cap.read()
            if success and is_frame_diff(pre_frame,frame):
                if (num%timeSpace <= needTime):
                    videoWriter.write(frame)
                    print('write'+ str(num))
            pre_frame = frame
            num = num + 1
            if not success:
                print('finished')
                break
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
        cap.release()

def is_frame_diff(pre_frame,this_frame):
    # 获取前一帧和这一帧的灰度图
    pre_frame_grey = cv2.cvtColor(pre_frame,cv2.COLOR_BGR2GRAY)
    this_frame_grey = cv2.cvtColor(this_frame,cv2.COLOR_BGR2GRAY)
    # 求两灰度图的差值
    frame_diff = cv2.absdiff(pre_frame_grey,this_frame_grey)
    empty_image = np.asarray(frame_diff,np.uint8)
    # 帧差过大就返回True
    if np.sum(empty_image) / np.sum(this_frame_grey) > 0.07:
        return True
    else:
        return False

def main():
    short_cut_video()

if __name__ == '__main__':
    main()