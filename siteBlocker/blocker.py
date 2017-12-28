from datetime import datetime as dt
import argparse


class blocker:
    '''Implementation of the siteBlocker'''

    # class variables are defined below
    # Path of the /etc/hosts file
    hosts_path = r'/etc/hosts_temp_test'

    # Changing the hostname of the site we want to block
    # by giving local host as mapping to the the actual site.

    redirect = '127.0.0.1'

    def __init__(self, starting_hour, finishing_hour,  block_that_sites = []):
        '''Starting hour, finishing hour, sites to be blocked as a list'''

        self.starting_hour = starting_hour
        self.finishing_hour = finishing_hour
        self.block_that_sites = block_that_sites

    def block_sites(self):
        '''Method to block the site by altering the hosts file'''

        print("Working hours")
        while dt(dt.now().year, dt.now().month, dt.now().day, int(self.starting_hour)) \
                < dt(dt.now().year, dt.now().month, dt.now().day, int(self.finishing_hour)):

            # Open file in appendable format using r+

            with open(blocker.hosts_path, 'r+') as file:
                file_content = file.read()
                for site in self.block_that_sites:
                    if site not in file_content:
                        file.write(blocker.redirect + ' ' + site + '\n')
        else:
            self.un_block()

    def un_block(self):
        '''Method to unblock the sites after working hours'''

        # read the actual file from the beginning and seek to the beginning again.

        with open(blocker.hosts_path, 'r+') as file:
            file_content = file.readlines()
            file.seek(0)

            # Write lines which are not in block_that_site variable,
            # which makes the original file to be intact.

            for line in file_content:
                if not any(site in line for site in self.block_that_sites):
                    file.write(line)

            # Delete the reset of the lines.

            file.truncate()
            print("Work hours complete! Enjoy :)")

    def break_time(self, break_hour):
        '''Add a break hour by calling the method and giving break hour'''

        self.starting_hour = break_hour + 1
        self.block_sites()

        print("Yay! break time")

        while dt(dt.now().year, dt.now().month, dt.now().day, break_hour) \
                < dt(dt.now().year, dt.now().month, dt.now().day, self.starting_hour):
            self.un_block()

        # Taking the first parameter of datetime function which is the time in hours.

        self.block_sites(dt.now().time()[0], self.finishing_hour)

    def add_more_sites(self, list_of_sites = []):
        '''appending more sites to the instance, taken as list'''

        self.block_that_sites.extend(list_of_sites)
        self.block_sites()

    def __str__(self):
        # Giving a string representation of the class, during calling.

        return 'starting time %s , ending time %s, list of blocked sites' \
               % (self.starting_time, self.finishing_hour, self.block_that_sites)


# This block seperates the current program from the above implementation
# In other words the below code is not executed when this module is imported.

if __name__ == '__main__':

    # create an arguement parser with the beloe method call"

    parser = argparse.ArgumentParser(description='Site blocker tool')

    # adding two optional arguments.

    parser.add_argument('-s', type=int, nargs='+',
                        action='store',
                        dest='hour_value',
                        help='Working Hours in 0-23 range.')

    parser.add_argument('-l', type=str, nargs='+',                  # or * if you want to support empty lists.
                        action='store',
                        dest='list_of_sites',
                        help='enter the list of sites to be blocked followed by space')

    # creating an object to parse the arguments.

    cmd_line_args = parser.parse_args()

    # Calling the implementation.

    appObject = blocker(cmd_line_args.hour_value[0],cmd_line_args.hour_value[1], cmd_line_args.list_of_sites)
    print (appObject.finishing_hour)
    print (appObject.starting_hour)
    print (appObject.block_that_sites)
    appObject.add_more_sites("www.amazon.com")
    appObject.block_sites()
