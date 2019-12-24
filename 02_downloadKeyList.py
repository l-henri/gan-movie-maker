import sys
sys.path.append('./gantools/gantools')
import ganbreeder
import ganMovieMaker
########

# An image is caracterized by a vector, labels and a truncation value

########


def main():
	print("Starting program")
	keysList = ["1664c75e5b4856155775f062", "97b567c44a077f715d160e95"]
	username = "henri.lieutaud@gmail.com"
	password = "AB6hzKSXYBf7"

	ganbreeder.get_info_batch(username, password, keysList)


if __name__ == '__main__':
	main()