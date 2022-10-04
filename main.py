# This is a sample Python script.
from elastic_search_loader import load
from extract_info import start_extracting


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Start processing ....')
    directory = 'C:\\Users\\aligh\\OneDrive\\Desktop\\ulb\\pdf_data\\test\\CVs\\'
    output_file_name = "data.json"
    # start_extracting(directory=directory, output_file=output_file_name)
    load()
    print("finish processing")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
