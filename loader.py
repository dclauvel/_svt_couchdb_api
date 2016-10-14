# This software may contain the intellectual property of EMC Corporation or be
# licensed to EMC Corporation from third parties. Use of this software and the
# intellectual property contained therein is expressly limited to the terms and
# conditions of the License Agreement under which it is provided by or on behalf
# of EMC. This code is provided AS IS, without warranty of any kind express or
# implied.

__author__ = "David CLAUVEL"
__version__ = "0.1"
__status__ = "Concept Code"

import logging
import os
import sys
from optparse import OptionParser
from lib.wrapper import wrapper
from lib.errors import Errors


# Globals
SETTINGS_FILE_NAME = 'cfg/config.cfg' 
OS_PATH =  os.path.dirname(os.path.realpath(__file__))                                           
settings = OS_PATH + '/' + SETTINGS_FILE_NAME


def main(f, client):

	wrapper().loader(settings, f, client)


	
if __name__ == '__main__':

	# Argument parser
	parser = OptionParser()
	parser.add_option("-f", "--file", 
		dest='loadfile',
		help="Collect ZIP file")
	parser.add_option("-c", "--client", 
		dest='client',
		help="Name of the client")
	(options, args) = parser.parse_args()

	# Set parsed values
	loadfile = options.loadfile
	client = options.client

	# Load if needed
	if not client:
		sys.exit("Error: specifiying the client with -c is required")	
	if not loadfile:
		sys.exit("Error: specifiying a file to load with -f is required")
	try: 
		open(loadfile)
		main(loadfile, client)
	except IOError:
		sys.exit("Error: can't read collect zip file: " + loadfile)
	except Errors.genError as e:
		print(e.msg)
		sys.exit(e.code)
	except:
		print "Unexpected error:", sys.exc_info()[0]
		raise