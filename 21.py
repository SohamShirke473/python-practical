# Base Class
class Vehicle:
    p=0
    def __init__(self,vt,rp):
        self.vt =vt
        self.rp=rp
    def VA(self):
        print(f"The available {self.vt} are {self.stock} with rent of Rs {self.rp} per day of {self.agency} agency")
        
# Derived CLass
class rentalagencies(Vehicle):
    def __init__(self,agency,vt,rp):
        self.agency = agency
        Vehicle.__init__(self,vt,rp)
    def Rentalperiod(self):        
        p=int(input("Enter the period"))
        return (p)
        
# Derived Class
class rentaltransition(rentalagencies):
    def __init__(self,agency,vt,stock,rp):
        self.stock=stock        
        rentalagencies.__init__(self,agency,vt,rp)
    def pb(self,p1,price,number):
        self.p1=p1
        self.price=price
        self.number=number
        amount=self.p1*self.price*self.number
        return amount
print("                                  This is the application for CAR and Bus Rental System                  ")
print("----------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------")


nc=200
pc=25
nb=100
pb=50
d=0
i=1

while(i<=20):
      i=i+1
      
      while (True):
          if( i==25):
              
              break
          #print(f"Available number of Cars are {nc} with rent {pc} per day and number of Buses are {nb} with rent {pb} per day")
          #print("---------------------------------------------------------------------------------------------------------------------------------------------")
          print(" Please enter the choice as per the Menu")
          print(" 1:For rent the car, 2:For Rent the Bus  3:for Exit")
          choice=int(input("Enter the choice"))
                       
              
          
                               
          if choice==1:
                                      
            v1 = rentaltransition("star","Cars",nc,pc)
            v1.VA()
            d=int(input("Enter the number of cars"))       
            nc=nc-d
            p1=v1.Rentalperiod()
            #print("Available Cars = ",nc)
            am=v1.pb(p1,25,d)
            print(f"Your order for {d} Cars of Star agency  is booked.Please pay Rupees{am}")
            print("----------------------------------------------------------------------")
                                      
                                         

                            
                      
          elif choice == 2:
               
                v1 = rentaltransition("Royal","Bus",nb,pb)
                v1.VA()
                d=int(input("Enter the number of Bus"))
                nb=nb-d
                p1=v1.Rentalperiod()
               # print("Available Buses = ",nb)
                am=v1.pb(p1,25,d)
                print(f"Your order for {d} Buses of  Royal agency  is booked.Please pay Rupees{am}")
                print("----------------------------------------------------------------------")
                         
                               
                            
          elif choice == 3:
               print ("I am not interested")
               i=25
                
              
                              
                      
                                
             
                                

    
          
                
  

