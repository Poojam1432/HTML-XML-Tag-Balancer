from pda import check_balance


def main():
    print("HTML / XML Tag Balancer")
    print("------------------------------")

    html = input("Enter your HTML: ")

    result = check_balance(html)

    if result["balanced"]:
        print("BALANCED: All tags are properly nested.")
    else:
        print("IMBALANCED")
        print("Error:", result["error"])

    print("Opening tags processed:", result["opening_tags_count"])


if __name__ == "__main__":
    main()