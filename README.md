# 📷 Images Optimizer - By Bruno Hubner

This script performs the optimization of an entire directory of images by removing the metadata and adjusting the image quality to an acceptable level, thus making the images lighter for web use.

This script was developed to be executed in the Linux environment, with Python installed, follow the steps below:
#

* Giving permission to install and run scripts:
````bash
$ sudo chmod +x ./install.sh
````

````bash
$ sudo chmod +x ./run.sh
````
#

* Installing dependencies:
````
$ ./install.sh
````

* Running Program:
````
$ ./run.sh
````
#
### Running Program manually:
<br/>

* Creating python virtual environment:
````
$ python3 -m venv venv
````

* Activating virtual environment:
````bash
$ source ./venv/bin/activate
````

* Intalling dependencies:
````
$ pip3 install -r requirements.txt
````

* Running Program:
````
$ python3 ./main.py
````
