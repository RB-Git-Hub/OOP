#Libray
import os

class Email():
    '''
    The Email class formulates the emails.

    Also emails can be marked as read and as spam using the functions
    This class is accessed by the Inbox class only. 
    '''
    def __init__(self, from_address, subject_line, email_contents,
has_been_read, is_spam):
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False

    # Marks an email as read          
    def mark_as_read(obj):
        obj.has_been_read = True
    
    # Marks email as spam        
    def mark_as_spam(obj):
        obj.is_spam = True
        


class Inbox():
    '''
    Inbox class holds the emails formed in the Email class in
    a list called email_list. 
    
    The functions are accessed using the main menu and are used to read and
    modifying the emails.

    '''
    email_list=[]

    # Adds an email to email_list using Email class to format
    def add_email(self,from_address, subject_line, email_contents):
        self.email_list.append(Email(from_address, subject_line,
email_contents, False, False))

    # Shows a list of all emails with an index for a selected sender address 
    def list_messages_from_sender(self, sender_address):
        count = 0
        for obj in self.email_list:
            if obj.from_address == (sender_address):
                count += 1    
                print(f"{count} {obj.subject_line}")

    # Shows full email selected by index, also marks as read
    def get_email(self,sender_address, index):
        count = 0
        for obj in self.email_list:
            if obj.from_address == (sender_address):
                count += 1
                try:
                    if count == int(index):  
                        print(f"\nSender: {obj.from_address}\nSubject:\
 {obj.subject_line}\nMessage: {obj.email_contents}")
                        Email.mark_as_read(obj)
                except:
                    pass

    # Marks a specific email as spam using the index                
    def mark_as_spam(self, sender_address, index):
        count = 0
        for obj in self.email_list:
            if obj.from_address == (sender_address):
                count += 1  
                #Try used to protect against selection of non int
                try:
                    if count == int(index):  
                        Email.mark_as_spam(obj)
                        print("\nEmail has been marked as spam")
                except:
                    pass

    # Shows a list of unread emails                
    def get_unread_emails(self):
        print("Unread Emails\n")
        for obj in self.email_list:
            if obj.has_been_read == False:
                print(obj.subject_line)

    # Shows emails marked as spam                
    def get_spam_emails(self):
        print("Spam Emails")
        for obj in self.email_list:
            if obj.is_spam == True:
                print(f"\nSender: {obj.from_address}\nSubject: \
{obj.subject_line}\nMessage: {obj.email_contents}")

    # Deletes an email selected by index        
    def delete(self,sender_address, index):
        count = 0
        for obj in self.email_list:
            if obj.from_address == (sender_address):
                count += 1  
                #Try used to protect against selection of non int
                try:
                    if count == int(index):  
                        self.email_list.remove(obj) 
                except:
                    pass
# Menu
usage_message = '''Welcome to the email system! What would you like to do?

s - send email.
l - list emails from a sender.
r - read and email.
m - mark email as spam.
gu - get unread emails.
gs - get spam emails.
d - delete email.
e - exit this program.
'''

user_choice = ""

# Menu selection
while True:
    os.system("cls")
    user_choice = input(usage_message).strip().lower()
    
    # s - Creates an email
    if user_choice == "s":
        os.system("cls")
        from_address = input("\nPlease enter the address of the\
sender\n: ").lower()
        subject_line = input("Please enter the subject line of the email\n: ")
        email_contents = input("Please enter the contents of the email\n: ")
        Inbox.add_email(Inbox, from_address, subject_line, email_contents)
        print("Email has been added to inbox.")
    
    # l - Lists all emails from selected sender    
    elif user_choice == "l":
        os.system("cls")
        sender_address = input("Please enter the address of the sender\n:")
        Inbox.list_messages_from_sender(Inbox,sender_address)
        input("\nPress enter to go back to main menu")

    # r - Displays an email selected from a sender list
    elif user_choice == "r":
        os.system("cls")
        
        # Lists all emails from selected sender
        sender_address = input("Please enter the address of the sender\
of the email\n:")
        Inbox.list_messages_from_sender(Inbox,sender_address)

        # Displays selected email from list by index
        email_index = (input("Please enter the index of the email that \
you would like to read\n:"))
        Inbox.get_email(Inbox,sender_address, email_index)

        input("\nPress enter to go back to main menu")

    # m - Displays an email selected from a sender list
    elif user_choice == "m":
        os.system("cls")

        # Displays email list from selected sender
        sender_address = input("Please enter the address of the sender \
of the email\n: ")
        Inbox.list_messages_from_sender(Inbox,sender_address)

        # Marks as spam the selected email from list by index
        email_index = (input("Please enter the index of the email to be \
marked as spam\n: "))
        Inbox.mark_as_spam(Inbox, sender_address, email_index)

        input("\nPress enter to go to main menu")

    # gu - Displays a list of all unread emails 
    elif user_choice == "gu":
        os.system("cls")
        Inbox.get_unread_emails(Inbox)

        input("\nPress enter to go to main menu")

    # gs - Displays all spam emails 
    elif user_choice == "gs":
        os.system("cls")
        Inbox.get_spam_emails(Inbox)
        input("\nPress enter to go to main menu")
    
    # e - Exit
    elif user_choice == "e":
        print("\nGoodbye")
        break
    
    # d - Deletes a specific email
    elif user_choice == "d":
        os.system("cls")

        # Displays email list from selected sender
        sender_address = input("Please enter the address of the sender \
of the email\n: ")
        Inbox.list_messages_from_sender(Inbox,sender_address)
        
        # Email selected by index deleted
        email_index = (input("\nPlease enter the index of the email to \
be deleted\n: "))
        Inbox.delete(Inbox, sender_address, email_index)

        print("Email has been deleted")

    # Incorrect selection message
    else:
        input("Oops - incorrect input")
