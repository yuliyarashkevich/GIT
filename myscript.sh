#!/bin/bash
cd t1
mkdir folder1 folder2 folder3
cd folder1
touch f1.txt f2.txt f3.txt f4.json f5.json
mkdir folder5 folder6 folder7
ls
mv f1.txt ../folder2/f1.txt
mv f2.txt ../folder2/f2.txt
