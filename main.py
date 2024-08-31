import json
import random
import sys


def get_winner(message_id, filename='result.json'):

    with open(filename, "r", encoding='utf-8') as f:
        data = json.loads(f.read())
        unique_users = set()
        user_name_by_id = {}

        for message in data["messages"]:
            if message.get("reply_to_message_id") == message_id:
                user_name_by_id[message["from_id"]] = {
                    "from": message["from"],
                    "text": message["text"],
                }
                unique_users.add(message["from_id"])

        users_cnt = len(unique_users)

        print("Уникальных участников ", users_cnt)
        input("Нажмите enter чтобы выбрать победителя!")

        winner = random.choice(list(unique_users))
        print(f"{winner}:{user_name_by_id[winner]['from']} победил!")
        print(f"С сообщением: {user_name_by_id[winner]['text']}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_winner(int(sys.argv[1]))
