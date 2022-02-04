#!/usr/bin/env python3
#import getpass;
import sys
import os
from tabnanny import verbose
from unittest import skip
import numpy as np
from pandas import read_csv
#from unittest.util import _MAX_LENGTH;
#import fdb;
#import pandas;
from time import sleep,time 

#class Class:
#     ""
#     def connection():
#         ""

#USR = getpass.getuser()
#PWD = getpass.getpass()
#print(f"USER {USR:10} PWD {PWD:10}" );
#class myfdb:
#con = fdb.Connection(
#    host='localhost',
#    database='MARKET.DB',
#    password=pwd,
#    charset='WIN1251'
#)   
#con.close()
##Basic example Pool
##from 
#from multiprocessing import Process, Queue, Pipe, Lock
##import (
##    Pool, Process, 
##)
#import os

#def fPool(x):
#    return x*x

#def fProcess(name):
#    print('hello', name)
##find process name
#def info(title):
#    print(title)
#    print('module name:', __name__)
#    print('parent process:', os.getppid())
#    print('process id:', os.getpid())

#def findProcess(name):
#    info('function f')
#    print('hello', name)

#def foo(q):
#    q.put('hellow')

#def fComunicateBetweenProcess(q):
#    q.put([42, None, 'hello'])
##Pipes
#def fPipes(conn):
#    conn.send([42, None, 'hello'])
#    conn.close()
##Synchronization between processes
#def fSyncronisation(l,i):
#    l.acquire()
#    try:
#        print('hellow word', i)
#    finally:
#        l.release()

#if __name__ == '__main__':
#    #Synchronization between processes
#    lock = Lock()
#    for num in range(10):
#        Process(target=fSyncronisation, args = (lock,num)).start()
#    #Pipes
#    #parent_conn, child_conn = Pipe()
#    #p = Process(target=fPipes, args=(child_conn,))
#    #p.start()
#    #print(parent_conn.recv())
#    #p.join()

#    #Queues
#    #q = mp.Queue()
#    #p = mp.Process(target=fComunicateBetweenProcess,args=(q,))
#    #p.start()
#    #print(q.get()) # prints "[42, None, 'hello']"
#    #p.join()



#    #mp.get_all_start_methods('spawn')
#    #q = mp.Queue()
#    #p = mp.Process(target=foo, args=(q,))
    
#    #ctx = mp.get_context('spawn')
#    #q1 = ctx.Queue()
#    #p1 = ctx.Process(target=foo, args=(q1,))
#    #p1.start()
#    #print(q1.get())
#    #p1.join()



#    #info('main line')
#    #p = Process(target=findProcess,args=('bob',))
#    #p.start()
#    #p.join =)
#    #Пул процессов
#    #with Pool(5) as p:
#    #    print(p.map(fPool,[1,2,3]))
#    #p = Process(target=fProcess, args=('bob',))
#    #p.start()
#    #p.join()

##


##import sys 
##import collections 
##import fdb
##from datetime import timedelta, datetime
##import csv
##import os
##import tempfile
##import urllib
##import win32con
##import win32api
##from env1.smb.SMBConnection import SMBConnection 
##conn = SMBConnection("vbox","ire0Tegr","192.168.1.75","192.168.1.68",use_ntlm_v2 =False)
##assert conn.connect("192.168.1.68",139)
##file_obj = tempfile.NameTemporaryFile()
##file_attributes, filesize = conn.retreiveFile('smbtest','/encrypt_decrypt/lic.nfo')
##print("{} {}".format(file_attributes, filesize))
##conn.close()

##import grafana_api
##grafana_api = GrafanaFace(
##          auth=("admin","graphana"),
##          host='192.168.91.4'
##          )




##class Class:
##    """
##    Изменение амперсанда
##    """
##    def __init__(self, data):
##        self.data = len(data)
##        delf.index = len(data)
##
##    def __iter__(self):
##
##
##import multiprocess
##import collections import multiprocessing
##sys.stdout.write("hello from Python %s\n" % (sys.version,))
##for line in sys.stdin:
##       if 'q' == line.rstrip():
##        break
##print(f'Input : {line}')
##print('Exit')
##con = fdb.connect(host="localhost", database='C:\RedDatabase\market\market.fdb',user='sysdba', password = 'ire0Tegr')
##cur = con.cursor()
##dt = (datetime.now() - timedelta(minutes=30).replace(microsecond=0))
##"select iif(exists(select * from cdr c where c.calldate > '" +str(dt) +"'),1,0) 
##TABLE_NAME = "SYSCONFIG"

#SELECT =
    #str(
    #"select 'ENGINE_VERSION' AS ""NAME"",rdb$get_context('SYSTEM','ENGINE_VERSION') AS ""VALUE"" from rdb$database"
    #+" union"
    #+" select 'DB_NAME', rdb$get_context('SYSTEM','DB_NAME') from rdb$database"
    #+" union"
    #+" select 'REPLICA', rdb$get_context('SYSTEM','REPLICA') from rdb$database"
    #+" union"
    #+" select 'REPLICATION_SEQUENCE', rdb$get_context('SYSTEM','REPLICATION_SEQUENCE') from rdb$database"
    #+" union"
    #+" select 'SESSION_ID', rdb$get_context('SYSTEM','SESSION_ID') from rdb$database"
    #+" union"
    #+" select 'NETWORK_PROTOCOL', rdb$get_context('SYSTEM','NETWORK_PROTOCOL') from rdb$database"
    #+" union"
    #+" select 'WIRE_COMPRESSED', rdb$get_context('SYSTEM','WIRE_COMPRESSED') from rdb$database"
    #+" union"
    #+" select 'WIRE_ENCRYPTED', rdb$get_context('SYSTEM','WIRE_ENCRYPTED') from rdb$database"
    #+" union"
    #+" select 'CLIENT_ADDRESS', rdb$get_context('SYSTEM','CLIENT_ADDRESS') from rdb$database"
    #+" union"
    #+" select 'CLIENT_HOST', rdb$get_context('SYSTEM','CLIENT_HOST') from rdb$database"
    #+" union"
    #+" select 'CLIENT_PID', rdb$get_context('SYSTEM','CLIENT_PID') from rdb$database"
    #+" union"
    #+" select 'CLIENT_PROCESS', rdb$get_context('SYSTEM','CLIENT_PROCESS') from rdb$database"    
    #+" union"
    #+" select 'CURRENT_USER', rdb$get_context('SYSTEM','CURRENT_USER') from rdb$database"
    #+" union"
    #+" select 'CURRENT_ROLE', rdb$get_context('SYSTEM','CURRENT_ROLE') from rdb$database"
    #+" union"
    #+" select 'CURRENT_ROLES ', rdb$get_context('SYSTEM','CURRENT_ROLES ') from rdb$database"
    #+" union"
    #+" select 'LDAP_ROLES ', rdb$get_context('SYSTEM','LDAP_ROLES ') from rdb$database"
    #+" union"
    #+" select 'LDAP_ROLES_DN', rdb$get_context('SYSTEM','LDAP_ROLES_DN') from rdb$database"
    #+" union"
    #+" select 'EFFECTIVE_USER', rdb$get_context('SYSTEM','EFFECTIVE_USER') from rdb$database"
    #+" union"
    #+" select 'TRANSACTION_ID', rdb$get_context('SYSTEM','TRANSACTION_ID') from rdb$database"
    #+" union"
    #+" select 'ISOLATION_LEVEL', rdb$get_context('SYSTEM','ISOLATION_LEVEL') from rdb$database"
    #+" union"
    #+" select 'LOCK_TIMEOUT', rdb$get_context('SYSTEM','LOCK_TIMEOUT') from rdb$database"
    #+" union"
    #+" select 'READ_ONLY', rdb$get_context('SYSTEM','READ_ONLY') from rdb$database"
    #)
    #cur.execute(SELECT)
    #for fieldDesc in cur.description:
    #    print(fieldDesc[fdb.DESCRIPTION_NAME].ljust(fieldDesc[fdb.DESCRIPTION_DISPLAY_SIZE]))
    #fieldIndexes = range(len(cur.description))
    #for row in cur:
    #    for fieldIndex in fieldIndexes:
            #fieldValue = str(row(fieldIndex))
            #fieldMaxWidth = cur.description[fieldIndex][fdb.DESCRIPTION_DISPLAY_SIZE]
            #print(fieldValue.ljust(fieldMaxWidth)) 
            #print()
#print(str(cur.fetchall()[0][0]))
#con.close()   
def find_longest_string(list_of_strings):
    longest_string = None
    longest_string_len = 0
    for s in list_of_strings:
        if len(s) > longest_string_len:
            longest_string_len=len(s)
            longest_string = s
    return 1

def main():
    # list_of_strings = ['abc', 'python', 'dima']

    # max_length = print(find_longest_string(list_of_strings))
    # sys.stdout.write("hello from Python %s\n" % sys.version)
    # pwd=getpass.getpass()
    # print("{:10}".format(pwd))
    # con = fdb.connect(dsn='C:\REDDATABASE\MARKET\MARKET.FDB', user='SYSDBA', password=pwd )
    # cur = con.cursor()
    # select = 'SELECT current_timestamp  as NAME FROM rdb$database'
    # cur.execute(select)
    # df = cur.fetchall()
    # for fieldDesc in cur.description:
    #    print(fieldDesc[fdb.DESCRIPTION_NAME].ljust(fieldDesc[fdb.DESCRIPTION_DISPLAY_SIZE]))
    # fieldIndexes = range(len(cur.description))
    # for row in df:
    #     for fieldIndex in fieldIndexes:
    #         fieldValue = str(row[fieldIndex])
    #         #print("{:10}".format(fieldValue))
    #         fieldMaxWidth = cur.description[fieldIndex][fdb.DESCRIPTION_DISPLAY_SIZE]
    #         print(fieldValue.ljust(fieldMaxWidth))
    # con.close()
    
    return 1 
if __name__ == "__main__":
# execute only if run as a script
    # 
    dt=0
    try:
        sdate=time
        
        
        filepath_fblog=r'C:\Program Files\RedDatabase\firebird.log'
        
        edate=time
        filepath_loep_bz2=r'C:\Temp\list_of_expires_passports\list_of_expires_passports.csv.bz2'
        df_loep_bz2=read_csv(
            # str, path object or file-like object
            filepath_or_buffer=filepath_loep_bz2
            # Any valid string path is acceptable. The string could be a URL. Valid URL schemes include http, ftp, s3, gs, and file. For file URLs, a host is expected. A local file could be: file://localhost/path/to/table.csv.
            # If you want to pass in a path object, pandas accepts any os.PathLike.
            # By file-like object, we refer to objects with a read() method, such as a file handle (e.g. via builtin open function) or StringIO.
            
            # sep: str, default ‘,’
            # Delimiter to use. If sep is None, the C engine cannot automatically detect the separator, but the Python parsing engine can, meaning the latter will be used and automatically detect the separator by Python’s builtin sniffer tool, csv.Sniffer. In addition, separators longer than 1 character and different from '\s+' will be interpreted as regular expressions and will also force the use of the Python parsing engine. Note that regex delimiters are prone to ignoring quoted data. Regex example: '\r\t'.
            
            # delimiter:str, default None
            # Alias for sep.
            
            # headerint, list of int, None, default ‘infer’
            # Row number(s) to use as the column names, and the start of the data. Default behavior is to infer the column names: if no names are passed the behavior is identical to header=0 and column names are inferred from the first line of the file, if column names are passed explicitly then the behavior is identical to header=None. Explicitly pass header=0 to be able to replace existing names. The header can be a list of integers that specify row locations for a multi-index on the columns e.g. [0,1,3]. Intervening rows that are not specified will be skipped (e.g. 2 in this example is skipped). Note that this parameter ignores commented lines and empty lines if skip_blank_lines=True, so header=0 denotes the first line of data rather than the first line of the file.
            ,header=None

            # names:array-like, optional
            # List of column names to use. If the file contains a header row, then you should explicitly pass header=0 to override the column names. Duplicates in this list are not allowed.
            
            # index_col:int, str, sequence of int / str, or False, optional, default None
            # Column(s) to use as the row labels of the DataFrame, either given as string name or column index. If a sequence of int / str is given, a MultiIndex is used.
            # Note: index_col=False can be used to force pandas to not use the first column as the index, e.g. when you have a malformed file with delimiters at the end of each line.
            
            # usecols:list-like or callable, optional
            # Return a subset of the columns. If list-like, all elements must either be positional (i.e. integer indices into the document columns) or strings that correspond to column names provided either by the user in names or inferred from the document header row(s). If names are given, the document header row(s) are not taken into account. For example, a valid list-like usecols parameter would be [0, 1, 2] or ['foo', 'bar', 'baz']. Element order is ignored, so usecols=[0, 1] is the same as [1, 0]. To instantiate a DataFrame from data with element order preserved use pd.read_csv(data, usecols=['foo', 'bar'])[['foo', 'bar']] for columns in ['foo', 'bar'] order or pd.read_csv(data, usecols=['foo', 'bar'])[['bar', 'foo']] for ['bar', 'foo'] order.
            # If callable, the callable function will be evaluated against the column names, returning names where the callable function evaluates to True. An example of a valid callable argument would be lambda x: x.upper() in ['AAA', 'BBB', 'DDD']. Using this parameter results in much faster parsing time and lower memory usage.
            
            # squeeze:bool, default False
            # If the parsed data only contains one column then return a Series.
            # Deprecated since version 1.4.0: Append .squeeze("columns") to the call to read_csv to squeeze the data.
            ,prefix='X'
            # Prefix to add to column numbers when no header, e.g. ‘X’ for X0, X1, …
            # mangle_dupe_cols:bool, default True
            # Duplicate columns will be specified as ‘X’, ‘X.1’, …’X.N’, rather than ‘X’…’X’. Passing in False will cause data to be overwritten if there are duplicate names in the columns.
            
            # dtypeType name or dict of column -> type, optional
            ,dtype={'X0':np.uint16,'X1':np.uint16}
            # Data type for data or columns. E.g. {‘a’: np.float64, ‘b’: np.int32, ‘c’: ‘Int64’} Use str or object together with suitable na_values settings to preserve and not interpret dtype. If converters are specified, they will be applied INSTEAD of dtype conversion.
            ,engine='python'
            # Parser engine to use. The C and pyarrow engines are faster, while the python engine is currently more feature-complete. Multithreading is currently only supported by the pyarrow engine.
            # New in version 1.4.0: The “pyarrow” engine was added as an experimental engine, and some features are unsupported, or may not work correctly, with this engine.

            # converters:dict, optional
            # Dict of functions for converting values in certain columns. Keys can either be integers or column labels.
            
            # true_values:list, optional
            # Values to consider as True.

            # false_values:list, optional
            # Values to consider as False.
            
            # skipinitialspace:bool, default False
            # Skip spaces after delimiter.
            # skiprowslist-like, int or callable, optional
            ,skiprows=1
            # Line numbers to skip (0-indexed) or number of lines to skip (int) at the start of the file.
            # If callable, the callable function will be evaluated against the row indices, returning True if the row should be skipped and False otherwise. An example of a valid callable argument would be lambda x: x in [0, 2].
            # 138726563
            
            # skipfooterint, default 0          
            # Number of lines at bottom of file to skip (Unsupported with engine=’c’).
            
            # nrows:int, optional
            # ,nrows=100            
            # Number of rows of file to read. Useful for reading pieces of large files.

            # na_values:scalar, str, list-like, or dict, optional
            # Additional strings to recognize as NA/NaN. If dict passed, specific per-column NA values. By default the following values are interpreted as NaN: ‘’, ‘#N/A’, ‘#N/A N/A’, ‘#NA’, ‘-1.#IND’, ‘-1.#QNAN’, ‘-NaN’, ‘-nan’, ‘1.#IND’, ‘1.#QNAN’, ‘<NA>’, ‘N/A’, ‘NA’, ‘NULL’, ‘NaN’, ‘n/a’, ‘nan’, ‘null’.

            # keep_default_na:bool, default True
            # Whether or not to include the default NaN values when parsing the data. Depending on whether na_values is passed in, the behavior is as follows:
            # If keep_default_na is True, and na_values are specified, na_values is appended to the default NaN values used for parsing.
            # If keep_default_na is True, and na_values are not specified, only the default NaN values are used for parsing.
            # If keep_default_na is False, and na_values are specified, only the NaN values specified na_values are used for parsing.
            # If keep_default_na is False, and na_values are not specified, no strings will be parsed as NaN.
            # Note that if na_filter is passed in as False, the keep_default_na and na_values parameters will be ignored.
            
            # na_filter:bool, default True
            # Detect missing value markers (empty strings and the value of na_values). In data without any NAs, passing na_filter=False can improve the performance of reading a large file.
            
            # verbose:bool, default False
            # Indicate number of NA values placed in non-numeric columns.
            
            # skip_blank_lines:bool, default True
            # If True, skip over blank lines rather than interpreting as NaN values.

            # parse_dates:bool or list of int or names or list of lists or dict, default False
            # The behavior is as follows:
            # * boolean. If True -> try parsing the index.
            # * list of int or names. e.g. If [1, 2, 3] -> try parsing columns 1, 2, 3 each as a separate date column.
            # * list of lists. e.g. If [[1, 3]] -> combine columns 1 and 3 and parse as a single date column.
            # * dict, e.g. {‘foo’ : [1, 3]} -> parse columns 1, 3 as date and call result ‘foo’
            # * If a column or index cannot be represented as an array of datetimes, say because of an unparsable value or a mixture of timezones, the column or index will be returned unaltered as an object data type. For non-standard datetime parsing, use pd.to_datetime after pd.read_csv. To parse an index or column with a mixture of timezones, specify date_parser to be a partially-applied pandas.to_datetime() with utc=True. See Parsing a CSV with mixed timezones for more.
            # * Note: A fast-path exists for iso8601-formatted dates.

            # infer_datetime_format:bool, default False
            # If True and parse_dates is enabled, pandas will attempt to infer the format of the datetime strings in the columns, and if it can be inferred, switch to a faster method of parsing them. In some cases this can increase the parsing speed by 5-10x.
            # keep_date_col:bool, default False
            # If True and parse_dates specifies combining multiple columns then keep the original columns.
            
            # date_parserfunction, optional
            # Function to use for converting a sequence of string columns to an array of datetime instances. The default uses dateutil.parser.parser to do the conversion. Pandas will try to call date_parser in three different ways, advancing to the next if an exception occurs: 1) Pass one or more arrays (as defined by parse_dates) as arguments; 2) concatenate (row-wise) the string values from the columns defined by parse_dates into a single array and pass that; and 3) call date_parser once for each row using one or more strings (corresponding to the columns defined by parse_dates) as arguments.
            
            # dayfirstbool, default False
            # DD/MM format dates, international and European format.
            
            # cache_datesbool, default True
            # If True, use a cache of unique, converted dates to apply the datetime conversion. May produce significant speed-up when parsing duplicate date strings, especially ones with timezone offsets.
            
            # iterator:bool, default False
            # Return TextFileReader object for iteration or getting chunks with get_chunk().
            # Changed in version 1.2: TextFileReader is a context manager.

            # chunksize:int, optional
            # Return TextFileReader object for iteration. See the IO Tools docs for more information on iterator and chunksize.
            # Changed in version 1.2: TextFileReader is a context manager.

            # compression:str or dict, default ‘infer’
            ,compression='bz2'
            # For on-the-fly decompression of on-disk data. If ‘infer’ and ‘%s’ is path-like, then detect compression from the following extensions: ‘.gz’, ‘.bz2’, ‘.zip’, ‘.xz’, or ‘.zst’ (otherwise no compression). If using ‘zip’, the ZIP file must contain only one data file to be read in. Set to None for no decompression. Can also be a dict with key 'method' set to one of {'zip', 'gzip', 'bz2', 'zstd'} and other key-value pairs are forwarded to zipfile.ZipFile, gzip.GzipFile, bz2.BZ2File, or zstandard.ZstdDecompressor, respectively. As an example, the following could be passed for Zstandard decompression using a custom compression dictionary: compression={'method': 'zstd', 'dict_data': my_compression_dict}.
            # Changed in version 1.4.0: Zstandard support.

            # thousands:str, optional
            # Thousands separator.
        
            # decimal:str, default ‘.’
            # Character to recognize as decimal point (e.g. use ‘,’ for European data).
        
            # lineterminator:str (length 1), optional
            # Character to break file into lines. Only valid with C parser.
            
            # quotechar:str (length 1), optional
            # The character used to denote the start and end of a quoted item. Quoted items can include the delimiter and it will be ignored.

            # quoting:int or csv.QUOTE_* instance, default 0
            # Control field quoting behavior per csv.QUOTE_* constants. Use one of QUOTE_MINIMAL (0), QUOTE_ALL (1), QUOTE_NONNUMERIC (2) or QUOTE_NONE (3).        
            
            # doublequote:bool, default True
            # When quotechar is specified and quoting is not QUOTE_NONE, indicate whether or not to interpret two consecutive quotechar elements INSIDE a field as a single quotechar element.

            # escapechar:str (length 1), optional
            # One-character string used to escape other characters.
            
            # comment:str, optional
            # Indicates remainder of line should not be parsed. If found at the beginning of a line, the line will be ignored altogether. This parameter must be a single character. Like empty lines (as long as skip_blank_lines=True), fully commented lines are ignored by the parameter header but not by skiprows. For example, if comment='#', parsing #empty\na,b,c\n1,2,3 with header=0 will result in ‘a,b,c’ being treated as the header.

            # encoding:str, optional
            # Encoding to use for UTF when reading/writing (ex. ‘utf-8’). List of Python standard encodings .
            # Changed in version 1.2: When encoding is None, errors="replace" is passed to open(). Otherwise, errors="strict" is passed to open(). This behavior was previously only the case for engine="python".
            # Changed in version 1.3.0: encoding_errors is a new argument. encoding has no longer an influence on how encoding errors are handled.

            # encoding_errors:str, optional, default “strict”
            # How encoding errors are treated. List of possible values .
            # New in version 1.3.0.
        
            # dialect:str or csv.Dialect, optional
            # If provided, this parameter will override values (default or not) for the following parameters: delimiter, doublequote, escapechar, skipinitialspace, quotechar, and quoting. If it is necessary to override values, a ParserWarning will be issued. See csv.Dialect documentation for more details.
        
            # error_bad_lines:bool, optional, default None
            # Lines with too many fields (e.g. a csv line with too many commas) will by default cause an exception to be raised, and no DataFrame will be returned. If False, then these “bad lines” will be dropped from the DataFrame that is returned.
            # Deprecated since version 1.3.0: The on_bad_lines parameter should be used instead to specify behavior upon encountering a bad line instead.

            # warn_bad_lines:bool, optional, default None
            # If error_bad_lines is False, and warn_bad_lines is True, a warning for each “bad line” will be output.
            # Deprecated since version 1.3.0: The on_bad_lines parameter should be used instead to specify behavior upon encountering a bad line instead.
        
            # on_bad_lines:{‘error’, ‘warn’, ‘skip’} or callable, default ‘error’
            # Specifies what to do upon encountering a bad line (a line with too many fields). Allowed values are :
            # *‘error’, raise an Exception when a bad line is encountered.
            # *‘warn’, raise a warning when a bad line is encountered and skip that line.
            # *‘skip’, skip bad lines without raising or warning when they are encountered.
            # *New in version 1.3.0:
            # *callable, function with signature (bad_line: list[str]) -> list[str] | None that will process a single bad line. bad_line is a list of strings split by the sep. If the function returns None`, the bad line will be ignored. If the function returns a new list of strings with more elements than expected, a ``ParserWarning will be emitted while dropping extra elements. Only supported when engine="python"
            # New in version 1.4.0.
        
            # delim_whitespace:bool, default False
            # Specifies whether or not whitespace (e.g. ' ' or '    ') will be used as the sep. Equivalent to setting sep='\s+'. If this option is set to True, nothing should be passed in for the delimiter parameter.

            # low_memory:bool, default True
            # Internally process the file in chunks, resulting in lower memory use while parsing, but possibly mixed type inference. To ensure no mixed types either set False, or specify the type with the dtype parameter. Note that the entire file is read into a single DataFrame regardless, use the chunksize or iterator parameter to return the data in chunks. (Only valid with C parser).

            # memory_map:bool, default False
            # If a filepath is provided for filepath_or_buffer, map the file object directly onto memory and access the data directly from there. Using this option can improve performance because there is no longer any I/O overhead.
        
            # float_precision:str, optional
            # Specifies which converter the C engine should use for floating-point values. The options are None or ‘high’ for the ordinary converter, ‘legacy’ for the original lower precision pandas converter, and ‘round_trip’ for the round-trip converter.
            # Changed in version 1.2.

            # storage_options:dict, optional
            # Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to urllib as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to fsspec. Please see fsspec and urllib for more details.
            # New in version 1.2.

        )
        # Returns
        # DataFrame or TextParser
        # A comma-separated values (csv) file is returned as two-dimensional data structure with labeled axes.
        print("DataFrameIndex :{}".format(df_loep_bz2.index))
        print("DataFrameColumns :{}".format(df_loep_bz2.columns))
        print("DataFrameTypes :{}".format(df_loep_bz2.dtypes))
        print("DataFrame :{}".format(df_loep_bz2.info(verbose=True)))
        print("DataFrame :{}".format(df_loep_bz2.info(verbose=False)))
        print("DataFrame memory-usage:{}".format(df_loep_bz2.info(memory_usage='deep')))
        print("DataFrame info:{}".format(df_loep_bz2.info()))
        print("Окончание чтения bz2:{} сек.".format(dt))
        dt=edate-time
        print(dt)

        edate=time
        url_loep_bz2 = 'https://xn--b1agjhrfhd.xn--b1ab2a0a.xn--b1aew.xn--p1ai/upload/expired-passports/list_of_expired_passports.csv.bz2'
        df_url_loep_bz2 = read_csv(
            filepath=url_loep_bz2
            # ,sepstr=
            # ,delimiterstr=
            # ,headerint=
            ,header=None
            ,prefix='X'
            ,dtype={'X0':np.uint16,'X1':np.uint16}
            ,engine='python'
            ,skiprows=1
            # ,nrows=100
            # 138726763
            ,compression='bz2'
            ,error_bad_lines=69_363
            ,warn_bad_lines= 138_726
        )
        print("DataFrameIndex: {}".format(df_url_loep_bz2.index))
        print("DataFrameColumns: {}".format(df_url_loep_bz2.columns))
        print("DataFrameTypes: {}".format(df_url_loep_bz2.dtypes))
        print("DataFrame Verbose: {}".format(df_url_loep_bz2.info(verbose=True)))
        print("DataFrame No-Verbose: {}".format(df_url_loep_bz2.info(verbose=False)))
        print("DataFrame memory-usage:{}".format(df_url_loep_bz2.info(memory_usage='deep')))
        print("DataFrame info:{}".format(df_url_loep_bz2.info()))
        dt=edate-time
        print("Окончание чтения url bz2:{} сек.".format(dt))        
        
        edate=time
        filepath_loep=r'C:\Temp\list_of_expires_passports\list_of_expires_passports.csv'
        df=read_csv(
            filepath_or_buffer=filepath_loep
            # ,usecols=['PASSP_SERIES', 'PASSP_NUMBER']
            ,header=None
            ,prefix='X'
            ,dtype={'X0':np.uint16,'X1':np.uint16}
            ,engine='python'
            ,skiprows=1
            # 138726563
            # ,nrows=100
            # ,skipfooter=138726563
            ,skip_blank_lines=False
            )
        print("Окончание чтения csv-файла:{} сек.".format(dt))
        print("DataFrameIndex {}".format(df.index))
        print("DataFrameColumns {}".format(df.columns))
        print("DataFrameTypes {}".format(df.dtypes))
        print("DataFrame {}".format(df.info(verbose=True)))
        print("DataFrame No-Verbose{}".format(df.info(verbose=False)))
        print("DataFrame memory-usage:{}".format(df_url_loep_bz2.info(memory_usage='deep')))
        print("DataFrame info:{}".format(df_url_loep_bz2.info()))
        dt=sdate-time
        print('Окончание чтения csv: {} сек.'.format(dt))
        
        print(type(df))
        print("Привет от Python {}\n".format(sys.version))
        
    except PendingDeprecationWarning as w:
        # Base class for warnings about features which are obsolete and expected to be deprecated in the future, but are not deprecated at the moment.
        # This class is rarely used as emitting a warning about a possible upcoming deprecation is unusual, and DeprecationWarning is preferred for already active deprecations.
        # Ignored by the default warning filters. Enabling the Python Development Mode shows this warning.
        # The deprecation policy is described in PEP 387.
        print('Предупреждения о использовании функций которые будут считаться устаревшими в будущем')
    except SyntaxWarning as w:
        # Base class for warnings about dubious syntax.
        print('Предупреждения об сомнительном синтаксисе {}'.format(w))
    #Warnings
    except RuntimeWarning as w:
        # Base class for warnings about dubious runtime behavior.
        print('Базовый класс предупреждений об устаревших функциях в python {} '.format(w))
    except FutureWarning as w:
    # Base class for warnings about deprecated features when those warnings are intended for end users of applications that are written in Python.
        print('Предупреждения об использовании устаревших функциях в python {} '.format(w))
    except ImportWarning as w:
    # Base class for warnings about probable mistakes in module imports.
    # Ignored by the default warning filters. Enabling the Python Development Mode shows this warning.
        print('Предупреждения связанные с перекодировкой {} '.format(w))
    # except EncodingWarning as w:
    #     # Base class for warnings related to encodings.
    #     # See Opt-in EncodingWarning for details.
    #     # New in version 3.10.
    #     print('Предупреждения cвязанные с перекодировкой {} '.format(w))
    except UnicodeWarning as w:
        # Base class for warnings related to Unicode.
        print('Предупреждение превышение системных параметров {} '.format(w))
    except ResourceWarning as w:
        # Base class for warnings related to resource usage.
        # Ignored by the default warning filters. Enabling the Python Development Mode shows this warning.
        # New in version 3.2.    
        print('Предупреждение превышение системных параметров {} '.format(w))
    except BytesWarning as w:
        # Base class for warnings related to bytes and bytearray.
        print('Предупреждение ссылок при использовании одной и той же памяти в массиве памяти {} '.format(w))
    except DeprecationWarning as w:
        # Base class for warnings about deprecated features when those warnings are intended for other Python developers.
        # Ignored by the default warning filters, except in the __main__ module (PEP 565). Enabling the Python Development Mode shows this warning.
        # The deprecation policy is described in PEP 387.
        print('Предупреждение используемое другими разработчиками {} '.format(w))
    except UserWarning as w:
        # Base class for warnings generated by user code.
        print('Предупреждения сформированные пользовательским кодом {} '.format(w))
    except Warning as w:
        # Base class for warning categories.
        print('ошибка преобразования кодировок {} '.format(w))    
# Exeptions    
    except ZeroDivisionError as e:
        print('Ошибка деления на ноль {}'.format(e))
    except BlockingIOError as e:
        print('Ошибка обращеннию блока операций {}'.format(e))
    except ChildProcessError as e:
        print('Ошибка дочернего процесса {}'.format(e))
    except ConnectionResetError as e:
        # A subclass of ConnectionError, raised when a connection is reset by the peer. Corresponds to errno ECONNRESET.
        print('Соединение сброшено {}'.format(e))
    except ConnectionRefusedError as e:
        #  A subclass of ConnectionError, raised when a connection attempt is refused by the peer. Corresponds to errno ECONNREFUSED.
        print('В соединение разорвано{}'.format(e))
    except ConnectionAbortedError as e:
        # A subclass of ConnectionError, raised when a connection attempt is aborted by the peer. Corresponds to errno ECONNABORTED.
        print('Ошибка в соединении отказано{}'.format(e))
    except BrokenPipeError as e:
        print('Ошибка попытка процесса отдать данные другому процессу{}'.format(e))
    except ConnectionError as  e:
        print('Ошибка соединения{}'.format(e))
    except FileExistsError as e:
        # Raised when trying to create a file or directory which already exists. Corresponds to errno EEXIST.
        print('Файл уже существует {}'.format(e))
    except FileNotFoundError as e:
        # Raised when a file or directory is requested but doesn’t exist. Corresponds to errno ENOENT.
        print('Файл не найден {}'.format(e))
    except InterruptedError as e:
        # Raised when a system call is interrupted by an incoming signal. Corresponds to errno EINTR.
        # Changed in version 3.5: Python now retries system calls when a syscall is interrupted by a signal, except if the signal handler raises an exception (see PEP 475 for the rationale), instead of raising InterruptedError.
        print('Выщвающий метод прерывается входящим сигналом {}'.format(e))
    except IsADirectoryError as e:
        # Raised when a file operation (such as os.remove()) is requested on a directory. Corresponds to errno EISDIR.
        print('Попытка удаления ссылочной дируктории {}'.format(e))
    except NotADirectoryError as e:
        # Raised when a directory operation (such as os.listdir()) is requested on something which is not a directory. On most POSIX platforms, it may also be raised if an operation attempts to open or traverse a non-directory file as if it were a directory. Corresponds to errno ENOTDIR.
        print('Путь не является каталогом {}'.format(e))
    except PermissionError as e:
        # Raised when trying to run an operation without the adequate access rights - for example filesystem permissions. Corresponds to errno EACCES and EPERM.
        print('Ошибка прав доступа {}'.format(e))
    except ProcessLookupError as e:
        # Raised when a given process doesn’t exist. Corresponds to errno ESRCH.
        print('Ошибка поиска процесса. Процесс не существует {}'.format(e))
    except TimeoutError as e:
        # Raised when a system function timed out at the system level. Corresponds to errno ETIMEDOUT.
        print('Ошибка выхода по таймауту {}'.format(e))
    except UnboundLocalError as e:
        print('ошибка выхода за пределы массива {}'.format(e))
    except KeyError as e:
        print('Ошибка поиска в установки в ключе словаря{}\n'.format(e) )
    except OverflowError as e:
        print('Ошибка переполнения памяти переменной или арефметическая операция не поддерживается {}'.format(e))
    except ModuleNotFoundError as e:
        print('Ошибка не найденного модуля{}\n'.format(e) )
    except FloatingPointError as e:
        print('Ошибка точности после запятой{}\n'.format(e))
    except ArithmeticError as e:
        print('Ошибка арифметики{}\n'.format(e) )
    except BufferError as e:
        print('Ошибка буфера{}\n'.format(e))
    except LookupError as e:
        print('Ошибка поиска{}\n'.format(e))
    except AssertionError as e:
        print('Ошибка доступа{}\n'.format(e))
    except AttributeError as e:
        # print(
            print('Ошибка атрибутов{}\n'.format(e))
            # )
    except EOFError as e:
        print('Ошибка выхода за пределы файла{}\n'.format(e))    
    except GeneratorExit as e:
        print('Ошибка входа из генератора значений{}\n'.format(e) )
    except ImportError as e:
        print('Ошибка импорта документа{}\n'.format(e))
    except MemoryError as e:
        print('Ошибка выделенной памяти{}\n'.format(e))
    except NameError as e:
        print('Ошибка использования глобального и локального имени переменной{}\n'.format(e))
    except NotImplementedError as e:
        print('Ошибка определения методов и классов от которых наследуется класс требует переопределения метода:{}\n'.format(e) )
    except OSError as e:
        # OSError(errno, strerror[, filename[, winerror[, filename2]]])
        if isinstance(e,IOError):
            print('Ошибка ввода/вывода {}'.format(e))
        elif isinstance(e,EnvironmentError):
            print('Ошибка вызова не существующей переменной окружения {}'.format(e))
        elif isinstance(e,WindowsError):
            print('Ошибка ввода/вывода {}'.format(e))
        else:
            print('ОШибка операционой системы включая файл не найден и объем дискового пространства #{} {} {} {} {}'.format(e.errno,e.strerror,e.filename,e.winerror,e.filename2))
    except IndentationError as e:
        print('Ошибка в синтаксисе файла {}'.format(e))
    except RecursionError as e:
        print('Ошибка превышения рекурсии по памяти{}'.format(e))
    except ReferenceError as e:
        print('Ошибка ссылочной такие как прокси сервер{}'.format(e))
    except RuntimeError as e:
        print('Ошибка не попадающая в прочие категории{}'.format(e))
    except StopIteration as e:
        print('Ошибка остановки итерации{}'.format(e))
    except StopAsyncIteration as e:
        print('Ошибка остановки асинхронной итерации{}'.format(e))
    except SyntaxError as e:
        print('Ошибка в синтаксисе файла {} {} {} {} {}'.format(e.msg,e.args,e.end_lineno,e.end_offset,e.filename,e.lineno,e.offset,e.text))
    except SystemExit as e:
        print('ошибка выхода из системы {}'.format(e))
    except TypeError as e:
        print('ошибка приведения типов {}'.format(e))
    except UnicodeEncodeError as e:
        print('Ошибка кодирования файла {}'.format(e))
    except UnicodeDecodeError as e:
        print('Ошибка декодирования фаайла {}'.format(e))
    except UnicodeTranslateError as e:
        print('Ошибка перевоода {}'.format(0))
    except UnicodeError as e:
        print('ошибка преобразования кодировок {} '.format(e))
    except Exception as e:
        print('Ошибка приложения{}\n'.format(e) )
    finally:
        print('Задержка по времени : {:10} сек.'.format(dt))
        if any: 
            any=None
        if df:
            df=None
        if df_loep_bz2:
            df_loep_bz2=None
        # if w:
        #     w=None
        # if e:
        #     e=None