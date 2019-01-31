import matplotlib.pyplot as plot

x = 0

y1 = []
y2 = []

while x < 100:
    # Função x^5
    y1.append(pow(x, 5))
    # Função 5x^4
    y2.append(5*pow(x, 4))
    x += 1


plot.plot(range(0, 100), y1, 'r', range(0, 100), y2, 'b')
plot.show()
