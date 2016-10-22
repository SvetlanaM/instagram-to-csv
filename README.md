## Scrape data from Instagram
============================
This is the very first version of this code. This code scrapes data from [Instagram](https://www.instagram.com/) social network. Since Instagram, changed review requirements for API usage, it is not so easy get any data from this social network. 

### Requirements
1. Python 3.4 || Python 3.5
2. [pip](https://pypi.python.org/pypi/pip/1.0.2) - tool for installing and managing Python packages
3. [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) (not required) - tool to keep the dependencies required by different projects in separate places
 
### Installation
1. Create virtual environment in your project folder
2. Install required libraries and packages
   <code>pip install -r requirements.txt</code>
3. Create csv folder in your project
4. Run code:
   <code>python scrapper.py</code>
5. Enter the name of the instagram account (example: swetus).

### Error messages
==============
1. The server could not fulfill the request. 
2. We failed reach the server.
3. Data in older format.
4. No instagram account found.

## ToDo
=======
1. Support for code in older format 
2. Exception for private accounts
3. Download comments from post detail

