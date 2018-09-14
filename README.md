# TheBlock
TheBlock is an attempt to create a decentralized twitter like social media platform, written in Python using Flask. TheBlock is a work in progress. Many features to still add. 

<b>Most recent update 0.7 done on 9/14/2018</b> Changed flash host to "0.0.0.0" to allow for outside connections.

<b>update 0.6 done on 9/1/2018</b> changed a lot of code related to the look of posts and how images show in each post.

To use this just clone the repo and use a CLI:

"python blockchain.py -p 5000"

"python blockchain_client.py -p 8080"

navigate to the approriate localhost addresses in your browser and have some fun. 

To use first create a wallet and then mess around with sending transactions. Use different ports on your computer to simulate multiple nodes on the network. 

You will need to have the python packages listed at the end of this document to run the program.

<hr>

<h3> TO DO: </h3>

1. Functioning wallet and ability to send "value" to wallets. Have a wallet GUI page but need to update its code to properly take into account the sending of "value" from your wallet to another. Right now it only adds up the received transactions and does not debit the sent transactions.

2.Image sharing is coming along nicely using base64. Sharing works now, but you need to put the images in the root folder and type in the name. Need to add ability to select images from anywhere on the computer and the name/path to autopopulate.

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
