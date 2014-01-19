SearchShodan
============

This is a basic example of how to search into Shodan using the ShodanAPI. 

### Installation

To make this project work, you need to create a _api.py_ file, and add the variable : 
```
SHODAN_API_KEY = "XXXXXXXXXXXXXXXX"
```

Then, you can start the project by typing : 
```
python SearchShodan.py
```

### Usage

```
$ python SearchShodan.py 
Usage: SearchShodan.py [options]

Options:
  -h, --help         show this help message and exit
  --search=SEARCH    Search argument (eg. dir 615)
  --threads=THREADS  Max threads (default 5)
  --limit=LIMIT      Limit the number of results
```
