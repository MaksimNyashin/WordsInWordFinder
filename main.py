st = set()
stwords = []
uswords = []
nused = []
def main():
    def stWords():
        import codecs
        with codecs.open("russian.txt", "r", "utf-8") as stream:
            global stwords
            stwords = list(stream.read().split('\n'))
            stream.close()
            
    def usWords():
        import codecs
        with codecs.open("used.txt", "r", "utf-8") as stream:
            global uswords
            uswords = list(stream.read().split('\n'))
            stream.close()

    def wrtUsed():
        import codecs
        with codecs.open("used.txt", "w", "utf-8") as stream:
            global uswords
            stream.write("\n".join(uswords))
            stream.close()

    stWords()
    usWords()
    def gen(s, m):
        def genUsed(s):
            def wrt(s):
                if s in uswords:
                    print(s)
                    global st
                    st.add(s)
                    return
            global uswords
            print()
            for w in sorted(uswords, key=lambda s: (-len(s), s)):
                cnt = 1
                for i in range(32):
                    #if w == "пень":
                        #print(chr(i + ord('а')), w.count(chr(i + ord('а'))), s.count(chr(i + ord('а'))))
                    if w.count(chr(i + ord('а'))) > s.count(chr(i + ord('а'))):
                        cnt = 0
                if cnt == 1:
                    wrt(w)
                        
        
        def genLen(l, s, m):
            def get_perm(a, r, m, h, l):
                def wrt(s):
                    global st
                    if s in st:
                        return
                    if s in uswords:
                        print(s)
                        st.add(s)
                        return
                    if s in stwords:
                        global nused
                        nused.append(s)
                        #print(nused)
                        #print(s)
                        st.add(s)
    
                if h == l:
                    if m == '':
                        wrt("".join(a[i] for i in r))
                    else:
                        b = 1
                        for i in range(l):
                            if m[i] != '*' and m[i] != a[r[i]]:
                                b = 0
                                break
                        if b == 1:
                            wrt("".join(a[i] for i in r))
                    return
                if h > 0:
                    try:
                        if m[h - 1] != '*' and a[r[-1]] != m[h - 1]:
                            return
                    except IndexError:
                        print(a, r, m, h, l)
                        exit(0)
                for i in range(len(a)):
                    if i in r:
                        continue
                    b = 1
                    if b == 1:
                        get_perm(a, r + [i], m, h + 1, l)

            st.clear()
            a = sorted(list(s))
            msk = list(m)
            get_perm(a, [], m, 0, l)

        if len(m) == 0:
            #for i in range(3, len(s) + 1):
                #genLen(i, s, '*' * i)
            genUsed(s)
        elif len(m) > 2:
            genLen(len(m), s, m)

    global uswords
    try:
        while True:
            b = 0
            s = input("Слово: ")
            if s.startswith("-а"):
                if s[3:] in stwords and s[3:] not in uswords:
                    uswords.append(s[3:])
                    wrtUsed()
                continue
            if s.startswith("-все"):
                stWords()
                continue
            if s.startswith("-юз"):
                usWords()
                continue
                    
            try:
                while True:
                    if b == 1:
                        print("Слово: " + s)
                    b = 1
                    m = input("Маска: ")
                    if m.startswith("-а"):
                        if m[3:] in stwords and m[3:] not in uswords:
                            uswords.append(m[3:])
                            wrtUsed()
                        continue
                    global nused
                    nused = []
                    try:
                        gen(s, m)
                        if len(nused) != 0:
                            print("\n" + "\n".join(nused))
                    except KeyboardInterrupt:
                        continue
                    while 1 == 1 and len(m) != 0:
                        word = input("Ответ: ")
                        if word in nused and word not in uswords:
                            uswords.append(word)
                            wrtUsed()
                            break
                        if word.startswith("-а"):
                            if word[3:] in nused and word[3:] not in uswords:
                                uswords.append(word[3:])
                                wrtUsed()
                            continue
                        break
            except KeyboardInterrupt:
                print()
                continue
    except KeyboardInterrupt:
        return

main()
