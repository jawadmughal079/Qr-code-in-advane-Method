

# first make the varaible of qr to store the functionality of qr code make in advance processer


# QRcode in capitcal is not a module it is a function 

# version means size of qr code 
# error_correction=qrcode.constants.ERROR_CORRECT_L
# ERROR_CORRECT ignore the error percentage when user scane the error
# box_size size of box 
# border size of border

#add.data=add the url into qrcode.Qrcode properties
#fit it can detect the link of url 
#qr_make_image this is use for fill the color into qrcode
# qr_make_image properites [fill_color , back_color ]
#img.save use for give the name to qr code 

# import qrcode as j 
# qr = j.QRCode(
#     version=1,
#     error_correction=j.constants.ERROR_CORRECT_L,
#     box_size=20,
#     border=20,
# )
# qr.add_data('https://www.w3schools.com/python/python_functions.asp#gsc.tab=0')
# qr.make(fit=True)

# img = qr.make_image(fill_color="red", back_color="yellow")
# img.save("enter your name.jpg")

#Step 1 : install th module pip install qrcode [pil ]
        # pil is use for improt the images         

import qrcode 

# Image I should be in the large Character 
from PIL import Image

# Step 2 make a variable to store and change the properties of qr code for make advance qr code 

#QRCode is function not a variable it is use to update the funtion 
qr=qrcode.QRCode(
    version=1,# version is the size of qr code 
    
    # constants.ERROR_CORRECT_L Shoul be in large Characters 
    error_correction=qrcode.constants.ERROR_CORRECT_H,# it help to ignore the user when scanning the qr code 
    border=10,
)

# True T must be capital because this is case sensetive 
qr.add_data('https://www.programiz.com/cpp-programming/online-compiler/')

qr.make(fit=True)# this is use for auto collect the url address for user 

img=qr.make_image(back_color="red" , fit_color="black")# this is use for add the color into images 

img.save("Given the name to Qr Code .png") # this is use for give the name to qr code and end with extension you want to give to image 
        