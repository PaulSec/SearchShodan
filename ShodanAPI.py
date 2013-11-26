from api import *
from shodan import WebAPI
import threading

lock_access_results = threading.Lock()

class ShodanAPI(object):
    _instance = None
    _api = None
    _results = []

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ShodanAPI, cls).__new__(
                                cls, *args, **kwargs)
            cls._api = WebAPI(SHODAN_API_KEY)
        return cls._instance

    def get_api(self):
    	return self._api

    def set_results(self, results):
    	lock_access_results.acquire()
    	self._results.extend(results['matches'])
    	lock_access_results.release()

    def get_results(self): 
    	return self._results