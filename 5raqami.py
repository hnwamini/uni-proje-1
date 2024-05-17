def reverse_decimal_number(number):
    if len(number) == 1:
        return number
    else:
        return number [-1] + reverse_decimal_number(number[:-1])
#ورودی را دریافت کنید
decimal_number = input("adad 5raqami ashari vared konid")

while len(decimal_number) < 5:
    decimal_number = input("vorodi bayd hadaghl 5raqami bashd,dobare adad vared konid")

reversed_number =
reverse_decimal_number(decimal_number)
print("عدد وارونه:", reversed_number)
