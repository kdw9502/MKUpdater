import os
import sys

def ReadCppList(mkpath):
    CppListFile = open('cpps.txt','w')
    relpaths = []
    for path,dir,files in os.walk("mplayball"):
        for file in files :
            if file.endswith('.cpp') :
                fullpath = path + '/' + file
                relpaths.append( os.path.relpath(fullpath,mkpath) )
    for path,dir,files in os.walk("../../Classes"):
        for file in files :
            if file.endswith('.cpp') :
                fullpath = path + '/' + file
                relpaths.append( os.path.relpath(fullpath,mkpath) )

    CppListFile.write("LOCAL_SRC_FILES := \\\n")
    for relpath in relpaths:
        CppListFile.write(relpath+' \\\n'*(relpath != relpaths[-1] ))
    CppListFile.write('\n\n')
    CppListFile.close()

def ReadDir(mkpath):
    DirListFile = open('dirs.txt','w')
    relpaths = []
    for path,dir,files in os.walk("../../Classes"):
        relpaths.append(os.path.relpath(path,mkpath))
    DirListFile.write("LOCAL_C_INCLUDES := \\\n")
    for relpath in relpaths:
        DirListFile.write('\t$(LOCAL_PATH)/'+relpath+' \\\n')
    DirListFile.write('\t$(LOCAL_PATH)/../../libs/boost\n\n')
    DirListFile.close()


def main():

    # 나머지 작성
    # 합치기
    pre = open("pre.txt" ,"r")
    post= open("post.txt","r")
    post_t= open("post.txt","r")
    if not os.path.exists('../KBOmanager/proj.android/jni/Android.mk') :
        mkpath = input("Can't find Android.mk, Enter the path of including Android.mk : ")
        if( os.path.isdir(mkpath)) :
            os.chdir(mkpath)
        else :
            print("Can't Open Path")

    else :
        os.chdir('../KBOmanager/proj.android/jni')

    ReadCppList(os.getcwd())
    ReadDir(os.getcwd())
    CppListFile = open('cpps.txt','r')
    DirListFile = open('dirs.txt','r')

    output = open("Android.mk",'w')
    output_t= open("../../proj.tstore/jni/Android.mk",'w')
    output.write(pre.read())
    pre.seek(0)
    output_t.write(pre.read())
    pre.close()

    output.write(CppListFile.read())
    CppListFile.seek(0)
    output_t.write(CppListFile.read())
    CppListFile.close()
    output.write(DirListFile.read())
    DirListFile.seek(0)
    output_t.write(DirListFile.read())
    DirListFile.close()
    output.write(post.read())
    post.seek(0)
    output_t.write(post_t.read())
    post.close()
    post_t.close()
    output.close()



if __name__ == '__main__' :
    main()
