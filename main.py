import numpy as np
import matplotlib.pyplot as plt

def genSampStd(mu, sigma, n):
    return np.std(np.random.normal(mu, sigma, n), axis=0)


n_input = np.arange(2, 1002)
std_output = np.zeros(1000)
for i in range(1000):
    std_output[i] = np.std(genSampStd(0, 1, (n_input[i],1000000)))

plt.plot(n_input, std_output)
plt.savefig('output2.png')
plt.show()
def genHist():
    data = (genSampStd(0, 1, (3,1000000)))
    mean_of_data = np.mean(data)
    std_of_data = np.std(data)
    proportion_in_2 = (data > mean_of_data-1*std_of_data).mean()
    print(f"\n\n")
    print(f"Mean of data: {mean_of_data}")
    print(f"Std of data: {std_of_data}")
    print(f"Percentile of data: {proportion_in_2}")
    print(f"\n\n")
    plt.hist(data, bins=300, density=True, alpha=0.7, color='blue')
    plt.xlabel('Data Values')
    plt.ylabel('Density')
    plt.title('Estimated Probability Density Function (Histogram)')
    plt.savefig('output.png')
    plt.show()