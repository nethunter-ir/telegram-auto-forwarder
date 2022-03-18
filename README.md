# فورواردر خودکار تلگرام

با استفاده از این برنامه‌ی پایتون، شما می‌توانید تمام پیام‌های جدید خود در چت‌ها، گروه‌ها یا کانال‌ها را به بخش "پیام‌های ذخیره شده" یا چت ، گروه یا کانال دیگر بفرستید.


## طریقه استفاده
همانطور که گفته شد، این برنامه با استفاده از "پایتون" نوشته شده است و برای استفاده از آن، کافی است که آن را به عنوان یک برنامه‌ی پایتون در "ترمینال لینوکس" یا "خط فرمان ویندوز" اجرا کنید.

پس از اولین اجرا و وارد کردن شماره تلفن و کد تأیید تلگرام و پیکربندی‌ها، در اجراهای بعدی، زمانی که برنامه در حال همگامسازی پایگاه‌داده‌ی خود با سرور است و پیام‌های جدید را نسبت به وضعیت خود دریافت میکند، پیام‌های جدید دریافت شده، به چت مورد نظر شما فرستاده میشوند.

```bash
python telefor.py
```

پس از اجرای برنامه، دو گزینه به کاربر نمایش داده میشود که برای ادامه‌ی کار، باید یکی از آن‌ها انتخاب شود.

```bash
Please select run mode:
'1' -> One Time Use
'9' -> Always On : 
```

در صورت انتخاب اولین گزینه(شماره ۱) در برنامه، هنگامی که برنامه و سرور همگامسازی شدند و پیام جدیدی برای مدتی دریافت نشد، برنامه بطور خودکار بسته میشود.

پ.ن:(این برنامه در داخل خود یک شمارنده‌ی داخلی دارد که تا "۱۰۰" میشمارد و در صورت دریافت هر پیام جدید، "۰" میشود. )

با انتخاب دومین گزینه(شماره ۹) پس از اتمام همگامسازی پیام‌های جدید، برنامه همچنان به کارش ادامه میدهد و منتظر دریافت پیام‌های جدید میماند.


پس از انتخاب یک گزینه در بخش قبل، سه گزینه‌ی دیگر به کاربر نمایش داده میشود که برای ادامه‌ی کار، باید یکی از آن‌ها انتخاب شود.

```bash
Please select run mode:
'1' -> Sync
'5' -> Sync & View
'9' -> Sync & View & Forward :
```

در صورت انتخاب اولین گزینه(شماره ۱) در برنامه، پیام‌های جدید، فقط با سرور همگامسازی می‌شوند و هیچ پیامی ارسال یا تیک خورده نمی‌شود.

با انتخاب دومین گزینه(شماره ۵) می‌توان از این برنامه برای ثبت مشاهده‌ی پیام‌ها(تیک دوم) و همگامسازی با سرور نیز استفاده کرد.

با انتخاب سومین گزینه(شماره ۹) می‌توان علاوه بر همگامسازی و ثبت مشاهده(تیک) برای پیام‌ها، آن‌ها را به محل مورد نظر نیز ارسال کرد.



(در صورتی که در شبکه‌ی شما، تلگرام فیلتر است، پس از چند ثانیه از شروع به کار برنامه، این شمارشگر بطور خودکار راه میافتد. )

# نکات
برای دریافت کدهای

"api_id" و "hash_id"

باید ابتدا به نشانی زیر بروید

https://my.telegram.org

و سپس وارد گزینه‌ی

"API development tools"

بشوید و فرم به نمایش در آمده را پر کنید.


سپس برای دریافت

"chat_id"

مورد نظرتان، می‌توانید در حسابتان در "تلگرام دسکتاپ" وارد شوید و سپس وارد چت، گروه یا کانال مورد نظر برای فوروارد پیام‌های جدید شوید و سپس بخشی از لینک که در مثالهای زیر، "1" است را کپی کنید

https://web.telegram.org/#/im?p=c1111111111_00000000000000000000

https://web.telegram.org/#/im?p=u111111111_00000000000000000000

https://web.telegram.org/#/im?p=g111111111

برای وارد کردن آی‌دی کانال‌ها، باید در ابتدای آی‌دی کانال، مقدار "100-" را نیز وارد کرد. برای مثال اگر آی‌دی کانال شما برای ارسال مطالب "1111111111" است، باید آن را به صورت "1001111111111-" در برنامه وارد کنید.

ممکن است در لینوکس نیاز باشد برای اجرای برنامه

glibc

را نصب کنید.

اگر تلگرام برای شما فیلتر است، از VPN یا Proxy استفاده کنید.

# مشارکت
مشتاق درخواست‌های شما برای تغییرات هستیم. البته برای تغییرات بزرگ، ممکن است نیاز به بحث و گفتگو باشد.

لطفاً از صحت عملکرد بروزرسانی‌ها، پیش از ارسال درخواست، اطمینان حاصل شود.

# مجوز
[بوست](https://choosealicense.com/licenses/bsl-1.0/)

#

# Telegram Auto Forwarder

With This Python app, You Can Forward All New Recived Messages From Chats, Groups or Channels to You'r "Saved Messages" Or Other Chat, Group or Channel.


## How Use

As Mentioned, This Project Written With "Python" and Just You Should run it as a Python Progarm From "Terminal" in "Linux" or "CMD" in "Windows" .

After First Run And Entering Phone Number and Confirm Code And Configs, in Next Executes, When App is Syncing Own Database With server And Receives New Messages According To Its Status, New Messages Forward To Target Chat.

```bash
python telefor.py
```
After Execute App, Two Options Are Displayed To The User That For Continue, Should Select One of Them.

```bash
Please select run mode:
'1' -> One Time Use
'9' -> Always On : 
```

After Select The First Option(Number 1) in App, When App And Server Were Synced And No New Message Were Recived For Some Time, App Will Closed Automatically.

P.S:(This App Has a Internal Counter That counts to "100" And In case of Recive Every New Message, it Becomes "0" . )

After Select The Second Option(Number 9) in App, When App And Server Were Synced, App Continue Working And Wait for Recive New Message.

After Select a Option in Previous Section, Three Options Are Displayed To The User That For Continue, Should Select One of Them.

```bash
Please select run mode:
'1' -> Sync
'5' -> Sync & View
'9' -> Sync & View & Forward :
```

After Select The First Option(Number 1) in App, New Messages Just Will Sync With Server, And No Message Will Not Forward or Seen.

After Select The Second Option(Number 5) in App,  New Messages Will Sync With Server, And Messages Will Seen(Second tick).

After Select The third Option(Number 9) in App,  New Messages Will Sync With Server, And Messages Will Forward And Seen(Second tick).

## Tips

For Recive You'r Telegram "api_id" and "hash_id" , You Can Go To This Link:

https://my.telegram.org

And Go to "API development tools" And Complite The Form. 

For Recive You'r Target "chat_id" , You Can Login To Your Account In "Telegram Web" And Go To You'r Target Chat, Group or Channel For Forward New Messages And Copy Just This Part Of URL That is "1" Similar To The Following Examples ↓:

https://web.telegram.org/#/im?p=c1111111111_00000000000000000000

https://web.telegram.org/#/im?p=u111111111_00000000000000000000

https://web.telegram.org/#/im?p=g111111111


For Entering Channel's id, You Should Add "-100" To The Beginning of The Address. For Example, if Your Channel's id For Forwarding is "1111111111" , You Should Enter "-1001111111111" in App.

in Linux, You May Need To Install "glibc" For Run This App.

if Telegram is Filtered For You, Use VPN or Proxy.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Boost](https://choosealicense.com/licenses/bsl-1.0/)
