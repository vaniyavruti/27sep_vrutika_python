#     Write a Python program to read an entire text file.
     
#open('test.txt','x')
fl = open('test.txt','r')
print(fl.read())
fl.write("hello python!")
fl.write('one')
fl.write('two')
fl.write('three')
fl.write('four')
fl.write('five')
fl.write('six')
fl.write('seven')
fl.write('eight')
fl.write('nine')
fl.close()


"""def fread(fname):
        txt = open(fname)
        print(txt.read())
fread('test.txt') """