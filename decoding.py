
###################𝓪𝓫𝓭𝓪𝓵𝓵𝓪𝓱 𝔃𝓪𝓱𝓮𝓻 𝓪𝓫𝓾 𝓼𝓮𝓭𝓸###############################
import cv2
import numpy as np

probability = np.load('Probability.npy')
TOTs = np.load('TOTs.npy')
avgnum = np.load("File array.npy")
IMshape = (350,623)
blacksize = 2


def AD(num, p):   
    im = []
    for tot in num:
        Lower, Upper = 0, 1
        for i in range(blacksize):
            for j in range(256):
                p[j] = Lower + (Upper - Lower) * TOTs[j]
                if tot < p[j]:
                    im.append(j)                    
                    if j != 0:
                        Lower = p[j-1]
                    Upper = p[j]
                    break
    return im

img = np.reshape(np.array(AD(avgnum, probability), dtype=np.uint8), IMshape)

cv2.imwrite('output3.png',img)
