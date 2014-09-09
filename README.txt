Denial of Service Attack and Reporting Tool (DoSART)
Description
This software is to test web servers about their ability to withstand HTTP Denial of Service Attack
and generate a report.

Installation
1. Install python-tk and python-pip using apt-get command in Debian based Linux, or yum command in Fedora Linux
2. run "python setup.py" in Terminal/Command Prompt in the root folder.
3. run "python run.py"

Bugs
1. After the application generates a report, the program hangs due to thread lock for allowing
   flask webserver to run. Use Ctrl+C in the terminal to proceed.
