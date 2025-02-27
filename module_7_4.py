team1_num = 5             # мастера
team2_num = 6             # волшебники
score_1 = 40              # мастера
score_2 = 42              # волшебники
team1_time = 1552.512     # мастера
team2_time = 2153.31451   # волшебники
tasks_total = 82          # всего задач
time_avg = 45.2
# challenge_result = 'Победа команды Волшебники данных!'

# использование %

print('В команде Мастера кода участников: %s' % team1_num, '!')
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num), '!')

# Использование format():

print('Команда Волшебники данных решила задач: {}'.format(score_2), '!')
print('Волшебники данных решили задачи за {}'.format(team1_time), 'с !')

# использование f-строк:

print(f'Команды решили {score_1} и {score_2} задачи.')

if team1_time/score_1 > team2_time/score_2:
    challenge_result = 'Победа команды Волшебники данных!'
elif team1_time/score_1 < team2_time/score_2:
    challenge_result = 'Победа команды Мастера кода!'
else:
    challenge_result = 'Ничья'


print(f'Результат битвы: {challenge_result}')

time_avg = (team1_time + team2_time)/(score_1 + score_2)

print(f'Сегодня было решено {score_1 + score_2} задачи, в среднем по {time_avg} секунд на задачу!')
