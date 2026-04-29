while True:
    amount = int(input("\nEnter the amount to be withdrawn: "))

    fifity_notes = amount // 50
    twenty_notes = (amount % 50) // 20
    ten_notes = ((amount % 50) % 20) // 10
    one_notes = ((amount % 50) % 20) % 10

    print(f"\nYou will receive: \n{fifity_notes}x $50 notes \n{twenty_notes}x $20 notes \n{ten_notes}x $10 notes \n{one_notes}x $1 notes")
