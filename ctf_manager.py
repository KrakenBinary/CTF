#!/usr/bin/python3
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
from inputimeout import inputimeout, TimeoutOccurred


class Watcher:
    def __init__(self, path):
        self.observer = Observer()
        self.path = path

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        # if event.is_directory:
        #     return None
        print(
            "[{}] noticed: [{}] on: [{}] ".format(
                time.asctime(), event.event_type, event.src_path
            )
        )
        print("=============================================")
        time.sleep(2)
        file_info = subprocess.run(["file", event.src_path])
        print(file_info.returncode)
        print("---------------------------------------------")
        time.sleep(2)
        file_exif = subprocess.run(["exiftool", event.src_path])
        print(file_exif.returncode)
        print("---------------------------------------------")
        time.sleep(2)
        try:
            print_strings_in = inputimeout(
                                    prompt='Print Strings? (y/n) >> ',
                                    timeout=20)
        except TimeoutOccurred:
            print_strings_in = 'n'
        if print_strings_in == 'y':
            file_strings = subprocess.run(["strings", "-n 8", event.src_path])
            print(file_strings.returncode)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print('End of download analysis')
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


if __name__ == "__main__":
    w = Watcher("/home/krakenbinary/Downloads")
    w.run()
