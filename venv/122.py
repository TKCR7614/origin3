print("Welcome to the seat-booking application of Burak757 passenger jets of The Apache airlines!")#Welcome words
print("Here is the the floor plan of the plane")#Show the floor plan of the plane to the customers.
#print the floor plan
print("1A 2A 3A 4A    78A 77A 79A 80A")
print("1B 2B 3B 4B    78B 77B 79B 80B")
print("1C 2C 3C 4C    78C 77C 79C 80C")
print("X  X  X  X     X   X   X   X")
print("1D 2D 3D 4D    S   S   79D 80D")
print("1E 2E 3E 4E    S   S   79E 80E")
print("1F 2F 3F 4F    S   S   79F 80F")
#something need to notice when booking a seat
print("Please note that The 'X' denotes the isles on the floor and the 'S' denotes storage area, no booking must be made on those spaces!")
#Store the seat number in a list
Seat = ['1A', '2A','3A','4A','78A','77A','79A','80A','1B','2B','3B','4B','78B','77B','79B','80B','1C','2C','3C','4C','77C','78C','79C','80C','1D','2D','3D','4D','79D','80D','1E',"2E",'3E','4E','79E','80E','1F','2F','3F','4F','79F','80F']
#Using a dictionary comprehension to store all the items that are in list into a dictionary as key, and all the value are 'F', because all the seats are available at first.
Seat1= {item:'F' for item in Seat}
def Show_booking_state():
    print(Seat1)#show Seat1 to show all the state of seats
    print('R indicates the seat is unavailable, and F indicates the seat is available ')#Some notices
def Book_a_seat():
    a=input("Please enter the seat number you want to book:")
    b=Seat1[a]
    if a in Seat is False:#If a is invalid
        print("Please enter a vaild seat number")
    elif a in Seat is True and b=='F':#a is valid and is an available seat
        h=input('please enter your passport number ')
        j=input('please enter your  first name')
        k=input('please enter your last name')
        Seat1[a]='h'+'j'+'k',a#change the value of chosen seat
        print('You have successfully booked'+a)
    elif a in Seat is True and b=='R':#a is valid but is an unavailable seat
        print('Sorry, this seat is unavailable')
def Free_a_seat():
    c=input('Please enter the seat you want to free')
    Seat1[c] = 'F'#change the value of seat that are freed
def Check_availability_of_seat():
    Seat2= {k:v for k,v in Seat1.items() if v=='f'}#use an if clause in a dictionary comprehension to select the available seats
    print(Seat2)#This new dictionary shows the seats are available
    print("These seats are available")
def Exit_program():
    d=input("Do you want to exit?:")
Menu=['Check availability of seat','Book a seat','Free a seat','Show booking state','Exit program']#create a menu includes the functionalities
print('Here is the menu includes the functionalities',Menu)#show the menu to customers
f=input('please enter the functionalities you want to process:')
if f=='Check availability of seat':
    Check_availability_of_seat()
elif f=='Book a seat':
    Book_a_seat()
elif f=='Free a seat':
    Free_a_seat()
elif f=='Show booking state':
    Show_booking_state()
elif f=='Exit program':
    Exit_program()











