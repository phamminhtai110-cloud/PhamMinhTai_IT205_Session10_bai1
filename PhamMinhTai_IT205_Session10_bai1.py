cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    print("\n===== SHOPEE CART =====")
    print("1. Xem gio hang")
    print("2. Them san pham")
    print("3. Cap nhat so luong")
    print("4. Xoa san pham")
    print("5. Thoat")

    choice = input("Nhap lua chon: ")

    if choice == "1":
        total_quantity = 0
        total_money = 0

        print("\nMa SP\tTen SP\t\t\tSL\tDon Gia")

        for item in cart_items:
            print(item[0], "\t", item[1], "\t", item[2], "\t", item[3])

            total_quantity += item[2]
            total_money += item[2] * item[3]

        print("Tong so luong:", total_quantity)
        print("Tong tien:", total_money)

    elif choice == "2":
        product_id = input("Nhap ma SP: ")
        product_name = input("Nhap ten SP: ")

        try:
            quantity = int(input("Nhap so luong: "))
            price = float(input("Nhap don gia: "))

            if quantity <= 0 or price < 0:
                print("Du lieu khong hop le!")
                continue

            found = False

            for item in cart_items:
                if item[0] == product_id:
                    item[2] += quantity
                    found = True
                    print("Da cong don so luong.")
                    break

            if not found:
                cart_items.append(
                    [product_id, product_name, quantity, price]
                )
                print("Them san pham thanh cong.")

        except ValueError:
            print("Du lieu khong hop le!")

    elif choice == "3":
        product_id = input("Nhap ma SP: ")

        try:
            new_quantity = int(input("Nhap so luong moi: "))

            if new_quantity <= 0:
                print("So luong phai > 0")
                continue

            found = False

            for item in cart_items:
                if item[0] == product_id:
                    item[2] = new_quantity
                    found = True
                    print("Cap nhat thanh cong.")
                    break

            if not found:
                print("Ma san pham khong ton tai trong gio hang.")

        except ValueError:
            print("Du lieu khong hop le!")

    elif choice == "4":
        product_id = input("Nhap ma SP can xoa: ")

        found = False

        for item in cart_items:
            if item[0] == product_id:
                cart_items.remove(item)
                found = True
                print("Xoa thanh cong.")
                break

        if not found:
            print("Ma san pham khong ton tai trong gio hang.")

    elif choice == "5":
        print("Tam biet!")
        break

    else:
        print("Lua chon khong hop le!")