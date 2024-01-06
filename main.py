import pprint as pp

#Function for signup
def signup(authentication_file):
    '''Creates the account for the users'''

    with open(authentication_file,'a+') as f:
        first_name = input('enter first name: ')
        last_name = input('Enter the last name: ')
        while True:
            email = input('Enter the username/email: ')
            if '@' not in email:
                print('please enter the correct email address!')
                continue
            with open(authentication_file,'r') as file:
                users_data= file.readlines()
                for user_data in users_data:
                    single_user = eval(user_data)
                    if single_user['email'] == email:
                        email_present = True
                    else:
                        email_present = False
                if users_data != []:
                    if email_present is True:
                        print('The email is already exisiting!')
                        continue
                    else:
                        break     
                else:
                    break
        password = input('Enter the password: ')
        address = input('enter the address:')
        f.write('{"first_name" : ' + '"'+first_name + '"' + ',')
        f.write('"last_name" : ' + '"'+ last_name + '"'+ ',')
        f.write('"email" : ' + '"'+ email + '"'+ ',')
        f.write('"password" : ' + '"'+ password + '"'+ ',')
        f.write('"address" : ' + '"'+ address + '"'+ '}')
        f.write('\n')
        
#Function for login
def login(authentication_file):
    '''Returns True Or False for login'''
    with open(authentication_file,'a+') as f:
        f = open(authentication_file,'r')
        login_username = input('Enter the username: ')
        login_password = input('Enter the password: ')
        users_data= f.readlines()
        if users_data != []:
            for user_data in users_data:
                single_user = eval(user_data)
                if (single_user['email'] == login_username) and (single_user['password'] == login_password):
                    authentication, email = True, single_user['email']

                    break
                else:
                    authentication = False
                    email = None
        else:
            authentication = False
            email = None
        return (authentication, email)

def view_products():
    #creates a file and add products in it
    with open('products.txt','w') as f:
        product_list = [
            {'code':'1','name':'biryani', 'price':100,'description':'the biryani is very nice','quantity':20},
            {'code':'2','name':'nehari', 'price':150,'description':'the nehari is very nice','quantity':10},
            {'code':'3','name':'haleem', 'price':50,'description':'the haleem is very nice','quantity':30}
            ]
        for product in product_list:
            f.write(str(product)+'\n')
    #reads the created file 
    with open('products.txt','r') as f:
        product_list_read = f.readlines() 
        for products in product_list_read:
            products = eval(products)
            # for keys in products.keys():
            #     if keys == 'code':
            #         print(products[keys])
            #     else:
            #         print(keys +': ' + products[keys])
            pp.pprint(products)
            print('--------------------------------------')





    

def add_to_cart(user_f,product_f):        
        options = input('enter the products you want to choose separated by commas(1xn,2xn): ')
        options = options.split(',')

        product_file = open(product_f,'r+')
        products = product_file.readlines()
        for product in products:
            product_for_cart = eval(product)
            product_for_product_list = eval(product)
            for option in options:
                option = option.split('x')    
                user_file = open(user_f,'a') 
                if option[0] == product_for_cart['code']:
                    product_for_cart['quantity'] =int(option[1])
                    product_for_product_list['quantity'] -= int(option[1])
                    user_file.write(str(product_for_cart)+'\n')
                    product_file.write(str(product_for_product_list)+'\n')



            # with open(str(user_f),'w+') as user_file:
                # cart = user_file.readlines()
                # for product in cart:
                #     product = eval(product)
                #     if product['code'] == str(option[0]):
                #         product['quantity'] -= option[1]
                #         # print(product['quantity'])
                #         print(product)  
           
        
        # products = product_file.readlines()
        # with open(user_f,'a') as user_file:
        #     for option in options:
        #         for product in products:
        #             product_ = eval(product)
        #             if product_['code'] == option:
        #                 user_file.write(str(product_)+'\n')

    



def view_cart(user_f):
    with open (user_f,'r') as user_file:
        cart = user_file.readlines() 
        for single_product in cart:
            product_in_cart = eval(single_product)
            # product_in_cart.pop('code')
            for keys in product_in_cart.keys():
                if keys == 'code':
                    print(product_in_cart[keys])
                else:
                    print(str(keys) +': ' + str(product_in_cart[keys]))
            # pp.pprint(products)
            print('*********************************')















welcome_message = 'Welcome to our app!'
print(welcome_message)
while True:
    login_signup = input('do you have an existing account? type Y or N: ')
    if login_signup == 'Y':
        print('Please Enter the Username & Password for login!!!')
        login_data = login('authentication.txt')
        if login_data[0] is True:
            print('yesss')
            view_products()
            add_to_cart(str(login_data[1])+'.txt','products.txt')
            cart_view_option = input('You want to view cart?(Y,N): ')
            if cart_view_option == 'Y':
                view_cart(str(login_data[1])+'.txt')
            else:
                break
            break
        
        
    elif login_signup == 'N':
        signup('authentication.txt')
        print('Please Enter the Username & Password for login!!!')
        print(login('authentication.txt'))
        break

