# TheBlock
The Block is a work in progress. Many features to still add.

1. Currently have the ability to send "value" and "notes" in blockchain transaction. Need to add a new GUI page to display "notes". This would be the posts that people make.

2. Functioning wallet and ability to send "value" to wallets. Have a wallet GUI page but need to update its code to properly take into account the sending of "value" from your wallet to another. Right now it only adds up the received transactions and does not debit the sent transactions.

3. Large work still to be done on the P2P networking code side. Right now the program works on localhost and can run multiple nodes using different ports. When trying to connect over the internet in P2P style it is not working. Need to research packages available for Python to help with the P2P networking code.

Slowly but surely adding features and learning new skills to make this project a reality.

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
