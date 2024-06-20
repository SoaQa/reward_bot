import json
import os
import random


winners_cnt = int(os.environ['WINNERS_CNT'])
message_id = int(os.environ['MESSAGE_ID'])


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

        print("Уникальных участников ", users_cnt)

        input(f"Нажми Enter чтобы получить случайных {winners_cnt} победителей!")

        for i in random.sample(list(unique_users), k=winners_cnt):
            print(i, " ", user_name_by_id[i])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_winner()
