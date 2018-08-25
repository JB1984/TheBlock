# TheBlock
TheBlock is an attempt to create a decentralized twitter like social media platform, written in Python using Flask. TheBlock is a work in progress. Many features to still add.

To use this just clone the repo and use a CLI:

"python blockchain.py -p 5000"

"python blockchain_client.py -p 8080"

navigate to the approriate localhost addresses in your browser and have some fun. 

To use first create a wallet and then mess around with sending transactions. Use different ports on your computer to simulate multiple nodes on the network. 

You will need to have the python packages listed at the end of this document to run the program.

<hr>

<h3> TO DO: </h3>

1. Functioning wallet and ability to send "value" to wallets. Have a wallet GUI page but need to update its code to properly take into account the sending of "value" from your wallet to another. Right now it only adds up the received transactions and does not debit the sent transactions.

2.Was able to get a working image sharing system started. Need to work to allow users to select an image to upload and then getting that file path through the system to the Python code that creates the base64 string from the image. Right now the image has to be in the main directory and also you need to type in the name eg. "myimage.png". Also for now due to the hardcoded part of the javascript to display the image it needs to be PNG. Need to fix so that it can be at least PNG, JPG...possibly more.

3.Idea would be to use "value" as a reward for running the network (mining) and this "value" would need to be purchased by advertisers to run ads. This would create a decentralized sharing network where the money and value created is spread to the contributors. Perhaps a "like" would give additional "value".

4. Large work still to be done on the P2P networking code side. Right now the program works on localhost and can run multiple nodes using different ports. When trying to connect over the internet in P2P style it is not working. Need to research packages available for Python to help with the P2P networking code.

Slowly but surely adding features and learning new skills to make this project a reality.

<hr>

Please note that I run this on my desktop with a Virtual Environment that does not upload into GitHub. My environment runs Python 3.7 with the following packages

Flask <br>
Flask-Cors <br>
Jinja2 <br>
MarkupSafe <br>
Werkzeug <br>
certifi <br>
chardet <br>
click <br>
idna <br>
itsdangerous <br>
pip <br>
pycryptodome <br>
requests <br>
setuptools <br>
six <br>
urllib3<br>
<br>

The starting point for my code was the below repository: <br>
https://github.com/adilmoujahid/blockchain-python-tutorial
