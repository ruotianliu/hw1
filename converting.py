import subprocess
import os

class ff_processor:


	def __init__(self):
		self.framerate_piece = None
		self.endfile_piece = None
		print("FFMPEG process initialized")

	def ff_framerate(self, framerate):
		self.framerate_piece = " -framerate %f" % framerate

	def ff_endfile(self, endfile):
		self.endfile_piece = " %s.mp4" % endfile


	def delete_old_video(self):
		for video_name in os.listdir('.'):
			if video_name.endswith('.mp4'):
				os.remove(video_name)
		print("Old videos removed from directory")


	def create_new_video(self):
		process_string = "ffmpeg -f image2 -i img%03d.jpg -pattern_type glob -vf 1350:-2"
		if self.framerate_piece is not None:
			process_string += self.framerate_piece
		if self.endfile_piece is not None:
			process_string += self.endfile_piece
		else:
			print("-> ERROR OCCURRED. Possible reasons:")
			print("-> Video name not entered. Please enter a name (without the .mp4)")
			self.endfile_piece = input()
			self.create_new_video()
		subprocess.check_call('ffmpeg -f image2 -framerate 0.1 -i img%03d.jpg pictures.mp4')
		print("Video converted")
if __name__ == "__main__":
	ff_ob = ff_processor()
	ff_ob.ff_framerate(0.5)
	ff_ob.ff_endfile("pictures")
	ff_ob.delete_old_video()
	ff_ob.create_new_video()
	print("Video process done!\n")
