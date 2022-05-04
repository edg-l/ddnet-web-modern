from abc import ABC, abstractmethod
from typing import Tuple
from jinja2 import Environment
from pathlib import Path
import shutil
import os


class BasePage(ABC):
    @abstractmethod
    def get_template(self) -> Tuple[str, dict]:
        """Returns the name of the template along with the variables needed to render it."""
        pass

    @abstractmethod
    def get_output(self) -> Tuple[str, dict]:
        """Returns the name of the output file."""
        pass

    def generate(self, build_dir: Path, env: Environment):
        template_path, data = self.get_template()
        template = env.get_template(template_path)
        os.makedirs(os.path.dirname(build_dir / self.get_output()), exist_ok=True)
        with open(build_dir / self.get_output(), "w") as f:
            f.write(template.render(**data))
