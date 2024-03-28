# -*- coding: utf-8 -*-
from pathlib import Path
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
        self.ffmpeg_path = Path(__file__).parent.parent.resolve() / "bin" / "ffmpeg"
        
    def getDuration(self, video_file):
        command = (u'"%s" -i "%s" 2>&1 | findstr "Duration"' %(self.ffmpeg_path,video_file))
        try:
           process = subprocess.check_output(command, shell=True)
           process = str(process).strip()
           process = process.split(" ")
           process = process[3][0:11]
        except Exception as e: 
            raise e
        return process
    def createSequence(self,input_file, frameRate,start_trim,end_trim, output_file):
        command = ('"%s" -i "%s" -r %s -vf scale=1280:-1 -q:v 3 -ss %s -to %s "%s"' % (self.ffmpeg_path,input_file,frameRate,start_trim,end_trim,output_file))
        try:
            subprocess.run(command, shell=True)
        except Exception as e: 
            raise e


if __name__ == "__main__":
    pass
