# repo-doc-agent


build  = docker build -t doc-agent .
run = docker run -p 8081:8081 doc-agent


Scan Repo
   ↓
Find Compose File
   ↓
[Exists?] ── No → Exit
   ↓ Yes
Read File
   ↓
Parse Services
   ↓
[Simple or Complex?]
   ↓           ↓
Short Summary  Detailed Summary

