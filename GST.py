print('Welcome to ultimate shitty GST calculator pro v0.1')
print('Please enter the value of your item below, not including shipping costs or NZ GST')
itemValue = input()
gstinc = str(float(itemValue) * 1.15)
gstexc = str(float(itemValue) * 0.15)

print('Your item will cost $' + gstinc + ' incl GST of $' + gstexc + '')
