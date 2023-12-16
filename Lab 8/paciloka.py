class Hotel:
    # Menyimpan setiap objek dari class Hotel agar dapat digunakan dalam class
    instances = []
    def __init__(self, name:str, available_rooms:int, room_price:int):
        self.__class__.instances.append(self)

        self.name = name
        self.available_rooms = available_rooms
        self.room_price = room_price
        self.profit = 0
        self.guests = set() # Berbentuk set karena nilai-nilainya harus unik

    def booking(self, guest_name:str, rooms_booked:int):
        if rooms_booked <= 0:
            print("Jumlah kamar yang akan dipesan harus lebih dari 0!")
        else:
            cost = rooms_booked * self.room_price
            if rooms_booked > self.available_rooms:
                print(f"Hotel {self.name} hanya memiliki {self.available_rooms} kamar yang tersedia")
            else:
                if guest_dict[guest_name].money < cost:
                    print(f"Saldo {guest_name} tidak cukup untuk melakukan booking!")
                else:
                    self.guests.add(guest_name)
                    self.available_rooms -= rooms_booked
                    self.profit += cost
                    guest_dict[guest_name].hotel_list.add(self.name) # Memodifikasi atribut user yang melakukan booking
                    guest_dict[guest_name].money -= cost
                    print(f"User dengan nama {guest_name} berhasil melakukan booking di hotel {self.name} dengan jumlah {rooms_booked} kamar!")

    def print_guests(self):
        """Print setiap user dalam set hotel.guests"""
        out_str = ""
        if len(self.guests) > 0:
            for name in self.guests:
                out_str = f"{out_str}, {name}"
            print(f"{self.name} | {out_str.strip(', ')}")
        else:
            print(f"Hotel {self.name} tidak memiliki pelanggan!")

    def get_profit(self):
        return self.profit

    def __str__(self) -> str:
        print(f"Nama hotel:\t\t {self.name}")
        print(f"Banyak kamar tersedia:\t\t {self.available_rooms}")
        print(f"Harga per kamar hotel:\t\t {self.room_price}")
        print(f"Profit:\t\t {self.profit}")
    
    @classmethod
    def print_hotels(self):
        """Print setiap objek dari class"""
        print("Daftar Hotel")
        for i in range(len(__class__.instances)):
            print(f"{i + 1}. {__class__.instances[i].name}")


class User:
    # Menyimpan setiap objek dari class User agar dapat diakses dalam class
    instances = []
    def __init__(self, name:str, money:int):
        self.__class__.instances.append(self)

        self.name = name
        self.money = money
        self.hotel_list = set()
    
    def topup(self, amt:int):
        """Memodifikasi atribut saldo pengguna berdasarkan jumlah topup yang dimasukkan"""
        if amt > 0:
            self.money += amt
            print(f"Berhasil menambahkan {amt} ke user {self.name}. Saldo user menjadi {self.money}")
        else:
            print("Jumlah saldo yang ditambahkan ke user harus lebih dari 0!")

    def print_hotels(self):
        out_str = ""
        if len(self.hotel_list) > 0:
            for name in self.hotel_list:
                out_str = f"{out_str}, {name}"
            print(f"{self.name} | {out_str.strip(', ')}")
        else:
            print(f"User {self.name} tidak pernah melakukan booking!")

    def get_money(self):
        return self.money

    def __str__(self) -> str:
        print(f"Nama user:\t\t {self.name}")
        print(f"Saldo user:\t\t {self.money}")

    @classmethod
    def print_users(self):
        print("Daftar Tamu")
        for i in range(len(__class__.instances)):
            print(f"{i + 1}. {__class__.instances[i].name}")

def main():
    initialize()

    while True:
        print("=============Welcome to Paciloka!=============\n")

        action = input("Masukkan perintah: ")
        # Print daftar hotel dan user yang ada
        if action == "1":
            Hotel.print_hotels()
            print()
            User.print_users()

        # Cetak profit dari hotel
        elif action == "2":
            hotel_name = input("Masukkan nama hotel: ")
            if hotel_name in hotel_dict:
                print(f"Hotel dengan nama {hotel_name} mempunyai profit sebesar {hotel_dict[hotel_name].get_profit()}")
            else:
                print("Nama hotel tidak ditemukan di sistem!")

        # Print saldo seorang user
        elif action == "3":
            guest_name = input("Masukkan nama user: ")
            if guest_name in guest_dict:
                print(f"User dengan nama {guest_name} mempunyai saldo sebesar {guest_dict[guest_name].get_money()}")
            else:
                print("Nama user tidak ditemukan di sistem!")

        # Melakukan topup untuk seorang user
        elif action == "4":
            guest_name = input("Masukkan nama user: ")
            if guest_name in guest_dict:
                pass
            else:
                print("Nama user tidak ditemukan di sistem!\n")
                continue
            try:
                amount = int(input("Masukkan jumlah uang yang akan ditambahkan ke user:"))
            except ValueError:
                print("Input harus berupa integer!")
                continue
            guest_dict[guest_name].topup(amount)

        # User melakukan booking hotel sejumlah x kamar
        elif action == "5":
            guest_name = input("Masukkan nama user: ")
            if guest_name not in guest_dict:
                print(f"Nama user tidak ditemukan di sistem!\n")
                continue
            else:
                hotel_name = input("Masukkan nama hotel: ")
                if hotel_name not in hotel_dict:
                    print(f"Nama hotel tidak ditemukan di sistem!\n")
                    continue
            try:
                rooms_booked = int(input("Masukkan jumlah kamar yang akan di-booking: "))
            except ValueError:
                print("Input harus berupa integer!")
                pass
            hotel_dict[hotel_name].booking(guest_name, rooms_booked)

        # Cetak list user per hotel
        elif action == "6":
            hotel_name = input("Masukkan nama hotel: ")
            hotel_dict[hotel_name].print_guests()

        # Cetak list hotel per user
        elif action == "7":
            guest_name = input("Masukkan nama user: ")
            guest_dict[guest_name].print_hotels()

        # Exit program
        elif action == "8":
            print("Terima kasih sudah mengunjungi Paciloka!")
            exit()

        else:
            print("Perintah tidak diketahui! Masukkan perintah yang valid")

        print()

def initialize():
    """
    Meminta input dari user dan memproses input menjadi struktur
    dictionary {nama_hotel/nama_guest : objek hotel/guest}
    """
    global hotel_dict
    global guest_dict

    # Melakukan inisialisasi dictionary
    hotel_dict = {}
    guest_dict = {}

    while True:
        try:
            num_of_hotels = int(input("Masukkan banyak hotel: "))
            num_of_guests = int(input("Masukkan banyak tamu: "))
            break
        except ValueError:
            print("Input harus berupa integer!")
            continue

    print()

    for i in range(num_of_hotels):
        idx = i + 1
        hotel_name = input(f"Masukkan nama hotel ke-{idx}: ")
        while True:
            try:
                num_of_rooms = int(input(f"Masukkan banyak kamar hotel ke-{idx}: "))
                room_price = int(input(f"Masukkan harga satu kamar hotel ke-{idx}: "))
                break
            except ValueError:
                print("Input harus berupa integer!")
                continue
        # Menambahkan objek ke key dengan nama objek
        hotel_dict[hotel_name] = Hotel(hotel_name, num_of_rooms, room_price)

    print()

    for j in range(num_of_guests):
        idx = j + 1
        guest_name = input(f"Masukkan nama user ke-{idx}: ")
        while True:
            try:
                user_balance = int(input(f"Masukkan saldo user ke-{idx}: "))
                break
            except ValueError:
                print("Input harus berupa integer!")
                continue
        # Menambahkan objek ke key dengan nama objek
        guest_dict[guest_name] = User(guest_name, user_balance)

if __name__ == "__main__":
    main()


