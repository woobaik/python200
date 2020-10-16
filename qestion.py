def delete_from_dict(a, *b):
    if not isinstance(a, dict):
        print(f"You need to send a dictionary. You sent: {type(a)}")
        return

    if len(b) != 1:
        print("You need to specify a word to delete.")

    else:
        if b[0] in a:
            del a[b[0]]
            print(f"{b[0]} has been deleted.")
        else:
            print(f"{b[0]} is not in dict. Won't delete.")
