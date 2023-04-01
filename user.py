# daftar library
import random
from dateutil.relativedelta import relativedelta
from tabulate import tabulate
from datetime import date

class User:

    __secret_code = ('2134', 'abcd', '2f9g', '9f92', '98hu', 'lp08', 'fd56', 'lk08')
    __list_refcod_user = {}

    def __init__(self, username, choosen_plan, register_date):
        self.username = username
        self.current_plan = choosen_plan
        self.register_date = register_date
        self.bill = self.current_plan.price
        self.referral_code = self.username + '-' + self.__secret_code[random.randint(0,7)]
        self.__list_refcod_user[self.username] = self.referral_code

    def upgrade_plan(self, new_plan):
        if new_plan.price <= self.current_plan.price:
            print("Anda tidak bisa melakukan upgrade, pilih plan yang lebih tinggi")
            return

        today = date.today()
        difference_in_years = relativedelta(today, self.register_date).years

        discount = 1
        if difference_in_years >= 1:
            discount = 0.95

        self.bill = new_plan.price * discount
        self.current_plan = new_plan
        return self.bill

    def redeem(self, code):
        if code in self.__list_refcod_user.values():
            self.bill = self.current_plan.price * 0.96
            return True, self.bill
        else:
            return False, "Referral code Anda tidak valid"

    def check_all_plan(self):
        for plan in list_plan:
            plan.check_plan()
            print("\n")

    def __str__(self):
        return tabulate([
            ['Username', self.username],
            ['Plan', self.current_plan.name],
            ['Register Date', self.register_date],
            ['Last Bill', self.bill],
            ['Referral Code', self.referral_code]
        ])

    def __add__(self, angka):
        return self.bill + angka