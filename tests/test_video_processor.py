"""Tests for the video_processor module."""

from pathlib import Path

import pytest
from reference_importer import ProcessorOptions, Timecode, VideoError


def test_processor_options_no_arguments() -> None:
    """Test ProcessorOptions class intialization without needed parameters."""
    with pytest.raises(TypeError):
        ProcessorOptions()  # pyright: ignore[reportCallIssue]


def test_processor_options() -> None:
    """Test ProcessorOptions class with valid parameters."""
    ProcessorOptions(
        video_start=Timecode.from_milliseconds(0.0, 24),
        video_end=Timecode.from_milliseconds(1000.0, 24),
        padding="%03d",
        frame_rate=24,
        output_dir=Path("test_dir"),
        output_file_name="test_file_name",
        output_extension=".jpg",
    )


def test_processor_options_mismatched_timecode_frame_rate() -> None:
    """Test ProcessorOptions class with mismatched start and end timecome frame rate."""
    with pytest.raises(VideoError):
        ProcessorOptions(
            video_start=Timecode.from_milliseconds(0.0, 24),
            video_end=Timecode.from_milliseconds(1000.0, 30),
            padding="%03d",
            frame_rate=24,
            output_dir=Path("test_dir"),
            output_file_name="test_file_name",
            output_extension=".jpg",
        )
