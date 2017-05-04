# $ANDROID_HOME/tools/bin/monkeyrunner 
# https://developer.android.com/studio/test/monkeyrunner/index.html

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys,time

device = MonkeyRunner.waitForConnection()

width = device.getProperty("display.width")
height = device.getProperty("display.height")

#back
device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

#go event page
device.touch(300,2100, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)

# scroll up
device.drag((100,1000),(100,0))
device.drag((100,1000),(100,0))
device.drag((100,1000),(100,0))
device.drag((100,1000),(100,0))

# get view
result = device.takeSnapshot()
#result.writeToFile(sys.argv[1],'png')
fink = (-1,247,172,174)
for y in range(0,int(height),10) :
 s = int(width)
 for x in range(0,int(width),5) :
  if result.getRawPixel(x,y) == fink :
   s=min(s,x)
   if x-s > 50 :
    print(x,y)
    device.touch(s,y+50, MonkeyDevice.DOWN_AND_UP)
    break

