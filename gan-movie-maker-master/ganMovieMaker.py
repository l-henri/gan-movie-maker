import sys
sys.path.append('./gantools/gantools')
import cli as gaanBreederCli
import os
import shutil
import ffmpeg
import glob
import cv2

movieFrameRate = 5
workdir = "output/01_test_global"
outputVideo = "output/test.mp4"
if not os.path.exists(workdir):
	os.makedirs(workdir)



########

# An image is caracterized by a vector, labels and a truncation value

########


def main():
	print("Starting program")
	# keysList = ["215d3c08abb5280283b9afc6", "5baefe73a9bc418f8b8678ee"]
	keysList = ["7968340a72eabab735d04dba", "0416461072e5e22fd6d1637c"]
	# keysList = ["1664c75e5b4856155775f062", "9556db302ee5a7b2c04907ea"]
	durations = [1, 1]

	# Calculating frame number from transition duration
	frameNumberPerDuration=[]
	for duration in durations:
		frameNumberPerDuration.append(int(movieFrameRate*duration))

	folderNames = []
	arguments = ["-uhenri.lieutaud@gmail.com", "-pAB6hzKSXYBf7", "--no-loop", "-o"+workdir]
	i = 0

	# Appel de la fonction sur chaque objet
	for key in keysList:

		# Creating arguments
		print(frameNumberPerDuration[i])
		if i == len(keysList)-1:
			arguments.append("-k '" + key + "' '" + keysList[0] + "'")
			# arguments.append("-l" + keysList[0])
			arguments.append("-n"+str(frameNumberPerDuration[i]))
			# arguments.append("-o"+folderNames[i]) 
		else:
			arguments.append("-k" + key + " " + keysList[i+1])
			# arguments.append("-l" + keysList[i+1])
			arguments.append("-n"+str(frameNumberPerDuration[i]))
			# arguments = ["-o outpout", "-uhenri.lieutaud@gmail.com", "-pAB6hzKSXYBf7", "-k" + key , "-l" + keysList[i+1]]
		# arguments.append("-o"+folderNames[i]) 
		arguments.append("-P"+ str(i).zfill(4)) 
		i += 1
		print(arguments)
		# Vérification des arguments
		args = gaanBreederCli.handle_args(arguments)
		print(args)
		
		# Appel de la fonction principale
		# print("la");
		# print(arguments);
		# print("la");
		gaanBreederCli.main(arguments)

	# print("workdir")
	# print(workdir)
	# stream = ffmpeg.input(workdir+ '/*.png', pattern_type='glob', framerate=movieFrameRate)
	# #stream = ffmpeg.framerate(24)
	# stream = ffmpeg.output(stream, outputVideo)
	# ffmpeg.run(stream_spec=stream)
	# # ffmpeg
	# #     .input('/path/to/jpegs/*.jpg', pattern_type='glob', framerate=25)
	# #     .output('movie.mp4')
	# #     .run()

	img_array = []
	for filename in glob.glob(workdir+ '/*.png'):
		img = cv2.imread(filename)
		height, width, layers = img.shape
		size = (width, height)
		img_array.append(img)

	out = cv2.VideoWriter(outputVideo, cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

	for i in range(len(img_array)):
		out.write(img_array[i])
	out.release()





if __name__ == '__main__':
	main()