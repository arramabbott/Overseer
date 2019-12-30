
class PythonFirewallParser(object):
    
    def __init__(self):
        self.first_line = "#Version: 0.1.5"
        self.source_ips = set()
        self.access_list = [
            '127.0.0.1'
            ]
        self.ips = {'137':set(),'139':set(),'1433':set(),'3389':set(),'5789':set()}

    def parse(self,file_handle):
        line_num = 0
        lines = file_handle.readlines()
        if lines[0].strip() != self.first_line:
            error = ["Error Parsing File\n"]
            return error
        for line in lines:
            line_num += 1
            if line_num > 5:    
                current_line = line.split(' ')
                dst_ip = str(current_line[5])
                dst_port = str(current_line[7])
                if dst_port in self.ips:
                    self.source_ips.add(dst_ip)
                    self.ips[dst_port].add(dst_ip)
        return self._print_to_list()

    def _print_to_list(self): 
        parsed_lines = list()
        for port in self.ips.keys():
            parsed_lines.append("Port "+port+":\n")
            for ip in self.ips[port]:   
                if ip in self.access_list:
                    parsed_lines.append("\t"+ip+"\t(access)\n")
                else:
                    parsed_lines.append("\t"+ip+"\n")  
        return parsed_lines
