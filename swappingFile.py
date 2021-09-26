def swapFileData():
    fileName_1 = input("Enter your 1st file name")
    with open(fileName_1, 'r') as a:
        data_a = a.read()

    fileName_2 = input("Enter your 2nd file here")
    with open(fileName_2, 'r') as b:
        data_b = b.read()


    with open(fileName_1, 'w') as a:
        a.write(data_b)
    
    with open(fileName_2, 'w') as b:
        b.write(data_a)
   

    print()
    a.close()
    b.close()
    

swapFileData()