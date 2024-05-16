#!/usr/bin/env python3
'''This script defines the Cache class'''

from typing import Callable, Optional, Union
import redis
import uuid


class Cache:
    '''Cache class defined'''

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Stores data in Redis using random key and returns the key
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self,
            key: str,
            fn: Optional[Callable[[bytes], Union[str, int, float, bytes]]] = None) -> Optional[Union[str, int, float, bytes]]:
        '''
        Retrieves data from Redis using the key
        '''
        data = self._redis.get(key)

        if data is None:
            return None

        if fn:
            return fn(data)

        return data

    def get_str(self, key: str) -> str:
        '''
        Returns the value as a str
        '''
        data = self.get(key, fn=lambda x: x.decode('utf-8'))
        return data

    def get_int(self, key: str) -> int:
        '''
        Returns the value as an int
        '''
        data = self.get(key, fn=int)
        return data
