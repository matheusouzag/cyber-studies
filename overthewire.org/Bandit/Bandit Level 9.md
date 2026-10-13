Bandit Level 8 → Level 9
Level Goal
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

Commands you may need to solve this level
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

Helpful Reading Material
Piping and Redirection

---
cat < data.txt | sort | uniq -u

EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl