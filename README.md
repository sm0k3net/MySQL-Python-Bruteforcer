# MySQL-Python-Bruteforcer
Bruteforcing script against mysql databases on python with threading


To run script need python 2.7 and the following python libraries:
MySQLdb
sys
threading
time

Additionaly need to put file 'mysql_user.txt' with credentials in the same directory as python script
Format of file is very simple, each line is new username:password

Commands:
python mysql_brute.py <hostname>
