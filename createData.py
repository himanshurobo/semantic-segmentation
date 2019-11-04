import numpy as np
import glob
import os
from PIL import Image, ImageDraw


def saveFile( img,outputPath):
    
    img = img.resize((224,224),resample=0)
    print((np.array(img)).shape)
    img.save(outputPath)
        

def getData(matchedPolyFiles,inputPoly_path,inputImg_path,width_in,height_in,width_out,height_out):
    

    
    notIncluded = ['134306tileX_195025tileY_0302222310232120012quadKey_19zoomLevel_5XStitchStride_5YStitchStride',
                '134541tileX_194950tileY_0302222310330001321quadKey_19zoomLevel_5XStitchStride_5YStitchStride']

    
    imE = np.empty((1,1,width_in,height_in))
    maskE = np.empty((1,1,width_out,height_out))
    
    for f in matchedPolyFiles:
        
        
        if f in notIncluded:
            print(f)
            continue
        
        polyFile = inputPoly_path+'/'+f+'.txt'
        imgFile =  inputImg_path +'/'+f+'.png'
        print(imgFile)
        lines = [eval(line.rstrip('\n')) for line in open(polyFile)]
        # print((lines))
        
        output = []
        for l in lines:
            # print(len(l))
            output.append([ tuple(a) for a in l])
        
        #just to save images
        img = Image.new('RGB', (1280, 1280),0)
        im = Image.open(imgFile).convert('RGB')
        for o in output:
            ImageDraw.Draw(img).polygon(o, outline=None, fill=(255,255,255))
        
        inputImg_path1 = os.path.join('./here/cleanImages/Images')
        inputPoly_path1 = os.path.join('./here/cleanImages/Masks')
        polyFile1 = inputPoly_path1+'/'+f+'.png'
        imgFile1 =  inputImg_path1 +'/'+f+'.png'
        saveFile(img,polyFile1)
        saveFile(im,imgFile1)
        # plt.imshow(img)
        # plt.figure()
        # plt.imshow(im)
        # plt.show()   

def getFiles():
    

    
    inputPoly_path = os.path.join('./here/labels_stitched_1280x1280/poly_xy_footprints')
    inputImg_path = os.path.join('./here/images')
    
    # subject_path = [os.path.join(input_path, 'Subject_0{}.mat'.format(i)) for i in range(1, 10)] + [os.path.join(input_path, 'Subject_10.mat')]
    # #subject_path = [os.path.join(input_path, 'Subject_0{}.mat'.format(i)) for i in range(1, 3)]
    # m = len(subject_path)

    imgFiles = [ (f.split("/")[-1]).split(".png")[0] for f in glob.glob(inputImg_path+"/*.png") ] 
    polyFiles = [ (f.split("/")[-1]).split(".txt")[0] for f in glob.glob(inputPoly_path+"/*.txt")]
    print(imgFiles[0])
    print(polyFiles[0])
    
    matchedPolyFiles = [f for f in imgFiles if f in polyFiles]
    print("+++",len(matchedPolyFiles))

    return matchedPolyFiles,inputPoly_path,inputImg_path



if __name__ == "__main__":
    
    width_in = 1280
    height_in = 1280
    width_out = 1280
    height_out = 1280
    m = 10
    
    
    matchedPolyFiles,inputPoly_path,inputImg_path = getFiles()
    print("-->>",len(matchedPolyFiles))
    getData(matchedPolyFiles[:m],inputPoly_path,inputImg_path,width_in,height_in,width_out,height_out)

    
    
    pass