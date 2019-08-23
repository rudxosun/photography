# -*- coding: utf-8 -*-
"""
1. 모든 이미지 사이즈가 같다는 가정
"""
from PIL import Image
import glob
import shutil #파일복사
import os


if os.path.isdir('/Users/git/Stacking/tmp'):
    if os.listdir('/Users/git/Stacking/pictures') != os.listdir('/Users/git/Stacking/tmp') :
        shutil.copytree('/Users/git/Stacking/pictures', '/Users/git/Stacking/tmp') #tmp로 사본 생성(윈도우와 맥 간의 경로 차이 주의(맥 Users, 윈동 user)
else :
    shutil.copytree('/Users/git/Stacking/pictures', '/Users/git/Stacking/tmp')


images = []
for file_name in glob.glob('/Users/git/Stacking/tmp/*'):
    im = Image.open(file_name)
    images.append(im)

pixels = []
pixcel = []
px = []
tmp = []


New = Image.new('RGB', images[0].size,'white')

def Hue(images): #images라는 튜플 -> Hue라는 리스트
    try:
        Hue_list = []
        for image in images:
            R, G, B = image.getpixel((x,y))
            Max, Min = max(R, G, B), min(R, G, B)
            if Max == R:
                H = 60*abs(G-B)/(Max-Min+0.01) #ZeroDivisionError방지용 0.01
            elif Max == G:
                H = 60*abs(B-R)/(Max-Min+0.01) + 120
            elif Max == B:
                H = 60*abs(R-G)/(Max-Min+0.01) + 240
            Hue_list.append(H)
    except ZeroDivisionError:
        print("0이 나올 리가 없는데...")
    return Hue_list

def Hue_I(image):
    Hue_list = []
    R, G, B = image.getpixel((x,y))
    Max, Min = max(R, G, B), min(R, G, B)
    if Max == R:
        H = 60*abs(G-B)/(Max-Min+0.01) #ZeroDivisionError방지용 0.01
    elif Max == G:
        H = 60*abs(B-R)/(Max-Min+0.01) + 120
    elif Max == B:
        H = 60*abs(R-G)/(Max-Min+0.01) + 240
    Hue_list.append(H)
    return H

def Bright(imange):
    Bright = []
    for image in images:
        R, G, B = image.getpixel((x,y))
        Br = (R + G + B)/3
        Bright.append(Br)
    return Bright






for y in range(images[0].size[1]):
    for x in range(images[0].size[0]):#range?
        #진행률
        '''
        for n in range(10):
            if (y/(images[0].size[1])) :
                print( n , "%진행완료(10%단위)")
'''
        #픽셀을 선택함 / 이미지를 돌려가며 할거


        R,G,B = 0,0,0
        for image in images:
            R += image.getpixel((x,y))[0] #튜플의 언패킹을 사용해보자
            G += image.getpixel((x,y))[1]
            B += image.getpixel((x,y))[2]
        pixel = (int(R/len(images)), int(G/len(images)), int(B/len(images))) # RGB의 평균값



        Hue_m = (sum(Hue(images)))/len(images)
        F = [0,0,0]
        Srgb = 256*256*256
        for image in images: #각 이미지에 대해
            if abs(Hue_m - Hue_I(image)) < Srgb:
            #if abs(Hue_m - Hue_I(image))*(256*256*(256/360)/5) + abs((image.getpixel((x,y))[0] - pixel[0])*(image.getpixel((x,y))[1] - pixel[1])*(image.getpixel((x,y))[2] - pixel[2])) < Srgb: #이미지의 공분산이 Srgb보다 작으면
                #print("Srgb와 분산",Srgb, abs((image.getpixel((x,y))[0] - pixel[0])*(image.getpixel((x,y))[1] - pixel[1])*(image.getpixel((x,y))[2] - pixel[2]))
                Srgb = abs(Hue_m - Hue_I(image))
                #Srgb = abs((image.getpixel((x,y))[0] - pixel[0])*(image.getpixel((x,y))[1] - pixel[1])*(image.getpixel((x,y))[2] - pixel[2]))
               # print("뽑힌 값", image.getpixel((x,y)))
                for i in range(3):
                    F[i] = int(image.getpixel((x,y))[i])
            else :
                pass


        New.putpixel((x,y),tuple(F))
        pixel = []

shutil.rmtree('/Users/git/Stacking/tmp')
New.save("new.jpg")



'''
오답노트
1. R, G, B를 따로따로 평균과 가까운 값을 취하니 [평균과 가까운 픽셀]이 아닌 [평균과 가까운 R과 G와 B를 요소로 가지고있는 새로운 픽셀]이 나옴
 - 공분산을 이용하여 3차원으로 해석 시도중
2. 생각보다 잘 됨. 하지만 지저분한 부분 많음. 물체가 움직일 때 그림자가 지고, non그림자와 그림자의 차이가 의자픽셀보다 클 경우 의자픽셀이 나옴
 = 명도관련 비중을 줄여서 공분산을 계산하면 더 좋을
3. 디렉토리 복사할 때 윈도우와 맥 간의 경로차 확인
4. Hue 조건을 줬더니 계수가 높으면 아무 픽셀이나 합쳐지고 낮으면 변화가 얼마 없는 면에 계단현상이 나타남.
 - Hue를 가중치 중 하나로 줘보자


'''



'''
        #색상이 +-10인 픽셀들은 더 밝은 픽셀로 대체한다.
        for i in range(len(images)):
            for j in range(len(images)):
                if i != j and abs(Hue(images)[i] - Hue(images)[j]) < 2 :
                    if Bright(images)[i] <= Bright(images)[j]:
                        images[i].putpixel((x,y), images[j].getpixel((x,y)))
                    else:
                        images[j].putpixel((x,y), images[i].getpixel((x,y)))
'''
'''
im1 = Image.open("1.jpg")
im2 = Image.open("2.jpg")
im3 = Image.open("3.jpg")
im4 = Image.open("4.jpg")
im5 = Image.open("5.jpg")
New = Image.new("RGB", (1000,1000),"white")
New_file = New.load()

px1, px2, px3, px4, px5 = [], [], [], [], []
avrg = []
tmp = []

#g = getpixel


for y in range(1000):
    for x in range(1000):
            for i in range(3):
                tmp.append(int((im1.getpixel((x,y))[i]+im2.getpixel((x,y))[i]+im3.getpixel((x,y))[i]+im4.getpixel((x,y))[i]+im5.getpixel((x,y))[i])/5))
            New.putpixel((x,y),tuple(tmp))
            tmp = []

        px1.append(im1.getpixel((x,y)))
        px2.append(im2.getpixel((x,y)))
        px3.append(im3.getpixel((x,y)))
        px4.append(im4.getpixel((x,y)))
        px5.append(im5.getpixel((x,y)))

for i in range(1000000):
    for j in range(3):
        tmp.append(int((px1[i][j]+px2[i][j]+px3[i][j]+px4[i][j]+px5[i][j])/5))
    avrg.append(tuple(tmp))
    #New.putpixel((i%1000,i//1000),tuple(tmp))
    tmp = []

for y in range(1000):
    for x in range(1000):
        New.putpixel((x,y),(avrg[1000*x+y]))


for j in range(3):
    for i in range(100):
        avrg[i][j] += (px1[i][j]+px2[i][j]+px3[i][j]+px4[i][j]+px5[i][j])/5



for y in range(10):
    for x in range(10):
        New.putpixel((x,y),(avrg[10*x+y]))
im.save("sample.png")
'''
