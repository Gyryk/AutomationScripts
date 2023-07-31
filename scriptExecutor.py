import os
import time
import fileSorter as fs
import appInstaller as ai
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# Update Events Controller
class EventHandler(FileSystemEventHandler):
	def on_modified(self, event):
		fs.createList()
		fs.moveFiles()
		print("Cleaned Downloads folder")
		for file in os.listdir(os.curdir):
			if file.endswith('dmg'):
				ai.input_var(file)
				ai.install_app()
				ai.remove_dmg()
				print("App Installation was completed successfully")

dir = os.path.join(os.path.expanduser('~'), 'Downloads')
handler = EventHandler()
observer = Observer()
# Execution
observer.schedule(handler, dir, recursive=True)
observer.start()

try:
	while True:
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()

observer.join()
