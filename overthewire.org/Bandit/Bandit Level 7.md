The password for the next level is stored somewhere on the server and has all of the following properties:

owned by user bandit7
owned by group bandit6
33 bytes in size

Commands you may need to solve this level
ls , cd , cat , file , du , find , grep

---
2>/dev/null = não usei porem tira os permission denied
find / -type f -size 33c -user bandit7 -group bandit6
cd /var/lib/dpkg/info
cat < bandit7.password

Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3