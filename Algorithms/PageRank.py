class Page(object):
    def __init__(self):
        self.__outbound = []
        self.__inbound = []
        self.__PR = 1

    def addLinks(self, pages):
        for page in pages:
            page.addInbound(self)
            self.__outbound.append(page)

    def addInbound(self, page):
        self.__inbound.append(page)

    def getOutNum(self):
        return len(self.__outbound)

    def getInNum(self):
        return len(self.__inbound)

    def getInbound(self):
        return self.__inbound

    def setPR(self, PR):
        self.__PR = PR
    
    def getPR(self):
        return self.__PR


a = Page()
b = Page()
c = Page()
d = Page()

a.addLinks([b])
b.addLinks([a, c])
c.addLinks([a])
d.addLinks([c])

dampener = 0.85

def getPR(page):
    mult = 0
    for i in page.getInbound():
        mult += i.getPR() / i.getOutNum()
    return (1-dampener) + (dampener * mult)

for i in range(0, 100):
    if abs(getPR(a) - a.getPR()) < 0.0001 and abs(getPR(b) - b.getPR()) < 0.0001 and abs(getPR(c) - c.getPR()) < 0.0001 and abs(getPR(d) - d.getPR()) < 0.0001:
        i = 101
    else:
        a.setPR(getPR(a))
        b.setPR(getPR(b))
        c.setPR(getPR(c))
        d.setPR(getPR(d))

        print(round(a.getPR(), 4), " ", round(b.getPR(), 4), " ", round(c.getPR(), 4), " ", round(d.getPR(), 4))
    
    
