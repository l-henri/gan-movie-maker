import sys
sys.path.append('./gantools/gantools')
import cli as gaanBreederCli
import os
import shutil
import ffmpeg

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
	keysList = ["ef5beb9c47ff5e3abb1b9975", "ca02a5106c5e238194f6e8c7"]
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
			arguments.append("-k" + key )
			arguments.append("-l" + keysList[0])
			arguments.append("-n"+str(frameNumberPerDuration[i]))
			# arguments.append("-o"+folderNames[i]) 
		else:
			arguments.append("-k" + key)
			arguments.append("-l" + keysList[i+1])
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
		gaanBreederCli.main(arguments)


	stream = ffmpeg.input(workdir+ '/*.png', pattern_type='glob', framerate=24)
	#stream = ffmpeg.framerate(24)
	stream = ffmpeg.output(stream, outputVideo)
	ffmpeg.run(stream)
	# ffmpeg
	#     .input('/path/to/jpegs/*.jpg', pattern_type='glob', framerate=25)
	#     .output('movie.mp4')
	#     .run()






if __name__ == '__main__':
	main()