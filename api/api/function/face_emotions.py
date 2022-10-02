# import os
# import sys
# import cv2
# import cognitive_face as CF

# video_path = "WIN_20211023_16_14_01_Pro.mp4"

# # 動画ファイル読込
# cap = cv2.VideoCapture(video_path)

# if not cap.isOpened():
#     # 正常に読み込めたのかチェックする
#     # 読み込めたらTrue、失敗ならFalse
#     print("動画の読み込み失敗")
#     sys.exit()

# # width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# # height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# # count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
# # fps = cap.get(cv2.CAP_PROP_FPS)

# # print("width:{}, height:{}, count:{}, fps:{}".format(width,height,count,fps))

# digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

# n= 0
# while True:
#     # read()でフレーム画像が読み込めたかを示すbool、フレーム画像の配列ndarrayのタプル
#     is_image,frame_img = cap.read()
    
#     if is_image:
#         # 画像を保存
#         cv2.imwrite(R"" + str(n).zfill(digit) + ".jpg" , frame_img)
#     else:
#         # フレーム画像が読込なかったら終了
#         break
#     n += 1
# ma=0
# igai=0
# #print(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
# sum=0
# x=0
# while x<int(cap.get(cv2.CAP_PROP_FRAME_COUNT)):
#     KEY = '5701f090ac67478bb7a45d2acc869e88'
#     BASE_URL = 'https://japaneast.api.cognitive.microsoft.com/face/v1.0'

#     CF.Key.set(KEY)
#     CF.BaseUrl.set(BASE_URL)
#     #print( str(x).zfill(digit) + ".jpg")
#     img_url =  str(x).zfill(digit) + ".jpg"
#     faces = CF.face.detect(img_url, attributes='emotion')
#     sum+=1
#     x+=int((cap.get(cv2.CAP_PROP_FRAME_COUNT))/10)
#     ma+=faces[0]['faceAttributes']['emotion']['neutral']
#     igai+=faces[0]['faceAttributes']['emotion']['anger']
#     igai+=faces[0]['faceAttributes']['emotion']['contempt']
#     igai+=faces[0]['faceAttributes']['emotion']['disgust']
#     igai+=faces[0]['faceAttributes']['emotion']['fear']
#     igai+=faces[0]['faceAttributes']['emotion']['happiness']
#     igai+=faces[0]['faceAttributes']['emotion']['sadness']
#     igai+=faces[0]['faceAttributes']['emotion']['surprise']
#     #print(faces['faceRectangle']['faceAttributes']['emotion']['anger'])
#     #print(faces)
# cap.release()

# #print(ma)
# #print(igai)
# #print(sum)

# ans=(igai-ma)/sum*100
# print(ans)

# for i in range(n):
#     m= str(i).zfill(digit) + ".jpg" 
#     os.remove(m)