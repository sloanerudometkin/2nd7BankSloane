class Transaction:
    def __init__(self, date: str, trans_type: str, amount: float):
        self.date = date
        self.type = trans_type.strip().lower()
        self.amount = amount
    
class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        self.balance = initial_balance

    def apply_transaction(self, transaction: Transaction):
        #applies a transaction to the account
        if transaction.type == "deposit":
            self.balance += transaction.amount
        elif transaction.type == "withdrawal":
            self.balance -= transaction.amount
        else:
            print(f"Warning: Unknown transaction type '{transaction.type}'... ignored.")

    def get_balance(self) -> float:
        #return current balance
        return self.balance
    
    def process_bank_file(file_name: str):
        #make new instance of bank account
        account = BankAccount

    #now i need to open and read the file line by line
        with open(file_name, 'r') as file:
            for line in file:
            #just in case there is empty lines
                if not line.strip():
                    continue
            #split the line
                date, trans_type, amount_str = line.strip(),split(",")
                amount = float(amount_str.strip())
        # transaction instance using the "Transaction" field in apply_transaction
                transaction = Transaction(date, trans_type, amount)
        #now apply it to the account
                account.apply_transaction(transaction)
        #now print the balance
        print(f"Final Balance: ${account.get_balance():.2f}")

    if __name__ == "__main__":
        process_bank_file("input data")

    

