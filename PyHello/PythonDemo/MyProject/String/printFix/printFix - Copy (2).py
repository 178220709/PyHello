import os
allFileNum = 0
def printPath(level, path):
    global allFileNum
    '''
    ��ӡһ��Ŀ¼�µ������ļ��к��ļ�
    '''
    # �����ļ��У���һ���ֶ��Ǵ�Ŀ¼�ļ��� 
    dirList = []
    # �����ļ�
    fileList = []  
    # �����ļ� ����·��
    filePathList = []
    # ����һ���б����а�����Ŀ¼��Ŀ������(google����)
    files = os.listdir(path)
    # �����Ŀ¼����
    dirList.append(str(level))
    for f in files:
        if(os.path.isdir(path + '/' + f)):
            # �ų������ļ��С���Ϊ�����ļ��й���
            if(f[0] == '.'):
                pass
            else:
                # ��ӷ������ļ���
                dirList.append(f)
        if(os.path.isfile(path + '/' + f)):
            # ����ļ�
            fileList.append(f)
            filePathList.append(path + '/' + f)
    # ��һ����־ʹ�ã��ļ����б��һ�����𲻴�ӡ
    i_dl = 0
    for dl in dirList:
        if(i_dl == 0):
            i_dl = i_dl + 1
        else:
            # ��ӡ������̨�����ǵ�һ����Ŀ¼
            print ('-' * (int(dirList[0])), dl)
            # ��ӡĿ¼�µ������ļ��к��ļ���Ŀ¼����+1
            printPath((int(dirList[0]) + 1), path + '/' + dl)
    for fl in fileList:
        # ��ӡ�ļ�
        print ('-' * (int(dirList[0])), fl)
        #fixPrint(fl)
        # ������һ���ж��ٸ��ļ�
        allFileNum = allFileNum + 1
    for fl in filePathList:
       fixPrint(fl)
def fixPrint(path):
    file  = open(path,"r",encoding="utf-8")
    newLines = [];
    all_the_text = file.readlines( )
    for line in all_the_text:
        index = line.find("print")
        #��鵱ǰ���Ƿ���print ͬʱ�Ƿ��Ѿ���()��
        if(index>=0 and line[index+5:index+8].find('(')==-1):
            #����print�����ݽ��д���,
            line = line.replace("print","print (") 
            if(line.find("\n")>0):
                 line =  line.replace("\n"," )" +"\n") 
            else:
                line+=")"
        newLines.append(line)
    file.close()

     #ֱ�Ӹ��ǵ�ԭ�����ļ� 
    newFile = open(path,"w",encoding="utf-8")
    for line in newLines:
      newFile.write(line)
    newFile.close()

if __name__ == '__main__':
   
    BASE_DIR = os.path.dirname(__file__) #��ȡ��ǰ�ļ��еľ���·��
    crawlersAP = os.path.join(  BASE_DIR, '../..' , "crawlers")
    crawlersPath = os.path.abspath(crawlersAP)

    py = os.path.join(  crawlersPath, "�ٶ�����", "123.py")
    fixPrint(py)
    printPath(1, crawlersPath)
    print ('���ļ��� =', allFileNum)