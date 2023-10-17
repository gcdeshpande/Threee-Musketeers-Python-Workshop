import matplotlib.pyplot as plt

def calculate_benfords_law(numbers):
    """Calculate the distribution of leading digits according to Benford's Law."""
    benfords_distribution = {str(i): 0 for i in range(1, 10)}
    total_count = 0

    for number in numbers:
        first_digit = str(number)[0]
        if first_digit in benfords_distribution:
            benfords_distribution[first_digit] += 1
            total_count += 1

    # Normalize the distribution
    for key in benfords_distribution:
        benfords_distribution[key] /= total_count

    return benfords_distribution

def plot_distribution(distribution):
    """Plot the distribution of leading digits."""
    labels = list(distribution.keys())
    values = [distribution[key] for key in labels]

    plt.bar(labels, values)
    plt.xlabel('Leading Digit')
    plt.ylabel('Frequency')
    plt.title("Distribution of Leading Digits According to Benford's Law")
    plt.show()

if __name__ == "__main__":
    # Sample bank statement data
    bank_statement = [3.9, 740.0, 1.9, 26.0, 32.0, 3.1, 38.0, 1.9, 1.9, 3.3, 1600.0, 3.5, 83.0, 1.3, 1.8, 5.6, 1.8, 4500.0, 1400.0, 8500.0, 1.5, 37.0, 4.3, 4.7, 630.0, 5200.0, 630.0, 4.8, 4.6, 2.9, 3.1, 1.7, 2.6, 4.5, 6.2, 13.0, 5.8, 4.5, 130.0, 36.0, 36.0, 2.9, 460.0, 9.5, 37.0, 1.9, 1.1, 13.0, 12.0, 120.0, 5.4, 8.6, 1.3, 19.0, 1.4, 23.0, 860.0, 7.8, 2.2, 1.6, 2.4, 8.9, 41.0, 1.8, 130.0, 2100.0, 59.0, 1.9, 8400.0, 160.0, 48.0, 5.8, 5.1, 8.5, 1.7, 6.1, 3.7, 5.5, 1300.0, 1.1, 85.0, 1100.0, 1.4, 9300.0, 8.6, 6.8, 1.4, 5300.0, 1.5, 610.0, 7.3, 360.0, 4.9, 2700.0, 440.0, 9100.0, 8.8, 3400.0, 7.1, 1.1, 630.0, 2.3, 2.5, 770.0, 9200.0, 3400.0, 1.1, 880.0, 120.0, 21.0, 8.4, 5.5, 7.2, 1.9, 2400.0, 4.9, 270.0, 8.2, 61.0, 160.0, 29.0, 2.4, 7.9, 160.0, 4.4, 1.2, 880.0, 9900.0, 1.5, 3.5, 1800.0, 180.0, 270.0, 230.0, 6.6, 39.0, 8.2, 2.3, 3800.0, 1.5, 2.7, 1.3, 11.0, 2.6, 6200.0, 1.4, 3200.0, 89.0, 4.5, 2.3, 8.4, 980.0, 88.0, 480.0, 2200.0, 1.9, 1.3, 5500.0, 5200.0, 34.0, 3.6, 7900.0, 1.9, 1.4, 9.3, 2.7, 170.0, 4.2, 7.3, 2300.0, 1200.0, 7.2, 7.8, 1200.0, 85.0, 6.3, 79.0, 3.5, 2.5, 2.8, 140.0, 61.0, 44.0, 8.7, 2800.0, 5600.0, 6.4, 440.0, 1.7, 2.1, 2.1, 5.1, 2.5, 9800.0, 4900.0, 540.0, 6.1, 5.9, 5.5, 8.4, 140.0, 880.0, 67.0, 2500.0, 3.6, 17.0, 7.3, 1.6, 3.9, 1.4, 120.0, 15.0, 38.0, 1.2, 35.0, 1700.0, 370.0, 3.4, 6.8, 2300.0, 1300.0, 7100.0, 17.0, 1.1, 1.6, 7.5, 240.0, 2500.0, 1800.0, 240.0, 8.3, 5.4, 2900.0, 24.0, 49.0, 1.3, 110.0, 320.0, 13.0, 530.0, 1800.0, 2.5, 3200.0, 7100.0, 190.0, 39.0, 3.3, 55.0, 2800.0, 2300.0, 16.0, 7.3, 2600.0, 8.2, 6.4, 170.0, 9.3, 42.0, 5.8, 870.0, 1.7, 4.7, 670.0, 7.1, 1.8, 14.0, 3.3, 150.0, 190.0, 2500.0, 83.0, 3100.0, 4.8, 2.8, 1.1, 180.0, 1.3, 1.9, 1.4, 2.7, 1.6, 47.0, 27.0, 2.7, 3700.0, 580.0, 75.0, 1.8, 3.4, 4.2, 9.2, 13.0, 1.6, 2.8, 51.0, 1200.0, 2.6, 1.7, 1300.0, 2.1, 7.5, 480.0, 4.6, 3.8, 580.0, 2600.0, 3200.0, 31.0, 2400.0, 6.2, 430.0, 130.0, 21.0, 260.0, 81.0, 1.6, 8.8, 2.6, 690.0, 280.0, 5500.0, 8.9, 4.8, 4.2, 2.2, 240.0, 2.2, 18.0, 1.7, 8.9, 1.3, 4500.0, 3.8, 14.0, 1.9, 7.3, 8.8, 16.0, 3.7, 1.8, 1.1, 6100.0, 1.3, 12.0, 670.0, 87.0, 1.8, 4.2, 2.7, 380.0, 4500.0, 790.0, 87.0, 3.9, 1800.0, 2200.0, 1800.0, 4300.0, 6.7, 5900.0, 17.0, 2300.0, 7700.0, 810.0, 7.8, 1.4, 8700.0, 6.5, 49.0, 1700.0, 1.9, 54.0, 2800.0, 330.0, 2.1, 280.0, 1.4, 3200.0, 74.0, 9400.0, 5.8, 28.0, 670.0, 1900.0, 1.3, 28.0, 4.6, 18.0, 1.2, 5900.0, 370.0, 5.5, 4.9, 1400.0, 160.0, 3.4, 7.7, 9600.0, 8400.0, 380.0, 13.0, 2.7, 750.0, 9.9, 7.3, 6400.0, 2900.0, 55.0, 2.4, 1.3, 92.0, 1.8, 1.4, 27.0, 21.0, 2.8, 1400.0, 990.0, 2.1, 3.8, 1.5, 210.0, 2.9, 2.4, 8400.0, 4500.0, 940.0, 240.0, 26.0, 2.4, 1500.0, 2.4, 250.0, 2400.0, 3600.0, 450.0, 6.8, 5600.0, 2800.0, 4300.0, 8.1, 940.0, 5.3, 26.0, 2300.0, 9.8, 7.1, 1.7, 6400.0, 8900.0, 9300.0, 3.1, 1900.0, 2.8, 5.3, 38.0, 690.0, 48.0, 6600.0, 2.1, 6.6, 1300.0, 7.3, 11.0, 17.0, 84.0, 8500.0, 3200.0, 62.0, 5.3, 7400.0, 170.0, 1900.0, 4.7, 610.0, 8.4, 120.0, 17.0, 1.2, 1.3, 4.7, 9.7, 5.5, 540.0, 2.2, 2.1, 330.0, 16.0, 2.9, 9.8, 820.0, 6.3, 6.9, 2.4, 6.4, 870.0, 12.0, 240.0, 8.3, 79.0, 25.0, 49.0, 3700.0, 250.0, 120.0, 3100.0, 1.8, 28.0, 1.7, 76.0, 2.8, 9.6, 6.8, 3.6, 870.0, 66.0, 230.0, 130.0, 2100.0, 1.5, 480.0, 1.9, 5.8, 1.8, 250.0, 1.9, 1.1, 3.5, 1.7, 170.0, 2.3, 490.0, 73.0, 1200.0, 8.1, 1.5, 1.6, 4.9, 690.0, 310.0, 1.9, 2.4, 1.8, 5.7, 7.2, 6200.0, 1.6, 15.0, 9.4, 4.5, 52.0, 3.1, 16.0, 1.3, 5.1, 370.0, 4.4, 7.3, 7.3, 8.2, 6.4, 3.7, 6.3, 320.0, 8.8, 8200.0, 61.0, 2200.0, 9.9, 5800.0, 49.0, 2.7, 1.3, 3.7, 2.7, 3.5, 8.5, 3.6, 7.7, 4.4, 8.5, 450.0, 2800.0, 2.1, 1800.0, 6700.0, 960.0, 8.5, 4800.0, 2.1, 2.5, 1200.0, 1100.0, 130.0, 640.0, 6700.0, 2.4, 190.0, 4500.0, 390.0, 19.0, 3.1, 1300.0, 1.4, 13.0, 1.3, 3400.0, 1.6, 4.3, 780.0, 5.1, 3.9, 7.2, 2.7, 1.7, 1.7, 72.0, 4700.0, 1.7, 2.8, 5.7, 67.0, 15.0, 1.6, 48.0, 4.9, 660.0, 1.2, 310.0, 790.0, 190.0, 2700.0, 19.0, 1.4, 1.1, 660.0, 2300.0, 45.0, 4.4, 6.9, 14.0, 710.0, 540.0, 1.3, 1.5, 8.5, 95.0, 2.1, 1.1, 260.0, 3.9, 1.2, 1.6, 1.5, 2500.0, 2.3, 23.0, 180.0, 59.0, 5.6, 5.4, 1100.0, 110.0, 660.0, 1.5, 4.3, 2.4, 9.9, 4.8, 34.0, 230.0, 4.7, 930.0, 9.4, 7.3, 4.6, 4500.0, 16.0, 8.4, 4.8, 150.0, 1.2, 3800.0, 3.7, 7.9, 27.0, 2600.0, 47.0, 1800.0, 7.6, 6.4, 3.1, 1.7, 570.0, 1.8, 5.2, 1.9, 14.0, 93.0, 1.4, 1.3, 1.6, 7.1, 2.9, 4.7, 1.8, 150.0, 1.4, 1.3, 240.0, 1.8, 7600.0, 9.4, 620.0, 420.0, 280.0, 54.0, 2900.0, 140.0, 6.7, 1.6, 7.4, 930.0, 3.2, 1300.0, 5500.0, 3.9, 2.6, 96.0, 5.6, 5.2, 23.0, 1.9, 1.5, 1500.0, 1100.0, 220.0, 2.1, 3400.0, 8.5, 5.6, 1.5, 21.0, 3100.0, 2.5, 7.6, 5.2, 8.3, 1.4, 61.0, 81.0, 1.4, 78.0, 1.4, 9900.0, 3.1, 4.6, 960.0, 130.0, 1.8, 6100.0, 4.2, 5.4, 1.2, 46.0, 1.2, 1.1, 2.2, 1300.0, 4.3, 3.9, 1.9, 26.0, 1100.0, 1.5, 7.6, 3400.0, 6400.0, 1.4, 2.9, 390.0, 14.0, 12.0, 75.0, 9.6, 19.0, 16.0, 67.0, 490.0, 1.1, 1800.0, 2400.0, 7200.0, 4.6, 1600.0, 4.7, 5.7, 1.8, 4.3, 3300.0, 4.3, 1.6, 1.3, 37.0, 12.0, 1600.0, 1200.0, 85.0, 9.2, 470.0, 380.0, 4100.0, 1.2, 2.2, 1.4, 5400.0, 230.0, 58.0, 1.3, 5.5, 16.0, 310.0, 130.0, 3.3, 1100.0, 1.4, 2.1, 1400.0, 3.9, 2.2, 440.0, 110.0, 1.8, 3.6, 5700.0, 2500.0, 1.6, 9.2, 16.0, 8900.0, 2.2, 4.1, 5.9, 34.0, 3.1, 6.4, 120.0, 250.0, 3500.0, 4.5, 6.7, 3.1, 340.0, 870.0, 16.0, 1.7, 1.8, 9.6, 6.9, 2.1, 2300.0, 9400.0, 1.5, 3.1, 1.5, 55.0, 1500.0, 2.2, 1.8, 11.0, 3500.0, 1.7, 15.0, 1.1, 1.6, 3.1, 270.0, 1500.0, 2.6, 1.5, 1.7, 480.0, 5.2, 1.1, 5.6, 2.7, 5.6, 780.0, 3.6, 5900.0, 7.8, 58.0, 1800.0, 4.2, 580.0, 110.0, 6400.0, 630.0, 1500.0, 13.0, 6.9, 160.0, 2300.0, 360.0, 2.1, 47.0, 12.0, 5200.0, 26.0, 3.4, 85.0, 9.4, 5.4, 5200.0, 1.4, 5700.0, 23.0, 2.1, 8.2, 2.2, 6.8, 1100.0, 3.2, 1900.0, 350.0, 2.2, 5.3, 6700.0, 5700.0, 14.0, 1.6, 2100.0, 140.0, 2.4, 7.2, 1.2, 11.0, 7.4, 3.7, 3600.0, 19.0, 1.2, 3600.0, 1.6, 1700.0, 6.5, 7.4, 8.9, 1.4, 4.6, 3.8, 13.0, 4.3, 8.8, 4.7, 2400.0, 170.0, 3.2, 290.0, 880.0, 7.7, 650.0, 940.0, 1.5, 4.5, 1.8, 2600.0, 9300.0, 2.2, 6.1, 8500.0, 47.0, 2.6, 3.7, 5.7, 43.0, 6.6, 6.2, 6.5, 1.8, 59.0, 58.0, 3.7, 520.0, 5600.0, 1.8, 450.0, 2600.0, 1.8, 1.3, 5800.0, 1.9, 2.5, 56.0, 37.0, 1.3, 2.5, 1.8, 4.6, 310.0]  # Add more numbers as needed

    distribution = calculate_benfords_law(bank_statement)
    plot_distribution(distribution)
