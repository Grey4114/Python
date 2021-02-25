"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
    ** Mae sure the C:/Users/chris_000/Downloads  directory is empty before running this script
"""
import os
import os.path
from os import path
import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.FileDownLoadPage import FileDownloadPage

class TestFileDownload(BaseClass):

    def test_file_download(self):
        # Enter the Page
        log = self.getLogger()
        fileDownload_page = FileDownloadPage(self.driver)
        log.info("TEST START")
        fileDownload_page.fileDownload_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/download"
        log.info("URL: " + url)


        # Verify the Header
        header_text = fileDownload_page.fileDownload_HeaderText().text
        assert ("File Downloader" in header_text)
        log.info("Header: " + header_text)


        # Download all files
        fileDownload_page.fileDownload_TextFile_1().click()     # Download text file 1
        fileDownload_page.fileDownload_TextFile_2().click()     # download text file 2
        fileDownload_page.fileDownload_PNGFile_1().click()      # download png file 1
        fileDownload_page.fileDownload_PNGFile_2().click()      # download png file 2
        fileDownload_page.fileDownload_PNGFile_3().click()      # download png file 3
        fileDownload_page.fileDownload_XLSMFile().click()       # download xmsl file
        fileDownload_page.fileDownload_ZipFile().click()        # download zip file


        # Verify all files downloaded
        pathDir = "C:/Users/chris_000/Downloads"
        os.chdir(pathDir)
        assert path.isfile("Hello.docx")
        assert path.isfile("upload_file.xlsx")
        assert path.isfile("Colbyashi Maru - Khaled Garbaya - Social.jpg")
        assert path.isfile("luminoslogo.png")
        assert path.isfile("some-file.txt")
        assert path.isfile("Testphoto.jpg")
        log.info("Downloads: Passed")


        # todo - add code to delete all files in the downloads directory


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



