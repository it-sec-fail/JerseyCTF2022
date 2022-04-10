# dnsmasq-ip-extract
Points: 300
Extract all unique IPs from dnsmasq-ip-extract-dnsmasq.log, hash each IP (SHA256), and write the IP + hash to a text file (IP and hash should be separated by a space, and each IP + hash entry should be on a new line).

NOTE: Alphabetical characters in the hash should be lower case, as seen in example below. Otherwise, your flag will be incorrect!

Example of text file output contents: `10.59.78.165 a6dd519bf8c7c50df5ae519963b5cf1590a471f88343c603168645ff335b26fe 10.244.220.245 20657ea410e8dd2dbf979a12fea35dd1b94beb6c2cac34f1d49c5824d03de5a1 10.18.47.24 c0e481d8f55dbb7de078cdcf67ebf627dc371e969e7dbb0b93afcce104e9247e`

The flag is the SHA256 hash of the output file. Example: `jctf{138706baa74bac72c8ee1c42eb3a7c6add2f71c0737c5044dcdd9cba7409ead6}`
