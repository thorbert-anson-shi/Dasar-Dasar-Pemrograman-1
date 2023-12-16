def main():
    # Mongkonversikan input user menjadi 2 dictionary,
    # dictionary parent_to_child, dan child_to_parent
    name_list = process_inputs()
    relations = process_relations(name_list)
    par_to_child = relations[0]
    child_to_par = relations[1]

    while True:
        print("""=====================================================================
Selamat Datang di Relation Finder! Pilihan yang tersedia:
1. CEK_KETURUNAN
2. CETAK_KETURUNAN
3. JARAK_GENERASI
4. EXIT
""")
        action = input("Masukkan pilihan: ")
        if action == "1":
            parent = input("Masukkan nama parent: ")
            child = input("Masukkan nama child: ")
            # Jika child tidak ada dalam list child_to_par, maka ia pasti tidak memiliki parent
            if child not in child_to_par:
                print(f"{child} bukan merupakan keturunan dari {parent}")
            else:
                # Mem-print message tergantung dengan jika child adalah keturunan parent
                if check_descendance(child_to_par, parent, child):
                    print(f"{child} benar merupakan keturunan dari {parent}")
                else:
                    print(f"{child} bukan merupakan keturunan dari {parent}")
        elif action == "2":
            parent = input("Masukkan nama parent: ")
            print_descendants(par_to_child, [parent], parent)
        elif action == "3":
            parent = input("Masukkan nama parent: ")
            child = input("Masukkan nama child: ")
            # Menjalankan fungsi get_generation_dist hanya apabila sudah dikonfirmasi
            # kalau parent dan child memiliki hubungan keturunan
            if parent == child:
                print(f"{child} memiliki hubungan dengan {parent} sejauh 0")
            elif child not in child_to_par:
                print("Child does not exist")
            elif check_descendance(child_to_par, parent, child):
                print(f"{child} memiliki hubungan dengan {parent} sejauh {get_generation_dist(child_to_par, parent, child)}")
            else:
                print("No connection")
        elif action == "4":
            print("""=====================================================================
Terima kasih telah menggunakan Relation Finder!
""")
            exit()
            
def check_descendance(child_to_par:dict, search:str, ch:str):
    # Base case: Jika orang yang dicari merupakan parent child, return True
    if child_to_par[ch] == search:
        return 1
    # Jika parent seorang child tidak memiliki parent, parent tersebut adalah parent paling buyut
    # Jika belum ada hubungan dengan parent paling buyut, maka child dan target tidak berhubungan keturunan
    if child_to_par[ch] not in child_to_par:
        return 0
    return check_descendance(child_to_par, search, child_to_par[ch])
    
    

def print_descendants(par_to_child:dict, descendants:list=[], src=""):
    children = []

    # Jika setiap child dari parent merupakan parent, append anak-anak parent tersebut ke list children
    for parent in descendants:
        if parent in par_to_child:
            children.extend(par_to_child[parent])
    
    # Base case: Jika child dari parent bukan merupakan parent, maka list tidak diubah
    if descendants == []:
        return

    # Mencegah program dari mencetak orang yang ingin dicari keturunannya
    if src in descendants:
        pass
    else:
        print("-", end=" ")
        [print(f"{descendants[i]} ", end="") for i in range(len(descendants))]
        print()
    
    print_descendants(par_to_child, children, src)


def get_generation_dist(child_to_par:dict, search:str, ch:str, gen_dist=1):
    # Base case: jika orang yang dicari adalah parent dari child, maka gen_dist tidak diincrement dan di return
    if search == child_to_par[ch]:
        return gen_dist
    else:
        # Increment gen_dist sampai menemukan target pencarian
        return get_generation_dist(child_to_par, search, child_to_par[ch], gen_dist + 1)
    

def process_inputs():
    """Memproses pasangan parent-child menjadi tuple untuk di append ke name_list"""
    print("Masukkan data relasi:")
    name_list = []
    while True:
        inp = input()
        if inp == "SELESAI":
            break
        i = inp.split()
        name_list.append((i[0], i[1]))

    return name_list

def process_relations(pairs:list, child_to_par={}, par_to_child={}):
    for pair in pairs:
        # Memodifikasi list child to parent
        child_to_par[pair[1]] = pair[0]

        # Memodifikasi list parent to child
        if pair[0] in par_to_child:
            par_to_child[pair[0]].append(pair[1])
        else:
            par_to_child[pair[0]] = [pair[1]]

    return par_to_child, child_to_par

if __name__ == "__main__":
    main()
        




