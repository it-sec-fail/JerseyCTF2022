# apache-logs
Points: 100
An apache log file that contains recent traffic was pulled from a web server. There is suspicion that an external host was able to access a sensitive file accidentally placed in one of the company website's directories. Someone's getting fired...
Identify the source IP address that was able to access the file by using the flag format: `jctf{IP address}`

## Solving

We got a apache webserverlog and boy, this is more difficult then I thought.
There are some lines, that could be the IP of interest. But I found the right one.
And yes, *bankrecords* are really sensitive I think :) 

```
cat webtraffic.log | grep bankrecords | awk ' { print "jctf{"$1"}" }'
jctf{76.190.52.148}
```
