from movie_user.models import UserModel


def get_user(user_ident):
    if not user_ident:
        return None

    # 根据id
    user = UserModel.objects.filter(pk=user_ident).first()

    if user:
        return user

    user = UserModel.objects.filter(phone=user_ident).first()
    print(user_ident)

    if user:
        return user

    user = UserModel.objects.filter(username = user_ident).first()

    if user:
        return user

    return None