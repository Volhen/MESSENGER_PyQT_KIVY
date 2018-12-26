import sys

import hmac

import hashlib

import random

import zlib

from Crypto.Cipher import AES

import logging

import settings


# ********** Data logging **********

class Loggings():

    def __init__(self, message):

        self._message = message

        msg_format = '%(client)s - %(message)s - %(asctime)s'

        logging.basicConfig(format=msg_format, level='DEBUG',
                            filename='log/hanle.log')

        self._logger = logging.getLogger('ServerLogger')

    def __call__(self, func):

        def wraper(*args, **kwargs):

            extras = {'client': args[1].getpeername()}

            self._logger.info(self._message, extra=extras)

            return func(*args, **kwargs)

        return wraper


# ********** Data compressed **********


def compressed(func):

    def wraper(*arg, **kwargs):

        bytes_data = func(*arg, **kwargs)

        return zlib.compress(bytes_data)

    return wraper


# ********** Data decompressed **********


def decompressed(func):

    def wraper(*arg, **kwargs):

        context = arg[0]

        decompressed_data = arg[1]

        bytes_data = zlib.decompress(decompressed_data)

        return func(context, bytes_data)

    return wraper


# ********** data encryption **********

def encrypted(func):

    def wraper(*arg, **kwargs):

        context = arg[0]

        data_text = arg[1]

        cipher = AES.new(settings.KEY, AES.MODE_EAX)

        nonce = cipher.nonce

        cipher_text, tag = cipher.encrypt_and_digest(data_text)

        return func(context, cipher_text)

    return wraper



# ********** data decryption **********

def decryption(func):

    def wraper(*arg, **kwargs):

        context = arg[0]

        data_text = arg[1]

        cipher = AES.new(settings.KEY, AES.MODE_EAX, nonce=nonce)

        plaintext = cipher.decrypt(data_text)

        return func(context, plaintext)

    return wraper

# ********** authentications **********


def login_required(func):

    def wraper(*arg, **kwargs):

        ctx, rqs, sock = arg
        
        saul = bytes(random.randint(30,0))

        sock.send(saul)

        secret = b'secret'

        session = hmac.new(saul, secret)

        request = sock.recv(settings.BUFFER_SIZE)

        return hmac.compare_digest(session, request)

        # return func(context, bytes_data)
        # НАДО ДОПИСА!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    return wraper