while True:
    acronym = []
    sentence = input('請輸入一段英文句子：')
    if sentence == 'q' or sentence == 'Q':
        break
    else:   
        txt = sentence.split(' ')
        for line in txt:
            acronym.append(line[0])
    print ('The acronym is: ', acronym)
