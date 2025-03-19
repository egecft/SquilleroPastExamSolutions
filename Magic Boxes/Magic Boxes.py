INPUT_FILE_NAME = "actions.txt"
# INPUT_FILE_NAME = "actions-simple.txt"
# INPUT_FILE_NAME = "actions-fail_bob.txt"
# INPUT_FILE_NAME = "actions-fail_carl.txt"


def read_actions():
    action_list = list()
    try:
        with open(INPUT_FILE_NAME, "r") as file:
            for line in file:
                clean_line = line.strip()
                splitted_line = clean_line.split()
                name = splitted_line[0]
                obect_name = splitted_line[-1]
                temp_list = [name, obect_name]
                action_list.append(temp_list)
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return action_list


def main():
    object_dict = dict()
    action_list = read_actions()
    value = True
    for action in action_list:
        if action[0] == "Bob":
            if (action[1] not in object_dict.keys()) and len(object_dict.keys()) < 42:
                object_dict[action[1]] = 1
                print(f"Alice stored a {action[1]}")
            elif (action[1] not in object_dict.keys()) and len(object_dict.keys()) >= 42:
                print(f"Alice cannot store a {action[1]}")
                value = False
                break
            elif action[1] in object_dict.keys():
                object_dict[action[1]] += 1
                print(f"Alice stored a {action[1]}")
        elif action[0] == "Carl":
            if action[1] not in object_dict.keys():
                print(f"Alice cannot give a {action[1]}")
                value = False
                break
            elif action[1] in object_dict.keys():
                if object_dict[action[1]] > 1:
                    object_dict[action[1]] -= 1
                    print(f"Alice gave a {action[1]}")
                elif object_dict[action[1]] == 1:
                    object_dict.pop(action[1])
                    print(f"Alice gave a {action[1]}")
    if value:
        print("\nAll good, no errors.")


if __name__ == "__main__":
    main()
