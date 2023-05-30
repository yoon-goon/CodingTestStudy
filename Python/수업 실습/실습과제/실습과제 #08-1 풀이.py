import sys
import os

def removeCommentsFromFile(fr, fw):
    for line in fr:
        ls = line.strip()

        if ls != "" and ls[0] == '#':
            continue
        else:
            if line.find('"') < 0 and line.find("'") < 0:
                idx = line.find('#')
                if idx >= 0:
                    news = line[:idx]
                    fw.write(news + "\n")
                else:
                    fw.write(line)
            else:
                inside = False
                written = False
                prevCh = None
                ch = None
                for i in range(len(line)):
                    prevCh = ch
                    ch = line[i]
                    if inside == False:
                        if ch == '#': 
                            fw.write(line[:i] + "\n")
                            written = True
                            break
                        else:
                            # 문자열 상수 시작
                            if ch == '"' or ch == "'":
                                inside = True
                            continue
                    else: # 문자열 안쪽. 
                        if (ch == '"' or ch == "'") and prevCh != '\\':
                            inside = False
                        continue
                if not written:
                    fw.write(line)

print(os.getcwd())

fileName = input("주석문을 제거할 파일 이름을 입력: ")

try:
    f = open(fileName, encoding="utf-8")
except FileNotFoundError:
    try:
        print(f"{fileName}이 없습니다. 다시 파일 이름을 입력하세요: ")
        fileName = input("주석문을 제거할 파일 이름을 입력: ")
        f = open(fileName, encoding="utf-8")
    except FileNotFoundError:
        print(f"{fileName}이 없습니다. 프로그램을 종료합니다.")
        sys.exit()
        
newFileName = "cr_" + fileName 
fw = open(newFileName, "w", encoding="utf-8")
removeCommentsFromFile(f, fw)
f.close()
fw.close()
