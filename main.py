# 14th of December 2024
# Neural networks. Working with images
# Task: Import any neural network and use it to search no less than two specified patterns on the image     

# # example
# import cv2
# from PIL import Image

# image_path = 'cat.jpg'
# cat_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface_extended.xml')
# image = cv2.imread(image_path)
# cat_face = cat_face_cascade.detectMultiScale(image)

# cat = Image.open(image_path)
# glasses = Image.open('glasses.png')
# cat = cat.convert("RGBA")
# glasses = glasses.convert("RGBA")
# for (x,y,w,h) in cat_face:
#     glasses = glasses.resize((w, int(h/3)))
#     cat.paste(glasses, (x, int(y+h/4)),glasses)
#     cat.save("cat_with_glasses.png")
#     cat_with_glasses = cv2.imread("cat_with_glasses.png")
#     cv2.imshow("Cat_with_glasses", cat_with_glasses)
#     cv2.waitKey()

import cv2
from PIL import Image

image_path = 'doug.jpg'
doug_eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
doug_smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
image = cv2.imread(image_path)
doug_eyes = doug_eyes_cascade.detectMultiScale(image)
doug_smile = doug_smile_cascade.detectMultiScale(image)

doug = Image.open(image_path)
rodya = Image.open('Rodya.png')
doug = doug.convert("RGBA")
rodya = rodya.convert("RGBA")
for (x,y,w,h) in doug_eyes:
    rodya = rodya.resize((w, int(100)))
    doug.paste(rodya, (x, int(y+h/4)),rodya)
    doug.save("doug_with_Rodya_1.png")
    doug_with_Rodya_1 = cv2.imread("doug_with_Rodya_1.png")
    cv2.imshow("doug_with_Rodya_1", doug_with_Rodya_1)
    cv2.waitKey()
for (x,y,w,h) in doug_smile:
    rodya = rodya.resize((w, int(h/3)))
    doug.paste(rodya, (x, int(y+h/4)),rodya)
    doug.save("doug_with_Rodya_2.png")
    doug_with_Rodya_2 = cv2.imread("doug_with_Rodya_2.png")
    cv2.imshow("doug_with_Rodya_2", doug_with_Rodya_2)
    cv2.waitKey()



        