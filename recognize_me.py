from tensorflow.keras.models import load_model
import cv2
import numpy as np

model = load_model('face_training.h5')

size = 150

#视频来源,通过摄像通获取视频流，0表示电脑自带摄像头


cap = cv2.VideoCapture(0)

#使用默认的人脸分类器
classfier = cv2.CascadeClassifier(r'haarcascade_frontalface_alt.xml')

#识别出人脸后画出边框的颜色
color = (0, 255, 0)

classes=["huang","lichangxuan","lilian","linwenxin","liutao","liuyangming","unKnow","xiaoshengze","xuhang","yuanxiaomei","zhangshangtong","zhuoqian"]

while cap.isOpened():
    ok, frame = cap.read() #读取一帧数据
    if not ok:  
        break


    #人脸检测，1.2和2 分别为图片缩放比例和需要检测的有效点数
    faceRects = classfier.detectMultiScale(frame, scaleFactor = 1.2, minNeighbors = 3, minSize = (64, 64))

    if len(faceRects) > 0:            #大于0则检测到人脸                                   
        for faceRect in faceRects:    #单独框出每一张人脸
            x, y, w, h = faceRect

        try:
            image = frame[y-10 : y + h+10 , x-10 : x + w+10]

            image = cv2.resize(image,(size,size))


            img = np.array(image)

            img = img.astype('float32')
            img = np.expand_dims(img,axis=0)


            face_id = model.predict(img, batch_size = 1)
            print(classes[face_id.argmax()])
            string = classes[face_id.argmax()]


            cv2.rectangle(frame,(x,y),(x+w,y+h),color,thickness=2)
            cv2.putText(frame,string,
            (x+30, y+30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,0,255),
            2)
        except:
            pass


    cv2.imshow('camera',frame)

    k = cv2.waitKey(1)
    if k & 0xFF == ord('q'):  
        break
cap.release()
cv2.destroyAllWindows()