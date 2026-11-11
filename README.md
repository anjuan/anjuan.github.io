anjuan.github.io
============

This is my GitHub-hosted (and powered by Jekyll) personal site which you can find at [AnjuanSimmons.com](https://AnjuanSimmons.com).

This site has changed hosts over the years (e.g., Yahoo, WordPress, Squarespace, and Google Sites), but I think that GitHub Pages will be its home for the foreseeable future. There are many reasons for this, but I think that the ability to simply manage text files instead of a backend database is near the top of the list.

This site is a detached fork of [Steven V. Miller's site](http://svmiller.com/) which is based on his [template](https://github.com/svmiller/steve-ngvb-jekyll-template) on GitHub. 

## Adding a blog post

The blog list at `/blog/` shows 10 posts per page, with each post's header image to its left. After adding a post to `_posts/`, run this from the repo root and commit what it changes:

```
python3 script/post_images.py
```

It copies the URL from the post's first `{% include image.html url="..." %}` into an `image:` front matter line and makes a small copy of the image in `images/thumbs/` so the list loads quickly. It needs Pillow (`python3 -m pip install Pillow`). If you skip it, the post still appears, using the default image from `default_post_image` in `_config.yml` (or the full-size image if the post has an `image:` line but no thumbnail yet).

I'm not sure this will help with search engine optimization, but, here goes: Anjuan operates at the intersection of business and technology by relentlessly focusing on delivering delight to customers while effectively using engineering resources. He’s currently a Technical Program Manager at Questback. When leading projects, he prefers Agile practices but will choose the right approach for the conditions on the ground. Anjuan works primarily in web application development and contributes to open source projects as often as possible.
