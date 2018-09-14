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

3.Idea would be to use "value" as a reward for running the network (mining) and this "value" would need to be purchased by advertisers to run ads. This would create a decentralized sharing network where the money and value created is spread to the contributors. Perhaps a "like" would give additional "value".

4. P2P networking for blockchain.py seem to be working, without sockets....just using flask. You MUST add port forwarding to router though for this to work. Use -p on the command line to specify the port you want to use. Transaction pools are still per each node on the network. Possibly in the future add a shared transaction pool to mine from.

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
