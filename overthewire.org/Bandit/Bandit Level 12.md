Bandido Nível 11 → Nível 12
Meta de nível
A senha para o próximo nível está armazenada no arquivo data.txt , onde todas as letras minúsculas (az) e maiúsculas (AZ) foram rotacionadas em 13 posições.

Comandos que você pode precisar para resolver este nível.
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

Material de leitura útil
Rot13 na Wikipédia

---
cat < data.txt | tr '{abcdefghijklmnopqrstuvwxyz}{ABCDEFGHIJKLMNOPQRSTUVWXYZ}' '{nopqrstuvwxyzabcdefghijklm}{NOPQRSTUVWXYZABCDEFGHIJKLM}'

The password is GROozWPO8QyN0mGrjUkID0WCYkZiQxrN