import time, os


GREEN = '\033[42m'
YELLOW = '\033[43m'
RED = '\033[41m'
BLUE = '\033[44m'
END = '\033[0m'

#1-flag

line = ' ' * 5
lenght = 10
height = 12

for i in range(height):
    if i < height // 3:
        color = YELLOW
    elif i < height * 2 // 3:
        color = GREEN
    else:
        color = RED
    print(f'{color}{line * lenght}{END}')


print()

#2-pattern

BLACK = "\033[40m"
WHITE = "\033[107m"

pattern = [
    "1110000000000000111",
    "000110000000001100",
    "000001000000010000",
    "000000100000100000",
    "000000010001000000",
    "000000001010000000",
    "000000000100000000",
]

def draw_pattern(repeats):
    width = len(pattern[0])
    for row in pattern:
        row = row.ljust(width, '0')
        row = row * repeats
        line = ""
        for cell in row:
            if cell == '1':
                color = WHITE
            else:
                color = BLACK
            line = line + color + " "
        print(line + END)

draw_pattern(7)
#3-animation

input('Нажмите Enter для запуска анимации...')
os.system('')

colors = [YELLOW, GREEN, RED, BLUE]

for step in range(4):
    os.system('cls' if os.name == 'nt' else 'clear')
    fg = colors[step]
    col = 3 + step * 3
    for r, row in enumerate(pattern):
        line = ''.join((fg if c == '1' else BLACK) + ' ' for c in row)
        print(f'\033[{3 + r};{col}H{line}{END}', end='') 
    print(f'\033[12;1HКадр {step + 1} из 4', end='', flush=True)
    time.sleep(0.5)

print('\033[12;1H\033')


#4 - diagramma
f=open('seq.txt')
numbers = [float(n) for n in f]

c1=[]
c2=[]
for n in range(0,len(numbers),2):
    c1.append(numbers[n])
for n in range(1,len(numbers),2):
    c2.append(numbers[n])

sum_c1 = (sum(abs(n) for n in c1) / len(c1))
sum_c2 = (sum(abs(n) for n in c2) / len(c2))


res_c1 = round(sum_c1 / (sum_c1+sum_c2) * 100)
res_c2 = 100 - res_c1

print(f'{GREEN}{" " * res_c1}{BLUE}{" " * res_c2}{END}')
print()
print(f'{GREEN} {END} нечётные:  {res_c1}%')
print(f'{BLUE} {END} чётные:    {res_c2}%')
print()
#5 - graphik

CELL = '  '
POINT = f'{GREEN}  {END}'

xs = range(-9, 10)

for y in range(9, -1, -1):
    cells = ''.join(POINT if abs(x) == y else CELL for x in xs)
    print(f'{y:2d} |{cells}')

print('   +' + '—' * (len(xs))*2)
print('    ' + ''.join(f'{x:<2d}' if x % 2 == 0 else '  ' for x in xs))