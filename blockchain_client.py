from collections import OrderedDict

import binascii
import base64
import json

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

import requests
from flask import Flask, jsonify, request, render_template


class Transaction:

    def __init__(self, sender_address, sender_private_key, recipient_address, value, note, picture):
        self.sender_address = sender_address
        self.sender_private_key = sender_private_key
        self.recipient_address = recipient_address
        self.value = value
        self.note = note
        self.picture = picture

    def __getattr__(self, attr):
        return self.data[attr]

    def to_dict(self):
        return OrderedDict({'sender_address': self.sender_address,
                            'recipient_address': self.recipient_address,
                            'value': self.value,
                            'note': self.note,
                            'picture': self.picture})

    def sign_transaction(self):

        private_key = self.sender_private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('./indexClient.html')


@app.route('/make/transaction')
def make_transaction():
    return render_template('./make_transaction.html')


@app.route('/view/transactions')
def view_transaction():
    return render_template('./view_transactions.html')


@app.route('/view/wallet_balance')
def view_wallet_balance():
    return render_template('./view_wallet_balance.html')


@app.route('/wallet/new', methods=['GET'])
def new_wallet():
    random_gen = Crypto.Random.new().read
    private_key = RSA.generate(1024, random_gen)
    public_key = private_key.publickey()
    response = {
        'private_key': binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'),
        'public_key': binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
    }

    #Save the generated key to the computer for use later
    f = open("private.pem", "wb")
    f.write(private_key.exportKey('PEM'))
    f.close()

    return jsonify(response), 200


@app.route('/generate/transaction', methods=['POST'])
def generate_transaction():

    p = open("private.pem", "r")
    priKey = RSA.import_key(p.read())
    pubKey = priKey.publickey()
    sender_address = binascii.hexlify(pubKey.exportKey(format='DER')).decode('ascii')
    sender_private_key = priKey
    recipient_address = request.form['recipient_address']
    value = request.form['amount']
    note = request.form['note']
    if request.form['picture'] != "":
        with open(request.form['picture'], "rb") as imageFile:
            pictureString = base64.b64encode(imageFile.read())
            pictureString1 = str(pictureString)
            print(pictureString)
            print(pictureString1)
    else:
        pictureString1 = ""

    transaction = Transaction(sender_address, sender_private_key, recipient_address, value, note, pictureString1)

    response = {'transaction': transaction.to_dict(), 'signature': transaction.sign_transaction()}

    return jsonify(response), 200


@app.route('/get_pub_key', methods=['GET'])
def get_pub_key():
    p = open("private.pem", "r")
    priKey = RSA.import_key(p.read())
    pubKey = priKey.publickey()
    sender_address = binascii.hexlify(pubKey.exportKey(format='DER')).decode('ascii')

    response = {'pub_key': sender_address}

    return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port)


