import sys
sys.path.append('./gantools/gantools')
import cli as gaanBreederCli


def main():
	print("Starting program")
	keysList = ["ef5beb9c47ff5e3abb1b9975", "0105c94f69e6edc0921827ca", "8fd260605dbfab1ea7936fe"]
	for key, i in keysList:
		print(i)
		# arguments = ["-o outpout", "-uhenri.lieutaud@gmail.com", "-pAB6hzKSXYBf7", "-k" +key , "-l0105c94f69e6edc0921827ca"]
		# args = gaanBreederCli.handle_args(arguments)

		# print("Calling main")
		# gaanBreederCli.main(arguments)


if __name__ == '__main__':
	main()