#Write a Python program to append text to a file and display the text. 

fl= open('test.txt','a')
fl.write("\n ten")
fl.close()


"""f1.write('id')
f1.write('Name')
f1.write('Subject')
f1.write(f"\nid:{1}\nName:{'Dip'}\nSubject:{'Python'}")   """





""" def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("Python Exercises\n")
                myfile.write("Java Exercises")
        txt = open(fname)
        print(txt.read())
file_read('abc.txt')
  """