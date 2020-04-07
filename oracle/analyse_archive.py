# -*- coding: utf-8 -*-
'''
oracle归档日志巡检
用法:python3 脚本 文件名 需要巡检的行数
'''

def get_file(line_num):
    big_list=[]
    temp_li=[]
    for i in range(line_num):
        line=file.readline()
        if pattern.match(line):
            big_list.append(temp_li)
            temp_li=[]
            continue
        else:
            temp_li.append(line)#将读取到的行保存进临时列表
    return big_list
#################################################################
def analyse_file(li):#读取分割结果,返回分析结果
    analyse_info=li[0]
    cost=analycost_pattern.search(analyse_info).group(1)
    cost=eval(cost)
    if cost>500:#此处可以根据需要修改超时的时间值
        erro_list.append(li)
##################################################################
def analyse_time(error_list):#筛选出错误相隔时间小于等于两分钟的条目
    timestamp_list=[]
    index_list=[]
    pattern=re.compile(r'.*?(\d*-\d*-\d*\s\d*:\d*:\d*).*')
    for result in error_list:
        strtime=pattern.match(result[0]).group(1)
        tupletime=time.strptime(strtime,'%Y-%m-%d %H:%M:%S')
        timestamp=time.mktime(tupletime)
        timestamp_list.append(timestamp)
    #print(timestamp_list)
    cur=0
    for num in range(len(timestamp_list)-1):
        nex=cur+1
        if timestamp_list[nex]-timestamp_list[cur]<=120:#此处120秒,指的是相隔两分钟之内的信息才被认为有效
            index_list.append(cur)
            index_list.append(nex)
            cur=nex
        else:
            cur=nex
    index_list=list(set(index_list))
    return index_list
#################################################################
if __name__ == '__main__':
    import re
    import sys
    import time
    f=open('./log.txt','a')
    file=open(sys.argv[1],'r')
    pattern=re.compile(r'^\n$')
    analycost_pattern=re.compile(r'.*\[Cost\]:(\d*).*')
    erro_list=[]
    result_list=[]
    li=get_file(int(sys.argv[2]))
    block_num=len(li)
    try:
        for i in range(block_num):
            li.remove([])
    except:
        pass
    for j in li:
        analyse_file(j)
    index_list=analyse_time(erro_list)
    for index in index_list:
        print(erro_list[index][0])
        f.write(erro_list[index][0])
    f.close()
