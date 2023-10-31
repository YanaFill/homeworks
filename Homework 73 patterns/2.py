import logging

class DataSource:
    def __init__(self, filename):
        self._observers = set()
        self._data = []
        self._filename = filename

    def register_observer(self, observer):
        self._observers.add(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._data)

    def read_data(self):
        with open(self._filename, 'r') as file:
            self._data = [int(line.strip()) for line in file]

    def update_data(self, new_data):
        self._data = new_data
        with open(self._filename, 'w') as file:
            for item in new_data:
                file.write(f"{item}\n")
        self.notify_observers()


class DataProxy:
    def __init__(self, data_source, log_file):
        self._data_source = data_source
        self._log_file = log_file
        self._data = []

    def read_data(self):
        self._data_source.read_data()
        self._log(f'Read data: {self._data_source._data}')

    def get_sum(self):
        self._log(f'Calculate sum')
        return sum(self._data_source._data)

    def get_maximum(self):
        self._log(f'Find maximum')
        return max(self._data_source._data)

    def get_minimum(self):
        self._log(f'Find minimum')
        return min(self._data_source._data)

    def _log(self, message):
        with open(self._log_file, 'a') as file:
            file.write(f"{message}\n")

    def update(self, data):
        self._data = data
        self._log(f'Data updated: {data}')


if __name__ == "__main__":
    logging.basicConfig(filename='data_access.log', level=logging.INFO)

    data_source = DataSource('data.txt')
    data_proxy = DataProxy(data_source, 'data_access.log')

    data_source.register_observer(data_proxy)

    data_proxy.read_data()
    print(f"Sum: {data_proxy.get_sum()}")
    print(f"Maximum: {data_proxy.get_maximum()}")
    print(f"Minimum: {data_proxy.get_minimum()}")


    data_source.update_data([1, 2, 3, 4, 5])
    print("Data updated")


    data_proxy.read_data()
    print(f"Sum: {data_proxy.get_sum()}")
    print(f"Maximum: {data_proxy.get_maximum()}")
    print(f"Minimum: {data_proxy.get_minimum()}")
