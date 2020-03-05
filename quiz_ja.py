import glob
import random
import time
#import subprocess
#import cv2
#import Image
list_quiz = [r.split('/')[-1] for r in glob.glob('./single_ja_wordcloud/*')]
quiz = random.choice(list_quiz)
'''
#subprocess.Popen(['preview','single_ja_wordcloud/'+quiz])
#img = Image.open('single_ja_wordcloud/'+quiz)
img = cv2.imread('single_ja_wordcloud/'+quiz)
cv2.imshow('sample',img)
'''
from PIL import Image
import numpy as np

img = Image.open('single_ja_wordcloud/'+quiz)
img.show()

time.sleep(10)

answer = quiz.replace('wordcloud_ja_','')
answer = answer.replace('_.png','')
print(answer)

'''
from msvcrt import getch

while True:
    key = ord(getch())
    if(key == 13):
        print(quiz)
'''