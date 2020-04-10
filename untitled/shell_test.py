# -*- coding:utf8 -*
#lilred

'''
cat access log | awk '{print $1 " " $7 " " $9}'


cat access.log | awk '{print $1}' |sort |uniq -c|sort -r|awk '{print $2 " " $1}'

'''
