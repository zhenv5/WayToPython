'''
For OOKAMI
'''

import subprocess
from os import listdir
from os.path import isfile, join


def run_command(command,is_print = True):
	print("command: %s" % command)
	p = subprocess.Popen(command,shell = True, stdout = subprocess.PIPE)
	o = p.communicate() 
	if is_print:
		print o[0]

def create_section_dir():
	run_command("mkdir Section_A")
	run_command("mkdir Section_B")
	run_command("mkdir Section_C")
	run_command("mkdir Section_D")

def get_last_first_name(file_name):
	last_name = file_name.split("%")[0]
	first_name = file_name.split("+")[1].split("-")[0]
	return last_name,first_name,file_name

def sort_files():
	mypath = "."
	onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and f.endswith("zip"))]
	#print onlyfiles
	files = [get_last_first_name(f) for f in onlyfiles]
	#print files 
	sorted_files = sorted(files,key = lambda x: x[0])
	#print sorted_files
	return sorted_files

def select_section(f):
	section_A = "Grady","Rzan","Section_A"
	section_B = "Mclntyre","Gzvin","Section_B"
	section_C = "Torosian","Vzken","Section_C"

	files = [f,section_A,section_B,section_C]

	sorted_files = sorted(files,key = lambda x: x[0])

	print sorted_files

	index = sorted_files.index(f)
	print index

	if index == 0:
		return "Section_A"
	elif index == 1:
		return "Section_B"
	elif index == 2:
		return "section_C"
	else:
		return "Section_D"

def move_file(f):
	dir_name = select_section(f)
	c = "mv " + f[2] + " " + dir_name + "/"
	run_command(c)


def unzip_files(f):
	dir_name = select_section(f)
	target_dir = join(dir_name,f[0] + "_" + f[1])
	c = "mkdir " + target_dir
	run_command(c)
	import zipfile
	target_zip = zipfile.ZipFile(join(".",f[2]),"r")
	target_zip.extractall(target_dir)


def main():
	create_section_dir()
	sorted_files = sort_files()
	for f in sorted_files:
		unzip_files(f)
		move_file(f)
main()
