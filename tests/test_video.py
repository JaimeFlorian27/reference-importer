"""Tests for Video class."""

from pathlib import Path

import pytest
from reference_importer import Timecode, Video, VideoMetadata

TESTS_DIRECTORY = Path(__file__).parent
SAMPLE_VIDEO = TESTS_DIRECTORY / "data" / "sample_video.mp4"


def test_video_no_arguments() -> None:
    """Test Video class intialization without needed parameters."""
    with pytest.raises(TypeError):
        Video()


def test_video_invalid_file() -> None:
    """Test Video class intialization with a non existent file."""
    with pytest.raises(FileNotFoundError):
        Video("missing_file.mp4")


def test_video_valid_file() -> None:
    """Test Video class intialization with a valid file."""
    Video(SAMPLE_VIDEO)


def test_video_metadata() -> None:
    """Test correct metadata creation for video file."""
    expected_resolution = (180, 120)
    expected_frame_rate = 24
    expected_timecode = Timecode(hours=0, minutes=0, seconds=1, frames=0, frame_rate=24)

    expected_metadata = VideoMetadata(
        expected_resolution,
        expected_frame_rate,
        expected_timecode,
    )

    video = Video(SAMPLE_VIDEO)

    assert video.metadata == expected_metadata
