"""Defines classes for storing and accessing the data of a video file."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import ffmpeg


class VideoError(Exception):
    """Base class for Exceptions raised by Video related objects."""


class VideoMetadataError(VideoError):
    """Class that represents an error related to video metadata."""


@dataclass
class Timecode:
    """Stores the data that describes a SMPTE Timecode."""

    hours: int
    minutes: int
    seconds: int
    frames: int
    frame_rate: int

    def __str__(self) -> str:
        """Returns the timecode in SMPTE format HH:MM:SS:FF."""
        return (
            f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
            f":{int(self.frames)}"
        )

    def as_frames(self) -> int:
        """Returns the timecode as the total number of frames."""
        return (
            self.hours * 3600 * self.frame_rate
            + self.minutes * 60 * self.frame_rate
            + self.seconds * self.frame_rate
            + self.frames
        )

    def with_milliseconds(self) -> str:
        """Returns the timecode as a formatted as HH:MM:SS.MS."""
        return (
            f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
            f".{int(self.frames/self.frame_rate*1000)}"
        )

    @staticmethod
    def from_string(timecode: str, frame_rate: int) -> Timecode:
        """Initializes a Timecode object from a string.

        Args:
            timecode: String in the format HH:MM:SS:FF.
            frame_rate: Frame rate of the video.

        Returns:
            Timecode object that describes the timecode.
        """
        # Parts could be missing, account for that.
        hours, minutes, seconds, frames = map(int, timecode.split(":"))
        return Timecode(
            hours=hours,
            minutes=minutes,
            seconds=seconds,
            frames=frames,
            frame_rate=frame_rate,
        )

    @staticmethod
    def from_milliseconds(milliseconds: float, frame_rate: int) -> Timecode:
        """Initializes a Timecode object from milliseconds.

        Args:
            milliseconds: Milliseconds to convert into timecode.
            frame_rate: Frame rate of the video.

        Returns:
            Timecode object that describes the milliseconds.
        """
        # Constants for time units in milliseconds.
        ms_per_second: int = 1000
        ms_per_minute: int = 60 * ms_per_second
        ms_per_hour: int = 60 * ms_per_minute

        # Calculate hours, minutes, seconds, and remaining milliseconds.
        hours: int = int(milliseconds // ms_per_hour)
        milliseconds %= ms_per_hour

        minutes: int = int(milliseconds // ms_per_minute)
        milliseconds %= ms_per_minute

        seconds: int = int(milliseconds // ms_per_second)
        milliseconds %= ms_per_second

        frames = int(milliseconds / (ms_per_second * frame_rate))

        return Timecode(
            hours=hours,
            minutes=minutes,
            seconds=seconds,
            frames=frames,
            frame_rate=frame_rate,
        )


@dataclass
class VideoMetadata:
    """Stores metadata of a video file."""

    resolution: tuple[int, int]
    frame_rate: int
    duration: Timecode


class Video:
    """Describes the data of a video file on disk."""

    def __init__(self, path: Path | str) -> None:
        """Initializes a Video object and its VideoMetadata.

        Args:
            path: path to the video file.
        """
        # Add better error for possibly incorrect path.
        self.path: Path = Path(path).expanduser().resolve()
        if not self.path.exists():
            _err_msg = f"File {self.path} does not exist."
            raise FileNotFoundError(_err_msg)
        self.metadata: VideoMetadata = self._construct_metadata()

    def _construct_metadata(self) -> VideoMetadata:
        """Contructs the VideoMetadata object for this Video object.

        Raises:
            VideoMetadataError: If the video could not be probed.
            VideoMetadataError: If the stream metadata could not be extracted.
            VideoMetadataError: If the stream metadata is empty.
            VideoMetadataError: If the frame rate could not be calculated.
            VideoMetadataError: If the duration could not be calculated.
            VideoMetadataError: If the resolution could not be extracted.

        Returns:
            VideoMetadata object describing some of the metadata of the video file.
        """
        try:
            probe_output: dict[str, Any] = ffmpeg.probe(
                str(self.path.expanduser().resolve()),
            )
        except ffmpeg.Error as e:
            _err_msg = "Could not probe video file."
            raise VideoMetadataError(_err_msg) from e

        # Extract only the necessary metadata from probe's output.
        try:
            stream_metadata: dict[str, Any] = probe_output["streams"][0]
        except (ValueError, IndexError, KeyError) as e:
            # log could not extract duration from video.
            _err_msg = "Could not get stream metadata from video."
            raise VideoMetadataError(_err_msg) from e
        if not stream_metadata:
            _err_msg = "Stream metadata is empty."
            raise VideoMetadataError(_err_msg)

        metadata: dict[str, Any] = {}

        # Calculate the frame rate of the video.
        try:
            # r_frame_rate is a fraction x/y.
            r_frame_rate: str = stream_metadata["r_frame_rate"]

            # Calculate the fraction.
            dividend, divisor = r_frame_rate.split("/")
            frame_rate = int(dividend) // int(divisor)

            metadata["frame_rate"] = frame_rate
        except (KeyError, ArithmeticError) as e:
            _err_msg = "Could not calculate frame rate."
            raise VideoMetadataError(_err_msg) from e

        # Construct the timecode that describes the video's duration.
        try:
            # duration is represented
            duration = float(stream_metadata["duration"]) * 1000
            metadata["duration"] = Timecode.from_milliseconds(
                duration,
                metadata["frame_rate"],
            )
        except KeyError as e:
            _err_msg = "Could not get duration."
            raise VideoMetadataError(_err_msg) from e

        # Extract the Resolution and add it to the metadata.
        try:
            metadata["resolution"] = (
                stream_metadata["width"],
                stream_metadata["height"],
            )
        except KeyError as e:
            _err_msg = "Could not get resolution."
            raise VideoMetadataError(_err_msg) from e

        # Construct the VideoMetadata object and return it
        return VideoMetadata(**metadata)
