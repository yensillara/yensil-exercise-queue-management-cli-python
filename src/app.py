import json, os
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")
imported= False
    
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue.get_queue())

def add(someone, phone_number):
    global queue
    print(f"You have {str(len(queue.get_queue()))} clients before you")
    dictionary = {'Name':someone, 'Mobil':phone_number}
    queue.enqueue(dictionary)
    print("You have added someone to the queue")
    print(queue)

def dequeue(number_to_delete):
    global queue
    send(body=f"Hello, {str(queue.get_queue()[int(number_to_delete)-1]['Name'])} it's time to eat",to=queue.get_queue()[int(number_to_delete)-1]['Mobil'])
    queue.dequeue(number_to_delete)
    print(f"the element {number_to_delete} was deleted to the queue")
    
def save():
    """
        abre/crea el archivo queue.json y guarda
        la lista de diccionarios que representan a los
        usuarios.
    """
    global queue
    with open(os.path.join(os.getcwd(), "queue.json"), "w") as queue_file:
        json.dump(queue.get_queue(), queue_file)

def load():
    global queue
    global imported
    if not imported: 
        with open(os.path.join(os.getcwd(), "queue.json"), "r") as queue_file:
            queue_as_dictionary = json.load(queue_file)
        for d in queue_as_dictionary:
            queue.enqueue(d)
        imported= True

    # queue = Queue(mode="FIFO", queue_as_dictionary)

print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    if option == 1:
        print("Add someone") 
        someone =input()
        print("Add Phone Number")
        phone_number= input()
        add(someone, phone_number)
    elif option == 2:
        print("Remove someone") 
        number_to_delete = input()
        dequeue(number_to_delete)
        print("")
    elif option == 3:
        count = 1
        for person in queue.get_queue():
            print(str(count)+'. '+str(person))
            count = count + 1
    elif option == 4:
        save()
        print("seved qeueu in qeueu.js")
    elif option == 5:
        load()
        print("Loading qeueu from qeueu.js")
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))

