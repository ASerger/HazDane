# template from https://towardsdatascience.com/how-to-download-an-image-using-python-38a75cfa21c
from os import write
import requests # to get image from the web
import shutil # to save it locally

class DownloadImages():
    def ByFileList(localFileList = 'cleanedUrls.txt'):
        ## Set up the image URL and filename
        # image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"
        baseFileName = "images/raw/image__"
        fileNumber = 0

        with open(localFileList, 'r') as file:
            for image_url in file:
                fileNumber = fileNumber + 1
                # Open the url image, set stream to True, this will return the stream content.
                r = requests.get(image_url.strip(), stream = True)
                # Check if the image was retrieved successfully
                if r.status_code == 200:
                    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                    r.raw.decode_content = True
                    fileName = f'{baseFileName}{fileNumber}.jpg'

                    # Open a local file with wb ( write binary ) permission.
                    with open(fileName,'wb') as f:
                        shutil.copyfileobj(r.raw, f)

                    print('Image sucessfully Downloaded: ', fileName)
                else:
                    print('Image Couldn\'t be retreived')


DownloadImages.ByFileList()