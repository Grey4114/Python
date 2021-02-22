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

    download_LinkText = (By.XPATH, "//a[text()='File Download']")
    download_Header = (By.XPATH, "//h3[text()='File Download']")

    # todo - TextFile1 path
    download_TextFile1 = (By.XPATH, "")
    # todo - TextFile2 path
    download_TextFile2 = (By.XPATH, "")
    # todo - PNGFile1 path
    download_PNGFile1 = (By.XPATH, "")
    # todo - PNGFile2 path
    download_PNGFile2 = (By.XPATH, "")
    # todo - PNGFile3 path
    download_PNGFile3 = (By.XPATH, "")
    # todo - XLSMFile path
    download_XLSMFile = (By.XPATH, "")
    # todo - UploadFile path
    download_UploadFile = (By.XPATH, "")


    def fileDownload_Link(self):
        return self.driver.find_element(*FileDownloadPage.download_LinkText)

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

    def fileDownload_UploadFile(self):
        return self.driver.find_element(*FileDownloadPage.download_UploadFile)


    """    
    hello_world.txt
    some - file.txt
    buy.jpg
    zloty-bills-922x614.jpg
    8q6s1bvaf6hanudbqd4a12fj44-457e5522dd50b21f78ec95e0a268043e.png
    CloudSauceLab.xlsm
    TestUploadPage.txt
    """
