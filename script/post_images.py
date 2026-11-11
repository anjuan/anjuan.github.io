#!/usr/bin/env python3
"""Keep the blog list's post images and thumbnails up to date.

The blog list (blog/index.html) shows each post's header image to the left of
the post. It reads the image from an `image:` line in the post's front matter
and, when one exists, uses a small copy from /images/thumbs/ so the page
doesn't download full-size originals.

For every post in _posts/, this script:
  1. Adds an `image:` line to the front matter if the post doesn't have one,
     copied from the first {% include image.html url="..." %} in the post.
  2. Creates /images/thumbs/<name>.jpg for the post's image (and for the
     default image in _config.yml) if that thumbnail doesn't exist yet.

It never changes a post that already has an `image:` line, and never
overwrites an existing thumbnail, so it's safe to run any time.

Run it from the repo root after writing a new post:

    python3 script/post_images.py

It needs Pillow (python3 -m pip install Pillow).
"""

import os
import re
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is required: python3 -m pip install Pillow")

POSTS_DIR = "_posts"
THUMBS_DIR = os.path.join("images", "thumbs")
THUMB_WIDTH = 640
THUMB_QUALITY = 80

INCLUDE_URL = re.compile(r'\{%-?\s*include\s+image\.html\b[^%]*?\burl="([^"]+)"')
IMAGE_LINE = re.compile(r"^image:\s*(.*?)\s*$", re.MULTILINE)
DEFAULT_LINE = re.compile(r"^default_post_image:\s*(.*?)\s*$", re.MULTILINE)


def split_front_matter(text):
    """Return (front_matter, body) or (None, text) if there is none."""
    match = re.match(r"---\r?\n(.*?\r?\n)---\r?\n", text, re.DOTALL)
    if not match:
        return None, text
    return match.group(1), text[match.end():]


def unquote(value):
    return value.strip().strip("\"'")


def add_image_line(path):
    """Add `image:` to a post's front matter. Returns the post's image URL."""
    with open(path, encoding="utf-8", newline="") as f:
        text = f.read()
    front, body = split_front_matter(text)
    if front is None:
        return None

    existing = IMAGE_LINE.search(front)
    if existing:
        return unquote(existing.group(1)) or None

    found = INCLUDE_URL.search(body)
    if not found:
        return None
    url = found.group(1)

    newline = "\r\n" if "\r\n" in front else "\n"
    new_front = front + 'image: "' + url + '"' + newline
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("---" + newline + new_front + "---" + newline + body)
    print("added image to " + os.path.basename(path))
    return url


def make_thumbnail(url):
    """Create images/thumbs/<stem>.jpg for a local /images/ URL."""
    if not url or not url.startswith("/"):
        return
    source = url.lstrip("/")
    stem = os.path.splitext(os.path.basename(source))[0]
    target = os.path.join(THUMBS_DIR, stem + ".jpg")
    if os.path.exists(target):
        return
    if not os.path.exists(source):
        print("missing image, no thumbnail: " + url)
        return

    with Image.open(source) as im:
        im = im.convert("RGBA")
        flat = Image.new("RGB", im.size, (255, 255, 255))
        flat.paste(im, mask=im.split()[3])
        if flat.width > THUMB_WIDTH:
            height = round(flat.height * THUMB_WIDTH / flat.width)
            flat = flat.resize((THUMB_WIDTH, height), Image.LANCZOS)
        os.makedirs(THUMBS_DIR, exist_ok=True)
        flat.save(target, "JPEG", quality=THUMB_QUALITY, optimize=True,
                  progressive=True)
    print("made " + target)


def main():
    if not os.path.isdir(POSTS_DIR):
        sys.exit("Run this from the root of the site repo.")

    urls = []
    for name in sorted(os.listdir(POSTS_DIR)):
        if name.endswith((".md", ".markdown", ".html")):
            urls.append(add_image_line(os.path.join(POSTS_DIR, name)))

    with open("_config.yml", encoding="utf-8") as f:
        default = DEFAULT_LINE.search(f.read())
    if default:
        urls.append(unquote(default.group(1)))

    for url in urls:
        make_thumbnail(url)


if __name__ == "__main__":
    main()
