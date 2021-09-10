# MazamaMedia_UserManagement

Step 1 — Install Python and pip(Linux)


we can install Python 3 by using the following command:

$ sudo apt-get install python3

Now that we have Python 3 installed, we will also need pip in order to install packages from PyPi, Python’s package repository.

$ sudo apt-get install -y python3-pip

Step 2 — Install virtualenv

To install virtualenv, we will use the pip3 command, as shown below:

$ pip3 install virtualenv

Step 3 — Install app

create your virtual environment. Let’s call it env.

$ virtualenv env

Now, activate the virtual environment with the following command:

$ . env/bin/activate

And then

pip install -r requirements.txt