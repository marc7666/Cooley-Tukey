import numpy as np


def fft(x):
    """
    This method calculates the DFT froms an audio file
    :param x: Audio signal
    :return: DFT
    """
    N = len(x)  # Signal size
    if N == 1:  # Base case: if the signal has size 1, the signal itself is returned
        return x
    even_positions = fft(x[0::2])  # Calculating the DFT for the even part of the signal
    odd_positions = fft(x[1::2])  # Calculating the DFT for the odd part of the signal
    T = [np.exp(-2j * np.pi * k / N) * odd_positions[k] for k in range(N // 2)]  # Calculating the term T
    return [even_positions[k] + T[k] for k in range(N // 2)] + [even_positions[k] - T[k] for k in range(
        N // 2)]  # Joining the results to calculate the complete DFT


if __name__ == "__main__":
    x = [1, 2, 3]
    X = fft(x)
    print(X)
