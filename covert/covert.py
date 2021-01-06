import urllib.request

import coverpy
from typer import Typer

app = Typer()


@app.command()
def download(search_string: str, out: str = None, size: int = 256):
    fetcher = coverpy.CoverPy()
    r = fetcher.get_cover(search_string)
    print(f"Found {r.album} by {r.artist}")
    out = out or f"{r.artist} - {r.album}.jpg"
    print(f"Fetching '{out}'")
    filename = urllib.request.urlretrieve(r.artwork(625), out)
