# webserver

webserver is a Python library for creating a local [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface).

## Forward

webserver is based off of Ruslan Spivak's Blog: [Let's Build A Webserver](https://ruslanspivak.com/lsbaws-part1/). Which I highly recommend you read. 

## Installation

Clone this repository to your local machine

Open a terminal and navigate to webserver's installation directory
```bash
cd *webserver_installation_directory*
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pipenv.
```bash
pip install pipenv
```
Use pipenv to install python requirements
```bash
pipenv sync
```

## Usage

Use this bash script to run webserver with default setup for CST8109
```bash
sudo sh run.sh
```
If you want to get your hands dirty; you can alternatively run webserver like so
```bash
pipenv run python webserver.py wsgiapp:app 
```
Once the server is running open a browser and navigate to [http://localhost:8888/index](http://localhost:8888/index) at the port the webserver is running on to check to see if it works.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
