# -*- coding: utf-8 -*-

import os
import subprocess



class ImageSequencer():

    def __init__(self, video_file="",output_dir="",output_name="test%03d.jpg", padding = "%03d" ,output_frameRate= 24):
        self.output_frameRate = output_frameRate
        self.video_file = video_file
        self.output_dir = output_dir
        self.output_name= output_name
        self.padding = padding
        self.trim_start = 0
        self.trim_end = 0
        self.ffmpeg_path = 'C:\\Users\\Usuario\\OneDrive\\Escritorio\\Arte\\Programación\\Maya\\scripts\\imageSequence\\ReferenceImporter\\lib\\ffmpeg\\ffmpeg.exe'
    
    def createSequence(self):
        self.output_name = "test%03d.jpg"
        self.output_name = self.output_dir + "\\" + self.output_name

        command = ([self.ffmpeg_path, '-i', self.video_file, '-r', '24', '-o', self.output_name])
        try:
            subprocess.call(command, shell=True)
        except:
            print("Failed to playblast during command call.")
        #Create Image Plane       
        #image_plane = cmds.imagePlane(fn = self.video_file)
        #cmds.setAttr("%s.useFrameExtension"%image_plane[0],True)


if __name__ == "__main__":
    pass