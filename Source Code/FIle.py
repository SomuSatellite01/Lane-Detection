import cv2
import numpy as np
def
make_coordinates(ima
ge,line_parameters):
slope,intercept=line_p
arameters
print(image.shape)
y1=image.shape[0]
y2=int(y1*(3/5))
x1=int((y1-
intercept)/slope)
17x2=int((y2-
intercept)/slope)
return
np.array([x1,y1,x2,y2])
return
def average_slope_intercept(image,lines):
18left_fit=[]
right_fit
=[]
for line in lines:
x1,y1,x2,y2=line.resha
pe(4)
parameters=np.polyfit((x1,x2),(y1,
y2),1) slope=parameters[0]
intercept=parameters[1]
if slope <0:
left_fit.append((slope,inter
cept))
else:
right_fit.append((slope,intercept))
19left_fit_average=np.average(left_fit,axis=0)
right_fit_average=np.average(right_fit,axis=
0)
left_line=make_coordinates(image,left_fit_a
verage)
right_line=make_coordinates(image,right_fit
_average) return
np.array([left_line,right_line])
def canny(image):
20gray=cv2.cvtColor(image,cv2.COLOR_RG
B2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
canny=cv2.Canny(blur,50,150)
return canny
def display_lines(image,lines):
line_image=np.zeros_like(i
mage) if lines is not
None:
for x1,y1,x2,y2 in lines:
cv2.line(line_image,(x1,y1),(x2,y2),(255,
0,0),10) return line_image
def
region_of_interest(im
21age): height=image.shape[0]
polygons=np.array([ [(200,height),(
1100,height),(550,250)]
])
mask=np.zeros_like(image)
cv2.fillPoly(mask,polygons,255)
22masked_image=cv2.bitwise_and(ima
ge,mask) return masked_image
cap=cv2.VideoCapture("test2.
mp4") while(cap.isOpened()):
_, frame=cap.read()
canny_image=cann
y(fra me)
cropped_image=region_of_interest(canny_image)
lines=cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),min
Li
neLength=40,m ax LineGap=5)
23averaged_lines=average_slope_intercept(frame,l
ines)
line_image=display_lines(frame,averaged_lines)
combo_image=cv2.addWeighted(frame,0.8,line_
image,1,1) cv2.imshow("result",combo_image)
if cv2.waitKey(1)==ord('q'):
24break
cap.release()
cv2.destroyAllWindows()

