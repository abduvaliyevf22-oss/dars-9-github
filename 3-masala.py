
questions = [
    {
        "savol": "Rossiya maydoni qancha kvadrat kilometr?",
        "variantlar": ["17,1 million", "8,5 million", "5,4 million", "2,7 million"],
        "javob": "a"
    },
    {
        "savol": "O'zbekiston poytahti qayer?",
        "variantlar": ["Toshkent", "Samarqand", "Buxoro", "Nukus"],
        "javob": "a"
    },
    {
        "savol": "Tojikiston poytahti qayer?",
        "variantlar": ["Dushanbe", "Khujand", "Kulob", "Qurgonteppa"],
        "javob": "a"
    },
    {
        "savol": "Qirg'iziston poytahti qayer?",
        "variantlar": ["Bishkek", "Osh", "Jalolobod", "Karako'l"],
        "javob": "a"
    },
    {
        "savol": "Turkmaniston poytahti qayer?",
        "variantlar": ["Ashxobod", "Mary", "Turkmenabat", "Daşoguz"],
        "javob": "a"
    },
    {
        "savol": "Qozog'iston poytahti qayer?",
        "variantlar": ["Nursulton", "Almati", "Shymkent", "Aqtobe"],
        "javob": "a"
    },
    {
        "savol": "Germaniya poytahti qayer?",
        "variantlar": ["Berlin", "Gamburg", "Myunxen", "Frankfurt"],
        "javob": "a"
    },
    {
        "savol": "Amerika Qo'shma Shtatlari poytahti qayer?",
        "variantlar": ["Vashington", "Nyu-York", "Chikago", "Los-Anjeles"],
        "javob": "a"
    },
    {
        "savol": "Fransiya poytahti qayer?",
        "variantlar": ["Parij", "Lion", "Marsel", "Nitsa"],
        "javob": "a"
    },
    {
        "savol": "Italiya poytahti qayer?",
        "variantlar": ["Rim", "Milan", "Florensiya", "Venetsiya"],
        "javob": "a"
    }
]

print("=== TEST SINOVI ===")
print(f"Savollar soni: {len(questions)}")
print("Javoblar uchun A, B, C yoki D ni kiriting.\n")

correct_count = 0
result = []

for index, item in enumerate(questions, start=1):
    print(f"{index}. {item['savol']}")
    for i, option in enumerate(item['variantlar'], start=1):
        letter = chr(64 + i)
        print(f"   {letter}. {option}")

    while True:
        answer = input("Javobingiz (A/B/C/D): ").strip().lower()
        if answer in ['a', 'b', 'c', 'd']:
            break
        print("Noto'g'ri format! Qayta kiriting.")

    is_correct = answer == item['javob']
    if is_correct:
        correct_count += 1

    result.append({
        "number": index,
        "user_answer": answer,
        "correct_answer": item['javob'],
        "is_correct": is_correct
    })

    print(f"Natija: {'To\'g\'ri' if is_correct else 'Noto\'g\'ri'}")
    print(f"To'g'ri javob: {item['javob'].upper()}\n")

percentage = (correct_count / len(questions)) * 100

print("\n=== YAKUNIY NATIJA ===")
print(f"To'g'ri javoblar soni: {correct_count} / {len(questions)}")
print(f"Foiz: {percentage:.2f}%")

print("\n=== HAR BIR SAVOL HAQIDA ===")
for item in result:
    status = "To'g'ri" if item["is_correct"] else "Noto'g'ri"
    print(f"{item['number']}-savol: Siz {item['user_answer'].upper()} tanladingiz. {status}. To'g'ri javob: {item['correct_answer'].upper()}")