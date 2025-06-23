import os
import datetime
from generator.qr_creator import QrCodeCreator
def handleFile(filePath : str):

    with open(filePath,'r',encoding='utf-8') as fs:
        data = fs.read().splitlines()
        for text in data:
            today = datetime.datetime.now()
            formatingDate = today.strftime('%Y-%m-%d')
            qrCode=QrCodeCreator(text)
            qrCode.save(f'./data/qrcodes/{text}_{formatingDate}.png')

if __name__ == "__main__":
    fileName =  input('Enter the file name ')
    if not os.path.exists("./file"):
        os.mkdir('file')
    else:
       handleFile(filePath=f'./file/{fileName}')
