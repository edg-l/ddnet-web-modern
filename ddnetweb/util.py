from hashlib import sha256
from os import getcwd

CURRENT_WORKING_DIR = getcwd()

def url_versioned(url: str) -> str:
    """Calculates the file checksum and returns the url with a version query that has the checksum value.
    Useful when aggresive caching is used (css, js, images...).
    
    The url should have a matching file under the static folder.
    """
    with open(f"{CURRENT_WORKING_DIR}/static{url}", 'r', encoding="utf-8") as f:
        data = f.read().encode("utf-8")
        checksum = sha256(data).hexdigest()
        return f"{url}?version={checksum}"