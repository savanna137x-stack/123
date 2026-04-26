import random
def generate_house():
    price_val = random.randint(5000, 500000)
    square_val = round(random.uniform(20.0, 300.0), 1)
    return {
        "price": f"{price_val}$",
        "square": f"{square_val}m",
        "price_val": price_val,
        "square_val": square_val
    }

def generate_houses_random_count(min_count=50, max_count=200):
    count = random.randint(min_count, max_count)
    return [generate_house() for _ in range(count)]

def generate_buyer(full_name: str = None, account_val: int = None):
    names = ["Ivan Ivanov", "Petr Petrov", "Anna Sidorova", "Olga Kuznetsova", "Sergey Smirnov", "Maria Ivanova"]
    if full_name is None:
        full_name = random.choice(names)
    if account_val is None:
        account_val = random.randint(10000, 500000)
    return {
        "full_name": full_name,
        "account": f"{account_val}$",
        "account_val": account_val
    }

def select_best_house_for_buyer(houses, buyer):
    budget = buyer.get("account_val", 0)
    affordable = [x for x in houses if x["price_val"] <= budget]
    if not affordable:
        return None
    best = sorted(affordable, key=lambda h: (-h["square_val"], h["price_val"]))[0]
    return {"price": best["price"], "square": best["square"]}

if __name__ == "__main__":
    houses = generate_houses_random_count(50, 200)
    buyer = generate_buyer("Anna Sidorova", 150000)
    best_house = select_best_house_for_buyer(houses, buyer)
    print({"houses_count": len(houses), "buyer": {"full_name": buyer["full_name"], "account": buyer["account"]}, "best_house": best_house})