class List:
    _all_list = {}

    def __new__(cls, lname): #Check and create class
        key = lname
        if key not in cls._all_list:#check if class has been created
            instance = super().__new__(cls)
            instance.lname = lname
            instance.item_bucket = []
            cls._all_list[key] = instance
        return cls._all_list[key]

    def add_item(self, itm):#add item to list bucket
        for i in self.item_bucket:
            if i["name"] == itm.name:
                i["amount"] += itm.amount
                return
        self.item_bucket.append(itm.return_item())

    def remove_item_amt(self, itm):#remove item from list bucket
        for i in self.item_bucket:
            if i["name"] == itm.name:
                i["amount"] -= itm.amount
                if i["amount"] <= 0:
                    self.item_bucket.remove(i)

    def delete_item(self, itm_name):
        for itm in self.item_bucket:
            if itm["name"] == itm_name:
                i = itm
                self.item_bucket.remove(i)

    def return_list(self):#return str of list
        return {"lname": self.lname, "bucket": self.item_bucket}

    def return_bucket(self):#return bucket
        return self.item_bucket

    def check_bucket(self, itm_name):#Check bucket for item
        for itm in self.item_bucket:
            if itm_name == itm["name"]:
                return itm["name"]
        print(f"{itm_name} not in List: {self.lname}")

    @classmethod
    def get_all_lnames(cls): #return dict with all list names
        list_all = []
        for key, instance in cls._all_list.items():
            list_all.append({"LIST NAME": instance.lname})
        return list_all

    @classmethod
    def get_all(cls):#return all instances
        list_all = []
        for key, instance in cls._all_list.items():
            list_all.append(instance.return_list())
        return list_all

    @classmethod
    def get_list(cls, listname):#return single instance of list
        for key, instance in cls._all_list.items():
            if listname == instance.lname:
                return instance.return_list()

    @classmethod
    def get_csv_data(cls):#Format the data to csv
        all_lists = cls.get_all()
        all_items = []
        for lst in all_lists:
            lname = lst["lname"]
            item_bucket = lst["bucket"]
            for item in item_bucket:
                i = {"lname": lname, "name": item["name"], "amount": item["amount"]}
                all_items.append(i)
        return all_items

    @classmethod
    def delete_list(cls, lname):
        if lname in cls._all_list:
            del cls._all_list[lname]
        else:
            print(f"'{lname}' does not exist")


# CLASS FOR THE ITEMS
class Item:
    def __init__(self, name, amount):
        if not name:
            raise ValueError("Invalid Item name")
        self.name = name
        self.amount = amount

    @property
    def name(self): #name
        return self._name

    @name.setter
    def name(self, name): #name setter
        if not name:
            raise ValueError("Invalid Item name")
        self._name = name

    def __str__(self):
        return f"{self.name}: {self.amount}"

    def return_item(self):
        return {"name": self.name, "amount": self.amount}

    @property
    def amount(self): #amount
        return self._amount

    @amount.setter
    def amount(self, amount): #amount setter
        try:
            if not isinstance(amount, int):
                amount = int(amount)
            self._amount = amount
        except Exception:
            raise ValueError("Invalid Input: Must be an int")
