import wpf , clr , os
import glob2
import codecs
clr.AddReference("System.Windows.Forms")
from System.Windows import Application, Window
from System.Windows.Forms import Form, OpenFileDialog, TextBox
from System.Windows.Forms import DockStyle ,MenuStrip, ToolStripMenuItem
from System.Windows.Forms import DialogResult , ScrollBars ,MessageBox
from System.Windows.Forms import MessageBoxButtons,MessageBoxIcon,MessageBoxDefaultButton
from System.Windows.Forms import FolderBrowserDialog, SaveFileDialog

class open_file_handle(object):
    
    def __init__(self,enc = "utf-8"):
        self.enc = enc
        self.file_list = list()
        self.filter = "TXT files (*.txt)|*.txt|LOG files (*.log)|*.log"
        pass

    def Open_File_dialog(self):
        """description of class"""
        dialog = OpenFileDialog()
        dialog.Filter = self.filter
        if dialog.ShowDialog() == DialogResult.OK:
            self.file_list.append(dialog.FileName)
            return True
        return False

    def open(self):
        if not self.file_list:
            return False
        f = self.file_list.pop()
        return codecs.open(f,'r',encoding=self.enc)

    def Save_File_dialog(self):
        dialog = SaveFileDialog()
        dialog.Filter = self.filter
        if dialog.ShowDialog() == DialogResult.OK:
            return open(dialog.FileName,"w+")
        return False

    def Folder_Browser_dialog(self,suffix):
        dialog = FolderBrowserDialog()
        if dialog.ShowDialog() == DialogResult.OK:
            folder = str(dialog.SelectedPath) +"\\**\\"
            files = glob2.glob(folder + suffix) #ex '*.log'
            for f in files:
                self.file_list.append(f)
            return True
        return False