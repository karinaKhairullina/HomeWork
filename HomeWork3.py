import csv
import datetime

messages_of_social_network=[]
id_from = []
messages= []
class User:
    def init(self, id, name, second_name, age, gender):
        self.id = id
        self.name = name
        self.second_name = second_name
        self.age = age
        self.gender = gender

    def repr(self):
        return f'{self.name}, {self.second_name}'

    def get_dict_from_user(self):
        return {
            'id': self.id,
            'name': self.name,
            'second_name': self.second_name,
            'age': self.age,
            'gender': self.gender,
        }

class UsersData:
    def init(self, file_path, columns):
        self.file_path = file_path
        self.columns = columns
        self.count = 0

    def clear(self): #чистим файл
        with open(self.file_path, 'w') as file:
            pass

    def add_user(self, user_obj):
        with open(self.file_path, 'a') as file:
            writer = csv.DictWriter(
                file, delimiter=';', fieldnames=self.columns)
            writer.writerow(user_obj.get_dict_from_user())

    def send_message(self, user1, user2, text_sms):
        id_from.append(user1.id)
        messages_of_social_network.append(text_sms)

        with open(self.file_path, 'a') as file:
            fieldnames = ['who_send', 'to_send', 'time', 'text']
            now = datetime.datetime.now()
            now=now.strftime('%H:%M %d/%m') #чтоб норм выводилась гадость
            writer = csv.DictWriter(
                file, delimiter=';', fieldnames=fieldnames)
            if self.count == 0:
                writer.writeheader()
                self.count = 1
            writer.writerow(
                {
                    'who_send': user1,
                    'to_send': user2,
                    'time': now,
                    'text': text_sms
                }

            )

    def delete_user(self, user_id):
        users_list_csv = self.get_list_of_users()
        index = None
        for idx, user in enumerate(users_list_csv):
            if int(user['id']) == user_id:
                index = idx
        if index is not None:
            users_list_csv.pop(index)
            with open(self.file_path, 'w') as file:
                writer = csv.DictWriter(
                    file, delimiter=';', fieldnames=self.columns)
                writer.writerows(users_list_csv)
        else:
            raise Exception(f'cant find user with id {user_id}')

    def get_list_of_users(self):
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(
                file, delimiter=';', fieldnames=self.columns)
            return [line for line in reader]

    def out_messages(self):
        with open(self.file_path, 'a') as file:
            fieldnames = ['all_messages']
            writer = csv.DictWriter(
                file, delimiter=';', fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(
                {'all_messages': messages_of_social_network})



    def get_user(self, user_id):
        with open(self.file_path, 'r') as file:
            user = None
            reader = csv.DictReader(
                file, delimiter=';', fieldnames=self.columns)

            for user_csv in reader:
                if int(user_csv['id']) == user_id:
                    user = user_csv

            return user

    def get_messages(self, userid, user2id): #по айди
        dictionary = []
        if userid in id_from and user2id in id_from:
            dictionary.append(messages_of_social_network[userid-1])
            dictionary.append(messages_of_social_network[user2id-1])
            with open(self.file_path, 'a') as file:
                fieldnames = ['messages_between']
                writer = csv.DictWriter(
                    file, delimiter=';', fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(
                    {'messages_between': dictionary})

        else:
            pass


data_obj = UsersData(
    'users1.csv', ['id', 'name', 'second_name', 'age', 'gender', 'text'])

user1 = User(1, 'Karina', 'Khairullina', 18, 'women')
user2 = User(2, 'Rumiya', 'Salfhova', 19, 'women)
data_obj.add_user(user1)
data_obj.add_user(user2)
data_obj.send_message(user1, user2, 'Hello, how are you')
data_obj.send_message(user2, user1, 'fine')
data_obj.out_messages()
data_obj.get_messages(1, 2)
print(id_from, messages_of_social_network)
