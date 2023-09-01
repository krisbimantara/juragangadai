def rupiah_format(angka):
    rev1 = str(angka)
    rev = rev1[::-1]
    rev2= ''
    i=0
    while i < len(rev):
        rev2 += rev[i]
        if (i+1) % 3 == 0 and i != (len(rev)-1) and rev[i] !='.':
            rev2 += '.'
        if rev[i]=='.':
            rev2 += ';,'
        i+=1
    return 'Rp. ' + rev2[::-1].replace(';.','')
