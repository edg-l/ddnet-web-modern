from .base_page import BasePage
from typing import Tuple
from pathlib import Path
from datetime import datetime
from .post import PostPage

class IndexPage(BasePage):
    def __init__(self, posts: [PostPage]):
        self.news = posts[0:10]

    def get_template(self) -> Tuple[str, dict]:
        return ("index.html", {
            "news": self.news
        })
    
    def get_output(self):
        return "index.html"
