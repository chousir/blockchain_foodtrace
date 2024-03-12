import argparse
import time
import base64
import ecdsa

def generate_ECDSA_keys():
    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) #this is your sign (private key)
    private_key = sk.to_string().hex() #convert your private key to hex
    vk = sk.get_verifying_key() #this is your verification key (public key)
    public_key = vk.to_string().hex()
    public_key = base64.b64encode(bytes.fromhex(public_key))
    
    return public_key.decode(), private_key

def sign_ECDSA_msg(private_key):
    message = str(round(time.time()))
    bmessage = message.encode()
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
    signature = base64.b64encode(sk.sign(bmessage))

    return signature.decode(), message

def validate_signature(public_key, signature, message):
    public_key = (base64.b64decode(public_key)).hex()
    signature = base64.b64decode(signature)
    vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)
    try:
        return vk.verify(signature, message.encode())
    except:
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--generate', action='store_true', help='generate ECDSA keys')
    parser.add_argument('-s', '--sign', metavar='PRIVATE_KEY', type=str, help='Sign a message with the given private key')
    parser.add_argument('-v', '--validate', nargs=3, metavar=('PUBLIC_KEY', 'SIGNATURE', 'MESSAGE'), help='Validate a signature')

    args = parser.parse_args()

    if args.generate:
        public_key, private_key = generate_ECDSA_keys()
        print(f'Public Key: {public_key}\nPrivate Key: {private_key}')
    elif args.sign:
        signature, message = sign_ECDSA_msg(args.sign)
        print(f'signature: {signature}\nmessage: {message}')
    elif args.validate:
        public_key, signature, message = args.validate
        is_valid = validate_signature(public_key, signature, message)
        print('Signature Validation: Success' if is_valid else 'Signature Validation: Failure')

if __name__ == '__main__':
    main()
