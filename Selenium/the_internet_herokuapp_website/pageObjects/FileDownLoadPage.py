"""
Website:  https://the-internet.herokuapp.com/download
Created:  2/14/2021
Notes:
    Connected Test Object Script - /tests/test_Page_FileDownload.py

    ** All the files in the C:/Users/chris_000/Downloads directory will be deleted
"""

from selenium.webdriver.common.by import By


class FileDownloadPage:
    def __init__(self, driver):
        self.driver = driver

    download_Link = (By.XPATH, "//a[text()='File Download']")               # Main Page link
    download_Header = (By.XPATH, "//h3[text()='File Downloader']")          # Page header text
    download_Files = (By.XPATH, "//a[contains(@href,'download')]")          # File List


    def fileDownload_LinkText(self):
        return self.driver.find_element(*FileDownloadPage.download_Link)

    def fileDownload_HeaderText(self):
        return self.driver.find_element(*FileDownloadPage.download_Header)

    def fileDownload_FileList(self):
        return self.driver.find_elements(*FileDownloadPage.download_Files)


