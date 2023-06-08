import pandas as pd
from datetime import datetime


def read_data(filename):
    data = {}
    try:
        # Read data from csv file and set the UserId column as index,
        # transpose column and row, and then convert to dictionary
        data = pd.read_csv(filename, index_col=0).T.to_dict()
    # I choose to exit the program if any exception occurred when reading data from csv file
    except FileNotFoundError:
        # Handling file not found exception
        print(f'File {filename} not found')
        exit()
    except Exception as e:
        # Handling others exception
        print(f"An exception occurred: {str(e)}")
        exit()
    return data


def search_by_userid(userID: int):
    if userID in userData:
        return userData[userID]
    return 'User not found'


def search_by_username(username: str):
    for userId, user in userData.items():
        if user['Username'] == username:
            return user
    return 'User not found'


def calculate_age(userID: int):
    user = search_by_userid(userID)
    if type(user) is dict:
        # if user have a type of dictionary, it means that the user exist. Otherwise, user not exist
        # Pandas has automatically parsed the datetime and convert to the format 'YYYY-mm-dd' so I need to parse
        b_date = datetime.strptime(user['DateOfBirth'], '%Y-%m-%d')
        return round((datetime.today() - b_date).days / 365)
    else:
        # I choose to raise an exception here because it forces to handle the exception when calling this function
        # rather than return a fixed value e.g 0
        raise Exception('User not found')


if __name__ == '__main__':
    userData = read_data('./userdata.csv')
    existUser = search_by_userid(100)
    print(existUser)
    notExistUser = search_by_userid(-1000)
    print(notExistUser)
    existUserByUsername = search_by_username('Kenna.Abernon')
    print(existUserByUsername)
    notExistUserByUsername = search_by_username('Bryan.Pham')
    print(notExistUserByUsername)
    try:
        ageOfExistingUser = calculate_age(100)
        print(f'User age: {ageOfExistingUser}')
        ageOfNotExistingUser = calculate_age(-1000)
        print(f'User age: {ageOfNotExistingUser}')
    except:
        print('User not found')
