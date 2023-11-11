import matplotlib.pyplot as plt
import numpy as np

def simulate_processing_time(fabric_size):
    # Giả lập thời gian xử lý với số lượng input là fabric_size
    # Đây có thể là một hàm hoặc đoạn mã mô phỏng công việc cần thời gian xử lý
    processing_time = fabric_size * 0.5 + np.random.uniform(0, 1)
    return processing_time

def run_experiment():
    fabric_sizes = [1, 2, 4, 8, 16, 32, 64]
    processing_times = []

    for fabric_size in fabric_sizes:
        total_processing_time = 0
        # Thực hiện nhiều lần để có kết quả trung bình
        num_trials = 10
        for _ in range(num_trials):
            total_processing_time += simulate_processing_time(fabric_size)
        average_processing_time = total_processing_time / num_trials
        processing_times.append(average_processing_time)

    return fabric_sizes, processing_times

def plot_results(fabric_sizes, processing_times):
    plt.plot(fabric_sizes, processing_times, marker='o')
    plt.title('Thời gian xử lý trung bình theo kích thước fabric')
    plt.xlabel('Kích thước fabric')
    plt.ylabel('Thời gian xử lý trung bình')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    fabric_sizes, processing_times = run_experiment()
    plot_results(fabric_sizes, processing_times)
