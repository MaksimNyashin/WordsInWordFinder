st = set()
stwords = []
def main():
    def stword():
        import codecs
        with codecs.open("russian.txt", "r", "utf-8") as stream:
            global stwords
            stwords = list(stream.read().split('\n'))
            stream.close()

    stword()
    def gen(s, m):
        def genLen(l, s, m):
            def get_perm(a, r, m, h, l):
                def wrt(s):
                    global st
                    if s not in st and s in stwords:
                        print(s)
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

        if len(m) < 3:
            for i in range(3, len(s) + 1):
                genLen(i, s, m)
        else:
            genLen(len(m), s, m)

    try:
        while True:
            b = 0
            s = input("Слово: ")
            try:
                while True:
                    if b == 1:
                        print("Слово: " + s)
                    b = 1
                    m = input("Маска: ")
                    gen(s, m)
            except KeyboardInterrupt:
                continue
    except KeyboardInterrupt:
        return

main()
