import json
import random
import sys


def get_winner(filename='result.json', message_id=175):
    with open(filename, "r", encoding='utf-8') as f:
        data = json.loads(f.read())

        unique_users = set()
        user_name_by_id = {}

        for i in data["messages"]:
            if i.get("reply_to_message_id") == message_id:
                user_name_by_id[i["from_id"]] = f'{i["from_id"]}: {i["from"]}'
                unique_users.add(i["from_id"])

        users_cnt = len(unique_users)

        while users_cnt >= 3:
            unique_users = random.sample(list(unique_users), k=users_cnt)

            print("Возможно им повезёт! \n")
            for i in unique_users:
                print(user_name_by_id[i])
            print("")

            print(f"Текущее количество участников {users_cnt}!")
            input("Нажми enter чтобы уменьшить его вдвое!")
            users_cnt = int(users_cnt / 2)

        print("")
        print(f"Финал! Количество участников {users_cnt}")
        unique_users = random.sample(unique_users, k=users_cnt)
        for i in unique_users:
            print(user_name_by_id[i])

        print("")
        input("Нажми Enter чтобы определить победителя! \n")
        winner = random.sample(unique_users, k=1)[0]
        print(f"Победил пользователь с ID и именем: {user_name_by_id[winner]}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f"message {sys.argv[1]}")
    get_winner(message_id=int(sys.argv[1]))
