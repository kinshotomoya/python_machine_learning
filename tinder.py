import pynder
import webbrowser
import numpy as np
import cv2
import urllib.request
import os
import time

def analysis_face(img):
    local_image_path = "test.jpg"
    request_img = urllib.request.urlretrieve(img, local_image_path)
    # web上の画像をlocalに保存する
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    loaded_img = cv2.imread(f"{local_image_path}")
    gray = cv2.cvtColor(loaded_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0:
        print("顔写真はなかったです")
        os.remove(local_image_path)
        # 画像を削除する
        return False
        # 顔検出されなかったら、抜ける
    for (x,y,w,h) in faces:
        # この中で、顔の部分に色をつけている処理をしている
        penned_img = cv2.rectangle(loaded_img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = penned_img[y:y+h, x:x+w]
    cv2.imshow('img',penned_img)
    cv2.destroyAllWindows()
    os.remove(local_image_path)
    return True


# tinderを自動でlikeする（以下のコードはworkしている）
session = pynder.Session("Facebook Access Token")
# このaccess_tokenは、2時間しか期限がないので、実行するたびに更新する
users = session.nearby_users()
for user in users:
    try:
        if user.distance_km < 5:
            user.superlike()
        user_photos = [photo_url for photo_url in user.get_photos(width="640")]
        # print(user_photos)
        for user_photo in user_photos:
            print(user.name)
            print(user.age)
            time.sleep(7)
            face_bool = analysis_face(user_photo)
            if not face_bool:
                continue
            user.like()
            webbrowser.open(user_photo)
    except:
        import traceback
        traceback.print_exc()
        print("例外発生!!!!!!!!")
