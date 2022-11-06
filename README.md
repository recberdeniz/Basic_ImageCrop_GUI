# Basic_ImageCrop_GUI </br>

This application is written by @recberdeniz to make a basic image crop process on basic GUI with PyQt5
In this application there is a main window includes label as an image frame, open button, clip button, save button
and clear button. With using a open button, user can load an image file to the frame(label) and getting a mouse
position going to be active that means when user click 2 different points on the frame, application going to get
this two pixel value each click and create a rectangle accordingly with this 2 different point values. When user click
the clip button, accordingly to rectangle, image going to cropped. Cropping function has some controls that user
firstly click on left bottom, right bottom, right top or left top of the rectangle with in the bounds of possibility
rectangle parameters going to change. Save button using for saving the cropped image with file dialog and user
have to insert a extend of file for example (cropped_image.png, cropped_image.jpg, cropped.tif). Lastly, clear
button using for clear a label that use as image frame. Loaded image sizes might be different, that's why I did not
set the image frame size.
