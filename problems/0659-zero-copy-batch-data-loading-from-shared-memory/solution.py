import numpy as np

class ZeroCopyBatchLoader:
    def __init__(self, data: np.ndarray, batch_size: int):
        """Store data in a flat contiguous buffer simulating shared memory."""
        self.n_samples = len(data)
        self.n_features = len(data[0])
        self.buffer = data.copy().reshape(-1)
        self.batch_size = batch_size
        pass

    def num_batches(self) -> int:
        """Return total number of batches."""
        total_batch = self.n_samples/self.batch_size
        if self.n_samples % self.batch_size > 0 :
            total_batch+=1
        return  int(total_batch)
        pass

    def get_batch(self, batch_idx: int) -> np.ndarray:
        """Return batch as a zero-copy view into the buffer."""
        start=batch_idx*self.n_features
        end = (min(batch_idx+self.batch_size,self.n_samples))*self.n_features
        return self.buffer[start:end].reshape((start-end)//self.n_features,self.n_features)
        pass

    def is_zero_copy(self, batch_idx: int) -> bool:
        """Check whether the batch shares memory with the buffer."""
        return np.shares_memory(self.get_batch(batch_idx),self.buffer)
        pass

    def get_batch_means(self) -> list:
        """Return list of per-batch mean values, each rounded to 4 decimals."""
        batch_means= []
        for i in range(self.num_batches()) :
            batch_means.append(np.mean(self.get_batch(i)))
        return batch_means
        pass

    def write_to_buffer(self, row: int, col: int, value: float) -> None:
        """Write a value directly into the flat buffer at (row, col)."""
        self.buffer[row*self.n_features+col]=value
        pass