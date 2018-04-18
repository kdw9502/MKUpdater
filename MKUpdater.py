import os
import sys

def ReadCppList(mkpath):

    #.mk 가 있는 디렉토리에서 실행됨
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

    CppListStr = "LOCAL_SRC_FILES := \\\n"
    for relpath in relpaths:
        CppListStr = CppListStr + relpath+' \\\n'*(relpath != relpaths[-1] )
    CppListStr = CppListStr + '\n\n'
    return CppListStr

def ReadDir(mkpath):

    #.mk 가 있는 디렉토리에서 실행됨
    relpaths = []
    for path,dir,files in os.walk("../../Classes"):
        relpaths.append(os.path.relpath(path,mkpath))
    DirListStr = "LOCAL_C_INCLUDES := \\\n"
    for relpath in relpaths:
        DirListStr = DirListStr + '\t$(LOCAL_PATH)/'+relpath+' \\\n'
    DirListStr = DirListStr + '\t$(LOCAL_PATH)/../../libs/boost\n\n'
    return DirListStr


def main():

    pre = open("pre.txt" ,"r").read()
    post= open("post.txt","r").read()
    post_t= open("post_t.txt","r").read()
    
    # 이 스크립트를 실행할 디렉토리를 변경하고 싶으면 이 경로만 변경하세요 (Android.mk가 있는 경로)
    mkpath = '../KBOmanager/KBOmanager/proj.android/jni/'
    
    if not os.path.exists(mkpath) :
        mkpath = input("Can't find jni path, Enter the path of jni path : ")
        if( os.path.isdir(mkpath)) :
            # .mk 가 있는 디렉토리로 이동
            os.chdir(mkpath)
        else :
            print("Can't Open Path")

    else :
        # .mk 가 있는 폴더로 이동
        os.chdir(mkpath)
    # FIXME:디렉토리 이동때문에 코드 파악이 힘듬

    CppListStr = ReadCppList(os.getcwd())
    DirListStr = ReadDir(os.getcwd())

    #.mk 가 있는 디렉토리에서 실행됨
    output = open("Android.mk",'w')
    output_t= open("../../proj.tstore/jni/Android.mk",'w')

    output.write(pre + CppListStr + DirListStr + post)
    output_t.write(pre + CppListStr + DirListStr + post_t)
    output.close()
    output_t.close()


if __name__ == '__main__' :
    main()
