class Singleton(object):
    ans = None

    @staticmethod
    def instance():
        if '_instance' not in Singleton.__dict__:
            print ("Instance does not exist. Creating.")
            Singleton._instance = Singleton()
        else:
            print ("Instance already exists. Not creating")
        return Singleton._instance


a1 = Singleton.instance()
a2 = Singleton.instance()

assert a1 is a2

a1.ans = 1
print ("See if a2 has the same property value of a1 after set")
print (f"   a1.ans={a1.ans}")
print (f"   a2.ans={a2.ans}")

assert a1 is a2
print (f"   testing equality Passed")