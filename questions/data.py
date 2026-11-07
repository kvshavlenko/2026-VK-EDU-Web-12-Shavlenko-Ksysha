QUESTIONS = []
for i in range(1, 35):
    QUESTIONS.append({
        'id': i,
        'title': f'Тестовый вопрос номер {i}?',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'answers_count': i % 5,
        'likes': i * 2,
        'tags': ['python', 'django'] if i % 2 == 0 else ['css', 'html']
    })

ANSWERS = []
for i in range(1, 15):
    ANSWERS.append({
        'id': i,
        'text': f'Это тестовый ответ номер {i}.',
        'likes': i,
        'is_correct': i == 1
    })