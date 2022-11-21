https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder

def rec_add(a, b):
    if a == 0:
        return b
    else:
        return rec_add(a-1, b+1)

if __name__ == '__main__':
    print(rec_add(3,4))
