from . import wks
from .user import User
import datetime


def save_info(user: User):
    """Save user info to google sheet"""
    lenght = int(len(wks.get_all_records())) + 2
    # wks.update_value(f'A{lenght}', str(datetime.datetime.now()))
    wks.update_value(f'A{lenght}', f'https://vk.com/id{user.get_uid()}')
    wks.update_value(f'B{lenght}', user.get_name())
    wks.update_value(f'C{lenght}', user.get_faculty())
    wks.update_value(f'D{lenght}', user.get_group())
    wks.update_value(f'E{lenght}', user.get_why())
    wks.update_value(f'F{lenght}', user.get_other_group())
    wks.update_value(f'G{lenght}', user.get_old_group())
    wks.update_value(f'H{lenght}', user.get_department())
    wks.update_value(f'I{lenght}', str(datetime.datetime.now()))
