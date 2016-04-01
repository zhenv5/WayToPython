'''
Demo of argparse: Parser for command-line options, arguments and sub-commands
'''

import argparse
if __name__ == "__main__":
	parse = argparse.ArgumentParser(description = "Demo of argpase",prog = "argparse-demo")

	parse.add_argument("-a","--aa",help = 'parameter a which is a integer',required = True)
	parse.add_argument("-b","--bb",help = 'parameter b which is a boolean',required = True,action = "store_true")
	
	args = parse.parse_args()

	print args.aa
	print args.bb


