class JustCounter:
    __privateCount = 0
    _protectedCount = 1

    def count(self):
        JustCounter.__privateCount += 1
        print("JustCounter.__privateCount :",JustCounter.__privateCount)
        JustCounter._protectedCount+=1
        print("JustCounter._protectedCount :",JustCounter._protectedCount)



counter = JustCounter()
counter.count()
counter.count()
# print("Hai",JustCounter.__privateCount)
print("Hai",JustCounter._protectedCount)