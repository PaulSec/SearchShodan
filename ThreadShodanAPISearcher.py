import threading
from ShodanAPI import *

class ThreadShodanAPISearcher(threading.Thread):

    def __init__ (self, command, page):
        threading.Thread.__init__(self)
        self.command = command
        self.page = page

    def run(self):
    	api = ShodanAPI().get_api()
    	res = api.search(self.command, page=self.page)
        ShodanAPI().set_results(res)