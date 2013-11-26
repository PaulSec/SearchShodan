import math
from ShodanAPI import *
from api import *
from ThreadShodanAPISearcher import *
import optparse
import sys

threads = []

def print_info(results):
    for result in results:
        print 'IP: %s' % result['ip']
        print result['data']
        print ''

def search_shodan(cmd):
    api = ShodanAPI().get_api()
    # Wrap the request in a try/ except block to catch errors
    try:
        # Search Shodan
        results = api.search(cmd)
        print 'There are ' + str(results['total']) + ' results.'
        nb_pages = math.ceil(int(results['total']) / 100.0)
        ShodanAPI().set_results(results)
        

        i = 2
        while (i <= nb_pages):
        	# Launch threads for each page
            thread = ThreadShodanAPISearcher(cmd, i)
            thread.start()
            threads.append(thread)
            i = i + 1

        # wait for all threads to finish
        for thread in threads:
            thread.join()

        print_info(ShodanAPI().get_results())
    except Exception, e:
        print 'Error: %s' % e

# option parser
parser = optparse.OptionParser()
parser.add_option('--search', help='Search argument (eg. dir 615)', dest='search')

if (len(sys.argv) <= 1):
    parser.print_help()
else:
    (opts, args) = parser.parse_args()
    search_shodan(opts.search)