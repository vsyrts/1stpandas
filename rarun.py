#!/usr/bin/env python3
# --*- coding: utf-8 -*--
import subprocess
import sys
import multiprocessing
import os
import time
"""
    Архивирование и разархивирование мультипоточность python (7-Zip, в проекте Rar)
"""
def unrar(*args,**kwargs):
    stime=time.time()
    archive_name=kwargs.get("archive_name")
    delete=''
    if len(args[0])==0 and len(kwargs)>0:
        if not(archive_name):
            archive_name=r'C:\Temp\util_bankrupts.xml.bz2'
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
        archive_type=kwargs.get('archive_type')
        if not(archive_type):
            extension=os.path.basename(archive_name).strip('.')[-1]
            # Switch: -t7z Format: 7Z
            # Switch: -tgzip Format: GZIP
            # Switch: -tzip Format: ZIP
            # Switch: -tbzip2 Format: BZIP2
            # Switch: -ttar Format: TAR
            # Switch: -tiso Format: ISO
            # Switch: -tudf Format: UDF
            archive_type='-t'+extension
        dstdir=kwargs.get('dstdir')
        if not(dstdir):
            dstdir=r'-oC:\\Temp\\extract'
    elif len(args[0])>0 and (('e' in args[0]) or ('x' in args[0])):
        args[0].remove('-sdel')
        delete=' '
    try:
        if len(args[0])>0:
            p=subprocess.Popen(
                args[0]
                , stdout=subprocess.PIPE
                , stderr=sys.stderr
            )
        elif len(kwargs)>0:
            p=subprocess(
                [archive_app,command,archive_type,delete,dstdir,archive_name]
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
    # files=(r'C:\Temp\util_bankrupts.xml.bz2',r'C:\Temp\190411.util_bankrupts.xml.bz2',r'C:\Temp\253_20190109.XML.bz2')
    # for file in files:
    #        lst.append([r'C:\Program Files\7-Zip\7z.exe','e','-bd','-tbzip2',r'-oC:\Temp\extract','-sdel',file]) 
    arch_files={r'C:\Temp\util_bankrupts.xml.bz2':r'C:\Temp\extract\util_bankrupts.xml',r'C:\Temp\190411.util_bankrupts.xml.bz2':r'C:\Temp\extract\190411.util_bankrupts.xml',r'C:\Temp\253_20190109.XML.bz2':r'C:\Temp\extract\253_20190109.XML'}
    for key,value in arch_files.items():
            lst.append([r'C:\Program Files\7-Zip\7z.exe','a','-bd','-tbzip2','-sdel',key,value])
    try:
        pool=multiprocessing.Pool(processes=5)
        print(pool.map(unrar,lst))
    except Exception as ex:
        print(ex)
    finally:
        pool.close()
