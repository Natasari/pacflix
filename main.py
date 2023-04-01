
import datetime as dt
from datetime import date
from plan import Plan
from plan import basic_plan, standard_plan, premium_plan
from plan import list_plan
from user import User

numb_people = int(input("Masukkan jumlah orang : "))
list_user = []

for i in range(numb_people):
    user_u = input("Masukkan username baru: ")
    plan_u = input("Pilih plan (basic/standard/premium): ").lower()
    ref_u = input("Referral code (jika ada): ")

    temp_plan = None
    try:
        if plan_u == 'basic':
            temp_plan = basic_plan
        elif plan_u == 'standard':
            temp_plan = standard_plan
        elif plan_u == 'premium':
            temp_plan = premium_plan
        else:
            raise Exception("Plan tidak tersedia")
    except Exception as e:
        print(e)
    else:
        user = User(user_u, temp_plan, date.today())
        list_user.append(user)
        if ref_u != '':
            valid, message = user.redeem(ref_u)
            if valid: 
                print(f"Anda berhasil melakukan redeem, tagihan Anda sebesar Rp {message}")
            else:
                print(message)
        print(user)