#คำสั่ง break, continue
#break ใน loop จะเป็นการหยุดการทำงานของ loop ทันที
#continue ใน loop ทำงานเมื่อใดจบ loop แค่รอบนั้นทันที แล้วให้ไปรอบต่อไปเลย

for i in range(5):
    if aa == 2:
        break
    print(aa, 'hi..')

print('++++++++++++++++')
for aa in range(5):
    if aa == 2:
        continue
    print(aa, 'hi..')
        