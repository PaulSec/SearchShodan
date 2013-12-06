import math
from ShodanAPI import *
from api import *
from ThreadShodanAPISearcher import *
import optparse
import sys

threads = []

def print_info(results):
    for result in results:
        print '%s' % result['ip']

def search_shodan(cmd, max_thread, limit):
    global threads 

    api = ShodanAPI().get_api()
    # Wrap the request in a try/ except block to catch errors
    try:
        # Search Shodan
        results = api.search(cmd)
        print 'There are ' + str(results['total']) + ' results.'

        # calculing the number of pages
        if (limit is None):
            nb_pages = math.ceil(int(results['total']) / 100.0)
        else:
            min_res = min(int(results['total']), int(limit))
         #   print min_res
            nb_pages = math.ceil(min_res / 100.0)

        #print "nb pages : " + str(nb_pages)
        #raw_input()

        ShodanAPI().set_results(results)
        

        i = 2
        while (i <= nb_pages):
        	# Launch threads for each page
            thread = ThreadShodanAPISearcher(cmd, i)
            thread.start()
            threads.append(thread)
            i = i + 1

            # result should be equal but to be sure >=
            # print threads
            if ((i-1) >= max_thread):
                for thread in threads:
                    thread.join()
                threads = []


        # wait for all threads to finish
        for thread in threads:
            thread.join()

        print_info(ShodanAPI().get_results())
    except Exception, e:
        print 'Error: %s' % e

# option parser
parser = optparse.OptionParser()
parser.add_option('--search', help='Search argument (eg. dir 615)', dest='search')
parser.add_option('--threads', help='Max threads (default 5)', dest='threads', default=4)
parser.add_option('--limit', help='Limit the number of results', dest='limit', default=None)

if (len(sys.argv) <= 1):
    parser.print_help()
else:
    (opts, args) = parser.parse_args()
    search_shodan(opts.search, opts.threads, opts.limit)