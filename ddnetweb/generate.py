import os
import shutil
from .util import CURRENT_WORKING_DIR
from pathlib import Path
from .pages import IndexPage, PostPage
from .jinja_env import create_env


def generate():
    """Generates all the pages and copies all files from
    the static folder in the current working directory to the build folder.
    """

    env = create_env()

    cwd = Path(CURRENT_WORKING_DIR)
    build_dir = cwd / "build"

    try:
        shutil.rmtree(build_dir)
    except FileNotFoundError:
        pass

    shutil.copytree(cwd / "static", build_dir)

    news_path = cwd / "news"

    posts = []

    for f in sorted(os.listdir(cwd / "news"), reverse=True):
        post = PostPage(news_path / f)
        post.generate(build_dir, env)
        posts.append(post)
    
    IndexPage(posts).generate(build_dir, env)
