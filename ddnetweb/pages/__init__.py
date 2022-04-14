from abc import ABC, abstractmethod
from typing import Tuple

class BasePage(ABC):
    @abstractmethod
    @staticmethod
    def get_template() -> Tuple[str, dict]:
        """Returns the name of the template along with the variables needed to render it."""
        pass