import threading
import os
import time

class Monitor(threading.Thread):
	def __init__(self, target):
		threading.Thread.__init__(self)
		self.target = target

	def get_cores(self):
		volume_list = os.listdir(self.target)

		if "Macintosh HD" in volume_list:
			volume_list.remove("Macintosh HD")
		if "MobileBackups" in volume_list:
			volume_list.remove("MobileBackups")

		return volume_list

	def run(self):
		while True:
			cores = self.get_cores()
			for core in cores:
				print core + " | ",
				self.join()
			time.sleep(1)

monitor = Monitor("/Volumes")
