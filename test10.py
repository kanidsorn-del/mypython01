# ============================
# Program  Average  5  Number
# ============================
# Enter number 1 : <input>
# Enter number 2 : <input>
# Enter number 3 : <input>
# Enter number 4 : <input>
# Enter number 5 : <input>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# ============================
# Program  Average  5  Number
# ============================
print('============================')
print('โปรแกรมคำนวณค่าเฉลี่ย 5 ตัวเลข')
print('============================')
num1 = float(input('ป้อนตัวเลขที่ 1 : '))
num2 = float(input('ป้อนตัวเลขที่ 2 : '))
num3 = float(input('ป้อนตัวเลขที่ 3 : '))
num4 = float(input('ป้อนตัวเลขที่ 4 : '))
num5 = float(input('ป้อนตัวเลขที่ 5 : '))
print('============================')
sum_of_numbers = num1 + num2 + num3 + num4 + num5
average_of_numbers = sum_of_numbers / 5
print(f'ผลรวมของ 5 ตัวเลขคือ : {sum_of_numbers}')
print(f'ค่าเฉลี่ยของ 5 ตัวเลขคือ : {average_of_numbers}')
print('============================')
# ใช้ , แสดงผล
print('============================')
print('ผลรวมของ 5 ตัวเลขคือ :', sum_of_numbers)
print('ค่าเฉลี่ยของ 5 ตัวเลขคือ :', average_of_numbers)
print('============================')
# ใช้ + แสดงผล
print('============================')
print('ผลรวมของ 5 ตัวเลขคือ : ' + str(sum_of_numbers))
print('ค่าเฉลี่ยของ 5 ตัวเลขคือ : ' + str(average_of_numbers))
print('============================')
# ใช้ format แสดงผล
print('============================')
print('ผลรวมของ 5 ตัวเลขคือ : {}'.format(sum_of_numbers))
print('ค่าเฉลี่ยของ 5 ตัวเลขคือ : {}'.format(average_of_numbers))
print('============================')
# ใช้ f-string แสดงผล
print('============================')
print(f'ผลรวมของ 5 ตัวเลขคือ : {sum_of_numbers}')
print(f'ค่าเฉลี่ยของ 5 ตัวเลขคือ : {average_of_numbers}')
print('============================')
# ใช้ f-string แสดงผล
print('============================')
print(f'ผลรวมของ 5 ตัวเลขคือ : {sum_of_numbers:.2f}')
print(f'ค่าเฉลี่ยของ 5 ตัวเลขคือ : {average_of_numbers:.2f}')
print('============================')
# ใช้ f-string แสดงผล
print('============================')
print(f'ผลรวมของ 5 ตัวเลขคือ : {sum_of_numbers:.3f}')
print(f'ค่าเฉลี่ยของ 5 ตัวเลขคือ : {average_of_numbers:.3f}')
print('============================')
# ใช้ f-string แสดงผล
print('============================')
print(f'ผลรวมของ 5 ตัวเลขคือ : {sum_of_numbers:.4f}')
print(f'ค่าเฉลี่ยของ 5 ตัวเลขคือ : {average_of_numbers:.4f}')
print('============================')
# ใช้ f-string แสดงผล
print('============================')
print(f'ผลรวมของ 5 ตัวเลขคือ : {sum_of_numbers:.5f}')
print(f'ค่าเฉลี่ยของ 5 ตัวเลขคือ : {average_of_numbers:.5f}')