# started basic code with jeff-work

import sys
import os
from custom_colors import bcolors

# Global Variables
tool_select_string = bcolors.OKGREEN + '1) list files, 2) download file, Q) quit-> ' + bcolors.ENDC


def Main():

    os.system('clear')

    message = raw_input(tool_select_string)

    while message != 'q':
        print 'Your selection: ' + message
        message = raw_input(tool_select_string)

    print bcolors.WARNING + 'Terminating program.' + bcolors.ENDC
    sys.exit(0)


# Boiler Plate
if __name__ == '__main__':
    Main()