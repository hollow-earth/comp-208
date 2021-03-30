import skimage.io as io
import numpy as np

#path = input("Enter path of image to be analyzed: ")
pathSave = input("Enter path of folder: ")

class ImageAnalysis:
    def __init__(self, imagePath):
        self.imageRaster = io.imread(imagePath + "mountain.png")
        self.imagePath = imagePath
    
    def __str__(self):
        return "Size of image: " + str(self.imageRaster.shape[1]) + " x " + str(self.imageRaster.shape[0])

    def show(self):
        io.imshow(self.imageRaster)
        io.show()

    def retrieveHidden(self):
        hiddenImage = np.empty([131, 100, 3], dtype=int)                                                        # width (cols), height (rows), depth

        for rows in range(0, 100):
            for columns in range(0, 131):
                hiddenImage[columns][rows] = self.imageRaster[columns*11][rows*11]
        
        io.imsave(pathSave + "hidden.png", hiddenImage)

    def fix(self):
        imageFixed = self.imageRaster                                                                           # Clone
        imageFixed = imageFixed.astype("int64")                                                                 # For some obscure reason, the array declared by imageRaster is uint8 by default. 
        averageColor = np.zeros(shape=(3))                                                                      # This sets the values at [0,255]. Hence why I had to convert them back to int64.
        for rows in range(0, 100):                                                                              # Might not be allowed by assignment rules, but I have previous C# experience
            for columns in range(0, 131):
                if columns != 0 and rows != 0:
                    averageColor = (imageFixed[columns*11+1][rows*11] + imageFixed[columns*11-1][rows*11] + imageFixed[columns*11][rows*11+1] + imageFixed[columns*11][rows*11-1])//4   #Average value
                elif rows == 0 and columns != 0:
                    averageColor = (imageFixed[columns*11+1][rows*11] + imageFixed[columns*11-1][rows*11] + imageFixed[columns*11][rows*11+1])//3
                elif columns == 0 and rows != 0:
                    averageColor = (imageFixed[columns*11+1][rows*11] + imageFixed[columns*11][rows*11+1] + imageFixed[columns*11][rows*11-1])//3
                elif rows == 0 and columns == 0:
                    averageColor = (imageFixed[columns*11+1][rows*11] + imageFixed[columns*11][rows*11+1])//2
                imageFixed[columns*11][rows*11] = averageColor
        #imageFixed = imageFixed.astype("uint8")                                                                # Uncomment this line to remove the lossy conversion warning int64 -> uint8
        io.imsave(pathSave + "mountain_fixed.png", imageFixed)

    def averageRGB(self):
        image = io.imread(self.imagePath + "hidden.png")
        averageColorRGB = np.zeros(shape=(np.shape(image)[0], np.shape(image)[1]))
        for rows in range(0, np.shape(image)[0]):                                                               # Height (rows)
            for columns in range(0, np.shape(image)[1]):                                                        # Width (cols)
                averageColorRGB[rows][columns] = round(np.average(image[rows][columns]))
        np.savetxt(pathSave + "hiddenCSV.csv", averageColorRGB, delimiter=",")
    
    def loadRGBFromFile(self, fileName):
        self.fileName = fileName
        file = np.loadtxt(pathSave + self.fileName, delimiter=",")
        loadedRGB = np.zeros((np.shape(file)[0], np.shape(file)[1], 3), dtype=np.uint8)
        for rows in range(0, np.shape(loadedRGB)[0]):                                                           # Height (rows)
            for columns in range(0, np.shape(loadedRGB)[1]):                                                    # Width (cols)
                x = file[rows][columns]
                loadedRGB[rows][columns] = [x,x,x]
        #loadedRGB = loadedRGB.astype("uint8")                                                                  # Uncomment this line to remove the lossy conversion warning int64 -> uint8
        io.imsave(pathSave + "hiddenBW.png", loadedRGB)
        io.imshow(loadedRGB)                                                                                    # Averaging the RGB values returns the same image, only black and white
        io.show()

analysis = ImageAnalysis(pathSave)
print(analysis)
analysis.retrieveHidden()
analysis.fix()
analysis.show()
analysis.averageRGB()
analysis.loadRGBFromFile("hiddenCSV.csv")