
#!/usr/bin/python3

def CutString(line, ref, end='</div>'):
    if (ref == 'a href') : 
        ref = '<' + ref
        end = '</a>'
    if (ref == 'img') : 
        ref = '<' + ref
        end = '</img>'
    try:
        if line.find(ref) > -1:
            for chr in range(line.find(ref), len(line), +1):
                if (line[chr:chr+len(ref)] is ref):
                    line = line.replace(line[chr:line.find(end, chr)+len(end)], '')
        return line.strip()
    except:
        pass
def StringCount(line, string):
    line, count = line + ' ', 0
    for chr in range(0, len(line), +1):
        if (line[chr:chr+len(string)] is string and line[chr+1:chr+1+len(string)] is ' '): count = count + 1
    return count
