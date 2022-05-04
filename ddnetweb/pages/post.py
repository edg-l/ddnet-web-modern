from .base_page import BasePage
from typing import Tuple
import frontmatter
import os
from datetime import datetime
import mistune
from ddnetweb.util import get_post_date


class PostPage(BasePage):
    def __init__(self, markdown_file: str):
        print("processing ", markdown_file)
        filename = os.path.basename(markdown_file)
        self.date = get_post_date(filename)
        with open(markdown_file, "r") as f:
            self.post = frontmatter.load(f)
            self.content = mistune.html(self.post.content)
            self.layout = self.post.metadata["layout"]
            self.title = self.post.metadata["title"]
            self.permalink = self.post.metadata["permalink"]
            self.tag = self.post.metadata.get("tag")
    
    def get_output(self):
        return self.post.metadata["permalink"][1:] + "index.html"

    def get_template(self) -> Tuple[str, dict]:
        return (
            "post.html",
            {
                "post": self
            },
        )
