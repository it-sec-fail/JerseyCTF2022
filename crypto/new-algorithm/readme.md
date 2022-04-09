# new-algorithm
Points: 75
On the first day of the job, a new cryptography intern is insisting to upper management that he developed a new encryption algorithm for the company to use for sensitive emails and should get a raise. This seems too good to be true... are you able to prove the intern wrong by decrypting it?
Here's an example of an encrypted email message using the intern's algorithm: `amN0Znt0UllfQUVTX0lOc1QzQGR9`

## Solving

Okay, there is this "*encrypted*" string... to it looks like something familiar. Let's try some base64 **decoding** :D.

```
echo "amN0Znt0UllfQUVTX0lOc1QzQGR9" | base64 -d
jctf{tRY_AES_INsT3@d}
```

Oh there it is :-) - Encoding is not encryption ;-)

Feel free to use this python script to solve the chall.
