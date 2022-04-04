# -*- coding: utf-8 -*-

import cv2
import os

files = os.listdir()


img_path_list = []

#dosyalarda sonu png ile bitenleri img_path_liste ekle
for f in files:
    if f.endswith(".png"):
        img_path_list.append(f)

print(img_path_list)  

# img_path_list'i oku   

for j in img_path_list:
    print(j)
    image = cv2.imread(j)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #haarcascade'i çek
    detector = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
    rects = detector.detectMultiScale(gray, scaleFactor =1.045 ,minNeighbors = 2)
    
    #kedileri numaralandır
    for(i, (x,y,w,h)) in enumerate(rects):
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,255),2)
        cv2.putText(image, "Kedi {}".format(i+1), (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.55,(0,255,255),2)
    
    cv2.imshow(j, image)
    if cv2.waitKey(0) & 0xFF == ord("q"): continue     