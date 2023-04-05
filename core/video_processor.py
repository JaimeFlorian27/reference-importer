# -*- coding: utf-8 -*-
import os
import subprocess
import ffmpeg


class VideoProcessor:

    def __init__(self, padding="%03d", output_frameRate=24):
        self.output_frameRate = output_frameRate
        self.padding = padding
        self.trim_start = 0
        self.trim_end = 0

    def get_duration(self, video_file):
        """
        Get the duration of a video file in HH:MM:SS.ms format.

        Args:
            video_file (str): Path to the video file.

        Returns:
            str: Formatted duration in HH:MM:SS.ms format.

        Raises:
            Error: If there is an issue with the ffprobe command or the video
            file cannot be probed.

        Example:
            >>> get_duration('path/to/video.mp4')
            '00:01:30.250'
        """

        video = ffmpeg.probe(video_file)
        # Extract the duration in seconds
        duration = float(video['format']['duration'])

        hours = int(duration // 3600)
        minutes = int((duration % 3600) // 60)
        seconds = int(duration % 60)
        milliseconds = int((duration % 1) * 1000)

        # Format the duration in HH:MM:SS.ms format
        formatted_duration = '{:02d}:{:02d}:{:02d}.{:03d}'.format(hours,
                                                                  minutes,
                                                                  seconds,
                                                                  milliseconds)
        return formatted_duration

    def create_image_sequence(self, input_file, frameRate, start_trim, end_trim, output_file):
        command = (
            '"%s" -i "%s" -r %s -vf scale=1280:-1 -q:v 3 -ss %s -to %s "%s"'
            % (
                self.ffmpeg_path,
                input_file,
                frameRate,
                start_trim,
                end_trim,
                output_file,
            )
        ).encode(self.encoding)
        try:
            subprocess.call(command)
        except Exception as e:
            raise e


if __name__ == "__main__":
    pass
