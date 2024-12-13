
import matplotlib.pyplot as plt

# Предположим, что наш CSV файл имеет столбцы "Month" и "Passengers"
# Построим график количества пассажиров по месяцам
plt.figure(figsize=(10, 6))
plt.plot(data['Month'], data[' "1958"'], marker='o', linestyle='-')
plt.title('Количество пассажиров по месяцам в 1958 году')
plt.xlabel('Месяц')
plt.ylabel('Количество пассажиров')
plt.grid(True)
plt.show()
