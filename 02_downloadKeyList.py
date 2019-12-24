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
	keysList = ["1664c75e5b4856155775f062", "97b567c44a077f715d160e95"]
	secretData = ganMovieMaker.loadSecretData()

	ganbreeder.get_info_batch(secretData["username"], secretData["password"], keysList)


if __name__ == '__main__':
	main()