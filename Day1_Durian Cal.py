#Prob. 1 ใส่ชื่อผลไม้ และ จำนวณ จะได้ราคาออกมา
#Prob. 2 สามารถเพิ่มสินค้าได้เรื่อยๆ และคำนวณออกมาได้เลย และคำนวณเงินทอนได้ด้วย
fruit = {'apple':150,
        'durian':300,
        'orange':50}

menucheck = {'a':'apple','b':'durian','c':'orange'}

print('ยินดีตอนรับสู่โปรแกรมคำนวณสินค้า')
print('-----------')

mainmenu = '''
ยินดีสู่โปรแกรมคำนวณ
[1]-สินค้าหลายชิ้น
[2]-สินค้าชิ้นเดียว
[3]-ปิดโปรแกรม
'''

while True:
    print(mainmenu)
    menu = input('กรุณาเลือกเมนู [1]-[3]: ')

    text1 = '''
    ------------
    ****ขายสินค้าหลายชิ้น****
    ------------
    '''

    allproduct = []
    productcheck = []
    submenu1 = 'a'

    if menu == '1':
        print(text1)
        while submenu1.lower() != 'q':
            print('กรุณาเลือกสินค้า\n[A]-แอปเปิ้ล [B]-ส้ม [C] ทุเรียน หรือ [Q] ออกจากเมนู [T]')
            submenu1 = input('สินค้า: ')
            if submenu1.lower() != 'q' and submenu1.lower() != 't':
                product = menucheck[submenu1.lower()]
                price = fruit[product]
                quantity = float(input('จำนวณ (kg): '))
                total = price*quantity
                d = [product,quantity]
                if product not in productcheck:
                    productcheck.append(product)
                    allproduct.append(d)
                else:
                    pindex = productcheck.index(product) #ตรวจสอบว่าสินค้าที่เคยพิมพ์แล้วอยู่ index ไหน
                    # allproduct[pindex][1] จำนวน
                    allproduct[pindex][1]= allproduct[pindex][1] + quantity

            elif submenu1.lower() == 'q':
                print('กำลังออกจากเมนู...')
                break
            elif submenu1.lower() == 't':
                print('กำลังรวมยอด')
                gran_total = 0
                for name,q in allproduct:
                    cal =fruit[name] *q
                    print('-{} จำนวณ: {} กินโลกรัม (รวม {:,.2f} บาท)'.format(name,q,cal))
                    gran_total = gran_total+cal 
                print('ยอดรวมทั้งหมด: {:,.2f} บาท'.format(gran_total))
                break
            print('-----------------')
    elif menu == '2':
        while True:
            product= input('กรุณาเลือกสินค้า": apple, durian, orange: ')
            quantity = float(input('จำนวนสินค้า กี่กิโลกรัม:'))
            print(quantity*fruit[product])
            print('-----------')
    elif menu == '3':
        print('ปิดโปรแกรมเรียบร้อยแล้ว')
        break







#print(allproduct)