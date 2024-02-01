



def solve(s1, s2,t):
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    if(s1 == s2):
        print(f'Test {t+1}: YES')
    else:
        print(f'Test {t+1}: NO')


for t in range(int(input())):
    s1 = input()
    s2 = input()
    solve(s1,s2,t)
