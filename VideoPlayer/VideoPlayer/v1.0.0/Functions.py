def ispath(Path:str) -> bool:
    try:
        if (not str(Path).isspace()) and (not Path == None):
            File = open(Path)
            File.close()
            return True
    except FileNotFoundError:
        print("FileInvalidError:文件路径无效")
        return False

if __name__ == "__main__":
    ispath("C:\\Users\\28363\\Downloads\\666.mp4")
    a = input(":")
    if a.isspace() or len(a) == 0:
        print("s")
