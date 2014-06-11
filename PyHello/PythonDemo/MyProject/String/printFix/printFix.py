
import os
allFileNum = 0
def printPath(level, path):
    global allFileNum
    '''
    打印一个目录下的所有文件夹和文件
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)
    # 先添加目录级别
    dirList.append(str(level))
    for f in files:
        if(os.path.isdir(path + '/' + f)):
            # 排除隐藏文件夹。因为隐藏文件夹过多
            if(f[0] == '.'):
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        if(os.path.isfile(path + '/' + f)):
            # 添加文件
            fileList.append(f)
    # 当一个标志使用，文件夹列表第一个级别不打印
    i_dl = 0
    for dl in dirList:
        if(i_dl == 0):
            i_dl = i_dl + 1
        else:
            # 打印至控制台，不是第一个的目录
            print ('-' * (int(dirList[0])), dl)
            # 打印目录下的所有文件夹和文件，目录级别+1
            printPath((int(dirList[0]) + 1), path + '/' + dl)
    for fl in fileList:
        # 打印文件
        print ('-' * (int(dirList[0])), fl)
        # 随便计算一下有多少个文件
        allFileNum = allFileNum + 1

def fixPrint(path):
    file  = open(path,"r",encoding="utf-8")
    all_the_text = file.readlines( )
    for line in all_the_text:
        if(line.index("print")>0):
            line="hhh"
    file.close()

if __name__ == '__main__':
   
    BASE_DIR = os.path.dirname(__file__) #获取当前文件夹的绝对路径
    crawlersAP = os.path.join(  BASE_DIR, '../..' , "crawlers")
    crawlersPath = os.path.abspath(crawlersAP)

    py = os.path.join(  crawlersPath, "百度贴吧", "百度贴吧爬虫v0.1.py")
    fixPrint(py)
    #file_path = os.path.join(BASE_DIR, 'Test_Data') #获取当前文件夹内的Test_Data文件
    printPath(1, crawlersPath)
    print ('总文件数 =', allFileNum)
