import sys
sys.path.append('./gantools/gantools')
import cli as gaanBreederCli


def main():
	print("Hello")
	arguments = ["-b 10","-o outpout", "-uhenri.lieutaud@gmail.com", "-pAB6hzKSXYBf7", "-kef5beb9c47ff5e3abb1b9975", "-l0105c94f69e6edc0921827ca"]
	args = gaanBreederCli.handle_args(arguments)

	print("Calling main")
	gaanBreederCli.main(arguments)


if __name__ == '__main__':
	main()