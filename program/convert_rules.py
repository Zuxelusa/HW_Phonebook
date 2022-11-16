def CSV(line):
    if line == "\n": line = ""
    else:
        line = line.replace(";", ";")
    return line

def HTML(line):
    if line == "\n": line = ""
    else:
        line = "<tr color:><td>" + line.replace(";", "</td><td>") + "</td></tr>\n"
    return line