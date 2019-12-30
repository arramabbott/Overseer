
import wpf , clr , os
import codecs
clr.AddReference("System.Windows.Forms")
from System.Windows import Application, Window
from System.Windows.Forms import Form, OpenFileDialog, TextBox
from System.Windows.Forms import DockStyle ,MenuStrip, ToolStripMenuItem
from System.Windows.Forms import DialogResult , ScrollBars ,MessageBox
from System.Windows.Forms import MessageBoxButtons,MessageBoxIcon, MessageBoxDefaultButton
from System.Windows.Forms import FolderBrowserDialog, SaveFileDialog
import open_file_handle
import PythonIISParser
import PythonMSSQLParser
import PythonFirewallParser
import PyKMLWriter

class MyWindow(Window):
    
    def __init__(self):
        wpf.LoadComponent(self, 'PyOverseer.xaml')

    def IIS_File_Click(self, sender, e):
        parser = PythonIISParser.PythonIISParser()
        file_handler = open_file_handle.open_file_handle()
        if not file_handler.Open_File_dialog():
            return
        result = self.print_to_outfile(file_handler,parser)

    def IIS_Folder_Click(self, sender, e):
        parser = PythonIISParser.PythonIISParser()
        file_handler = open_file_handle.open_file_handle()
        if not file_handler.Folder_Browser_dialog('*.log'):
            return
        result =self.print_to_outfile(file_handler,parser)

    def MSSQL_File_Click(self, sender, e):
        parser = PythonMSSQLParser.PythonMSSQLParser()
        file_handler = open_file_handle.open_file_handle("utf-16")
        if not file_handler.Open_File_dialog():
            return
        result =self.print_to_outfile(file_handler,parser)

    def MSSQL_Folder_Click(self, sender, e):
        parser = PythonMSSQLParser.PythonMSSQLParser()
        file_handler = open_file_handle.open_file_handle("utf-16")
        if not file_handler.Folder_Browser_dialog('*.log'):
            return
        result =self.print_to_outfile(file_handler,parser)

    def Firewall_File_Click(self, sender, e):
        parser = PythonFirewallParser.PythonFirewallParser()
        file_handler = open_file_handle.open_file_handle()
        if not file_handler.Open_File_dialog():
            return
        result =self.print_to_outfile(file_handler,parser)

    def Firewall_Folder_Click(self, sender, e):
        parser = PythonFirewallParser.PythonFirewallParser()
        file_handler = open_file_handle.open_file_handle()
        if not file_handler.Folder_Browser_dialog('*.txt'):
            return
        result =self.print_to_outfile(file_handler,parser)

    def print_to_outfile(self,file_handler,parser):
        parsed_files = []
        parsed_data = []
        while True:
            in_file = file_handler.open()
            if in_file is not False:
                file_name = in_file.name.split("\\")[-1]
                parsed_data.append("\n********  "+file_name+"  ********\n")
                parsed_data += parser.parse(in_file)
                parsed_files.append(file_name)
                in_file.close()
            else:
                break
        save_handle = file_handler.Save_File_dialog()
        if save_handle is False:
            return False
        for parsed_line in parsed_data:
            save_handle.write(parsed_line)
        self.outputBox.AppendText("The following files have been parsed:\n")
        for file_name in parsed_files:
            self.outputBox.AppendText(file_name+"\n")
        self.outputBox.AppendText("Total lines: "+str(len(parsed_data))+"\n")
        self.outputBox.AppendText("Written to: "+save_handle.name+"\n")
        if hasattr(parser, 'source_ips'):
            kmlWriter = PyKMLWriter.PyKMLWriter()
            kmlWriter.write(parser.source_ips)
            self.outputBox.AppendText("Source Ips:\n")
            for ip in parser.source_ips:
                self.outputBox.AppendText(ip +"\n")
        save_handle.close()
        os.startfile(save_handle.name)
        return parsed_data

    def OnExit(self, sender, e):
        self.Close()

if __name__ == '__main__':
    Application().Run(MyWindow())
