
class PythonMSSQLParser(object):

    def __init__(self):
        self.first_line = "Date,Source,Severity,Message"
        self.line_filter = "Login failed for user"
        self.source_ips = set()
 
    def parse(self,file_handle):
        parsed_lines = list()
        lines = file_handle.readlines()
        if lines[0].strip() != self.first_line:
            error = ["Error Parsing File\n"]
            return error
        for line in lines:
            if (self.line_filter) in line:
                start_index = line.index("[")
                end_index = line.index("]")
                ip_address = line[start_index+8:end_index].strip()
                self.source_ips.add(ip_address)
                split_line = line
                split_line = split_line.replace(","," ").split(" ")
                date = split_line[0]
                time = split_line[1]
                user_name = split_line[8]
                delimiter = " "
                sequence = (date,time,user_name,ip_address)
                line = delimiter.join(sequence)
                parsed_lines.append(line + "\n")
        return parsed_lines