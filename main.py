#!/usr/bin/env python3
import os
import sys
import hashlib
import pathlib

EXPECTED_BYTES = 218373
EXPECTED_SHA256 = "7a65cc6126dab180a06871bccd0c05afd3b85dbcb43b2ad119e15b09db0ef9bc"

def parse_jpeg(data: bytes):
    if len(data) < 2 or data[0:2] != b'\xff\xd8':
        raise SystemExit("Invalid JPEG: missing SOI marker (FF D8)")
    if len(data) < 2 or data[-2:] != b'\xff\xd9':
        raise SystemExit("Invalid JPEG: missing EOI marker (FF D9)")
    
    i = 2
    n = len(data)
    width = None
    height = None
    
    while i < n - 1:
        if data[i] != 0xff:
            i += 1
            continue
        
        while i < n and data[i] == 0xff:
            i += 1
        if i >= n:
            break
        
        marker = data[i]
        i += 1
        
        if marker == 0xd8 or marker == 0xd9 or (0xd0 <= marker <= 0xd7) or marker == 0x01:
            continue
        if marker == 0xff:
            i -= 1
            continue
            
        if i + 2 > n:
            raise SystemExit("Invalid JPEG: truncated segment header")
        
        length = (data[i] << 8) + data[i+1]
        if i + length > n:
            raise SystemExit("Invalid JPEG: segment length exceeds file size")
        
        if marker in (0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7, 0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf):
            if length < 7:
                raise SystemExit("Invalid JPEG: SOF segment too short")
            height = (data[i+3] << 8) + data[i+4]
            width = (data[i+5] << 8) + data[i+6]
            break
            
        i += length
        
    if width is None or height is None:
        raise SystemExit("Invalid JPEG: could not find SOF0/SOF2 frame header")
        
    return width, height

def main():
    script_dir = pathlib.Path(__file__).parent
    img_path = script_dir / "frontpage.jpg"
    
    if not img_path.is_file():
        raise SystemExit(f"frontpage.jpg not found at {img_path}")
        
    data = img_path.read_bytes()
    actual_bytes = len(data)
    actual_sha256 = hashlib.sha256(data).hexdigest()
    
    if actual_bytes != EXPECTED_BYTES:
        raise SystemExit(f"Size mismatch: expected {EXPECTED_BYTES}, got {actual_bytes}")
    if actual_sha256 != EXPECTED_SHA256:
        raise SystemExit(f"SHA256 mismatch: expected {EXPECTED_SHA256}, got {actual_sha256}")
        
    width, height = parse_jpeg(data)
    if width > 1024 or height > 1024:
        raise SystemExit(f"Dimensions exceed 1024 max: {width}x{height}")
        
    outdir_str = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    outdir = pathlib.Path(outdir_str)
    outdir.mkdir(parents=True, exist_ok=True)
    
    entry_path = outdir / "entry.png"
    entry_path.write_bytes(data)
    entry_path.chmod(0o644)
    
    re_data = entry_path.read_bytes()
    re_bytes = len(re_data)
    re_sha256 = hashlib.sha256(re_data).hexdigest()
    if re_bytes != EXPECTED_BYTES or re_sha256 != EXPECTED_SHA256:
        raise SystemExit("Verification failed after writing entry.png")
        
    print(f"Success: dimensions {width}x{height}, byte count {re_bytes}")

if __name__ == "__main__":
    main()
