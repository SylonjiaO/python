# A Simple Calculation
while(True):
    try:

        firstno=int(input("Enter the First Number:"))
        secondno=int(input("Enter the Secocnd Number: "))
        result=firstno/(secondno -3)
        print("Total = %.2f"%result)
        break
    except ValueError:
         print("Sorry... Only Numbers")
         continue
    except ZeroDivisionError:
         print("Sorry... Only Numbers greater/less than 3")
         continue
    except MemoryError:
        print("Not Enough Memory")
        break
    except IOError:
        print("Sorry..Hardware Failure..")
        break
    except: #Common Exception Handler
        print("Sorry Something Wrong Occured...")
        continue

    finally:
        print("Thanks, This is the end of this program")
        
