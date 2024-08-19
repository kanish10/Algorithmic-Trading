def select_market():
    markets = {
        1: 'USA',
        2: 'India',
        3: 'Canada',
        3: 'Japan',
        4: 'Korea'
    }

    print("Select the market for algorithmic trading:")
    for key, value in markets.items():
        print(f"{key}: {value}")

    choice = int(input("Enter the number corresponding to your choice: "))

    selected_market = markets.get(choice, 'USA')
    print(f"Market selected: {selected_market}")

    return selected_market


if __name__ == "__main__":
    market = select_market()
    # Store the selected market or pass it to the next part of your workflow
