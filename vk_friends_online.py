import vk
import getpass


api_id = 6286380    # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    login = str(input('Login: '))
    return login


def get_user_password():
    password = str(input('Password: '))
    return password


def get_online_friends(api_id, login, password):
    session = vk.AuthSession(
        app_id=api_id,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_online_ids = api.friends.getOnline()
    friends_online = api.users.get(user_ids=friends_online_ids)
    return friends_online


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend.get('first_name'), friend.get('last_name'))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(api_id, login, password)
    output_friends_to_console(friends_online)