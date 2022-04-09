# dns-joke
Points: 100
## Description
A system administrator hasn't smiled in days. Legend has it, there is a DNS joke hidden somewhere in [www.jerseyctf.com](www.jerseyctf.com). Can you help us find it to make our system administrator laugh?

## Solving
To get the flag, check the `dns` entries of the www.jerseyctf.com subdomain. 

```
jerseyctf.com TXT @192.168.178.1 +short
"jctf{DNS_J0k3s_t@k3_24_hrs}"
```
	
