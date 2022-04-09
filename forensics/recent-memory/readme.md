# recent-memory
Points: 250
Use the memory image in the Google drive link below. An attacker left behind some evidence in the network connections. Follow the attacker's tracks to find the flag.

https://drive.google.com/drive/folders/1ubSx3pwHOSZ9oCShHBPToVdHjTev7hXL

## Solving

Okay let's analyze the memory file, I will use volitality3 for this. 

With this command we can get all net sessions stored in the memory.
```
python vol.py -f ~/Downloads/recent-memory.mem windows.netstat.NetStat
```

If everything worked like intended, we'll see a long list with net connections. Some connection looks interessting, because the process is `nc.exe`:

```
Offset	Proto	LocalAddr	LocalPort	ForeignAddr	ForeignPort	State	PID	Owner	Created

0x858a82a72010	TCPv4	192.168.86.35	50082	52.85.61.5	443	CLOSE_WAIT	5732	SearchApp.exe	2022-02-26 14:06:51.000000 
0x858a8794cb20	TCPv4	192.168.86.35	50083	54.230.244.36	80	CLOSE_WAIT	5732	SearchApp.exe	2022-02-26 14:06:51.000000 
0x858a840aab60	TCPv4	192.168.86.35	3389	192.168.86.40	54666	ESTABLISHED	388	svchost.exe	2022-02-26 14:58:41.000000 
0x858a87972a20	TCPv4	192.168.86.35	50073	23.194.131.74	443	CLOSE_WAIT	5732	SearchApp.exe	2022-02-26 14:06:49.000000 
0x858a8423f010	TCPv4	192.168.86.35	50877	13.91.129.128	443	ESTABLISHED	3044	MsMpEng.exe	2022-02-26 15:21:29.000000 
0x858a8729a4a0	TCPv4	192.168.86.35	49748	52.226.139.180	443	ESTABLISHED	404	svchost.exe	2022-02-26 14:04:46.000000 
0x858a8492aa20	TCPv4	192.168.86.35	50071	23.194.131.74	443	CLOSE_WAIT	5732	SearchApp.exe	2022-02-26 14:06:49.000000 
0x858a8492f270	TCPv4	192.168.86.35	50088	54.230.244.194	80	CLOSE_WAIT	5732	SearchApp.exe	2022-02-26 14:06:51.000000 
0x858a87f3f010	TCPv4	192.168.86.35	50876	161.35.53.62	5283	ESTABLISHED	2756	nc.exe	2022-02-26 15:21:29.000000 
0x858a82926550	TCPv4	192.168.86.35	49907	52.226.139.180	443	ESTABLISHED	404	svchost.exe	2022-02-26 14:05:46.000000 
0x858a880103d0	TCPv4	192.168.86.35	50089	54.230.244.116	80	CLOSE_WAIT	5732	SearchApp.exe	2022-02-26 14:06:51.000000 
0x858a87f95b10	TCPv4	192.168.86.35	50070	72.21.91.29	80	CLOSE_WAIT	5732	SearchApp.exe	2022-02-26 14:06:49.000000 
0x858a87ae5b50	TCPv4	192.168.86.35	50074	23.194.131.74	443	CLOSE_WAIT	5732	SearchApp.exe	2022-02-26 14:06:49.000000 
0x858a87aafb20	TCPv4	192.168.86.35	50090	23.221.224.18	443	CLOSE_WAIT	5732	SearchApp.exe	2022-02-26 14:06:52.000000 
0x858a871bf1e0	TCPv4	192.168.86.35	50072	23.194.131.74	443	CLOSE_WAIT	5732	SearchApp.exe	2022-02-26 14:06:49.000000 
```

So let's connect to this address:

```
nc 161.35.53.62 5283
jctf{f0ll0w_7h3_7r41l}
```
