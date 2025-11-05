def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67,32)")


def get_user_input():
    data = input("Enter temperature values: ")

    temp_list = data.split(",")
    temp_list = [float(i) for i in temp_list]
    return temp_list


def calc_average_temperature(temp_list):
    return sum(temp_list) / len(temp_list)


def calc_min_max_temperature(temp_list):
    return [min(temp_list), max(temp_list)]


def sort_temperature(temp_list):
    return sorted(temp_list)


def calc_median_temperature(temp_list):
    sorted_list = sort_temperature(temp_list)
    n = len(sorted_list)
    mid = n // 2


    if n % 2 == 1:
        return sorted_list[mid]
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2



def main():
    display_main_menu()
    temp_list = get_user_input()

    avg = calc_average_temperature(temp_list)
    min_max = calc_min_max_temperature(temp_list)
    median = calc_median_temperature(temp_list)
    sorted_list = sort_temperature(temp_list)

    print("Sorted temperatures:", sorted_list)
    print("Average temperature:", avg)
    print("Minimum, Maximum temperature:", min_max)
    print("Median temperature:", median)


if __name__ == "__main__":
    main()
