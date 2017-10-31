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
                if (line[chr:chr+len(ref)] == ref):
                    line = line.replace(line[chr:line.find(end, chr)+len(end)], ' ')
        return line.strip()
    except:
        pass
def StringCount(line, string):
    line, count = line + ' ', 0
    for chr in range(0, len(line), +1):
        if line[chr:chr+len(string)] == string and line[chr:chr+len(string)+1] == string + ' ': 
            count = count + 1
    return count
def GetCut(line, ref, end='</div>'):
    for ch in range(len(line), -1, -1):
        if line[ch:ch+len(ref)] == ref:
            return line[ch+len(ref):len(line)-len(end)-1]
def StringReplaceAll(string, old, new, newText=''):
    for chr in string.split(' '):
        if chr == old: newText = newText + new + ' '
        else: newText = newText + chr + ' '
    return newText


line = 'test beta beta deneme <title> bu bir başlıktır </title> '

print('CutString', CutString(line, '<title>', '</title>'))

print('StringCount', StringCount(line, 'beta'))

print('StringReplaceAll', StringReplaceAll(line, 'beta', 'replace' ))

print('GetCut', GetCut(line, '<title>', '</title>'))


