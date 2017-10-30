#!/usr/bin/python3

def CutString(line, ref, end='</div>'):
    if (ref == 'a href') : 
        ref = '<' + ref
        end = '</a>'
    if (ref == 'img') : 
        ref = '<' + ref
        end = '</img>'
    if (ref == 'span'):
        ref = '<' + ref
        end = '</span>'
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
        if line[chr:chr+len(string)] == string and line[chr:chr+len(string)+1] == string + ' ': 
            count = count + 1
    return count
def StringReplaceAll(string, old, new):
    newText = ''
    for chr in string.split(' '):
        if chr == old: newText = newText + new + ' '
        else: newText = newText + chr + ' '
    return newText
"""string = 'test beta deneme beta'
print(StringCount(line, 'beta'))
print(StringReplaceAll(string, 'beta', 'replace' ))
"""
