from zipfile import ZipFile
path = "C:\\Users\\neiln\\Downloads\\11_B613SelfieCameraNewVersion_v1.7_apkpure.com_source_from_JADX.apk.zip"

print(str(path).split('\\')[4].split('.apk')[0])
with ZipFile(path, 'r') as zipObj:
    listOfFileNames = zipObj.namelist()
    for fileName in listOfFileNames:
        if str(fileName)==('AndroidManifest.xml'):
            app_zip_name = str(path).split('\\')[4].split('.')[0]
            print("equals with ", app_zip_name+fileName)
        elif str(fileName).endswith('AndroidManifest.xml'):
            print(fileName)
            app_zip_name = str(path).split('\\')[4].split('.')[0] + str(fileName).split('/')[2]
            print("ends with ",app_zip_name)
        elif str(fileName).startswith('AndroidManifest.xml'):
            print("starts with ", fileName)
