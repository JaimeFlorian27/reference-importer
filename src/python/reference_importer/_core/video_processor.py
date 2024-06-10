"""Video Processor module."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

import ffmpeg

from .video import VideoError

if TYPE_CHECKING:
    from .video import Timecode, Video


@dataclass
class ProcessorOptions:
    """Options to configure video processing."""

    video_start: Timecode
    video_end: Timecode
    padding: str
    frame_rate: int
    output_dir: Path
    output_file_name: str
    output_extension: str

    def __post_init__(self) -> None:
        """Post initialization checks."""
        # Check if video_start and video_end frame rates match.
        if self.video_start.frame_rate != self.video_end.frame_rate:
            _err_msg = "Mismatched frame rates between video_start and video_end."
            raise VideoError(_err_msg)

    def output_file(self) -> Path:
        """Returns the output file Path."""
        suffix = f".{self.padding}.{self.output_extension}"
        return Path(self.output_dir / self.output_file_name).with_suffix(suffix)


class VideoProcessor:
    """Video Processor class."""

    @staticmethod
    def create_image_sequence(video: Video, options: ProcessorOptions) -> None:
        """Creates an image sequence from a video file using FFmpeg.

        Args:
            video: Video object.
            options: ProcessorOptions object.

        Returns:
            None.
        """
        # Create the output directory if it does not exist.
        try:
            options.output_dir.mkdir(parents=True, exist_ok=True)
        except (FileExistsError, PermissionError) as e:
            _err_msg = "Output directory could not be created."
            raise ValueError(_err_msg) from e

        # Create the image using FFmpeg.
        (
            ffmpeg.input(
                str(video.path),
                ss=options.video_start.with_milliseconds(),
                to=options.video_end.with_milliseconds(),
            )
            # .filter("scale", width=1280, height=-1) # add control
            .filter("fps", fps=options.frame_rate)
            .output(str(options.output_file()))
            .run()
        )


if __name__ == "__main__":
    pass
