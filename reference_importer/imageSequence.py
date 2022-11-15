# -*- coding: utf-8 -*-
import sys
import os
import subprocess



class ImageSequencer():

    def __init__(self, video_file="",
                 output_name="", 
                 padding = "%03d" ,
                 output_frameRate= 24):
        
        self.output_frameRate = output_frameRate
        self.video_file = video_file
        self.output_name= output_name
        self.padding = padding
        self.trim_start = 0
        self.trim_end = 0
        self.encoding = 'cp1252'
        self.ffmpeg_path = os.path.abspath(os.path.dirname(__file__)
                                           ).decode(self.encoding)
        self.ffmpeg_path = os.path.join(self.ffmpeg_path,
                                        '..',
                                        'lib',
                                        'ffmpeg', 
                                        'ffmpeg')
        
    def getDuration(self, video_file):
        command = (u'"%s" -i "%s" 2>&1 | findstr "Duration"' %(self.ffmpeg_path,video_file)).encode(self.encoding)
        try:
           process = subprocess.check_output(command, shell=True).encode(self.encoding)
           process = str(process).strip()
           process = process.split(" ")
           process = process[1][0:11]
        except Exception as e: 
            raise e
        return process
    def createSequence(self,input_file, frameRate,start_trim,end_trim, output_file):
        command = ('"%s" -i "%s" -r %s -vf scale=1280:-1 -q:v 3 -ss %s -to %s "%s"' % (self.ffmpeg_path,input_file,frameRate,start_trim,end_trim,output_file)).encode(self.encoding)
        try:
            subprocess.call(command)
        except Exception as e: 
            raise e


if __name__ == "__main__":
    pass