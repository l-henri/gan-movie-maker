import sys
sys.path.append('./gantools/gantools')
import cli as ganBreederCli
import os
import shutil
import ffmpeg
import json
import glob
import cv2


movieFrameRate = 10
workdir = "output/01_test_global"
outputVideo = "output/test.mp4"
if not os.path.exists(workdir):
	os.makedirs(workdir)



########

# An image is caracterized by a vector, labels and a truncation value

########


def main():
	print("Starting program")
	keysList = ["95a912068b0ea9b806fd4dfe", "f4e93d278917d57ce2bc8ae6"]
	durations = [0, 1]

	# Calculating frame number from transition duration
	frameNumberPerDuration=[]
	for duration in durations:
		frameNumberPerDuration.append(int(movieFrameRate*duration))

	folderNames = []
	secretData = loadSecretData()
	arguments = ["-u%s" % secretData["username"], "-p%s" % secretData["password"], "--no-loop", "-o"+workdir]
	i = 0

	# Appel de la fonction sur chaque objet
	for key in keysList:

		# Creating arguments
		# print(frameNumberPerDuration[i])
		if i == len(keysList)-1:
			# arguments.append("-k '" + key + "' '" + keysList[0] + "'")
			arguments.append("-k" + key )
			arguments.append("-l" + keysList[0])
			arguments.append("-n"+str(frameNumberPerDuration[i]))
			# arguments.append("-o"+folderNames[i])
		else:
			# arguments.append("-k" + key + " " + keysList[i+1])
			arguments.append("-k" + key )
			arguments.append("-l" + keysList[i+1])
			arguments.append("-n"+str(frameNumberPerDuration[i]))
			# arguments = ["-o outpout", "-uhenri.lieutaud@gmail.com", "-pAB6hzKSXYBf7", "-k" + key , "-l" + keysList[i+1]]
		# arguments.append("-o"+folderNames[i])
		arguments.append("-P"+ str(i).zfill(4))
		i += 1
		# print(arguments)
		# # Vérification des arguments
		# args = ganBreederCli.handle_args(arguments)
		# print(args)
		# Appel de la fonction principale
		ganBreederCli.main(arguments)

'''
	## Saving as movie
	stream = ffmpeg.input(workdir+ '/*.png', pattern_type='glob', framerate=movieFrameRate)
	#stream = ffmpeg.framerate(24)
	stream = ffmpeg.output(stream, outputVideo)
	ffmpeg.run(stream)
	# ffmpeg
	#     .input('/path/to/jpegs/*.jpg', pattern_type='glob', framerate=25)
	#     .output('movie.mp4')
	#     .run()
	'''

img_array = []

size=(None)

for filename in glob.glob(workdir + '/*.png'):
	img = cv2.imread(filename)
	height, width, layers = img.shape
	size = (width, height)
	img_array.append(img)

out = cv2.VideoWriter(outputVideo, cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
	out.write(img_array[i])
out.release()


def loadSecretData():
	with open("secretData.json") as json_file:
		return json.load(json_file)

if __name__ == '__main__':
	main()