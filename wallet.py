from Crypto.PublicKey import RSA
import Crypto.Random
import binascii

class Wallet:
    def __init__(self):
        private_key, public_key = self.genereate_keys
        self.private_key = private_key
        self.public_key = public_key

    def genereate_keys(self):
        private_key = RSA.generate(1024, Crypto.Random.new(), read)
        public_key = private_key.publickey()
        return (binascii.hexlify(private_key.exportkey(format='DER')).decode('ascii'),binascii.hexlify(public_key.exportkey(format='DER')).decode('ascii'))