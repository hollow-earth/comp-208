import skimage.io as io
import numpy as np

#path = input("Enter path of image to be analyzed: ")
pathSave = input("Enter path of root folder: ")
mountain = input("Enter filename + extension for the mountain picture: ")

if pathSave[-1] != "\\":
    pathSave += "\\"

class ImageAnalysis:
    def __init__(self, imagePath):                                                                              # As usual, this is performed when the class is loaded
        self.imageRaster = io.imread(imagePath + mountain)                                                      # We load the mountain.png file, or whatever name is given to it
        self.imagePath = imagePath
    
    def __str__(self):                                                                                          # This is what we want to print
        return "Size of image: " + str(self.imageRaster.shape[1]) + " x " + str(self.imageRaster.shape[0])

    def show(self):                                                                                             # This just shows the mountain image
        io.imshow(self.imageRaster)                                                                             
        io.show()

    def retrieveHidden(self):
        hiddenImage = np.empty([131, 100, 3], dtype=int)                                                        # width (cols), height (rows), depth

        for rows in range(0, 100):                                                                              # We parse the image for those 12th pixels
            for columns in range(0, 131):
                hiddenImage[columns][rows] = self.imageRaster[columns*11][rows*11]                              # We add those to a numpy array, then display it
        
        io.imsave(pathSave + "hidden.png", hiddenImage)

    def fix(self):
        imageFixed = self.imageRaster                                                                           # Clone
        imageFixed = imageFixed.astype("int64")                                                                 # For some obscure reason, the array declared by imageRaster is uint8 by default. 
        averageColor = np.zeros(shape=(3))                                                                      # This sets the values at [0,255]. Hence why I had to convert them back to int64.
        for rows in range(0, 100):                                                                              # Might not be allowed by assignment rules, but I have previous C# experience
            for columns in range(0, 131):                                                                       # These are variations of the average values, they change depending on the position
                if columns != 0 and rows != 0:                                                                  # of the pixel in question (corner takes the average of two pixels for example)
                    averageColor = (imageFixed[columns*11+1][rows*11] + imageFixed[columns*11-1][rows*11] + imageFixed[columns*11][rows*11+1] + imageFixed[columns*11][rows*11-1])//4
                elif rows == 0 and columns != 0:                                                                # We use floored division // to return an integer instead of doing round()
                    averageColor = (imageFixed[columns*11+1][rows*11] + imageFixed[columns*11-1][rows*11] + imageFixed[columns*11][rows*11+1])//3
                elif columns == 0 and rows != 0:
                    averageColor = (imageFixed[columns*11+1][rows*11] + imageFixed[columns*11][rows*11+1] + imageFixed[columns*11][rows*11-1])//3
                elif rows == 0 and columns == 0:
                    averageColor = (imageFixed[columns*11+1][rows*11] + imageFixed[columns*11][rows*11+1])//2
                imageFixed[columns*11][rows*11] = averageColor
        #imageFixed = imageFixed.astype("uint8")                                                                # Uncomment this line to remove the lossy conversion warning intxx -> uint8
        io.imsave(pathSave + "mountain_fixed.png", imageFixed)

    def averageRGB(self):
        image = io.imread(self.imagePath + "hidden.png")                                                        # We load the previous hidden file, though this could be done internally
        averageColorRGB = np.zeros(shape=(np.shape(image)[0], np.shape(image)[1]))                              # We make an empty array the size of the image
        for rows in range(0, np.shape(image)[0]):                                                               # Height (rows)
            for columns in range(0, np.shape(image)[1]):                                                        # Width (cols)
                averageColorRGB[rows][columns] = round(np.average(image[rows][columns]))                        # We average the RGB values
        np.savetxt(pathSave + "hiddenCSV.csv", averageColorRGB, delimiter=",")                                  # We save as .csv
    
    def loadRGBFromFile(self, fileName):
        self.fileName = fileName
        file = np.loadtxt(pathSave + self.fileName, delimiter=",")                                              # We load that same CSV we exported earlier
        loadedRGB = np.zeros((np.shape(file)[0], np.shape(file)[1], 3), dtype=np.uint8)                         # Of course, force the array to be uint8 instead of default float64
        for rows in range(0, np.shape(loadedRGB)[0]):                                                           # Height (rows)
            for columns in range(0, np.shape(loadedRGB)[1]):                                                    # Width (cols)
                x = file[rows][columns]                                                                         # We retrieve the data once by doing this instead of three times
                loadedRGB[rows][columns] = [x,x,x]                                                              # We assign axis=2 with this value for each pixel
        #loadedRGB = loadedRGB.astype("uint8")                                                                  # Uncomment this line to remove the lossy conversion warning intxx -> uint8
        io.imsave(pathSave + "hiddenBW.png", loadedRGB)                                                         # Finally, we save the image, then next line shows it
        io.imshow(loadedRGB)                                                                                    # Averaging the RGB values returns the same image, only black and white
        io.show()

analysis = ImageAnalysis(pathSave)
print(analysis)
analysis.retrieveHidden()
analysis.fix()
analysis.show()
analysis.averageRGB()
analysis.loadRGBFromFile("hiddenCSV.csv")