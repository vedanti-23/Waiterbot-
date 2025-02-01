print("Hello!\nWelcome to 'Naivedyam Foods'")
customer_name=input("Please enter your name").title()

enemies_list=["Sarika","Tanya","Mahesh","Mamata"]

if customer_name in enemies_list:
    print("Get out of the Shop")
else:
   print(f"\nHello!{customer_name},thank you foe coming here today.")

   menu={
       "Chole Bhature":120,
       "Paneer rolls":200,
       "Idli Sambhar":100,
       "Regular Thali":200
   }
   print(f"{customer_name},what would you like to order?\n Here is our menu{menu}.")
   total_items=int(input("How many itmes would you like to order?"))
   order_list={}

   for item in range(1,total_items+1):
       order=input(f"Your Order no. {item}Please.")
       quantity=int(input(f"How many plates of{order}you want."))
       order_list[order]=quantity

   print(order_list)

   total_price=0
   for menu_item, menu_item_price in order_list.items():
       for order_item,order_item_quantity in menu.items():
           if menu_item==order_item:
               total_price +=menu_item_price * order_item_quantity

   print(f"\nSounds Good {customer_name}!\n we will have those {order_list}along with the quantity.")
   print(f"Thank You {customer_name}.\nYour total bill is:{total_price}")
   print("Vist Again!")

