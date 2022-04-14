from abc import ABC, abstractmethod
from typing import Tuple
from jinja2 import Environment
from pathlib import Path


class BasePage(ABC):
    @staticmethod
    @abstractmethod
    def get_template() -> Tuple[str, dict]:
        """Returns the name of the template along with the variables needed to render it."""
        pass

    @classmethod
    def generate(cls, build_dir: Path, env: Environment):
        template_path, data = cls.get_template()
        template = env.get_template(template_path)
        with open(build_dir / template_path, 'w') as f:
            f.write(template.render(**data)) 