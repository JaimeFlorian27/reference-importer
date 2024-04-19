from __future__ import annotations
import re
import shutil
import subprocess
import platform
from pathlib import Path

TIMECODE_REGEX = r"Duration: (\d{2}:\d{2}:\d{2}.\d)"


class FfmpegError(Exception):
    ...

class MissingFfmpeg(FfmpegError):
    ...


class ImageSequencer:
    def __init__(
        self,
        video_file: str = "",
        output_name: str = "",
        padding: str = "%03d",
        output_frame_rate: int = 24,
    ) -> None:
        self.output_frame_rate = output_frame_rate
        self.video_file = video_file
        self.output_name = output_name
        self.padding = padding
        self.trim_start = 0
        self.trim_end = 0
        self.ffmpeg_path = self.get_ffmpeg_path()

    @classmethod
    def get_ffmpeg_path(cls) -> Path:
        """Resolves the path to ffmpeg.

        The script first attempts to use the ffmpeg available in the bin folder,
        otherwise it fallbacks to the first match of ffmpeg avaiable in Path.

        Raises:
            MissingFfmpeg: If no ffmpeg binaries are available.

        """
        _ffmpeg_binary = f"ffmpeg{'.exe' if platform.system() == 'Windows' else ''}"
        ffmpeg_executable = Path(__file__).parent.parent.resolve() / "bin" / _ffmpeg_binary 
        if not ffmpeg_executable.exists():
            ffmpeg_executable = shutil.which("ffmpeg")

        if not ffmpeg_executable:
            raise MissingFfmpeg()
        return Path(ffmpeg_executable)

    def get_duration(self, video_file: str) -> str:
        """Gets the duration of the video from the output of ffmpeg -i.

        Args:
            video_file: Video file.

        Raises:
            FfmpegError: If ffmpeg errors out and does not yield an output.
            ValueError: If there is no match for the duration in ffmpeg's output.

        Returns:
            Duration of the video in timecode.
        """
        command = f'"{self.ffmpeg_path}" -i "{video_file}"'
        try:
            output = str(
                subprocess.run(
                    command,
                    shell=True,
                    stderr=subprocess.STDOUT,
                    stdout=subprocess.PIPE,
                    check=False,
                ),
            )

        except subprocess.CalledProcessError as e:
            _except_msg: str = "Unable to get ffmpeg output"
            raise FfmpegError(_except_msg) from e

        # re.search searches across the whole string (multiline output).
        match: re.Match | None = re.search(TIMECODE_REGEX, output)

        if not match:
            _except_msg: str = f"Unable to find Duration for video {video_file}"
            raise ValueError(_except_msg)

        # the timecode is the first group of the match.
        duration: str = str(match.groups(0)[0])
        return duration

    def create_sequence(
        self,
        input_file: str,
        frame_rate: int,
        start_trim: str,
        end_trim: str,
        output_file: str,
    ):
        command = (
            f'"{self.ffmpeg_path}" -i "{input_file}" -r {frame_rate}'
            f" -vf scale=1280:-1 -q:v 3 -ss {start_trim} -to {end_trim} "
            f'"{output_file}"'
        )
        try:
            subprocess.run(command, shell=True, check=False)
        except subprocess.CalledProcessError as e:
            raise FfmpegError from e


if __name__ == "__main__":
    pass
