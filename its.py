import cv2
letter = ['@', '%', '#', '*', 'o','=','-',':',',','.']

#gray scale 
def get_gray_scale(file_name):
    img = cv2.imread(file_name)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gs_image= 'gray_scale_'+file_name.split(".")[0] +'.png'
    cv2.imwrite(gs_image, img_gray)
    
    return gs_image
#image to string all or nothing
def image_to_string_aon(file_name):
    img = cv2.imread(file_name )
    img_height = img.shape[0]
    img_width = img.shape[1]
    for i in range(img_width):
        for j in range(img_height):
            test= letter[(img[i][j][0]//26)]
            print(test,end="")
        print()
    
#main
def main():
    file_name= "test.PNG"
    gs_image = get_gray_scale(file_name)
    image_to_string_aon(gs_image)

    

#main 
if __name__ == '__main__':
    main()