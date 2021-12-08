def brokendisplay():
    f = open("input day 8.txt", "r")
    lines = f.readlines()
    delim = '|'
    totalcodes = []
    totaleasynumbers = 0
    for line in lines:
        codes = []
        index = line.index(delim)
        if lines.index(line) is not len(lines) - 1:
            line = line[:-1]
        line = line[index + 2:]

        for code in line.split(' '):
            codes.append(code)
        totalcodes.append(codes)

    for code in totalcodes:
        for number in code:
            if len(number) == 2 or len(number) == 3 or len(number) == 4 or len(number) == 7:
                totaleasynumbers += 1
    print(line)
    print(codes)
    print(totalcodes)
    print(totaleasynumbers)

def decodeDisplay():
    f = open("input day 8.txt", "r")
    lines = f.readlines()
    delim = '|'
    totalcodes = []
    totaaloutput = []
    for line in lines:
        delimvlag = 0
        codeinline = []
        inputnumbers = []
        outputnumbers = []
        if line[-1] == '\n':
            line = line[:-1] #remove last \n
        allnumbers = line.split(' ')
        for number in allnumbers:
            if number == delim:
                delimvlag = 1
            if delimvlag == 0:
                inputnumbers.append(number)
            if delimvlag == 1 and number != delim:
                outputnumbers.append(number)

        codeinline.append(inputnumbers)
        codeinline.append(outputnumbers)
        totalcodes.append(codeinline)

    for codeline in totalcodes:
        nummers = ['', '', '', '', '', '', '', '', '', '']
        output = []
        for code in codeline[0]:
            if len(code) == 2:
                een = set(code)
                nummers[1] = code
            if len(code) == 3:
                zeven = set(code)
                nummers[7] = code
            if len(code) == 4:
                vier = set(code)
                nummers[4] = code
            if len(code) == 7:
                acht = set(code)
                nummers[8] = code
        for code in codeline[0]:
            if len(code) == 5 and een.issubset(set(code)):
                drie = set(code)
                nummers[3] = code
            if len(code) == 6 and een.issubset(set(code)) is False:
                zes = set(code)
                nummers[6] = code
        linksonder = acht.copy()
        linksonder = acht.difference(drie)
        linksboven = linksonder.intersection(vier)
        linksonder = linksonder.difference(vier)
        for code in codeline[0]:
            if len(code) == 6 and linksonder.issubset(set(code)) and een.issubset(set(code)):
                nul = set(code)
                nummers[0] = code
            if len(code) == 6 and set(code) == acht.difference(linksonder):
                negen = set(code)
                nummers[9] = code
            if len(code) == 5 and linksonder.issubset(set(code)):
                twee = set(code)
                nummers[2] = code
            if len(code) == 5 and linksboven.issubset(set(code)):
                vijf = set(code)
                nummers[5] = code
        for outputnummer in codeline[1]:
            for nummer in nummers:
                if len(set(nummer).symmetric_difference(set(outputnummer))) == 0:
                    output.append(str(nummers.index(nummer)))
        outputstring = "".join(output)
        totaaloutput.append(int(outputstring))
    print(sum(totaaloutput))









