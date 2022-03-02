import ffmpeg
import maya.cmds as cmds



class imageSequencer():

    def __init__(self, video_file,output_dir,output_name, padding = "%03d"):
        self.video_file = video_file
        self.output_dir = output_dir
        self.output_name= output_name
        self.padding = padding
        self.trim_start = 0
        self.trim_end = 0
    
    def createSequence(self):
        #Import Video
        input = ffmpeg.input(self.video_file)
        input.filter('fps',12, round='up')

        #Set Trimming
        #input.trim(start_frame = trim_start, end_frame = trim_end)
        
        #Create Image Sequence
        self.output_name = self.output_dir + self.output_name
        output = ffmpeg.output(input, self.output_name)
        output.run()
        
        #Create Image Plane       
        #image_plane = cmds.imagePlane(fn = self.video_file)
        #cmds.setAttr("%s.useFrameExtension"%image_plane[0],True)