#!/bin/bash

echo "Getting the DNS Joke Flag for you..."
flag=$(dig jerseyctf.com TXT +short)

echo "The flag is: ${flag}"
