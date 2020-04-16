
###################𝓪𝓫𝓭𝓪𝓵𝓵𝓪𝓱 𝔃𝓪𝓱𝓮𝓻 𝓪𝓫𝓾 𝓼𝓮𝓭𝓸###############################


# image using PIL module
# importing PIL
import cv2
import numpy as np
blocksize = 2
#reading the image and convert it to grayscaling 
gray = cv2.imread('input3.png',cv2.IMREAD_GRAYSCALE)
#convert the image to a flatten array
im = np.array(gray).flatten()
IMshape = im.shape

print('array is created')
#create an array of zeros
probability = np.zeros(shape=(256,))
tot = np.zeros(shape=(256,))
totsum =0
#cluc the propbablity 
for i in im:
    probability[i] += 1
     
print("probability is culculated ")
     
print(probability)    
#devide the prob on the image size    
for i in range(256):
     probability[i] /= im.size
     totsum += probability[i]
     tot[i] = totsum
print("devide the prob on the image size")    
     
#if the image size is not dividable on the blocksize add some zeros
#while im.size % blocksize != 0:
     # im = np.append(im, 0)
   
print("add some zeros")
#artihmetic coding function 
def AC(array , a):
    upperperv = 1
    lowerprev = 0
    for i in array :
        UPPRE = upperperv
        LOPRE = lowerprev
        if i == 0:
            tots= 0
        else:
            tots =tot[i-1]
            
        lowerprev = LOPRE + (UPPRE - LOPRE)* tots
        upperperv = LOPRE + (UPPRE - LOPRE)* tot[i]
        
    avg = (upperperv + lowerprev)/2
    return avg
    print("avg is done")
    
noOfLoops = im.size // blocksize 
tags = np.zeros(shape=(noOfLoops, ))

for i in range(noOfLoops):
    tags[i] = AC(im[i*blocksize:i*blocksize +blocksize],probability)
    
print("done")

np.save('File array' ,tags)
np.save('Probability' , probability)
np.save('TOTs',tot)

