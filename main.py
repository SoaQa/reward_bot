import json
import random
import sys


    
def get_winner(message_id, winners_count=1, filename='result.json'):
    def print_winner(id_for_print: int):
        winner = user_data_by_id[id_for_print]
        print(f"{id_for_print}:{winner['from']} победил!")
        print(f"С сообщением: {winner['date']} {winner['text']}", end="\n\n\n")

    with open(filename, "r", encoding='utf-8') as f:
        data = json.loads(f.read())
        unique_user_ids = set()
        user_data_by_id = {}

        for message in data["messages"]:
            if message.get("reply_to_message_id") == message_id and message["from_id"] not in unique_user_ids:
                user_data_by_id[message["from_id"]] = {
                    "from": message["from"],
                    "text": message["text"],
                    "date": message["date"],
                }
                unique_user_ids.add(message["from_id"])

        users_cnt = len(unique_user_ids)

        print("Уникальных участников ", users_cnt)
        
        if 1 < winners_count < users_cnt:
            input(f"Нажмите enter чтобы выбрать {winners_count} победителей!\n")
            winner_ids = random.sample(list(unique_user_ids), winners_count)
            for winner_id in winner_ids:
                print_winner(winner_id)

        elif winners_count == 1 < users_cnt:
            input("Нажмите enter чтобы выбрать победителя!\n")
            winner_id = random.choice(list(unique_user_ids))
            print_winner(winner_id)

        else:
            ValueError(f"Количество победителей не верно {winners_count}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_winner(int(sys.argv[1]), int(sys.argv[2]) if len(sys.argv) == 3 else 1)
