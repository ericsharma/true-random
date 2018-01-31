import binascii
import ecdsa
import sha3
import base58
import hashlib
from Crypto.Cipher import AES
from getTrueRandom import generateTrueRandom

privateKey = generateTrueRandom(32)

print "Private key is:" + binascii.hexlify(privateKey)

signingObj = ecdsa.SigningKey.from_string(privateKey, curve = ecdsa.SECP256k1)
publicKeyObj = signingObj.verifying_key
publicKeyString = b"04" + binascii.hexlify(publicKeyObj.to_string())
print "Public key is:" + publicKeyString

ripemd160 = hashlib.new('ripemd160')
ripemd160.update(hashlib.sha256(binascii.unhexlify(publicKeyString)).digest())
hashedPublicKey = b"00" + binascii.hexlify(ripemd160.digest())
checksum = binascii.hexlify(hashlib.sha256(hashlib.sha256(binascii.unhexlify(hashedPublicKey)).digest()).digest()[:4])
binaryAddr = binascii.unhexlify(hashedPublicKey + checksum)
print "binary Adress:" + binaryAddr

adress = base58.b58encode(binaryAddr)
print "Your bitcoin adress is:" + adress
