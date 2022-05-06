import time
print("Welcome to Sandy's Homegoods!")
time.sleep(1)
print(" To begin select an item from the menu to add to cart.")
time.sleep(2)
menu ={'candle':7.00, 'shampoo':8.50, 'brush':4.50, 'conditioner':7.25, 'soap':5.75}
cart = []
price =[]

def start():
    flag = True
    while flag:
        print("~ Product Menu: ")
        time.sleep(.3)
        for x in menu:
            print(x)
            time.sleep(.3)
    
        time.sleep(.5)
        print()
        product = input("What would you like to purchase?: ").lower()
        #print('You typed in: ' + product)
        try:
            product_cost = menu[product]
            price.append(product_cost)
            #print(f"Price of {product_cost} addded to Price List")
            cart.append(product)
            print()
            print("1 " + product + " added to cart")
            print(f'Current cart: {cart}')
        except:
            print("Seems we cant find that product, try to type a Menu item")
            print()
            time.sleep(2)
            start()
        print()
        
        
                
        def Shop_more():
            Continue = input("Would you like to continue ordering? ").lower()
            if Continue == 'No'.lower():
                total = (sum(price))
                print (f'Your total balance is: ${total}')
                print()
                time.sleep(.5)
                print('Calculating tax... ')
                tax =float(total * .05)
                total_balance = float(total + tax)
                time.sleep(.5)
                tax_2 = "{:.2f}".format(tax)
                tb_2 = "{:.2f}".format(total_balance)
                print(f'Your tax is ${tax_2}')
                time.sleep(.5)
                print(f'Making your total balance: ${tb_2}')
                time.sleep(.5)
                print('Please pay on the next screen...')
                quit()
            if Continue == 'Yes'.lower():
                print()    
            else:
                print ('Please enter Yes or No. Thank you!')
                Shop_more()
        Shop_more()
start()   

