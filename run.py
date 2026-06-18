# app/utils.py

import random
from datetime import datetime, timedelta

from .models import Client, deposite


GERMANY_BANKS = [
    "Deutsche Bank",
    "Commerzbank",
    "DZ Bank",
    "KfW Bank",
    "HypoVereinsbank",
    "Postbank",
    "N26",
    "Sparkasse",
    "Berliner Sparkasse",
    "Hamburger Sparkasse",
    "ING Germany",
    "DKB",
    "Santander Germany",
    "Aareal Bank",
    "Helaba",
    "BayernLB",
    "LBBW",
    "Oldenburgische Landesbank",
    "Targobank",
    "HSBC Germany",
]

GERMANY_CITIES = [
    "Berlin",
    "Frankfurt",
    "Munich",
    "Hamburg",
    "Cologne",
    "Dusseldorf",
    "Stuttgart",
    "Leipzig",
]


DESCRIPTIONS = [
    "International Transfer",
    "Salary Payment",
    "Online Purchase",
    "Bank Deposit",
    "Incoming Transfer",
    "Business Payment",
    "Card Payment",
]


def generate_demo_iban():

    checksum = random.randint(10, 99)

    bank_code = str(
        random.randint(10000000, 99999999)
    )

    customer_number = str(
        random.randint(1000000000, 9999999999)
    )

    return (
        f"DE{checksum}"
        f"{bank_code}"
        f"{customer_number}"
    )


def generate_transactions(account_number):

    try:

        client = Client.objects.get(
            AccountNUm=account_number
        )

    except Client.DoesNotExist:

        return "Client not found"

    start_date = datetime(2020, 1, 1)

    end_date = datetime.now()

    current_date = start_date

    created = 0

    while current_date <= end_date:

        bank = random.choice(
            GERMANY_BANKS
        )

        city = random.choice(
            GERMANY_CITIES
        )

        description = random.choice(
            DESCRIPTIONS
        )

        amount = random.randint(
            500,
            15000
        )

        deposit = deposite.objects.create(

            date=current_date,

            uuid=f"DEP{random.randint(100000000,999999999)}",

            amount=amount,

            approved=True,

            BankCountry="Germany",

            BankAddress=f"{city}, Germany",

            holdername=(
                client.user.get_full_name()
                or client.user.username
            ),

            swiftcode="DEUTDEFF",

            accountnumber=generate_demo_iban(),

            Currency="EUR",

            statedecr=description,

            bankname=bank,

            disc=description

        )

        client.deposite.add(
            deposit
        )

        created += 1

        current_date += timedelta(
            days=random.randint(5, 20)
        )

    return f"{created} transactions created"