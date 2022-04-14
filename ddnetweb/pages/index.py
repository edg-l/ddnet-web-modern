from .base_page import BasePage
from typing import Tuple

class IndexPage(BasePage):
    @staticmethod
    def get_template() -> Tuple[str, dict]:
        return ("index.html", {})