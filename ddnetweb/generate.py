import os
import shutil
from .util import CURRENT_WORKING_DIR
from pathlib import Path
from .pages import IndexPage
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
    #os.mkdir(build_dir)

    shutil.copytree(cwd / "static", build_dir)

    IndexPage.generate(build_dir, env)