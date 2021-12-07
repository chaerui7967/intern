import sys
import chardet

word = '갉'

print(chardet.detect(word.encode()))
print(sys.getdefaultencoding())

encode_utf8 = word.encode('utf-8')
print(encode_utf8, type(encode_utf8))

encode_utf16 = word.encode('utf-16')
print(encode_utf16, type(encode_utf16))

encode_euckr = word.encode('euc-kr')
print(encode_euckr, type(encode_euckr))

encode_cp949 = word.encode('cp949')
print(encode_cp949, type(encode_cp949))


print(b'\xea\xb0\x80'.decode('utf8'))


# unicode
with open('unicode.txt', 'w') as f:

    count = 0
    for i in range(0xac00, 0xd7a4):
        if i % 15 == 0:
            f.write('\n')
            print()
        f.write(hex(i) + '|' + chr(i) + ' ')
        print(hex(i), '|', chr(i), end= ' ')


# support encoding
# ASCII, UTF-8, UTF-16 (2 변형), UTF-32 (4 변형)
# Big5, GB2312, EUC-TW, HZ-GB-2312, ISO-2022-CN (중국어 번체 및 간체) 
# EUC-JP, SHIFT_JIS, CP932, ISO-2022-JP (일본어) 
# EUC-KR, ISO-2022-KR (한국어) 
# KOI8-R, MacCyrillic, IBM855, IBM866, ISO-8859-5, windows-1251 (키릴 문자) 
# ISO-8859-2, windows-1250 (헝가리어) 
# ISO-8859-5, windows-1251 (불가리아어) 
# windows-1252 (영어) 
# ISO-8859-7, windows-1253 (그리스어) 
# ISO-8859-8, windows-1255 (시각적 및 논리적 히브리어) 
# TIS-620 (태국)

# 출처: https://somjang.tistory.com/entry/Python-문자열의-인코딩을-확인하는-방법 [솜씨좋은장씨]