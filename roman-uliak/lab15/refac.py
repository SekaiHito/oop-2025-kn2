#неправильно
def print_user_info(user):
    print("User information:")
    print("Name:", user.name)
    print("Email:", user.email)
    print("Length of name:", len(user.name))

#правильно
def format_user_info(user):
    return (
        f"Name: {user.name}\n"
        f"Email: {user.email}\n"
        f"Length of name: {len(user.name)}"
    )

def print_user_info(user):
    print("User information:")
    print(format_user_info(user))
