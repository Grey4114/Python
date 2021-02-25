"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intentpage
"""

from selenium.webdriver.common.by import By


class FileDownloadPage:
    def __init__(self, driver):
        self.driver = driver

    download_Link = (By.XPATH, "//a[text()='File Download']")       # Main Page link
    download_Header = (By.XPATH, "//h3[text()='File Downloader']")        # Page header text

    download_TextFile1 = (By.XPATH, "//a[@href='download/Hello.docx']")                 # Text File 1
    download_TextFile2 = (By.XPATH, "//a[@href='download/upload_file.xlsx']")           # Text File 2
    download_PNGFile1 = (By.XPATH, "//a[@href='download/Colbyashi Maru - Khaled Garbaya - Social.jpg']")    # PNG File
    download_PNGFile2 = (By.XPATH, "//a[@href='download/luminoslogo.png']")            # PNG File 2
    download_PNGFile3 = (By.XPATH, "//a[@href='download/some-file.txt']")               # PNG File 3
    download_XLSMFile = (By.XPATH, "//a[@href='download/Testphoto.jpg']")               # XLSM File



    def fileDownload_LinkText(self):
        return self.driver.find_element(*FileDownloadPage.download_Link)

    def fileDownload_HeaderText(self):
        return self.driver.find_element(*FileDownloadPage.download_Header)

    def fileDownload_TextFile_1(self):
        return self.driver.find_element(*FileDownloadPage.download_TextFile1)

    def fileDownload_TextFile_2(self):
        return self.driver.find_element(*FileDownloadPage.download_TextFile2)

    def fileDownload_PNGFile_1(self):
        return self.driver.find_element(*FileDownloadPage.download_PNGFile1)

    def fileDownload_PNGFile_2(self):
        return self.driver.find_element(*FileDownloadPage.download_PNGFile2)

    def fileDownload_PNGFile_3(self):
        return self.driver.find_element(*FileDownloadPage.download_PNGFile3)

    def fileDownload_XLSMFile(self):
        return self.driver.find_element(*FileDownloadPage.download_XLSMFile)


