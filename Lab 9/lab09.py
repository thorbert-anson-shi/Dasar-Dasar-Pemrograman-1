class Person:
    # Initializes private variables for Person superclass
    def __init__(self, name: str, payment: int, stamina: int) -> None:
        self.__name = name
        self.__payment = payment
        self.__stamina = stamina
        self.__total_work = 0

    def set_stamina(self, stamina: int) -> None:
        self.__stamina = stamina

    def set_total_work(self, total_work: int) -> None:
        self.__total_work = total_work

    def get_name(self) -> str:
        return self.__name

    def get_payment(self) -> int:
        return self.__payment

    def get_stamina(self) -> int:
        return self.__stamina

    def get_total_work(self) -> int:
        return self.__total_work

    def pay_day(self) -> int:
        return self.__payment * self.__total_work

    def is_available(self, cost_stamina: int) -> bool:
        return self.__stamina >= cost_stamina

    def work(self, cost_stamina: int) -> None:
        self.set_stamina(self.get_stamina() - cost_stamina)
        self.set_total_work(self.get_total_work() + 1)


class Worker(Person):
    # Keeps track of all instantiated objects from the class Worker
    instances = {}

    def __init__(self, name: str) -> None:
        # Make sure there are no duplicate names
        if name.lower() not in __class__.instances:
            super().__init__(name, 5000, 100)
            # Add instance to dictionary with the key being its name
            __class__.instances[name.lower()] = self
            # Initialize bonus as a worker's own private variable
            self.__bonus = 0
        else:
            print("Nama worker harus unik!")

    def set_bonus(self, bonus: int):
        self.__bonus = bonus

    def get_bonus(self):
        return self.__bonus

    def work(self, bonus: int, cost_stamina: int) -> bool:
        print("Hasil cek ketersediaan pegawai: ")
        # Only make person work if stamina is enough
        if self.is_available(cost_stamina):
            # Calls self.work() from superclass and increments bonus
            super().work(cost_stamina)
            self.__bonus += bonus
            print(f"Pegawai dapat menerima pekerjaan")
            print(f"{'=' * 32}\nBerhasil memberi pekerjaan kepada {self.get_name()}")
            return True
        else:
            print(
                f"Pegawai tidak dapat menerima pekerjaan. Stamina pegawai tidak cukup."
            )
            return False

    def pay_day(self) -> int:
        # Give worker money as calculated in superclass + flat bonus per job
        return super().pay_day() + self.__bonus


class Manager(Person):
    def __init__(self, name: str, payment: int, stamina: int) -> None:
        super().__init__(name, payment, stamina)
        # Create a list of worker names
        self.__list_worker = []

    def get_worker_list(self):
        return self.__list_worker

    def hire_worker(self, name: str) -> None:
        # Prematurely decrement manager stamina and increment manager total_work
        self.work(10)
        # Make sure there are no duplicate workers
        if name in self.__list_worker:
            print("Sudah ada!")
            # Only let object "keep" total work if process is successful
            self.set_total_work(self.get_total_work() - 1)
        else:
            # Create worker object and add it to instance dictionary as per Worker.__init__()
            Worker(name)
            self.__list_worker.append(name)
            print("Berhasil mendapat pegawai baru")

    def fire_worker(self, name: str) -> None:
        # Prematurely decrement manager stamina and increment manager total_work
        self.work(10)
        # Only fire worker if worker exists in worker list
        if name in self.__list_worker:
            self.__list_worker.remove(name)
            del Worker.instances[name]  # delete worker instance completely
            print(f"Berhasil memecat {name.title()}")
        else:
            print("Nama tidak ditemukan!")
            # Only let object "keep" total work if process is successful
            self.set_total_work(self.get_total_work() - 1)

    def give_work(self, name: str, bonus: int, cost_stamina: int) -> None:
        # Prematurely decrement manager stamina and increment manager total_work
        self.work(10)
        # Make sure to only give workers in worker list
        if name in self.__list_worker:
            # Fetches object from instance dict and assigns them work
            if Worker.instances[name].work(bonus, cost_stamina) == True:
                pass
            # Dirty trick to make sure manager doesn't get total_work incremented when worker stamina is insufficient
            else: self.set_total_work(self.get_total_work() - 1)
        else:
            print("Nama tidak ditemukan!")
            # Only let object "keep" total work if process is successful
            self.set_total_work(self.get_total_work() - 1)

def main() -> int:
    manager_name = input("Masukkan nama manajer: ")
    try:
        pay_per_work = int(input("Masukkan jumlah pembayaran: "))
        manager_stamina = int(input("Masukkan stamina manajer: "))
    except ValueError:
        raise Exception("Jumlah pembayaran dan stamina manajer harus berupa int")

    # Create manager object before running the main loop
    manager = Manager(manager_name, pay_per_work, manager_stamina)

    # While manager still has more than 10 stamina
    while manager.is_available(10):
        print(
            """PACILOKA
-----------------------
1. Lihat status pegawai
2. Beri tugas
3. Cari pegawai baru
4. Pecat pegawai
5. Keluar
-----------------------
"""
        )

        action = input("Masukkan pilihan: ")

        if action == "1":
            #        vvv Gets name of class vvv
            print(
                f"{type(manager).__name__:<20}|{manager.get_name():<20}|Total kerja: {manager.get_total_work():<20}|Stamina: {manager.get_stamina():<20}|Gaji: {manager.pay_day():<20}"
            )
            worker_objs = Worker.instances  # Returns dictionary of instantiated objects
            for name in Worker.instances:
                print(
                    f"{type(worker_objs[name]).__name__:<20}|{worker_objs[name].get_name().title():<20}|Total kerja: {worker_objs[name].get_total_work():<20}|Stamina: {worker_objs[name].get_stamina():<20}|Gaji: {worker_objs[name].pay_day():<20}"
                )
        elif action == "2":
            worker_name = input("Tugas akan diberikan pada: ")
            try:
                given_bonus = int(input("Bonus pekerjaan: "))
                cost_stamina = int(input("Beban stamina: "))
            except ValueError:
                print("Bonus dan cost stamina harus dalam bentuk int")
            # Give work to
            manager.give_work(worker_name.lower(), given_bonus, cost_stamina)

        elif action == "3":
            worker_name = input("Nama pegawai baru: ")
            manager.hire_worker(worker_name.lower())

        elif action == "4":
            worker_name = input("Nama pegawai yang akan dipecat: ")
            manager.fire_worker(worker_name.lower())

        elif action == "5":
            print(f"{'-' * 32}\nBerhenti mengawasi hotel, sampai jumpa!\n{'-' * 32}")
            exit()

        print()
    print(f"{'=' * 30}\nStamina manager sudah habis, sampai jumpa!\n{'=' * 30}")


if __name__ == "__main__":
    main()
