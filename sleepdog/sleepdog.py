#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import json
import argparse

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from slacker import Slacker


class CreateFileHandler(FileSystemEventHandler):

    def __init__(self, pattern, channel, token):
        self.pattern = pattern
        self.channel = channel
        self.token = token

    def on_created(self, event):
        if event.is_directory:
            return
        if self.pattern in event.src_path:
            message = ""
            if os.path.splitext(os.path.basename(event.src_path))[1] == ".json":
                with open(event.src_path) as f:
                    output = json.load(f)
                    message = json.dumps(output, indent=4, sort_keys=True)
            else:
                with open(event.src_path) as f:
                    message = f.read()

            message = "```" + message + "```"
            slack = Slacker(self.token)
            slack.chat.post_message(self.channel, message)


def main():
    current_dir = os.getcwd()

    parser = argparse.ArgumentParser()
    parser.add_argument("--pattern", default=".json", help="file name pattern to watch")
    parser.add_argument("--channel", default="general", help="channel to post")
    parser.add_argument("--token", required=True, help="slack token")
    parser.add_argument("--dir", default=current_dir, help="target dir to watch (default:current dir)")
    args = parser.parse_args()

    while True:
        event_handler = CreateFileHandler(args.pattern, args.channel, args.token)
        observer = Observer()
        observer.schedule(event_handler, args.dir, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()


if __name__ in "__main__":
    main()
