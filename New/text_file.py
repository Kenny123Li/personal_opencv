#Creation of text file needed for classifier training
#
filename = "negative_images/bg"
file  = open(filename, "w")


for x in range(2):
    file.write("img"+str(x+1)+".jpg\n")


file.close()
