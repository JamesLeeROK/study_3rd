import tkinter as tk

root = tk.Tk()
root.geometry('400x300')
root.title('조각 피자 주문 프로그램')
label_pizza = tk.Label(root, text = '피자')
label_pizza.pack()
pizza_menu = {
    '치즈피자' : 3200,
    '콤비네이션 피자' : 3500,
    '불고기 피자' : 3600
}
checked_var = {}
for pizza, price in pizza_menu.items() :
    checked_var[pizza] = tk.BooleanVar()
    checkbutton = tk.Checkbutton(root,
                                 variable = checked_var[pizza],
                                 text = f'{pizza}({price}원)')
    checkbutton.pack(anchor = 'w')

def order() :
    total_price = 0
    order_list = '주문내역 : \n'

    for pizza, price in pizza_menu.items() :
        if checked_var[pizza].get() == True :
            order_list += f'-{pizza}({price}원)\n'
            total_price += price
        order_list += f'\n총 가격 : {total_price}원'
        order_text.set(order_list)

order_btn = tk.Button(root, text = '주문', command = order)
order_btn.pack()
order_text = tk.StringVar()
order_label = tk.Label(root, textvariable = order_text)
order_label.pack()
root.mainloop()