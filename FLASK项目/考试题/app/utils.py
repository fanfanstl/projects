from django.db.models import Q

from app.models import UserModel


def get_user(user_ident):
    if not user_ident:
        return None
    user = UserModel.objects.filter(Q(phone=user_ident) & Q(is_delete=False)).first()
    if user:
        return user
    user = UserModel.objects.filter(Q(mail=user_ident) & Q(is_delete=False)).first()
    if user:
        return user
    try:
        user = UserModel.objects.filter(Q(id=user_ident) & Q(is_delete=False)).first()
        if user:
            return user
    except:
        return None
    return None
