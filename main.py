from pyscript import document, display

def create_order(e) :

    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")
    prod6 = document.getElementById("item6")
    prod7 = document.getElementById("item7")
    prod8 = document.getElementById("item8")
    prod9 = document.getElementById("item9")
    prod10 = document.getElementById("item10")
    

    subtotal = (float(prod1.value) * prod1.checked
    + float(prod2.value) * prod2.checked 
    + float(prod3.value) * prod3.checked 
    + float(prod4.value) * prod4.checked 
    + float(prod5.value) * prod5.checked 
    + float(prod6.value) * prod6.checked 
    + float(prod7.value) * prod7.checked 
    + float(prod8.value) * prod8.checked 
    + float(prod9.value) * prod9.checked
    + float(prod10.value) * prod10.checked )

    size = document.querySelector("input[name='size']:checked")
    price = float(size.value)

    subtotal = subtotal + price

    taxrate = 0.12
    tax = subtotal * taxrate
    grandtotal = subtotal + taxrate

    display(f'Subtotal: Php {subtotal}', target="output1")
    display(f'VAT: Php {tax}', target="output1", append=True)
    display(f'Total Amount: Php {grandtotal}', target="output1", append=True)
    display("Thank you for your order!", target="output1", append=True)
