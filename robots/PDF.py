import sys
import os


class PDF(object):
    def pdf(self, docx):
        sofficepath = 'soffice'
        convertcmd = '%s --headless --convert-to pdf %%s' % sofficepath
        os.popen(convertcmd % docx)
