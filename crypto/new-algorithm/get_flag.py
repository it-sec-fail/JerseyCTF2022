#!/usr/bin/env python

import base64

string = input("Please tell me the \"encrypted\" string: ")

print("The flag is: \n\t" + base64.b64decode(string).decode('utf-8'))

