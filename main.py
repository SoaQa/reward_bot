import json
import random


winners_cnt = 4
message_id = 1101


def get_winner(filename='result.json'):

    assert message_id is not None

    with open(filename, "r", encoding='utf-8') as f:
        data = json.loads(f.read())

        unique_users = set()
        user_name_by_id = {}

        for message in data["messages"]:
            if message.get("reply_to_message_id") == message_id:
                user_name_by_id[message["from_id"]] = message["from"]
                unique_users.add(message["from_id"])

        users_cnt = len(unique_users)

        print("Уникльных участников ", users_cnt)

        input("Нажми Enter чтобы получить случайных 4 победителей!")

        for i in random.sample(list(unique_users), k=winners_cnt):
            print(i, " ", user_name_by_id[i])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_winner()
