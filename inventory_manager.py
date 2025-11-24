import pandas as pd
import os

DATA_FILE = "inventory.csv"

def load_inventory():
    # load the csv if there's one, otherwise just return an empty table
    if os.path.isfile(DATA_FILE):
        try:
            df = pd.read_csv(DATA_FILE)
        except Exception:
            # if file is broken or something, just reset it
            print("Couldn't read file, starting new list.")
            df = pd.DataFrame(columns=["item", "quantity"])
        return df
    else:
        # no file to load
        return pd.DataFrame(columns=["item", "quantity"])


def save_inventory(df):
    # TODO: probably should handle errors but works for now
    df.to_csv(DATA_FILE, index=False)
    print("Saved.")


def add_item(df):
    name = input("Item name: ").strip().lower()

    q = input("Quantity: ").strip()
    try:
        q = int(q)
    except ValueError:
        print("Quantity must be a number.")
        return df

    # update if already exists
    if name in df["item"].values:
        # it's a bit ugly but works
        df.loc[df["item"] == name, "quantity"] = df.loc[df["item"] == name, "quantity"] + q
    else:
        idx = df.index.max() + 1 if len(df) else 0
        df.loc[idx] = [name, q]

    print("Done.")
    return df


def remove_item(df):
    target = input("Remove which item: ").strip().lower()
    if target in df["item"].values:
        df = df[df["item"] != target]
        print("Removed.")
    else:
        print("Item not found.")
    return df


def update_quantity(df):
    name = input("Item to update: ").strip().lower()

    if name not in df["item"].values:
        print("Doesn't exist.")
        return df

    new_q = input("New quantity: ").strip()
    try:
        new_q = int(new_q)
    except:
        print("Invalid number.")
        return df

    df.loc[df["item"] == name, "quantity"] = new_q
    print("Updated.")
    return df


def search_item(df):
    name = input("Search for: ").strip().lower()
    row = df[df["item"] == name]
    if len(row):
        print(row)
    else:
        print("Nothing found.")


def view_inventory(df):
    if df.empty:
        print("No items.")
    else:
        print(df)


def main():
    inv = load_inventory()

    while True:
        print()
        print("1 add")
        print("2 remove")
        print("3 update qty")
        print("4 view")
        print("5 search")
        print("6 quit")

        choice = input("Choice: ").strip()

        if choice == "1":
            inv = add_item(inv)
        elif choice == "2":
            inv = remove_item(inv)
        elif choice == "3":
            inv = update_quantity(inv)
        elif choice == "4":
            view_inventory(inv)
        elif choice == "5":
            search_item(inv)
        elif choice == "6":
            save_inventory(inv)
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
