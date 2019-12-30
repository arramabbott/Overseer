
class PythonIISParser(object):

    def __init__(self):
        self.first_line = "#Software: Microsoft Internet Information Services 7.5"
        self.source_ips = set()
        self.allowed = []

    def parse(self,file_handle):
        parsed_lines = list()
        lines = file_handle.readlines()
        if lines[0].strip() != self.first_line:
            error = ["Error Parsing File\n"]
            return error
        for line in lines:
            bad_request = True
            for community in self.allowed:
                if community in line:
                    bad_request = False
                    break
            if bad_request:
                line = line.split(" ")

                date       = line[0]
                time       = line[1]
                method     = line[4]
                query      = line[5]
                source_ip  = line[9]
                user_agent = line[10]
                status     = line[11]

                delimiter = " "
                sequence = (date,time,method,query,source_ip,user_agent,status)
                line = delimiter.join(sequence)
                parsed_lines.append(line+"\n")
                self.source_ips.add(source_ip)
        return parsed_lines
