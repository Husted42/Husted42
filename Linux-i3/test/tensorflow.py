import tensorflow as tf
import time

def show_gpu_info():
    print("TensorFlow version:", tf.__version__)
    print("\nAvailable devices:")
    gpus = tf.config.list_physical_devices('GPU')
    if not gpus:
        print("❌ No GPU found.")
        return False
    for i, gpu in enumerate(gpus):
        print(f"✅ GPU {i}: {gpu.name}")
    logical_gpus = tf.config.list_logical_devices('GPU')
    print(f"\nNumber of physical GPUs: {len(gpus)}")
    print(f"Number of logical GPUs: {len(logical_gpus)}")
    return True

def test_gpu_parallel_computation():
    print("\nTesting GPU performance with large matrix multiplication...")

    # Define large matrices
    size = 5000
    with tf.device('/GPU:0'):
        a = tf.random.uniform([size, size])
        b = tf.random.uniform([size, size])

        start_time = time.time()
        c = tf.matmul(a, b)
        tf.experimental.sync_devices()  # Ensure computation completes before timing
        elapsed = time.time() - start_time

    print(f"✅ Matrix multiplication completed in {elapsed:.2f} seconds on GPU.")

def main():
    gpu_available = show_gpu_info()
    if gpu_available:
        test_gpu_parallel_computation()

if __name__ == "__main__":
    main()
