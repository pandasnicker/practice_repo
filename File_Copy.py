# Program to move files from source to destination

import os
import json
import time

from watchdog.observers import Observer
from watchdog.events import LoggingFileSystemEventHandler

folderPath = "C:\\Users\\mgula\\Downloads\\From_Folder"
destPath = "C:\\Users\\mgula\\Downloads\\Copied_Folder"


class myEventHandler(LoggingFileSystemEventHandler):

    def mover(self):
        for fName in os.listdir(folderPath):
            print(fName)
            src = folderPath + '\\' + fName
            dest = destPath + '\\' + fName
            os.rename(src,dest)
            print("File moved from {0} to {1}".format(src,dest))

    def on_modified(self, event):
        # time.sleep(5)
        print(f"Hey buddy, {event.src_path} has been modified")
        # self.mover()
        for fName in os.listdir(folderPath):
            src = folderPath + '\\' + fName
            dest = destPath + '\\' + fName
            os.rename(src,dest)
            print("File moved from {0} to {1}".format(src,dest))


    def on_thread_start(self, src):
        print("Observer thread started monitoring ",src)
        if len(os.listdir(folderPath)):
            self.mover()


if __name__ == "__main__":
    eventHandler = myEventHandler()
    eventHandler.on_thread_start(folderPath)
    obs = Observer()
    obs.schedule(eventHandler, folderPath, recursive = False)
    obs.start()

    try:
        while True:
            time.sleep(5)
            print("Process awake")
    except KeyboardInterrupt:
        print("User Interrupted the process")
        obs.stop()

    obs.join()