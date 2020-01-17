import sys
sys.path.append('./gantools/gantools')
import ganbreeder
import ganMovieMaker
########

# An image is caracterized by a vector, labels and a truncation value

########


def main():
	print("Starting program")
	print('Downloading keyframe info from ganbreeder...')
	keysList = ["95a912068b0ea9b806fd4dfe", "f4e93d278917d57ce2bc8ae6"]
	secretData = ganMovieMaker.loadSecretData()

	ganbreeder.get_info_batch(secretData["username"], secretData["password"], keysList)


if __name__ == '__main__':
	main()