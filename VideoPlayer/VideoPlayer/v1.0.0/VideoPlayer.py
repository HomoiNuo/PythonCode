import click
import cv2
import os
import Functions

def FullWindow(ctx,param,value)->bool:
    global fw
    fw = True
    
   
fw = False

@click.command()
@click.option("--fullwindow","-fw",required=False,is_flag=True,callback=FullWindow,help="全屏播放视频")
@click.option("--currentpath","-cp",required=False,default=None,type=str,help="视频与播放器在同一文件夹下时可使用")
@click.option("--title","-t",required=False,type=str,default=None,is_flag=False,help="设置窗口标题")
@click.option("--xaxis","-x",required=False,default=0,type=int,help="设置窗口宽度")
@click.option("--yaxis","-y",required=False,default=0,type=int,help="设置窗口高度")
@click.option("--loop","-l",required=False,default=1,type=int,help="视频循环播放次数（为0时无限循环）")
@click.argument("FileName",required=False)

def Function(filename,fullwindow,xaxis,yaxis,loop,currentpath,title,*args, **kwargs):
    if (not (title == None)) or (str(title).isspace()):
        Title = title
    else:
        Title = filename
    CurrentTime = 1
    PlanTime = 1
    IsExit = False
    if loop < 0:
        PlanTime = 0 
    if loop == 0:
        IsEndlessLoop = True
    if loop > 0:
        IsEndlessLoop =False
    while CurrentTime <= PlanTime:
        if not (currentpath == None or str(currentpath).isspace()):
            Functions.ispath(os.path.abspath('.')+"\\"+str(currentpath))
            Video = cv2.VideoCapture(os.getcwd()+"\\"+str(currentpath))
        elif Functions.ispath(filename):
            Video = cv2.VideoCapture(filename)
        else:
            print("FileInvalidError:文件路径无效")
            break
        FPS = Video.get(cv2.CAP_PROP_FPS)
        Delay = int(750 / FPS)
        if xaxis == 0 or yaxis == 0:
            if fw:
                cv2.namedWindow(Title, cv2.WINDOW_NORMAL)
                cv2.setWindowProperty(Title, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            else:
                cv2.namedWindow(Title, cv2.WINDOW_FREERATIO)
        else:
            cv2.resizeWindow(Title,xaxis,yaxis)
        while True:
            Read, Frame = Video.read()
            if not Read:
                break
            cv2.imshow(Title, Frame)
            if cv2.waitKey(Delay) == ord('q'):
                IsExit = True
                break
        Video.release()
        if IsEndlessLoop:
            PlanTime +=1
        if IsExit:
            break
        CurrentTime +=1
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
        try:
            Function()
        except KeyboardInterrupt:
            pass
        