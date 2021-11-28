import hashlib
import random
import string

def tuple_dict():
    tuple_example = ("a", 2, "password", "Password")

    for mutable in enumerate(tuple_example):
        hash_example = hash(mutable)
        print(hash_example)


def random_string(length):
    result = ''.join((random.choice(string.ascii_lowercase) for x in range(length)))
    return result


def generate_dict():
    for i in range(100):
        print("'" + random_string(random.randint(1, 10)) + "'"
              + " : " + "'" + random_string(random.randint(1, 10)) + "', ")

list = []

def read_file():
    file = open('plainTextPass.txt', 'r')

    for x in file:
        line = file.readline()  # stores a line in line
        bytes1 = line.encode()
        hashed = hashlib.sha256(bytes1).hexdigest()
        list.append(hashed)

    print(list)

read_file()
# e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
# sha256 = hashlib.sha256(bytes).hexdigest()


dict = {'lbrst': 'tg', 'd': 'mnlx', 'udzsoa': 'pun',
        'aad': 'dfjis',
        'rlvqljopne': 'jpxm',
        'pmhjgxqf': 'kqobyuaywh',
        'gfwj': 'cokhnxihfa',
        'yzhbpddxtq': 'dbav',
        'pwjnb': 'nktgxq',
        'vqvpdm': 'idi',
        'zw': 'vjvvxbeltl',
        'zljlopj': 'sblzucesx',
        'rwmkfvmtdh': 'nzwu',
        'srmaiqfgth': 'glcdjx',
        'uojlglmdqb': 'rg',
        'csjdigxctv': 'axpneo',
        'uzijbf': 'yvnvpya',
        'chfil': 'bij',
        'nq': 'hsg',
        'vlk': 'uiqkjxtf',
        'gelaxs': 'zggnt',
        'wfnnpul': 'jxhaskxh',
        'kvbeow': 'a',
        'wzzatxwx': 'i',
        'hbpdirdvg': 'ma',
        'dk': 'aofteah',
        'ynxzymkx': 'lmnjopouw',
        'uhaad': 'ohckd',
        'gvhjtoqtuh': 'gdwymalfiz',
        'vbz': 'mzigyuqm',
        'i': 'nomwbem',
        'jqvx': 'rismdqs',
        'bohfm': 'xtx',
        'vmofpfcd': 'gukv',
        'gi': 'no',
        'zodcxdudp': 'ahizszaam',
        'of': 'xqvqroth',
        'dewgbh': 'lqcixddpar',
        'jdj': 'qnqmv',
        'bogetnwbrk': 'ikupr',
        'l': 'cudnm',
        'qi': 'bedzq',
        'k': 'ciskxwc',
        'nzkugkwjbj': 'zkncs',
        'csnxofy': 'rbpkbmt',
        'abprl': 'zkihgxejtp',
        'cl': 'mwa',
        'vuycsivp': 'uzsifcpjdc',
        'fbkthptwy': 'hzeuzgdke',
        'jpusro': 'qgldpwizpm',
        'aleg': 'hidfp',
        'rdhgrw': 'ielcx',
        'fmpeduh': 'fdwhnve',
        'vvcxbh': 'jmqqg',
        'aoehz': 'pylpenhtu',
        'ypdorqgn': 'wisepz',
        'alhy': 'glqx',
        'qfuvl': 'cupeb',
        'mxccydh': 'stq',
        'kqzeyhkpuv': 'pxbnnam',
        'pupvzel': 'cjvjg',
        't': 'puwooxsu',
        'geku': 'ujqbxtgvf',
        'mqfbpejz': 'synxmepka',
        'm': 'kfcadygimf',
        'kimog': 'avzkxxv',
        'fixxwsouyh': 'kb',
        'iyicbgldoa': 'fz',
        'a': 'uxx',
        'jdwiiaf': 'pwqohs',
        'abotrpja': 'laalhdkgap',
        'qw': 'teixfwinq',
        'zxaapelp': 'pjsaxdauq',
        'oi': 'p',
        'owzeepz': 'ogbyni',
        'sdvvomngiy': 'hurtnnf',
        'uaa': 'eyjllqaf',
        'zmvoczilhu': 'wsdgbrp',
        'ee': 'ba',
        'edf': 'oyph',
        'b': 'tfuhkkq',
        'a': 'nscix',
        'wdvyweu': 'ojhse',
        'l': 'rjcepn',
        'dvjfsj': 'vkjg',
        'zkz': 'mvaceh',
        'g': 'xdp',
        'ceyr': 'kgkz',
        'rmjchrwrim': 'lkpxyfpak',
        'jekry': 'ww',
        'ok': 'cdyxlezcf',
        'k': 'dntxlwp',
        'kslio': 'pgg',
        'cdos': 'axexzb',
        'ly': 'hgqcwxxrqk',
        'wktdyqwiqp': 'mdl',
        'z': 'tt',
        'dtzic': 'ih',
        'qufqexdkfc': 'm',
        'ncvkiro': 'wfj'}

# print(dict.keys())