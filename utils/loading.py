from rich.progress import track
import time

def loading(text="Loading..."):

    for _ in track(range(30), description=text):
        time.sleep(0.03)