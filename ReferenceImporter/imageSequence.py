# -*- coding: Cp1252 -*-

import os
import subprocess



class ImageSequencer():

    def __init__(self, video_file="",output_name="", padding = "%03d" ,output_frameRate= 24):
        self.output_frameRate = output_frameRate
        self.video_file = video_file
        self.output_name= output_name
        self.padding = padding
        self.trim_start = 0
        self.trim_end = 0
        self.ffmpeg_path = ('C:\\Users\\Usuario\\OneDrive\\Escritorio\\Arte\\Programación\\Maya\\scripts\\imageSequence\\ReferenceImporter\\lib\\ffmpeg\\ffmpeg.exe')
        print(self.ffmpeg_path)
    
    def createSequence(self,input_file, frameRate, output_file):
        command = ('ffmpeg -i %s -r %s %s' % (input_file,frameRate,output_file)).encode('Cp1252')
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