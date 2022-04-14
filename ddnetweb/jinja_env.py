from jinja2 import Environment, PackageLoader, select_autoescape
from .util import url_versioned
from datetime import datetime

def create_env() -> Environment:
    env = Environment(
        loader=PackageLoader("ddnetweb"),
        autoescape=select_autoescape()
    )

    env.globals["APP_NAME"] = "DDraceNetwork"
    env.globals["GENERATED_AT"] = datetime.now()

    env.filters["versioned"] = url_versioned
    return env