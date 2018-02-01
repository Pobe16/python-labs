# Write a program to allow a user to create a customer invoice. It should allow entry of 
# customer number, name, address & telephone number. The user should then be presented 
# with an invoice detail line which allows entry of a product code quantity and unit 
# price. A 'print invoice' button should calculate the invoice total (including VAT at 
# 20%) and print an appropriately formatted invoice in a message box.

import easygui as eg

customer = []
purchases = []


def gb():
    print("Good bye!")


def main():
    global msg
    global purchases
    title = "Invoice printer"

    if customer == []:
        msg = "No customer selected."
    else:
        msg = "#" + customer[0] + " " + customer[1] + " " + customer[2] + " " + customer[3]

    msg = msg + "\n" + str(len(purchases)) + " items purchased."

    values = ["Edit customer", "Add Item", "Remove Item", "Print invoice"]

    choice = eg.buttonbox(msg, title, values)

    if choice == "Edit customer":
        new_customer()
    elif choice == "Add Item":
        add_item()
    elif choice == "Remove Item":
        remove_item()
    elif choice == "Print invoice":
        if customer == []:
            print("Customer data empty.")
            main()
        elif purchases == []:
            print("Purchase list empty.")
            main()
        else:
            print_invoice()
    else:
        gb()


def add_item():
    msg = "Enter item details."
    title = "New purchase"
    fields = ["Product code", "Price (£)", "Quantity"]
    item = eg.multenterbox(msg, title, fields)
    while 1:
        if item is None:
            main()
            break
        errmsg = ""
        for i in range(len(fields)):
            if item[i].strip() == "":
                errmsg = errmsg + ('"%s" is a required field.\n\n' % fields[i])
            if i > 0:
                try:
                    if float(item[i]) < 0.01:
                        errmsg = errmsg + ('"%s" have to be a positive number.\n\n' % fields[i])
                except ValueError:
                    errmsg = errmsg + ('"%s" have to be a number.\n\n' % fields[i])

        if errmsg == "":
            break  # no problems found

        item = eg.multenterbox(errmsg, title, fields, item)
    purchases.append(item)
    main()


def remove_item():
    if len(purchases)>0:
        purchases.pop(len(purchases)-1)
        main()
    else:
        print("No items purchased yet.")
        main()


def new_customer():
    global customer
    msg = "Enter customer's data."
    title = "Customer"
    fields = ["ID", "Name", "Address", "Telephone number"]
    cust = eg.multenterbox(msg, title, fields)
    while 1:
        if cust is None:
            main()
            break
        errmsg = ""
        for i in range(len(fields)):
            if cust[i].strip() == "":
                errmsg = errmsg + ('"%s" is a required field.\n\n' % fields[i])
        if errmsg == "":
            break  # no problems found
        cust = eg.multenterbox(errmsg, title, fields, cust)
    customer = cust
    main()


def print_invoice():
    global customer
    global purchases
    msg = "Check the invoice. Press OK to print."
    title = "Print preview"
    office_address = "Mikosoft \nFlat 0/1\n63 Seedhill Road\nPA1 1QS Paisley\n\r"
    text = office_address + "\n\r"

    for i in customer:
        text = text + i + "\n"

    text = text + "\rProduct\tPrice\tQuantity\tWith VAT\r"

    value = 0

    for j in purchases:
        for k in j:
            text = text + k + "\t"
        subvalue = float(j[1]) * float(j[2]) * 1.2
        text = text + str(subvalue) + "\n"
        value = value + subvalue

    text = text + "\rTotal:\t" + str(value)

    printing = eg.textbox(msg, title, text)

    if printing == None:
        main()
    else:
        print(printing)


main()