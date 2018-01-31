import binascii
import ecdsa
import sha3
from Crypto.Cipher import AES
from getTrueRandom import generateTrueRandom

privateKey = generateTrueRandom(32)
print "Private key is:" + binascii.hexlify(privateKey)

signingObj = ecdsa.SigningKey.from_string(privateKey, curve = ecdsa.SECP256k1)
publicKeyObj = signingObj.verifying_key
publicKeyString = binascii.hexlify(publicKeyObj.to_string())

print "Public key is:" + publicKeyString

keccakObj = sha3.keccak_256()
keccakObj.update(publicKeyObj.to_string())
publicAdress64 = keccakObj.hexdigest()
publicAdressFinal = "0x" + publicAdress64[-40:]

print "Public ETH adress is: " + publicAdressFinal
