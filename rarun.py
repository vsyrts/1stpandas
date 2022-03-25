#!/usr/bin/env python3
# --*- coding: utf-8 -*--
import subprocess
import sys
import multiprocessing
import os
import time
from collections import OrderedDict
"""
    Архивирование и разархивирование мультипоточность python (7-Zip, в проекте Rar)
"""
def read_dict(*args,**kwargs):
    from json import loads
    filename=""
    if kwargs.get('file'):
        filename=kwargs.get('file') 
    elif args.__getitem__(0): 
        filename=args.__getitem__(0) 
    with open(filename,"+r") as file:
        mdict=loads(file.read())
    return mdict

def unrar(*args,**kwargs):
    stime=time.time()
    archive_name=None
    delete=''
    if kwargs.get("archive_name"):
        archive_name=kwargs.get("archive_name")
    elif(args[0].__len__()>0 and ('a' in args[0])):
        archive_name=args[0][-3]
    else:
        archive_name=args[0][-2]
    if not(archive_name):  
        archive_name=r'C:\Temp\util_bankrupts.xml.bz2'
    extension=os.path.splitext(archive_name)[1]
    if len(args[0])!=0:
        dict_types=args[0].pop(-1)
        args[0].insert(2,dict_types.get(extension.lower()))
    elif len(kwargs)!=0:
        archive_type=kwargs.get('archive_type')
        dict_types=kwargs.get("dict_types")
        if not(archive_type):
            archive_type=dict_types.get(extension.lower())
        if len(args[0])==0 and len(kwargs)>0:
            archive_app=kwargs.get("archive_app")
        if not(archive_app):
            archive_app=os.path.normpath('C:\Program Files\7-Zip\7z.exe')
        command=kwargs.get("command")
        if not(command):
            command='e'
        delete=kwargs.get("del")
        if not(delete):
            if command=='a':
                if os.path.basename(archive_app)=='7z.exe':
                    delete="-sdel"
                elif os.path.basename(archive_app) in ('rar.exe',):
                    delete="-df"
            else:
                delete=" "
        dstdir=kwargs.get('dstdir')
        if not(dstdir):
            dstdir=r'-oC:\\Temp\\extract'
    elif len(args[0])>0:
        if (('e' in args[0]) or ('x' in args[0])):
            args[0].remove('-sdel')
            delete=' '
    p={}
    try:
        if len(args[0])>0:
            
            margs= list(dict.fromkeys(args[0]))
            p=subprocess.Popen(
                margs
                , stdout=subprocess.PIPE
                , stderr=sys.stderr
            )
        elif len(kwargs)>0:
            p=subprocess.Popen(
                [archive_app,command,archive_type,delete,dstdir,archive_name]
                , stdout=subprocess.PIPE
                ,stderr=sys.stderr
            )
        for line in p.stdout:
            print(line.strip().decode(encoding='utf-8',errors='ignore'))
        p.communicate()
        if delete==' ':
            if len(args[0])>0:
                if args[0][1]=='a':
                    os.remove(args[0][-2])
                else:
                    os.remove(args[0][-1])
            elif len(kwargs)>0:
                os.remove(archive_name)
    except Exception as ex:
        print(ex)
    finally:
        dtime=stime-time.time()
        if p.pid:
            p.kill()
    return (p.returncode,"{:4f}".format(dtime))

if __name__=="__main__":
    lst=list()
    mdict=read_dict(r"7ztypes.json")
    # files=[r'C:\Temp\util_bankrupts.xml.gz',r'C:\Temp\190411.util_bankrupts.xml.gz',r'C:\Temp\253_20190109.XML.gz']
    # for file in files:
    #        lst.append([r'C:\Program Files\7-Zip\7z.exe','e','-bd','-aoa',r'-oC:\Temp\extract','-sdel',file,mdict]) 
    arch_files={r'C:\Temp\util_bankrupts.xml.zip':r'C:\Temp\extract\util_bankrupts.xml',r'C:\Temp\190411.util_bankrupts.xml.zip':r'C:\Temp\extract\190411.util_bankrupts.xml',r'C:\Temp\253_20190109.XML.zip':r'C:\Temp\extract\253_20190109.XML'}
    for key,value in arch_files.items():
            lst.append([r'C:\Program Files\7-Zip\7z.exe','a','-bd','-sdel',key,value,mdict])
    try:
        # unrar(lst[0])
        pool=multiprocessing.Pool(processes=5)
        print(pool.map(unrar,lst))
    except Exception as ex:
        print(ex)
    finally:
        pool.close()
