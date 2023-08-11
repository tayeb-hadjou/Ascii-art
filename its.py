import cv2
letter = ['@', '%', '#', '*', 'o','=','-',':',',','.']
pbs=1 #pixel block size

#gray scale 
def get_gray_scale(file_name):
    img = cv2.imread(file_name)
    #print(img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gs_image= 'gray_scale_'+file_name.split(".")[0] +'.png'
    cv2.imwrite(gs_image, img_gray)
    
    return gs_image

def image_to_string_aon(file_name):
    
    img = cv2.imread(file_name )
    img = cv2.resize(img, (500, 500))
    img_height = img.shape[0]
    img_width = img.shape[1]
    print(img_height,img_width)
    for i in range(0,img_height,pbs):
        for j in range(0,img_height,pbs):
            avg = img[i:i+pbs,j:j+pbs].mean()
            if(avg>=0):
                test= letter[(int(avg)//26)]
                print(test,end="")
        print()
#main
def main():
    file_name= "test.jpg"
    gs_image = get_gray_scale(file_name)
    image_to_string_aon(gs_image)
#main 
if __name__ == '__main__':
    main()