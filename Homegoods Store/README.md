# Sandy's Homegoods

An application allowing for the ordering of everyday home items, with a receipt and tax caluculated at the end.

Technologies: Python

![Homegoods Store](https://user-images.githubusercontent.com/98543446/167227039-b68309d1-86e9-41df-9f6b-a1916c6a5462.gif)


## Item Validation

To make sure one couldn't type in the incorrect item name, Exception handling (try/except) was put in place to compared input with available products in array. 

```
    product = input("What would you like to purchase?: ").lower()
        try:
            product_cost = menu[product]
            price.append(product_cost)
            cart.append(product)
            print()
            print("1 " + product + " added to cart")
            print(f'Current cart: {cart}')
        except:
            print("Seems we cant find that product, try to type a Menu item")
            print()
            time.sleep(2)
            start()
```

If available, added item to cart. If not, response indicated to try again and would restart program.

![Homegoods Store - Validation](https://user-images.githubusercontent.com/98543446/167227258-bb119e22-2f86-46cd-9c34-cab45d92b4f1.gif)

## Total and Tax

At the end of the order, total price was added and tax percentage calculated. Total sum was displayed.

![Homegoods-2](https://user-images.githubusercontent.com/98543446/167227671-617bc58c-b71f-451e-9765-b798a3236db8.png)


