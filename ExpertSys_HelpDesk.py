
def raiseTicket(raiseTicketData,idCount):
    print('\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\-Raise a Ticket-///////////////////////////////\n')
    idCount+=1
    dataDicto={}
    ticketTitle=input('Enter Ticket title: ')
    issue=input('Enter your issue: ')
    dataDicto['ID']=idCount
    dataDicto['TicketTitle']=ticketTitle
    dataDicto['Issue']=issue
    dataDicto['Action']='[RaisedTicket]'
    raiseTicketData.append(dataDicto)

def queryManagement(raiseTicketData):
    print('\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\-Query Management-///////////////////////////////\n')
    count=0
    conditon=True
    if(len(raiseTicketData)!=0):
        for item in raiseTicketData:
            count+=1
            print('\nQuery No.',count)
            print('TicketTitle:',item['TicketTitle'])
            print('Issue:',item['Issue'])
            print('Action: ',item['Action'])
        while(conditon):
            userAns=input('\nDo you want to update issues(y/n)').lower()
            if(userAns=='y'):
                userIp=int(input("\nEnter the query no. :"))
                if(userIp<=len(raiseTicketData) and (userIp>=1) ):
                    item01=raiseTicketData[(userIp)-1]
                    print('\nID:',item01['ID'])
                    print('\nTicketTitle:',item01['TicketTitle'])
                    print('\nIssue:',item01['Issue'])
                    print('\nAction:',item01['Action'])
                    userAns01=input('\nEnter Upadate(inProgress/Resolved):').lower()
                    if((userAns01=='inprogress')):
                        item01['Action']='[inProgress]'
                    elif((userAns01=='resolved')):
                        item01['Action']='[Resolved]'
                    else:
                        pass
                else:
                    print('\nPlease enter Valid input......')
            elif(userAns=='n'):
                conditon=False
            else:
                print('\nEnter the valid input in format(y/n)......')
    else:
        print('\nNo issues found...........')
def FAQ():
    print('\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\-FAQ-/////////////////////////////////////////////')
    print('\n1.How do i create an account?\n2.How do i reset my password?\n3.Can i change my username?')
    userInput001=input("Enter your choice(1 or 2 or 3): ")
    if(userInput001=='1'):
        print('''\nCreating an account on GitHub is straightforward. Here's a step-by-step guide:Visit the GitHub website: Go to github.com in your web browser.Sign Up: On the GitHub homepage, you'll see a "Sign up" section. You need to provide a username, your email address, and a password. Alternatively, you can sign up using your existing Google account by clicking on "Sign up with Google".''')
    elif(userInput001=='2'):
        print('''\nGo to the GitHub login page: Visit github.com and click on the "Sign in" button at the top right corner of the page.Click on "Forgot password?": Below the password field on the login page, you'll see a "Forgot password?" link. Click on it.''')
    elif(userInput001=='3'):
        print('''\nYes, you can change your username on GitHub. Here's how you can do it:Sign in to your GitHub account: Go to github.com and sign in using your current username and password.Access your account settings: Once you're logged in, click on your profile picture in the top-right corner of the page. In the dropdown menu, select "Settings".''')
    else:
        print('\n Give correct input(1 or 2 or 3)......')


def main(userInput,raiseTicketData,idCount):
    if(userInput=='1'):
        raiseTicket(raiseTicketData,idCount)
    elif(userInput=='2'):
        queryManagement(raiseTicketData)
    elif(userInput=='3'):
        FAQ()
    elif(userInput=='4'):
        print('\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\-Thank You for Using HelpDesk Management System-/////////////////////')
        quit()

if __name__=='__main__':
    condition=True
    raiseTicketData=[]
    idCount=0
    while(condition):
        print('\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\-Helpdesk Management System -////////////////////////////\n\n1.Raise Ticket\n2.Query Management\n3.FAQ\n4.Exit')
        userInput=input('\nEnter your choice: ')
        main(userInput,raiseTicketData,idCount)

        