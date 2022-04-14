from . import BasePage
from typing import Tuple

class IndexPage(BasePage):
    @staticmethod(f)
    def get_template() -> Tuple[str, dict]:
        return ("index", {})