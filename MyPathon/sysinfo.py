import sys
import time
def printTime():
    time_format= '%Y-%m-%d %X'
    time_content = time.strftime(time_format)
    print(time_content)
    time_result =time.strptime(time_content,time_format)
    print(time_result)
def printsysParam():
    print(sys.version_info)


printsysParam()
printTime()