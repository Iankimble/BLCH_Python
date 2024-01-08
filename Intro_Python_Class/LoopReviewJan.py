shoppingCart_1=['apple','organge','bannana']
shoppingCart_2=['grapes','mango','apple']
shoppingCart_3=['pears','avocado','watermelon','apple']

def removeApple(shopping_list):
    shopping_list.remove('apple')
    print('removing apples...')
    print(shopping_list)

removeApple(shoppingCart_2)