import os

#print(os.getcwd())

directory = '/home/pi/Desktop/personal_opencv/New/negative_images'
bg = open("bg", "w")
many = 0

for filename in os.listdir(directory):
    if filename.endswith(".gitkeep"):
        continue
    else:
        many += 1
        bg.write("negative_images/"+str(filename)+"\n")
        continue
print(many)
bg.close()

#for i in range(20):
#    bg.write("negative_images/nimg"+str(i+1)+".jpg\n")

#bg.close()

