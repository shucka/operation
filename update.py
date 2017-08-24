# -*- coding: UTF-8 -*-
# @Time    : 2017-08-24
# @Author  : shuck 664888772@qq.com

import os, time,shutil,sys,logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='update.log',
                filemode='a')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

#复制文件夹所有文件到指定目录   更新文件
def updateData( rootDir, abdir):

    for lists in os.listdir( rootDir): 
        path = os.path.join( rootDir, lists)
        abpath = os.path.join( abdir, lists)

        if os.path.isfile( path):
            if not os.path.exists( abdir):
                os.makedirs( abdir)
            try:
                shutil.copy( path, abdir)
                logging.info('Success Copy %s to %s' % (path, abdir))
            except :
                logging.warning('Unexpected error: %s %s to %s' % (sys.exc_info()[0], path, abdir))

        if os.path.isdir( path):
            updateData( path, abpath) 



#根据要更新的文件夹备份文件
def backData( updateDir, rootDir, backDir):

    for lists in os.listdir( updateDir): 
        updatefile = os.path.join( updateDir, lists) #要更新的文件
        rootfile = os.path.join( rootDir, lists)     #要备份的文件
        backfile = os.path.join( backDir, lists)     #备份文件

        if os.path.isfile( updatefile):
            if not os.path.exists( backDir):
                os.makedirs( backDir)
            
            if os.path.exists( rootfile):                
                try:
                    shutil.copy( rootfile, backfile)
                    logging.info('Success Copy %s to %s' % (rootfile, backfile))
                except :
                    logging.warning ('Unexpected error: %s %s to %s' % (sys.exc_info()[0], rootfile, backfile))

        if os.path.isdir( updatefile):
            backData( updatefile, rootfile, backfile)


#设置备份的目录
today = time.strftime("%Y-%m-%d", time.localtime())
backRootDir = 'D:/operation/back'
if os.path.exists( os.path.join( backRootDir, today)):
    backdirname = today + '_'  + str(int( time.time()))
else:
    backdirname = today

#前台的备份与更新目录
wwwDir = "D:/operation/www"
updateDir       = "D:/operation/update"
backDir   = backRootDir + "/" + backdirname

#更新trunk
print ('开始备份文件....')
backData( updateDir, wwwDir, backDir )
print ('文件备份结束！！！！')
print ('...')
print ('...')
print ('...')
print ('...')

print ('开始更新文件....')
updateData( updateDir, wwwDir )
print ('文件更新结束！！！！')