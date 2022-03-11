# -*- coding: Cp1252 -*-

import os
import subprocess
import os



class ImageSequencer():

    def __init__(self, video_file="",output_name="", padding = "%03d" ,output_frameRate= 24):
        self.output_frameRate = output_frameRate
        self.video_file = video_file
        self.output_name= output_name
        self.padding = padding
        self.trim_start = 0
        self.trim_end = 0
        self.ffmpeg_path = os.path.abspath(os.path.dirname(__file__)).decode('Cp1252')
        self.ffmpeg_path = os.path.join(self.ffmpeg_path,'lib\\ffmpeg\\', 'ffmpeg').replace("\\","/")
    
    def getDuration(self, video_file):
        command = ('"%s" -i %s 2>&1 | grep "Duration"' %(self.ffmpeg_path,video_file)).encode('Cp1252')
        try:
            
           process = subprocess.check_output(command, shell=True).encode('Cp1252')
           process = process.splitlines(True)
           process = process[1].strip()
           process = process.split(" ")[1][0:11]
        except Exception as e: 
            print(e)
            raise e
        return process
    def createSequence(self,input_file, frameRate,start_trim,end_trim, output_file):
        command = ('%s -i %s -r %s -vf scale=1280:-1 -ss %s -to %s %s' % (self.ffmpeg_path,input_file,frameRate,start_trim,end_trim,output_file)).encode('Cp1252')
        print(command)
        try:
            subprocess.call(command)
        except Exception as e: 
            print(e)
            raise e
        #Create Image Plane       
        #image_plane = cmds.imagePlane(fn = self.video_file)
        #cmds.setAttr("%s.useFrameExtension"%image_plane[0],True)


if __name__ == "__main__":
    pass