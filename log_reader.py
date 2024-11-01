def iterate_log_file():
    with open("log.txt", "r") as log_file:
        for line in log_file:
            array = eval(line.strip())  # Convert string back to array
            print(array)  # Process the array (replace with your actual processing)


if __name__ == "__main__":
    iterate_log_file()
