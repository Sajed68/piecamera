# -*- coding: utf-8 -*-

# ***************************License:***********************************
"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
# Author: Sajed Rakhshani
# Start: 27 Mordad 1397
# URL: gitlab.com/sajed68
# URL: github.com/Sajed68
# #####################################################



import time
from picamera.array import PiRGBArray
from picamera import PiCamera


class PieCamera(PiCamera):
    def __init__(self, resolution=(480, 320), framerate=30, format='bgr', use_video_port=True, resize=None, splitter_port=0, burst=False, bayer=False):
        super(PieCamera, self).__init__()
        self.resolution = resolution
        self.framerate = framerate
        self.rawCapture = PiRGBArray(self)
        time.sleep(0.1)
        self.stream = self.capture_continuous(self.rawCapture, format=format, use_video_port=use_video_port, resize=resize, splitter_port=splitter_port, burst=burst, bayer=bayer)
    
    
    def read(self):
        for frame in self.stream:
            img = frame.array
            self.rawCapture.truncate(0)
            break
        ret = True if img is not None else False
        return ret, img
    
    
    def update_attribs(self, resolution=(480, 320), framerate=30, format='bgr', use_video_port=True, resize=None, splitter_port=0, burst=False, bayer=False):
        self.resolution = resolution
        self.framerate = framerate
        self.rawCapture = PiRGBArray(self, size=resolution)
        time.sleep(0.1)
        self.stream = self.capture_continuous(self.rawCapture, format=format, use_video_port=use_video_port, resize=resize, splitter_port=splitter_port, burst=burst, bayer=bayer)
