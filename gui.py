import hashlib as hasht
import tkinter as tk

from constants import *
from sys import argv

class Hashtool(object):
    def __init__(self) -> None:
        try:
            inputfilename = argv[1]
        except IndexError:
            inputstr = input("请输入要进行Hash操作的文本")


Hashtool()