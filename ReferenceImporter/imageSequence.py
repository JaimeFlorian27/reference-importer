import ffmpeg



class ImageSequencer():

    def __init__(self, video_file="",output_dir="",output_name="test%03d.jpg", padding = "%03d" ,output_frameRate= 24):
        self.output_frameRate = output_frameRate
        self.video_file = video_file
        self.output_dir = output_dir
        self.output_name= output_name
        self.padding = padding
        self.trim_start = 0
        self.trim_end = 0
    
    def createSequence(self):
        #Import Video
        self.video_file.encode('Cp1252')
        print(self.video_file)
        input = ffmpeg.input(self.video_file)
        input.filter('fps',self.output_frameRate, round='up')

        #Set Trimming
        #input.trim(start_frame = trim_start, end_frame = trim_end)
        
        #Create Image Sequence
        self.output_dir.encode('Cp1252')
        self.output_name = "test%03d.jpg"
        self.output_name = self.output_dir + '\\'+ self.output_name
        self.output_name.encode('Cp1252')
        print(self.video_file)
        output = ffmpeg.output(input, self.output_name)
        try:
            output.run(capture_stdout=True, capture_stderr=True)
        except ffmpeg.Error as e:
            print('stdout:', e.stdout.decode('utf-8'))
            print('stderr:', e.stderr.decode('utf-8'))
            raise e
        
        #Create Image Plane       
        #image_plane = cmds.imagePlane(fn = self.video_file)
        #cmds.setAttr("%s.useFrameExtension"%image_plane[0],True)


if __name__ == "__main__":
    pass