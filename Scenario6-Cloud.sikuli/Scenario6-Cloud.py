openApp("D:\\MS\\Interop\\IntelliJ\\InstallFolder\\IntelliJIDEACommunityEdition\\bin\\idea.exe")
while exists("1410763469450-2.png"):sleep(3)
wait("1410763599145-2.png",60)
click("1408716102829-2.png")
wait("1408716434998-2.png",1800)
for n in range(4): 
 sleep(1)
 type(Key.TAB)
for n in range(2): 
 sleep(1)
 type(Key.ENTER)

wait("1410771774607-2.png",60)
ProjectName = "Sample"
paste(ProjectName)

for n in range(7): 
 sleep(1)
 type(Key.TAB)
type(Key.ENTER)
wait(Pattern("1410776176450-2.png").similar(0.80),60)
sleep(2)
rightClick("1410785156354-1.png")
type(Key.ALT + "f")
sleep(1)
type(Key.DOWN + Key.UP + Key.UP + Key.RIGHT) 
sleep(2)
type(Key.ENTER)
wait("1410785293792-1.png",30)
AzureProjectName = "AzureProject"
paste(AzureProjectName)
for n in range(2): 
 sleep(1)
 type(Key.TAB)
type(Key.ENTER)
wait("1410785743174-1.png",10)
sleep(2)
r = find("1409061481024-1.png").nearby(10)
t = r.find("1409117840021-1.png")
click(t)
sleep(1)
click(t)
sleep(2)
click("1409121625175-4.png")
wait("1409121645360-1.png")
sleep(2)
JDKPath = "C:\Program Files\Java\jdk1.7.0_40"
paste(JDKPath)
type(Key.TAB + Key.TAB + Key.ENTER)
sleep(2)
click("1410861989521-2.png")
sleep(1)
type(Key.TAB)
JDKBlobPath = "https://3rdpartyjdkstorage.blob.core.windows.net/eclipsedeploy/jdk1.7.0_67.zip"
paste(JDKBlobPath)
sleep(2)
click("1410862347401-2.png")
sleep(2)
r= find("1409121812654-2.png").nearby(10)
t = r.find("1409121861228-2.png")
click(t)
sleep(1)
click("1409121625175-3.png")
wait("1409121956780-2.png")
sleep(1)
ServerPath = "D:\MS\Interop\Tomcat\GlassFish4"
paste(ServerPath)
sleep(1)
type(Key.TAB + Key.TAB + Key.ENTER)
sleep(1)
click("1410863065871-2.png")
sleep(2)
wait("1410788195236-4.png",10)
sleep(2)
type(Key.ENTER) 
sleep(1)
type(Key.DOWN + Key.DOWN)
sleep(1)
rightClick("1410788347443-4.png")
type(Key.ALT + "f")
sleep(1)
type(Key.DOWN + Key.UP + Key.UP + Key.RIGHT + Key.DOWN + Key.ENTER)
sleep(3)
wait("1409129183315-4.png")
click("1409129208043-4.png")
wait("1409129222353-3.png")
click("1409129261046-3.png")
wait("1409129567170-3.png")
sleep(2)
PublishSettingFile = "D:\MS\Interop\AzurePublishSettingFile\CollaberaInteropTest-9-15-2014-credentials.publishsettings"
paste(PublishSettingFile)
sleep(2)
type(Key.TAB + Key.TAB + Key.ENTER)
sleep(2)
click("1409129853272-3.png")
wait("1410788893543-3.png",10)
while exists("1409131510174-3.png"): sleep(5)
sleep(2)
r = find("1409132671116-3.png").right(700)
t = r.find("1409132703085-3.png")
click(t)
sleep(2)
type("b" + Key.ENTER)
sleep(2)
r = find("1409221267480-3.png").right()
t = r.find("1409221567852-3.png")
click(t)
sleep(2)
type("d" + "d" + "d" + "d" + "d" + "d" + "d" + Key.ENTER)
sleep(2)
r = find("1409221724099-3.png").right()
t = r.find("1409221737500-3.png")
click(t)
sleep(2)
type("w" + "w" + Key.ENTER)
sleep(2)
r = find("1409221954037-3.png").right()
t = r.find("1409222176787-3.png")
click(t)
sleep(2)
type("s" + Key.ENTER)
sleep(2)
r= find("1409147154037-3.png").nearby(10)
t = r.find("1409147186219-3.png")
click(t)
sleep(1)
click(t)
sleep(2)
type(Key.TAB)
sleep(1)
paste("brilliotest")
sleep(1)
type(Key.TAB)
sleep(1)
paste("brillio@123")
sleep(1)
type(Key.TAB + Key.TAB)
sleep(1)
paste("brillio@123")
sleep(1)
click("1409148604792-3.png")
while exists("1409148699671-3.png"):sleep(5)
while exists("1409148815960-3.png"):sleep(5)




