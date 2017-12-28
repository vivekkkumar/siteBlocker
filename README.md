# siteBlocker
A command line application to block mentioned websites to browse during productive hours. 

This class implementation can be imported and can be used in other modules.

1. This application can be invoked by,

# python blocker.py -h
usage: blocker.py [-h] [-s HOUR_VALUE] [-l LIST_OF_SITES [LIST_OF_SITES ...]]

Site blocker tool

optional arguments:
  -h, --help            show this help message and exit
  -s HOUR_VALUE [HOUR_VALUE ...]
                        Working Hours in 0-23 range.
  -l LIST_OF_SITES [LIST_OF_SITES ...]
                        enter the list of sites to be blocked followed by
                        space
ex:
# python blocker.py -s 9 17 -l www.facebook.com
['www.facebook.com']
Working hours

2. Behaviour:

During working hours the application blocks the access to mentioned site by redirecting the sites to local host and hence no access to these sites.

3. Validated inputs:
  Proper time formats like 0-23
  Running the program for full cycle and hosts file is reverted back to the original.
  giving a break time.
  Adding extra sites to already present list.

4. Known Issues:
  Only works for this format - 0-23
  If program is crashed, the host file is not revoked back [ Working on it :) ]
  When the blocking method runs there is no possibility to add more sites to block (working on it as well)
  
  
