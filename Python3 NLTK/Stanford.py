# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/16'

import sys
import os

class StanfordCoreNLP():
    def __init__(self,jarpath):
        self.root = jarpath
        self.tempsrcpath = "tempsrc" # 输入临时文件路径
        self.jarlist = ["ejml-0.23.jar","javax.json.jar","jollyday.jar","joda-time.jar","protobuf.jar","slf4j-api.jar","slf4j-simple.jar","stanford-corenlp-3.8.0.jar","xom.jar"]
        self.jarpath = ""
        self.buildjars()

    def buildjars(self):
        for jar in self.jarlist:
            self.jarpath += self.root+jar+";"

    def savefile(self,path,sent):
        fp = open(path,"wb")
        fp.close()

    def delfile(self,path):
        os.remove(path=path)

class StanfordPOSTagger(StanfordCoreNLP):
    def __init__(self,jarpath,modelpath):
        StanfordCoreNLP.__init__(self,jarpath=jarpath)
        self.modelpath = modelpath
        self.classfier = "edu.stanford.nlp.tagger.maxent.MaxentTagger"
        self.dellimiter = "/"
        self.__buildcmd()

    def __buildcmd(self):
        self.cmdline = 'java -mxlg -cp "'+self.jarpath+'" '+self.classfier+'-model"'+self.modelpath+'" -tagSeparator ' +self.dellimiter

    def tag(self,sent):
        self.savefile(self.tempsrcpath,sent)
        tagtxt = os.popen(self.cmdline +" -textFile " + self.tempsrcpath,'r').read()
        self.delfile(self.tempsrcpath)

        return tagtxt

    def tagfile(self,inputpath,outpath):
        os.system(self.cmdline+' -textfile '+inputpath+' > ' +outpath)
