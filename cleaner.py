def clean_data(data):
    cleaned = []
    seen = set()

    for title, price in data:
        title = title.lower().strip()
        price = price.replace("₹", "").strip()

        if title not in seen:
            seen.add(title)
            cleaned.append((title, price))

    return cleaned