import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CoreMonitor(FileSystemEventHandler):
    def __init__(self, observer):
        self.observer = observer

    def on_any_event(self, event):
        self.observer.stop()


if __name__ == "__main__":
    path = '/Volumes'
    observer = Observer()
    event_handler = CoreMonitor(observer)
    observer.schedule(event_handler, path)
    observer.start()
    # try:
    #     while True:
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     observer.stop()
    observer.join()