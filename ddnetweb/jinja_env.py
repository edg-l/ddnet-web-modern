from jinja2 import Environment, PackageLoader, select_autoescape
from .util import url_versioned, format_datetime
from datetime import datetime
import os


def create_env() -> Environment:
    env = Environment(loader=PackageLoader("ddnetweb"), autoescape=select_autoescape())

    env.globals["APP_NAME"] = os.environ.get("APP_NAME", default="DDraceNetwork")
    env.globals["DDNET_VERSION"] = os.environ.get("DDNET_VERSION")

    env.globals["GENERATED_AT"] = datetime.now()

    env.filters["versioned"] = url_versioned
    env.filters["date"] = format_datetime
    return env
