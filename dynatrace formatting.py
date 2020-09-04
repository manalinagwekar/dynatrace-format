# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:17:46 2020

@author: manali
"""

file1 = open('format.txt','r')
file2 = open('output.txt','w')
file2.write('DYNATRACE ')
a=file1.read().splitlines()
file2.write(a[2]+' '+a[3]+' - '+a[0]+', '+a[1]+'\n')
file2.write('---'+'\n')
file2.write(a[4]+' - '+a[5]+'\n')
if len(a)!=6:
    file2.write('---'+'\n')
if len(a)==11 and a[8]!='Root cause':
    file2.write(a[6]+' - '+a[7]+', '+a[8]+'\n')
    file2.write('---'+'\n')
    file2.write(a[9]+' - '+a[10]+'\n')  
if len(a)==10:
    file2.write(a[6]+' - '+a[7]+'\n')
    file2.write('---'+'\n')
    file2.write(a[8]+' - '+a[9]+'\n')
if len(a)==9 and a[8]!='Root cause':
    file2.write(a[6]+' - '+a[7]+', '+a[8])   
if len(a)==8:
    file2.write(a[6]+' - '+a[7]+'\n')
file1.close()
file2.close()
