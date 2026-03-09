
**ExCamera Binaries**

We use static binaries provided by authors of the [ExCamera system](https://github.com/excamera/excamera-static-bins). Our binaries correspond to the commit `5f25f75` from January 5, 2018.


**Video Data**

As input data, we use the video [drop.avi](https://www.engr.colostate.edu/me/facil/dynamics/files/drop.avi), published by the [Colorado State University Dynamics Lab](https://www.engr.colostate.edu/me/facil/dynamics/).

The video was converted with `ffmpeg`, and later split into individual `y4m` files.

You can reproduce the split using `ffmpeg 4.4.1` (later versions produce very minor differences in some of the frames)

```bash
ffmpeg-4.4.1-amd64-static/ffmpeg -i drop.avi -pix_fmt yuv420p -f yuv4mpegpipe - | python split_y4m.py 30
```

And the following Python script to manually split frames

```python
#!/usr/bin/env python3

import re, sys


def split_y4m(input_stream, frames_per_chunk):
    # e.g. b"YUV4MPEG2 W256 H240 F30:1 Ip A0:0 C420jpeg\n"
    header = input_stream.readline()

    # Parse W and H directly
    W = int(re.search(r"W(\d+)", header.decode()).group(1))
    H = int(re.search(r"H(\d+)", header.decode()).group(1))
    # YUV420: W*H + 2*(W//2)*(H//2)
    frame_size = W * H * 3 // 2

    chunk_idx = 0
    while True:
        frames = []
        for _ in range(frames_per_chunk):
            # b"FRAME\n" or b"FRAME params\n"
            marker = input_stream.readline()
            if not marker:
                break
            data = input_stream.read(frame_size)
            if not data:
                break
            frames.append(marker + data)
        if not frames:
            break
        out_path = f"{chunk_idx:08d}.y4m"
        with open(out_path, "wb") as f:
            # avoid printing this ffmpeg option
            # for binary compatibility of headers
            header = b" ".join(
                f for f in header.split() if not f.startswith(b"XCOLORRANGE")
            )
            f.write(header + b"\n")
            f.writelines(frames)
        print(f"Wrote {out_path} ({len(frames)} frames)")
        chunk_idx += 1


split_y4m(sys.stdin.buffer, int(sys.argv[1]))
```
