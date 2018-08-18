# piecamera
simply read a frame from picamera module.

simple class to read frames from picamera.

```python
import cv2
from piecamera improt PieCamera


camera = PieCamera()

key = -1
while key == -1:
  ret, frame = camera.read()
  cv2.imshow('frame', frame)
  key = cv2.waitKey(1)
  
cv2.destroyWindow('frame')
```

**PieCamera** class also gets some **picamera** configuration at initiate state such as _frame rate_ , _resolution_, and so on. you can change those properties after defining camera source in the middle of program by using **PieCamera.update_attribs**. but, remember that it's initiate the camera again, so you will see some delays.
