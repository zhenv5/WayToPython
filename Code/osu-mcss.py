'''
title: CCSS Compliance Notes - Ubuntu

author: zhenv5

link: https://cse.osu.edu/computing-services/security/ccss-certification/ubuntu

This script aims to solve this problem:

ANTI-MALWARE:  The anti-malware script found viruses.

Check the /var/log/anti-malware.log file.

Once investigated, remove this message by deleting this echo line from
/etc/bash.bashrc (should be near the end).

MCSS:  The MCSS script check failed.

Check /var/log/mcss.log.

Once investigated, remove this message by deleting the this echo line from
/etc/bash.bashrc (should be near the end).

The system will be shutdown in 0 days if this is not fixed.
'''

import subprocess
import os 


def run_command(command):
	print command
	p = subprocess.Popen(command,shell = True, stdout = subprocess.PIPE)
	o = p.communicate() 
	print o[0]

def initial():

	run_command("sudo apt-get clean")
	run_command("sudo apt-get update")
	run_command("sudo apt-get -y --purge dist-upgrade")

	
	if not os.path.exists("ubuntu-mcss-1.3/"):
		if not os.path.exists("ubuntu-mcss-1.3.tar.gz"):
			print "download ubuntu-mcss-1.3.tar.gz"
			run_command("wget http://web.cse.ohio-state.edu/cs/security/ccss/resources/ubuntu-mcss-1.3.tar.gz")
		else:
			run_command("tar -vxzf ubuntu-mcss-1.3.tar.gz")

	os.chdir("ubuntu-mcss-1.3/")

	run_command("sudo ./install.sh")

	run_command("sudo ./mcss -i")
	
	print 'Finished  setups'

if __name__ == "__main__":
	initial()
