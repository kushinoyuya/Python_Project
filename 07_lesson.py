import re

print("##########演習7-1##########")
def test_password(text):
    test_length = re.match(re.compile(r'.{8,}'), text)
    test_lower = re.search(re.compile(r'[a-z]'), text)
    test_upper = re.search(re.compile(r'[A-Z]'), text)
    test_number = re.search(re.compile(r'[0-9]'), text)
    if test_length:
        print('8文字以上：OK')
    else:
        print('8文字以上にしてください。')
    if test_lower:
        print('小文字英字を含む：OK')
    else:
        print('小文字英字を1文字以上含めてください。')
    if test_upper:
        print('大文字英字を含む：OK')
    else:
        print('大文字英字を1文字以上含めてください。')
    if test_number:
        print('数字を含む：OK')
    else:
        print('数字を1文字以上含めてください。')
    if test_length and test_lower and test_upper and test_number:
        print('パスワードの強度は大丈夫です！')
test_password('a1Aaaaaa')


print("##########演習7-2##########")
def test_password(text):
    test_length = re.match(re.compile(r'.{8,}'), text)
    test_characters = re.match(re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)'), text)
    if test_length:
        print('8文字以上：OK')
    else:
        print('8文字以上にしてください。')
    if test_characters:
        print('大文字小文字数字をそれぞれ1文字以上含む：OK')
    else:
        print('大文字小文字数字をそれぞれ1文字以上含めてください。')
    if test_length and test_characters:
        print('パスワードの強度はじゅうぶんです！')
test_password('a1Aaaaaa')


print("##########演習7-3##########")
def strip_text(text, *character):
    if character:
        l_regex = re.compile(r'^%s*' % character[0])
        r_regex = re.compile(r'%s*$' % character[0])
    else:
        l_regex = re.compile(r'^\s*')
        r_regex = re.compile(r'\s*$')
    text = l_regex.sub('', text)
    text = r_regex.sub('', text)
    print(text)

strip_text('    前後のスペース文字を取り除く    ')
strip_text('XXXX前後のXを取り除くXXXX', 'X')
