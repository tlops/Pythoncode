#!/usr/bin/env python
# -*-coding: utf-8 -*-
def checkString(string):
    a= string
    count={}
    for i in a:
        count[i]=count.get(i,0)+1
    for key, value in count.items():
        print key, value

abc=raw_input("Enter your string:")
checkString(abc)


#if__name__=='__main__':
#    main()
