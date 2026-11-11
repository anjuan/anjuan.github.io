anjuan.github.io
============

This is my GitHub-hosted (and powered by Jekyll) personal site which you can find at [AnjuanSimmons.com](https://AnjuanSimmons.com).

This site has changed hosts over the years (e.g., Yahoo, WordPress, Squarespace, and Google Sites), but I think that GitHub Pages will be its home for the foreseeable future. There are many reasons for this, but I think that the ability to simply manage text files instead of a backend database is near the top of the list.

This site is a detached fork of [Steven V. Miller's site](http://svmiller.com/) which is based on his [template](https://github.com/svmiller/steve-ngvb-jekyll-template) on GitHub. 

## Adding a blog post

The blog list at `/blog/` shows 10 posts per page, with each post's header image to its left. Each post needs an `image:` front matter line and a small copy of the image in `images/thumbs/` so the list loads quickly. `script/post_images.py` makes both: it copies the URL from the post's first `{% include image.html url="..." %}` into `image:` and creates the thumbnail.

You don't need to run it yourself. The **Post images** GitHub Action (`.github/workflows/post-images.yml`) runs it whenever a post or image is pushed to `master`, commits anything it adds, and asks GitHub Pages to rebuild. Expect a commit from `github-actions[bot]` a minute or so after you add a post, so pull before editing locally. If the post and its image are uploaded separately, it catches up when the second one lands.

To run it by hand instead, use "Run workflow" on the Actions tab, or run this from the repo root and commit what it changes (it needs Pillow: `python3 -m pip install Pillow`):

```
python3 script/post_images.py
```

Until it runs, a new post still appears in the list using the default image from `default_post_image` in `_config.yml` (or the full-size image if the post has an `image:` line but no thumbnail yet).

I'm not sure this will help with search engine optimization, but, here goes: Anjuan operates at the intersection of business and technology by relentlessly focusing on delivering delight to customers while effectively using engineering resources. He’s currently a Technical Program Manager at Questback. When leading projects, he prefers Agile practices but will choose the right approach for the conditions on the ground. Anjuan works primarily in web application development and contributes to open source projects as often as possible.
