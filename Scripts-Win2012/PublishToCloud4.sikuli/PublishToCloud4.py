openApp("C:\\Program Files (x86)\\JetBrains\\IntelliJ IDEA Community Edition 13.1.4\\bin\\idea.exe")
while exists("1411974135231.png"):sleep(3)
wait("1412059467913.png",60)
click("1411979652430.png")
wait("1411979758494.png",10)
click("1411979962588.png")
wait("1411980017234.png",10)
click("1411980141650.png")
wait("1411980179375.png",5)
sleep(1)
type(Key.BACKSPACE)
sleep(1)
projectName = "sample"
paste(projectName)
click("1411980213677.png")
wait("1411980595307.png",10)
wait("1411980679764.png",150)
sleep(5)
click("1411982068953.png")
while not exists("1411982297134.png"): click("1412066247357.png")
sleep(2)
azureProject = "AzureProject"
paste(azureProject)
sleep(2)
click("1411982409547.png")
wait("1411983856705.png",10)
r = find("1411994847155.png")
t = r.find("1411994663496.png").nearby(10)
click(t)
sleep(2)
click(t)
sleep(2)
click("1411984316571.png")
while not exists("1411984446737.png"):click("1411984316571.png")
sleep(2)
JDKPath = "C:\\Program Files\\Java\\jdk1.7.0_65"
paste(JDKPath)
sleep(2)
click("1411984634578.png")
wait("1411984707247.png",10)
click("1412084026670.png")
sleep(2)
type(Key.TAB)
JDKBlobPath = "https://3rdpartyjdkstorage.blob.core.windows.net/eclipsedeploy/jdk1.6.0_34.zip"
paste(JDKBlobPath)
sleep(2)
click("1411984764023.png")
wait("1411984829944.png",10)
r = find("1411995242878.png")
t = r.find("1411984939990.png").nearby(10)
click(t)
sleep(1)
click("1411985049534.png")
while not exists("1411985084998.png"):click("1411985049534.png")
sleep(2)
serverPath = "C:\\EclipseAzureJDT\\JavaServers\\glassfish4\\glassfish4"
paste(serverPath)
sleep(2)
click("1411985219323.png")
wait("1411985675760.png",10)
sleep(2)
click("1411985728288.png")
wait("1411986725410.png",10)
click("1411986746838.png")
wait("1411986817920.png",10)
click("1411986849364.png")
sleep(2)
warFilePath = "C:\WarFile\sample_warexploded.war"
paste(warFilePath)
click("1411987004420.png")
wait("1411987095258.png",10)
click("1411987161666.png")
wait("1411987272968.png",40)
click("1411992707288.png")
sleep(2)
type(Key.ENTER)
sleep(2)
type(Key.DOWN + Key.DOWN)
sleep(2)
click("1411992827521.png")
while not exists("1411992886505.png"):click("1412083738747.png")
click("1411992911799.png")
wait("1411992947046.png",10)
click("1411992972888.png")
while not exists("1411992999160.png"):click("1411992972888.png")
sleep(2)
publishSetting = "C:\PublishSetting\CollaberaInteropTest-9-29-2014-credentials.publishsettings"
paste(publishSetting)
sleep(2)
click("1411993641567.png")
wait("1411993695701.png",10)
click("1411993725293.png")
while exists ("1411997470257.png"): sleep(5)
sleep(2)
wait("1411997578525.png",10)
sleep(5)
r = find("1412049723172.png").right(900)
t = r.find("1412049886955.png")
click(t)
sleep(2)
type("b" + Key.ENTER)
sleep(2)
r = find("1412055068368.png").right()
t = r.find("1412055082980.png")
click(t)
sleep(2)
type("d" + "d" + "d" + "d" + "d" + "d" + "d" + Key.ENTER)
sleep(2)
sleep(2)
r = find("1412067378055.png").right()
t = r.find("1412067428577.png")
click(t)
sleep(2)
type("w" + "w" + Key.ENTER)
sleep(2)

sleep(2)
r = find("1412067557140.png").right()
t = r.find("1412067719550.png")
click(t)
sleep(2)
type("s" + Key.ENTER)
sleep(2)
r= find("1411998073837.png").nearby(10)
t = r.find("1411998097066.png")
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
click("1411998169888.png")




