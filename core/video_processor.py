# -*- coding: utf-8 -*-
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
        duration = float(video["format"]["duration"])

        hours = int(duration // 3600)
        minutes = int((duration % 3600) // 60)
        seconds = int(duration % 60)
        milliseconds = int((duration % 1) * 1000)

        # Format the duration in HH:MM:SS.ms format
        formatted_duration = "{:02d}:{:02d}:{:02d}.{:03d}".format(
            hours, minutes, seconds, milliseconds
        )
        return formatted_duration

    def create_image_sequence(
        self, input_file, frame_rate, start_trim, end_trim, output_file
    ):
        """
        Creates an image sequence from a video file using FFmpeg.

        Args:
            input_file (str): Path to the input video file.

            frame_rate (int): Frame rate of the output image sequence.

            start_trim (Optional[str]): Start timecode for trimming the input
            video file (default: None).

            end_trim (Optional[str]): End timecode for trimming the input video
            file (default: None).

            output_file (str): Path to the output image sequence file. The file
            path should include the image file pattern,
            e.g., '/path/to/output_file_%04d.png'.

        Returns:
            None

        Raises:
            ValueError: If the output file path doesn't include the image file
            pattern.

        Example:
            >>> create_image_sequence('/path/to/input_file.mp4',
                                      30, start_trim='00:00:10',
                                      end_trim='00:01:30',
                                      output_file='/path/output_file_%04d.png')
        """
        (
            ffmpeg.input(input_file, ss=start_trim, to=end_trim)
            .filter("scale", width=1280, height=-1)
            .filter("fps", fps=frame_rate)
            .output(output_file, q=3)
            .run()
        )


if __name__ == "__main__":
    pass
