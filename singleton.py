from multiprocessing import Process, Manager

class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instance = instance
        return cls._instance


class LimitedSingleton:
    _instances = []
    _instances_max = 3
    _instance_actual = -1
    
    def __new__(cls, *args, **kwargs):
        if len(cls._instances) < cls._instances_max:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instances.append(instance)
        cls._instance_actual += 1
        cls._instance_actual %= cls._instances_max
        return cls._instances[cls._instance_actual]
    
    
class SingletonMetaclass(type):
    _instance = None
    
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            instance = super().__call__(*args, **kwargs)
            cls._instance = instance
        return cls._instance
    
    
def singleton_creator(return_list):
        instance = Singleton()
        return_list.append(instance)
        return instance


if __name__ == '__main__':
    
    # Singleton with limited instances
    for _ in range(5):
        LimitedSingleton()
    assert len(LimitedSingleton._instances) == LimitedSingleton._instances_max

    # Clasic Singleton 
    x = Singleton()
    y = Singleton()
    assert x is y
    
    # Singleton as Metaclass
    class MetaclassTest(metaclass=SingletonMetaclass):
        pass
    x = MetaclassTest()
    y = MetaclassTest()
    assert x is y
    
    # Multiprocesing solution
    init_list = []
    return_list = Manager().list()
    for _ in range(5):    
        process = Process(target=singleton_creator, args=(return_list, ))
        init_list.append(process)
        process.start()
    for proccess in init_list:
        process.join()
    print(return_list)