"""One Ingredient, One Craving — a macro strawberry, rendered in PIL.

Entry program for make.fun bounty the-picture-that-tastes-of-one-20261122-2047.
It ships the committed entry.png unchanged: it reads the image from the
repository root, checks it is a whole 1024x1024 PNG no larger than 1 MiB,
writes those exact bytes to the output path, then re-reads the output and
compares it byte for byte. Standard library only, no network, deterministic.
"""

import os
import struct
import sys
import zlib

SOURCE_NAME = "entry.png"
MAX_BYTES = 1048576
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_png_size(data):
    """Return (width, height) from the IHDR chunk of a PNG byte string."""
    if len(data) < 33:
        fail("entry.png is too short to hold a PNG header")
    if data[:8] != PNG_MAGIC:
        fail("entry.png does not start with the PNG magic bytes")
    ihdr_length = struct.unpack(">I", data[8:12])[0]
    ihdr_type = data[12:16]
    if ihdr_type != b"IHDR" or ihdr_length != 13:
        fail("entry.png has no valid IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def validate_png(data):
    """Check magic, size, dimensions and that the file ends with IEND."""
    if len(data) > MAX_BYTES:
        fail(f"entry.png is {len(data)} bytes, over the 1048576 byte limit")
    width, height = read_png_size(data)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        fail(f"entry.png is {width}x{height}, expected 1024x1024")
    if not data.endswith(b"IEND\xaeB`\x82"):
        fail("entry.png does not end with a valid IEND chunk")
    return width, height


def output_path():
    """Where the grader wants the image: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.png")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    if not os.path.isfile(source):
        fail(f"could not find {SOURCE_NAME} next to main.py")
    with open(source, "rb") as handle:
        data = handle.read()
    width, height = validate_png(data)

    dest = output_path()
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as handle:
        handle.write(data)
    with open(dest, "rb") as handle:
        written = handle.read()
    if written != data:
        fail("output entry.png differs from the committed entry.png")
    crc = zlib.crc32(data) & 0xFFFFFFFF
    print(f"wrote {dest}: {width}x{height} PNG, {len(data)} bytes, crc32={crc:08x}")


if __name__ == "__main__":
    main()
